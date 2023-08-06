# This file is part of pymadcad,  distributed under license LGPL v3

'''	
	This module defines triangular meshes and edges webs.
	
	
	containers
	----------
	
	The classes defined here are 'points containers' it means that they are storing a list of points (as a member `point`), a list of groups (member `group`) and index points and groups for other purpose (faces and edges).
	All of these follow this line:
	
	- storages are using basic types, no object inter-referencing, making it easy to copy it
	
	- storages (points, groups, faces, edges, ...) are used as shared ressources
	
		python objects are ref-counted, allowing multiple Mesh instance to have the same point buffer. The user is responsible to ensure that there will be no conflict in making one mesh modifying the buffer in a way that makes it invalid for an other mesh referencing it.
		
		To avoid conflicts, operations that are changing each point (or the most of them) reallocate a new list. Then operations like `mergeclose` or `stripgroups` won't affect other Meshes that shared the same buffers initially.
		
	- as build from shared ressources, these classes can be build from existing parts at a nearly zero cost (few verifications, no computation)
	
	- the user is allowed to hack into the internal data, ensure that the Mesh is still consistent after.
'''

from copy import copy, deepcopy
from random import random
import numpy as np
import numpy.lib.recfunctions as rfn
from array import array
from collections import OrderedDict, Counter
from numbers import Integral, Real
import math

from .mathutils import *
from . import displays
from . import text
from . import hashing
from .asso import Asso
from . import settings

__all__ = [
		'Mesh', 'Web', 'Wire', 'MeshError', 'web', 'wire', 
		'edgekey', 'lineedges', 'striplist', 'suites', 'line_simplification', 'mesh_distance',
		'connpp', 'connpp', 'connpe', 'connef',
		]

class MeshError(Exception):	pass

class Container:
	''' common methods for points container (typically Mesh or Wire) '''
	
	def __init__(self, points=(), groups=(), options=None):
		self.points = points
		self.groups = groups
		self.options = options or {}
	
	# --- basic transformations of points ---
	
	def transform(self, trans):
		''' apply the transform to the points of the mesh, returning the new transformed mesh'''
		trans = transformer(trans)
		transformed = copy(self)
		transformed.points = typedlist((trans(p) for p in self.points), dtype=vec3)
		return transformed
			
	def mergeclose(self, limit=None, start=0):
		''' merge points below the specified distance, or below the precision 
			return a dictionnary of points remapping  {src index: dst index}
		'''
		if limit is None:	limit = self.precision()
		'''
		# O(n**2 /2) implementation
		merges = {}
		for j in reversed(range(start, len(self.points))):
			for i in range(start, j):
				if distance(self.points[i], self.points[j]) <= limit:
					merges[j] = i
					break
		self.mergepoints(merges)
		return merges
		'''
		# O(n) implementation thanks to hashing
		merges = {}
		points = hashing.PointSet(limit)
		for i in range(start, len(self.points)):
			used = points.add(self.points[i])
			if used != i:	merges[i] = used
		self.mergepoints(merges)
		self.points = points.points
		self.points.shrink()
		return merges
		
	def mergegroups(self, defs=None, merges=None):
		''' merge the groups according to the merge dictionnary
			the new groups associated can be specified with defs
			the former unused groups are not removed from the buffer and the new ones are appended
			
			if merges is not provided, all groups are merged, and defs is the data associated to the only group after the merge
		'''
		if merges is None:	
			self.groups = [defs]
			self.tracks = typedlist.full(0, len(self.tracks), 'I')
		else:
			l = len(self.groups)
			self.groups.extend(defs)
			for i,t in enumerate(self.tracks):
				if t in merges:
					self.tracks[i] = merges[t]+l
		
	def stripgroups(self):
		''' remove groups that are used by no faces, return the reindex list '''
		used = [False] * len(self.groups)
		for track in self.tracks:
			used[track] = True
		self.groups = copy(self.groups)
		self.tracks = copy(self.tracks)
		reindex = striplist(self.groups, used)
		for i,track in enumerate(self.tracks):
			self.tracks[i] = reindex[track]
		return reindex
	
	def finish(self):
		''' finish and clean the mesh 
			note that this operation can cost as much as other transformation operation
			job done
				- mergeclose
				- strippoints
				- stripgroups
				- check
		'''
		self.mergeclose()
		#self.strippoints()	# not needed since the new mergeclose implementation
		self.stripgroups()
		self.check()
		return self
	
	# --- verification methods ---
		
	def isvalid(self):
		''' return true if the internal data is consistent (all indices referes to actual points and groups) '''
		try:				self.check()
		except MeshError:	return False
		else:				return True
	
	# --- selection methods ---
	
	def maxnum(self):
		''' maximum numeric value of the mesh, use this to get an hint on its size or to evaluate the numeric precision '''
		m = 0
		for p in self.points:
			for v in p:
				a = abs(v)
				if a > m:	m = a
		return m
	
	def precision(self, propag=3):
		''' numeric coordinate precision of operations on this mesh, allowed by the floating point precision '''
		return self.maxnum() * NUMPREC * (2**propag)
		
	def usepointat(self, point, neigh=NUMPREC):
		''' Return the index of the first point in the mesh at the location. If none is found, insert it and return the index '''
		i = self.pointat(point, neigh=neigh)
		if i is None:
			i = len(self.points)
			self.points.append(point)
		return i
	
	def pointat(self, point, neigh=NUMPREC):
		''' return the index of the first point at the given location, or None '''
		for i,p in enumerate(self.points):
			if distance(p,point) <= neigh:	return i
	
	def pointnear(self, point):
		''' return the nearest point the the given location '''
		return min(	range(len(self.points)), 
					lambda i: distance(self.points[i], point))
					
	def box(self):
		''' return the extreme coordinates of the mesh (vec3, vec3) '''
		if not self.points:		return Box()
		max = deepcopy(self.points[0])
		min = deepcopy(self.points[0])
		for pt in self.points:
			for i in range(3):
				if   pt[i] < min[i]:	min[i] = pt[i]
				elif pt[i] > max[i]:	max[i] = pt[i]
		return Box(min, max)
		
		
	def option(self, update=None, **kwargs):
		''' update the internal options with the given dictionnary and the keywords arguments.
			This is only a shortcut to set options in a method style.
		'''
		if update:	self.options.update(update)
		if kwargs:	self.options.update(kwargs)
		return self


class Mesh(Container):
	''' set of triangles, used to represent volumes or surfaces.
		As volumes are represented by their exterior surface, there is no difference between representation of volumes and faces, juste the way we interpret it.
		
		Attributes:
			points:     typedlist of vec3 for points
			faces:		typedlist of uvec3 for faces, the triplet is (a,b,c) such that  cross(b-a, c-a) is the normal oriented to the exterior.
			tracks:	    typedlist of integers giving the group each face belong to
			groups:     custom information for each group
			options:	custom informations for the entire mesh
	'''
	#__slots__ = 'points', 'faces', 'tracks', 'groups', 'options'
	
	# --- standard point container methods ---
	
	def __init__(self, points=None, faces=None, tracks=None, groups=None, options=None):
		self.points = ensure_typedlist(points, vec3)
		self.faces = ensure_typedlist(faces, uvec3)
		self.tracks = ensure_typedlist(tracks if tracks is not None else typedlist.full(0, len(self.faces), 'I'), 'I')
		self.groups = groups or [None] * (max(self.tracks, default=-1)+1)
		self.options = options or {}
	
	def __add__(self, other):
		''' append the faces and points of the other mesh '''
		if isinstance(other, Mesh):
			r = Mesh(
				self.points if self.points is other.points else self.points[:], 
				self.faces[:], 
				self.tracks[:], 
				self.groups if self.groups is other.groups else self.groups[:],
				)
			r.__iadd__(other)
			return r
		else:
			return NotImplemented
			
	def __iadd__(self, other):
		''' append the faces and points of the other mesh '''
		if isinstance(other, Mesh):		
			if self.points is other.points:
				self.faces.extend(other.faces)
			else:
				lp = len(self.points)
				self.points.extend(other.points)
				self.faces.extend(f+lp  for f in other.faces)
			if self.groups is other.groups:
				self.tracks.extend(other.tracks)
			else:
				lt = len(self.groups)
				self.groups.extend(other.groups)
				self.tracks.extend(track+lt  for track in other.tracks)
			return self
		else:
			return NotImplemented
		
	# --- mesh optimization ---
	
	def owngroups(self):
		return Mesh(self.points, copy(self.faces), deepcopy(self.tracks), deepcopy(self.groups))
		
	def ownpoints(self):
		return Mesh(deepcopy(self.points), deepcopy(self.faces), copy(self.tracks), self.groups)
	
	def strippoints(self):
		points, faces, reindex = strippoints(self.points, self.faces)
		return (
			Mesh(points, faces, copy(self.tracks), self.groups), 
			reindex,
			)
	
	def stripgroups(self):
		groups, tracks, reindex = strippoints(self.groups, self.tracks)
		return (
			Mesh(self.points, copy(self.faces), tracks, groups),
			reindex,
			)
	
	def mergepoints(self, merges):
		''' merge points with the merge dictionnary {src index: dst index}
			merged points are not removed from the buffer.
		'''
		i = 0
		while i < len(self.faces):
			f = self.faces[i]
			self.faces[i] = f = (
				merges.get(f[0], f[0]),
				merges.get(f[1], f[1]),
				merges.get(f[2], f[2]),
				)
			if f[0] == f[1] or f[1] == f[2] or f[2] == f[0]:
				self.faces.pop(i)
				self.tracks.pop(i)
			else:
				i += 1
		self.faces.shrink()
	
	def strippoints(self, used=None):
		''' remove points that are used by no faces, return the reindex list.
			if used is provided, these points will be removed without usage verification
			
			return a table of the reindex made
		'''
		if used is None:
			used = [False] * len(self.points)
			for face in self.faces:
				for p in face:
					used[p] = True
		self.points = deepcopy(self.points)
		self.faces = deepcopy(self.faces)
		reindex = striplist(self.points, used)
		self.points.shrink()
		for i,f in enumerate(self.faces):
			self.faces[i] = uvec3(reindex[f[0]], reindex[f[1]], reindex[f[2]])
		return reindex
	
	def flip(self):
		''' flip all faces, getting the normals opposite '''
		return Mesh(self.points, 
					typedlist((uvec3(f[0],f[2],f[1]) for f in self.faces), dtype=uvec3), 
					self.tracks, 
					self.groups)
					
					
	# ---- mesh checks -----
		
	def issurface(self):
		''' return True if the mesh is a well defined surface (an edge has 2 connected triangles at maximum, with consistent normals)
			such meshes are usually called 'manifold'
		''' 
		reached = set()
		for face in self.faces:
			for e in ((face[0], face[1]), (face[1], face[2]), (face[2],face[0])):
				if e in reached:	return False
				else:				reached.add(e)
		return True
	
	def isenvelope(self):
		''' return True if the surfaces are a closed envelope (the outline is empty)
		'''
		return len(self.outlines_oriented()) == 0
	
	def check(self):
		''' raise if the internal data is inconsistent '''
		if not (isinstance(self.points, typedlist) and self.points.dtype == vec3):	raise MeshError("points must be a typedlist(dtype=vec3)")
		if not (isinstance(self.faces, typedlist) and self.faces.dtype == uvec3): 	raise MeshError("faces must be a typedlist(dtype=uvec3)")
		if not (isinstance(self.tracks, typedlist) and self.tracks.dtype == 'I'): 	raise MeshError("tracks must be a typedlist(dtype='I')")
		l = len(self.points)
		for face in self.faces:
			for p in face:
				if p >= l:	raise MeshError("some point indices are greater than the number of points", face, l)
			if face[0] == face[1] or face[1] == face[2] or face[2] == face[0]:	raise MeshError("some faces use the same point multiple times", face)
		if len(self.faces) != len(self.tracks):	raise MeshError("tracks list doesn't match faces list length")
		if max(self.tracks, default=-1) >= len(self.groups): raise MeshError("some face group indices are greater than the number of groups", max(self.tracks, default=-1), len(self.groups))
	

	# --- selection methods ---
	
	def group_near(self, point):
		''' return the id of the group with the triangle the closest to the given point '''
		return self.tracks[self.face_near(point)]
		
	def face_near(self, point):
		''' return the index of the closest triangle to the given point '''
		return min(	range(len(self.faces)), 
					lambda i: distance_pt(point, self.facepoints(i)))
	
	def qualify(self, *quals, select=None, replace=False):
		''' set a new qualifier for the given groups 
		
			Parameters:
				quals:				the qualifiers to enable for the selected mesh groups
				select (iterable):	if specified, only the groups having all those qualifiers will be added the new qualifiers
				replace (bool):		if True, the qualifiers in select will be removed
				
			Example:
			
				>>> pool = meshb.qual('part-a') + meshb.qual('part-b')
				>>> set(meshb.faces) == set(pool.group('part-b').faces)
				True
				
				>>> chamfer(mesh, ...).qual('my-group', select='chamfer', replace=True)
				>>> mesh.group('my-group')
				<Mesh ...>
		'''
		for group in self.groups:
			if not select or all(key in group   for key in select):
				if replace:
					for key in select:
						if key in group:
							del group[key]
				for key in quals:
					group[key] = None
		
		return self
	
	def group(self, quals):
		''' extract a part of the mesh corresponding to the designated groups.
			
			Groups can be be given in either the following ways:
				- a set of group indices
					
					This can be useful to combine with other functions. However it can be difficult for a user script to keep track of which index correspond to which created group
					
				- an iterable of group qualifiers
				
					This is the best way to designate groups, and is meant to be used in combination with `self.qual()`.
					This mode selects every group having all the input qualifiers
					
			Example:
			
				>>> # create a mesh with only the given groups
				>>> mesh.group({1, 3, 8, 9})   
				<Mesh ...>
				
				>>> # create a mesh with all the groups having the following qualifiers
				>>> mesh.group(['extrusion', 'arc'])   
				<Mesh ...>
		'''
		faces = typedlist(dtype=uvec3)
		tracks = typedlist(dtype='I')
		for i in self.qualified_faces(quals):
			faces.append(self.faces[i])
			tracks.append(self.tracks[i])
		return Mesh(self.points, faces, tracks, self.groups)
		
	def qualified_faces(self, quals):
		if isinstance(quals, int):
			yield from self.qualified_faces({quals})
		elif isinstance(quals, str):
			yield from self.qualified_faces([quals])
		
		elif isinstance(next(iter(quals)), int):
			if not isinstance(quals, set):	quals = set(quals)
			for i,t in enumerate(self.tracks):
				if t in quals:
					yield i
		else:
			seen = {}
			for i,t in enumerate(self.tracks):
				if t not in seen and quals:
					seen[t] = all(k in self.groups[t]   for k in quals)
				if seen[t]:
					yield i
				
	def qualified_groups(self, quals):
		if isinstance(next(iter(quals)), int):
			yield from quals
		else:
			for i, group in enumerate(self.groups):
				if all(key in group   for key in quals):
					yield i
	
	# --- extraction methods ---
		
	def facenormal(self, f):
		''' normal for a face '''
		if isinstance(f, Integral):	
			f = self.faces[f]
		p0 = self.points[f[0]]
		e1 = self.points[f[1]] - p0
		e2 = self.points[f[2]] - p0
		return normalize(cross(e1, e2))
	
	def facenormals(self):
		''' list normals for each face '''
		return typedlist(map(self.facenormal, self.faces), vec3)
	
	def edgenormals(self):
		''' dict of normals for each UNORIENTED edge '''
		normals = {}
		for face in self.faces:
			normal = self.facenormal(face)
			for edge in ((face[0], face[1]), (face[1], face[2]), (face[2],face[0])):
				e = edgekey(*edge)
				normals[e] = normals.get(e,0) + normal
		for e,normal in normals.items():
			normals[e] = normalize(normal)
		return normals
	
		
	def vertexnormals(self):
		''' list of normals for each point '''
		
		# collect the mesh border as edges and as points
		outline = self.outlines_oriented()
		border = set()
		for a,b in outline:
			border.add(a)
			border.add(b)
		
		# sum contributions to normals
		l = len(self.points)
		normals = typedlist.full(vec3(0), l)
		for face in self.faces:
			normal = self.facenormal(face)
			if not isfinite(normal):	continue
			for i in range(3):
				o = self.points[face[i]]
				# point on the surface
				if face[i] not in border:
					# triangle normals are weighted by their angle at the point
					contrib = anglebt(self.points[face[i-2]]-o, self.points[face[i-1]]-o)
					normals[face[i]] += contrib * normal
				# point on the outline
				elif (face[i], face[i-1]) in outline:
					# only the triangle creating the edge does determine its normal
					normals[face[i]] += normal
					normals[face[i-1]] += normal
		
		for i in range(l):
			normals[i] = normalize(normals[i])
		assert len(normals) == len(self.points)
		return normals
		
	def tangents(self):
		''' tangents to outline points '''
		# outline with associated face normals
		edges = {}
		for face in self.faces:
			for e in ((face[0], face[1]), (face[1], face[2]), (face[2],face[0])):
				if e in edges:	del edges[e]
				else:			edges[(e[1], e[0])] = self.facenormal(face)
		
		# cross neighbooring normals
		tangents = {}
		for loop in suites(edges, cut=False):
			assert loop[-1] == loop[0],  "non-manifold mesh"
			loop.pop()
			for i in range(len(loop)):
				c = cross(	edges[(loop[i-2],loop[i-1])], 
							edges[(loop[i-1],loop[i])] )
				o = cross(  self.points[loop[i-2]] - self.points[loop[i]],
				            edges[(loop[i-2],loop[i-1])] + edges[(loop[i-1],loop[i])] )
				tangents[loop[i-1]] = normalize(mix(o, c, clamp(length2(c)/length2(o)/NUMPREC, 0, 1) ))
		return tangents
	
	
	def facepoints(self, f):
		''' shorthand to get the points of a face (index is an int or a triplet) '''
		if isinstance(f, Integral):
			f = self.faces[f]
		return self.points[f[0]], self.points[f[1]], self.points[f[2]]
	
	def edges(self):
		''' set of UNORIENTED edges present in the mesh '''
		edges = set()
		for face in self.faces:
			edges.add(edgekey(face[0], face[1]))
			edges.add(edgekey(face[1], face[2]))
			edges.add(edgekey(face[2], face[0]))
		return edges
	
	def edges_oriented(self):
		''' iterator of ORIENTED edges, directly retreived of each face '''
		for face in self.faces:
			yield face[0], face[1]
			yield face[1], face[2]
			yield face[2], face[0]
	
	def group(self, groups):
		''' return a new mesh linked with this one, containing only the faces belonging to the given groups '''
		if isinstance(groups, set):			pass
		elif hasattr(groups, '__iter__'):	groups = set(groups)
		else:								groups = (groups,)
		faces = typedlist(dtype=uvec3)
		tracks = typedlist(dtype='I')
		for f,t in zip(self.faces, self.tracks):
			if t in groups:
				faces.append(f)
				tracks.append(t)
		return Mesh(self.points, faces, tracks, self.groups)
	
	def outlines_oriented(self):
		''' return a set of the ORIENTED edges delimiting the surfaces of the mesh '''
		edges = set()
		for face in self.faces:
			for e in ((face[0], face[1]), (face[1], face[2]), (face[2],face[0])):
				if e in edges:	edges.remove(e)
				else:			edges.add((e[1], e[0]))
		return edges
	
	def outlines_unoriented(self):
		''' return a set of the UNORIENTED edges delimiting the surfaces of the mesh 
			this method is robust to face orientation aberations
		'''
		edges = set()
		for face in self.faces:
			for edge in ((face[0],face[1]),(face[1],face[2]),(face[2],face[0])):
				e = edgekey(*edge)
				if e in edges:	edges.remove(e)
				else:			edges.add(e)
		return edges
	
	def outlines(self):
		''' return a Web of ORIENTED edges '''
		return Web(self.points, self.outlines_oriented())
		
	def groupoutlines(self):
		''' return a dict of ORIENTED edges indexing groups.
			
			On a frontier between multiple groups, there is as many edges as groups, each associated to a group.
		'''
		edges = typedlist(dtype=uvec2)		# outline
		tracks = typedlist(dtype='I')		# groups for edges

		tmp = {}	# faces adjacent to edges
		for i,face in enumerate(self.faces):
			for e in ((face[1],face[0]),(face[2],face[1]),(face[0],face[2])):
				track = self.tracks[i]
				if e in tmp:
					if tmp[e] != track:
						edges.append(e)
						tracks.append(track)
					del tmp[e]
				else:
					tmp[(e[1],e[0])] = track
		edges.extend(tmp.keys())
		tracks.extend(tmp.values())
		return Web(self.points, edges, tracks, self.groups)
		
	def frontiers(self, *args):
		''' return a Web of UNORIENTED edges that split the given groups appart.
		
			if groups is None, then return the frontiers between any groups
		'''
		if len(args) == 1 and hasattr(args[0], '__iter__'):
			args = args[0]
		groups = set(args)
		edges = typedlist(dtype=uvec2)
		tracks = typedlist(dtype='I')
		couples = OrderedDict()
		belong = {}
		for i,face in enumerate(self.faces):
			if groups and self.tracks[i] not in groups:	
				continue
			for edge in ((face[0],face[1]),(face[1],face[2]),(face[2],face[0])):
				e = edgekey(*edge)
				if e in belong:
					if belong[e] != self.tracks[i]:
						g = edgekey(belong[e],self.tracks[i])
						edges.append(e)
						tracks.append(couples.setdefault(g, len(couples)))
					del belong[e]
				else:
					belong[e] = self.tracks[i]
		return Web(self.points, edges, tracks, list(couples))
	
	def surface(self):
		''' total surface of triangles '''
		s = 0
		for f in self.faces:
			a,b,c = self.facepoints(f)
			s += length(cross(a-b, a,c))/2
		return s
	
	def barycenter(self):
		''' surface barycenter of the mesh '''
		if not self.faces:	return vec3(0)
		acc = vec3(0)
		tot = 0
		for f in self.faces:
			a,b,c = self.facepoints(f)
			weight = length(cross(b-a, c-a))
			tot += weight
			acc += weight*(a+b+c)
		return acc / (3*tot)
	
	def splitgroups(self, edges=None):
		''' split the mesh groups into connectivity separated groups.
			the points shared by multiple groups will be duplicated
			if edges is provided, only the given edges at group frontier will be splitted
			
			return a list of tracks for points
		'''
		if edges is None:	edges = self.frontiers().edges
		# mark points on the frontier
		frontier = [False]*len(self.points)
		for a,b in edges:
			frontier[a] = True
			frontier[b] = True
		# duplicate points and reindex faces
		points = copy(self.points)
		idents = typedlist.full(0, len(self.points), 'I')		# track id corresponding to each point
		duplicated = {}		# new point index for couples (frontierpoint, group)
		def repl(pt, track):
			if frontier[pt]:
				key = (pt,track)
				if key in duplicated:	i = duplicated[key]
				else:
					i = duplicated[key] = len(points)
					points.append(points[pt])
					idents.append(track)
				return i
			else:
				idents[pt] = track
				return pt
		faces = typedlist((uvec3(repl(a,t), repl(b,t), repl(c,t))  
						for (a,b,c),t in zip(self.faces, self.tracks)), dtype=uvec3)
		
		self.points = points
		self.faces = faces
		return idents
		
	def split(self, edges):
		''' split the mesh around the given edges. 
			The points in common with two or more designated edges will be dupliated once or more, and the face indices will be reassigned so that faces each side of the given edges will own a duplicate of that point each.
		'''
		# get connectivity and set of edges to manage
		conn = connef(self.faces)
		edges = set(edgekey(*edge)   for edge in edges)
		# collect the points to multiply
		ranks = Counter(p  for e in edges for p in e)
		separations = set(p  for p, count in ranks.items() if count > 1)
		newfaces = deepcopy(self.faces)
		# for each edge, reassign neighboring faces to the proper points
		for edge in edges:
			for pivot in edge:
				if edge in conn and pivot in newfaces[conn[edge]]:
					dupli = len(self.points)
					self.points.append(self.points[pivot])
					
					# change the point index in every neighbooring face
					front = edge
					while front in conn:
						fi = conn[front]
						f = arrangeface(self.faces[fi], pivot)
						fm = arrangeface(newfaces[fi], pivot)
						
						assert f[0] == pivot
						if fm[0] != pivot: 
							break
						
						newfaces[fi] = uvec3(dupli, fm[1], fm[2])
						if pivot == front[0]:	front = (pivot, f[2])
						elif pivot == front[1]:	front = (f[1], pivot)
						else:
							raise AssertionError('error in connectivity')
						if edgekey(*front) in edges:
							break
		
		self.faces = newfaces
					
		
	# NOTE: splitfaces(self) ?
		
	def islands(self, conn=None) -> '[Mesh]':
		''' return the unconnected parts of the mesh as several meshes '''
		if not conn:	
			conn = connef(self.faces)
		# propagation
		islands = []
		reached = [False] * len(self.faces)	# faces reached
		stack = []
		start = 0
		while True:
			# search start point
			for start in range(start,len(reached)):
				if not reached[start]:
					stack.append(start)
					break
			# end when everything reached
			if not stack:	break
			# propagate
			island = Mesh(points=self.points, groups=self.groups)
			while stack:
				i = stack.pop()
				if reached[i]:	continue	# make sure this face has not been stacked twice
				reached[i] = True
				island.faces.append(self.faces[i])
				island.tracks.append(self.tracks[i])
				f = self.faces[i]
				for i in range(3):
					e = f[i],f[i-1]
					if e in conn and not reached[conn[e]]:
						stack.append(conn[e])
			islands.append(island)
		return islands
		
	def propagate(self, atface, atisland=None, find=None, conn=None):
		''' return the unconnected parts of the mesh as several meshes '''
		if not conn:	
			conn = connef(self.faces)
		
		reached = [False] * len(self.faces)	# faces reached
		stack = []
		# procedure for finding the new islands to propagate on
		if not find:
			start = [0]
			def find(stack, reached):
				for i in range(start[0],len(reached)):
					if not reached[i]:
						stack.append(i)
						break
				start[0] = i
		# propagation
		while True:
			# search start point
			find(stack, reached)
			# end when everything reached
			if not stack:	break
			# propagate
			while stack:
				i = stack.pop()
				if reached[i]:	continue	# make sure this face has not been stacked twice
				reached[i] = True
				atface(i, reached)
				f = self.faces[i]
				for i in range(3):
					e = f[i],f[i-1]
					if e in conn and not reached[conn[e]]:
						stack.append(conn[e])
			if atisland:
				atisland(reached)
				
	def islands(self, conn=None) -> '[Mesh]':
		''' return the unconnected parts of the mesh as several meshes '''
		islands = []
		faces = typedlist(dtype=uvec3)
		tracks = typedlist(dtype='I')
		def atface(i, reached):
			faces.append(self.faces[i])
			tracks.append(self.tracks[i])
		def atisland(reached):
			islands.append(Mesh(self.points, deepcopy(faces), deepcopy(tracks), self.groups))
			faces.clear()
			tracks.clear()
		self.propagate(atface, atisland, conn=conn)
		return islands
	
	def orient(self, dir=None, conn=None) -> 'Mesh':
		''' flip the necessary faces to make the normals consistent, ensuring the continuity of the out side.
			
			Argument `dir` tries to make the result deterministic:
			
				* if given, the outermost point in this direction will be considered pointing outside
				* if not given, the farthest point to the barycenter will be considered pointing outside
				
				note that if the mesh contains multiple islands, that direction must make sense for each single island
		'''
		if dir:	
			metric = lambda p, n: (dot(p, dir), abs(dot(n, dir)))
			orient = lambda p, n: dot(n, dir)
		else:	
			center = self.barycenter()
			metric = lambda p, n: (length2(p-center), abs(dot(n, p-center)))
			orient = lambda p, n: dot(n, p-center)
		if not conn:	
			conn = Asso(  (edgekey(*e),i)
							for i,f in enumerate(self.faces)
							for e in ((f[0],f[1]), (f[1],f[2]), (f[2],f[0]))
							)
		
		faces = self.faces[:]
		normals = self.facenormals()
		
		reached = [False] * len(self.faces)	# faces reached
		stack = []
		
		# propagation
		while True:
			# search start point
			best = (-inf,0)
			candidate = None
			for i,f in enumerate(faces):
				if not reached[i]:
					for p in f:
						score = metric(self.points[p], normals[i])
						if score > best:
							best, candidate = score, i
							if orient(self.points[p], normals[i]) < 0:
								faces[i] = (f[2],f[1],f[0])
			# end when everything reached
			if candidate is None:
				break
			else:
				stack.append(candidate)
			# process neighbooring
			while stack:
				i = stack.pop()
				if reached[i]:	continue	# make sure this face has not been stacked twice
				reached[i] = True
				
				f = faces[i]
				for i in range(3):
					e = f[i], f[i-1]
					for n in conn[edgekey(*e)]:
						if reached[n]:	continue
						nf = faces[n]
						# check for orientation continuity
						if arrangeface(nf,f[i-1])[1] == f[i]:
							faces[n] = (nf[2],nf[1],nf[0])
						# propagate
						stack.append(n)
		
		return Mesh(self.points, faces, self.tracks, self.groups)
		
	# NOTE not sure this method is useful
	def replace(self, mesh, groups=None) -> 'Mesh':
		''' replace the given groups by the given mesh.
			If no groups are specified, it will take the matching groups (with same index) in the current mesh
		'''
		if not groups:
			groups = set(mesh.tracks)
		new = copy(self)
		new.faces = typedlist((f	for f,t in zip(self.faces, self.tracks)	if t not in groups), dtype=uvec3)
		new.tracks = typedlist((t	for t in self.tracks	if t not in groups), dtype='I')
		new += mesh
		return new
	
	
	# --- renderable interfaces ---
	
	def display_triangles(self, scene):
		from . import rendering, text
		grp = []
		if self.options.get('debug_points', False):
			for i,p in enumerate(self.points):
				grp.append(text.TextDisplay(scene, 
					p, 
					' '+str(i), 
					size=8, 
					color=(0.2, 0.8, 1),
					align=('left', 'center'), 
					layer=-4e-4,
					))
		
		if self.options.get('debug_faces', None) == 'indices':
			for i,f in enumerate(self.faces):
				p = (self.points[f[0]] + self.points[f[1]] + self.points[f[2]]) /3
				grp.append(text.TextDisplay(scene, p, str(i), 9, (1, 0.2, 0), align=('center', 'center'), layer=-4e-4))
		if self.options.get('debug_faces', None) == 'tracks':
			for i,f in enumerate(self.faces):
				p = (self.points[f[0]] + self.points[f[1]] + self.points[f[2]]) /3
				grp.append(text.TextDisplay(scene, p, str(self.tracks[i]), 9, (1, 0.2, 0), align=('center', 'center'), layer=-4e-4))
		
		fn = np.array([tuple(self.facenormal(f)) for f in self.faces])
		points = np.array([tuple(p) for p in self.points], dtype=np.float32)		
		edges = []
		for i in range(0, 3*len(self.faces), 3):
			edges.append((i, i+1))
			edges.append((i+1, i+2))
			edges.append((i, i+2))
		
		idents = []
		for i in self.tracks:
			idents.append(i)
			idents.append(i)
			idents.append(i)
		
		m = copy(self)
		idents = m.splitgroups()
		edges = m.groupoutlines().edges
		normals = m.vertexnormals()
		
		if not m.points or not m.faces:	
			return displays.Display()
		
		grp.append(displays.SolidDisplay(scene, 
				glmarray(m.points), 
				glmarray(normals), 
				m.faces, 
				edges,
				idents,
				color = self.options.get('color'),
				))
		return rendering.Group(scene, grp)
	
	def display_groups(self, scene):
		m = copy(self)
		idents = m.splitgroups()
		edges = m.groupoutlines().edges
		normals = m.vertexnormals()
		
		return displays.SolidDisplay(scene, 
				m.points, 
				normals, 
				m.faces, 
				edges,
				idents,
				color = self.options.get('color'),
				)
	
	def display(self, scene):
		m = copy(self)
		
		m.split(m.frontiers().edges)
		edges = m.outlines().edges
		
		# select edges above a threshold
		tosplit = []
		thresh = cos(settings.display['sharp_angle'])
		conn = connef(m.faces)
		for edge, f1 in conn.items():
			if edge[1] > edge[0]:	continue
			f2 = conn.get((edge[1],edge[0]))
			if f2 is None:	continue
			if m.tracks[f1] != m.tracks[f2] or dot(m.facenormal(f1), m.facenormal(f2)) <= thresh:
				tosplit.append(edge)
		
		m.split(tosplit)
		
		# get the group each point belong to
		idents = [0] * len(m.points)
		for face, track in zip(m.faces, m.tracks):
			for p in face:
				idents[p] = track
		
		normals = m.vertexnormals()
		
		if not m.points or not m.faces:	
			return displays.Display()
		
		return displays.SolidDisplay(scene, 
				typedlist_to_numpy(m.points, 'f4'), 
				typedlist_to_numpy(normals, 'f4'), 
				typedlist_to_numpy(m.faces, 'u4'),
				typedlist_to_numpy(edges, 'u4'),
				typedlist_to_numpy(idents, 'u4'),
				color = self.options.get('color'),
				)
	
	def __repr__(self):
		return '<Mesh with {} points at 0x{:x}, {} faces>'.format(len(self.points), id(self.points), len(self.faces))
	
	def __str__(self):
		return 'Mesh(\n  points={},\n  faces={},\n  tracks={},\n  groups={},\n  options={})'.format(
					reprarray(self.points, 'points'),
					reprarray(self.faces, 'faces'),
					reprarray(self.tracks, 'tracks'),
					reprarray(self.groups, 'groups'),
					repr(self.options))
		

def reprarray(array, name):
	content = ', '.join((repr(e) for e in array))
	return '['+content+']'

def striplist(list, used):
	''' remove all elements of list that match a False in used, return a reindexation list '''
	reindex = [-1] * len(list)
	j = 0
	for i,u in enumerate(used):
		if u:
			list[j] = list[i]
			reindex[i] = j
			j += 1
	list[j:] = []
	return reindex

def npcast(storage, dtype=None):
	if isinstance(storage, typedlist):
		raw = np.array(storage, copy=False)
		if raw.dtype.fields:
			return np.stack([ raw[f] for f in raw.dtype.fields.keys() ], axis=-1)
		else:
			return raw
	elif hasattr(storage[0], '__len__'):
		buff = np.empty((len(storage), len(storage[0])), dtype=dtype)
		for i,e in enumerate(storage):
			buff[i][:] = e
		return buff
	else:
		return np.array(storage, dtype=dtype)

def numpy_to_typedlist(array: 'ndarray', dtype) -> 'typedlist':
	''' convert a numpy.ndarray into a typedlist with the given dtype, if the conversion is possible term to term '''
	ndtype = np.array(typedlist(dtype)).dtype
	if ndtype.fields:
		return typedlist(rfn.unstructured_to_structured(array).astype(ndtype, copy=False), dtype)
	else:
		return typedlist(array.astype(ndtype, copy=False), dtype)
	
def typedlist_to_numpy(array: 'typedlist', dtype) -> 'ndarray':
	''' convert a typedlist to a numpy.ndarray with the given dtype, if the conversion is possible term to term '''
	tmp = np.array(array, copy=False)
	if tmp.dtype.fields:
		return rfn.structured_to_unstructured(tmp, dtype)
	else:
		return tmp.astype(dtype)
		
def ensure_typedlist(obj, dtype):
	''' return a typedlist with the given dtype, create it from whatever is in obj if needed '''
	if isinstance(obj, typedlist) and obj.dtype == dtype:
		return obj
	else:
		return typedlist(obj, dtype)


class Web(Container):
	''' set of bipoint edges, used to represent wires
		this definition is very close to the definition of Mesh, but with edges instead of triangles
		
		Attributes:
			points:     typedlist of vec3 for points
			edges:      typedlist of couples for edges, the couple is oriented (meanings of this depends on the usage)
			tracks:     typedlist of integers giving the group each line belong to
			groups:     custom information for each group
			options:	custom informations for the entire web
	'''

	# --- standard point container methods ---
	
	def __init__(self, points=None, edges=None, tracks=None, groups=None, options=None):
		self.points = ensure_typedlist(points, vec3)
		self.edges = ensure_typedlist(edges, uvec2)
		self.tracks = ensure_typedlist(tracks or typedlist.full(0, len(self.edges), 'I'), 'I')
		self.groups = groups or [None] * (max(self.tracks, default=-1)+1)
		self.options = options or {}
		
	def __add__(self, other):
		''' append the faces and points of the other mesh '''
		if isinstance(other, Web):
			r = Web(
				self.points if self.points is other.points else self.points[:], 
				self.edges[:], 
				self.tracks[:], 
				self.groups if self.groups is other.groups else self.groups[:],
				)
			r.__iadd__(other)
			return r
		else:
			return NotImplemented
			
	def __iadd__(self, other):
		''' append the faces and points of the other mesh '''
		if isinstance(other, Web):
			if self.points is other.points:
				self.edges.extend(other.edges)
			else:
				lp = len(self.points)
				self.points.extend(other.points)
				self.edges.extend(e+lp  for e in other.edges)
			if self.groups is other.groups:
				self.tracks.extend(other.tracks)
			else:
				lt = len(self.groups)
				self.groups.extend(other.groups)
				self.tracks.extend(t+lt   for t in other.tracks)
			return self
		else:
			return NotImplemented
	
	def flip(self):
		''' reverse direction of all edges '''
		return Web(	self.points, 
					typedlist((uvec2(b,a)  for a,b in self.edges), dtype=uvec2), 
					self.tracks, 
					self.groups)
		
	def segmented(self, group=None):
		''' return a copy of the mesh with a group each edge 
		
			if group is specified, it will be the new definition put in each groups
		'''
		return Web(self.points, self.edges,
					typedlist(range(len(self.edges)), dtype='I'),
					[group]*len(self.edges),
					self.options,
					)
		
	# --- mesh optimization ---
	
	def mergepoints(self, merges):
		''' merge points with the merge dictionnary {src index: dst index}
			remaining points are not removed
		'''
		i = 0
		while i < len(self.edges):
			e = self.edges[i]
			self.edges[i] = e = uvec2(
				merges.get(e[0], e[0]),
				merges.get(e[1], e[1]),
				)
			if e[0] == e[1]:
				self.edges.pop(i)
				self.tracks.pop(i)
			else:
				i += 1
	
	def strippoints(self, used=None):
		''' remove points that are used by no edges, return the reindex list.
			if used is provided, these points will be removed without usage verification
			
			return a table of the reindex made
		'''
		if used is None:
			used = [False] * len(self.points)
			for edge in self.edges:
				for p in edge:
					used[p] = True
		self.points = deepcopy(self.points)
		self.edges = deepcopy(self.edges)
		reindex = striplist(self.points, used)
		for i,e in enumerate(self.edges):
			self.edges[i] = uvec2(reindex[e[0]], reindex[e[1]])
		return reindex
		
	# --- verification methods ---
			
	def isline(self):
		''' true if each point is used at most 2 times by edges '''
		reached = typedlist.full(0, len(self.points), 'I')
		for line in self.edges:
			for p in line:	reached[p] += 1
		for r in reached:
			if r > 2:	return False
		return True
	
	def isloop(self):
		''' true if the wire form a loop '''
		return len(self.extremities()) == 0
	
	def check(self):
		''' check that the internal data references are good (indices and list lengths) '''
		if not (isinstance(self.points, typedlist) and self.points.dtype == vec3):	raise MeshError("points must be a typedlist(dtype=vec3)")
		if not (isinstance(self.edges, typedlist) and self.edges.dtype == uvec2): 	raise MeshError("edges must be in a typedlist(dtype=uvec2)")
		if not (isinstance(self.tracks, typedlist) and self.tracks.dtype == 'I'): 	raise MeshError("tracks must be in a typedlist(dtype='I')")
		l = len(self.points)
		for line in self.edges:
			for p in line:
				if p >= l:	raise MeshError("some indices are greater than the number of points", line, l)
				if p < 0:	raise MeshError("point indices must be positive", line)
			if line[0] == line[1]:	raise MeshError("some edges use the same point multiple times", line)
		if len(self.edges) != len(self.tracks):	raise MeshError("tracks list doesn't match edge list length")
		if max(self.tracks, default=-1) >= len(self.groups): raise MeshError("some line group indices are greater than the number of groups", max(self.tracks, default=-1), len(self.groups))
		
	# --- extraction methods ---
		
	def extremities(self):
		''' return the points that are used once only (so at wire terminations)
			1D equivalent of Mesh.outlines()
		'''
		extr = set()
		for l in self.edges:
			for p in l:
				if p in extr:	extr.remove(p)
				else:			extr.add(p)
		return extr
	
	def groupextremities(self):
		''' return the extremities of each group.
			1D equivalent of Mesh.groupoutlines()
			
			On a frontier between multiple groups, there is as many points as groups, each associated to a group.
		'''
		indices = typedlist(dtype='I')
		tracks = []
		tmp = {}
		# insert points belonging to different groups
		for i,edge in enumerate(self.edges):
			track = self.tracks[i]
			for p in edge:
				if p in tmp:
					if tmp[p] != track:
						indices.append(p)
						tracks.append(track)
					del tmp[p]
				else:
					tmp[p] = track
		indices.extend(tmp.keys())
		tracks.extend(tmp.values())
		return Wire(self.points, indices, tracks, self.groups)
		
	def frontiers(self, *args):
		''' return a Wire of points that split the given groups appart.
		
			if groups is None, then return the frontiers between any groups
		'''
		if len(args) == 1 and hasattr(args[0], '__iter__'):
			args = args[0]
		groups = set(args)
		indices = typedlist(dtype='I')
		tracks = typedlist(dtype='I')
		couples = OrderedDict()
		belong = {}
		for i,edge in enumerate(self.edges):
			track = self.tracks[i]
			if groups and track not in groups:	continue
			for p in edge:
				if p in belong:
					if belong[p] != track:
						g = edgekey(belong[p],track)
						indices.append(p)
						tracks.append(couples.setdefault(g, len(couples)))
					del belong[p]
				else:
					belong[p] = track
		return Wire(self.points, indices, tracks, list(couples))
		
		
	def group(self, groups):
		''' return a new mesh linked with this one, containing only the faces belonging to the given groups '''
		if isinstance(groups, set):			pass
		elif hasattr(groups, '__iter__'):	groups = set(groups)
		else:								groups = (groups,)
		edges = typedlist(dtype=uvec2)
		tracks = typedlist(dtype='I')
		for f,t in zip(self.edges, self.tracks):
			if t in groups:
				edges.append(f)
				tracks.append(t)
		return Web(self.points, edges, tracks, self.groups)
		
	def assignislands(self) -> 'Web':
		conn = connpe(self.edges)
		reached = [False] * len(self.edges)
		stack = []
		start = 0
		group = 0
		while True:
			# search start point
			for start in range(start,len(reached)):
				if not reached[start]:
					stack.append(start)
					break
			# end when everything reached
			if not stack:	break
			# propagate
			island = Web(points=self.points, groups=self.groups)
			while stack:
				i = stack.pop()
				if reached[i]:	continue	# make sure this face has not been stacked twice
				reached[i] = True
				yield i, group
				for p in self.edges[i]:
					stack.extend(n	for n in conn[p] if not reached[n])
			group += 1
	
	def groupislands(self) -> 'Web':
		tracks = typedlist.full(0, len(self.edges), dtype='I')
		track = 0
		for edge, track in self.edgeislands():
			tracks[edge] = track
		return Web(self.points, self.edges, tracks, [None]*(track+1))
		
	def islands(self) -> '[Web]':
		''' return the unconnected parts of the mesh as several meshes '''
		islands = []
		island = Web(points=self.points, groups=self.groups)
		for edge, group in self.assignislands():
			if group > len(islands):
				islands.append(island)
				island = Web(points=self.points, groups=self.groups)
			else:
				island.edges.append(self.edges[edge])
				island.tracks.append(self.tracks[edge])
		return islands
	
	def length(self):
		''' total length of edges '''
		s = 0
		for a,b in lineedges(self):
			s += distance(self.points[a], self.points[b])
		return s
	
	def barycenter(self):
		''' curve barycenter of the mesh '''
		if not self.edges:	return vec3(0)
		acc = vec3(0)
		tot = 0
		for e in self.edges:
			a,b = self.edgepoints(e)
			weight = distance(a,b)
			tot += weight
			acc += weight*(a+b)
		return acc / (2*tot)
	
	def arcs(self):
		''' return the contiguous portions of this web '''
		return [Wire(self.points, typedlist(loop, dtype=uvec2))		for loop in suites(self.edges, oriented=False)]
		
	def edgepoints(self, e):
		if isinstance(e, Integral):	e = self.edges[e]
		return self.points[e[0]], self.points[e[1]]
	
	def edgedirection(self, e):
		''' direction of edge e '''
		if isinstance(e, Integral):	e = self.edges[e]
		return normalize(self.points[e[1]] - self.points[e[0]])
	
	def __repr__(self):
		return '<Web with {} points at 0x{:x}, {} edges>'.format(len(self.points), id(self.points), len(self.edges))
	
	def __str__(self):
		return 'Web(\n  points={},\n  edges={},\n  tracks={},\n  groups={},\n  options={})'.format(
					reprarray(self.points, 'points'),
					reprarray(self.edges, 'edges'),
					reprarray(self.tracks, 'tracks'),
					reprarray(self.groups, 'groups'),
					repr(self.options))
					
	def display(self, scene):		
		points = typedlist(dtype=vec3)
		idents = typedlist(dtype='I')
		edges = []
		frontiers = []
		def usept(pi, ident, used):
			if used[pi] >= 0:	
				return used[pi]
			else:
				used[pi] = i = len(points)
				points.append(self.points[pi])
				idents.append(ident)
				return i
		
		for group in range(len(self.groups)):
			used = [-1]*len(self.points)
			frontier = set()
			for edge,track in zip(self.edges, self.tracks):
				if track != group:	continue
				edges.append((usept(edge[0], track, used), usept(edge[1], track, used)))
				for p in edge:
					if p in frontier:	frontier.remove(p)
					else:				frontier.add(p)
			for p in frontier:
				frontiers.append(used[p])
				
		if not points or not edges:
			return displays.Display()
		
		return displays.WebDisplay(scene,
				npcast(points), 
				npcast(edges),
				frontiers,
				idents,
				color=self.options.get('color'))


def glmarray(array, dtype='f4'):
	''' create a numpy array from a list of glm vec '''
	buff = np.array(glm.array(array), copy=False)
	if buff.dtype == np.float64:	buff = buff.astype(np.float32)
	elif buff.dtype == np.int64:	buff = buff.astype(np.int32)
	return buff

def web(*arg):
	''' Build a web object from supported objects:
	
		:web:               return it with no copy
		:wire:              reference points and generate edge couples
		:primitive:         call its ``.mesh`` method and convert the result to web
		:iterable:          convert each element to web and join them
		:list of vec3:      reference it and generate trivial indices
		:iterable of vec3:  get points and generate trivial indices
	'''
	if not arg:	raise TypeError('web take at least one argument')
	if len(arg) == 1:	arg = arg[0]
	if isinstance(arg, Web):		return arg
	elif isinstance(arg, Wire):	
		return Web(
				arg.points, 
				arg.edges(), 
				arg.tracks[:-1] if arg.tracks else None, 
				groups=arg.groups,
				)
	elif hasattr(arg, 'mesh'):
		return web(arg.mesh())
	elif isinstance(arg, (typedlist,list,tuple)) and isinstance(arg[0], vec3):
		return Web(arg, [(i,i+1) for i in range(len(arg)-1)])
	elif hasattr(arg, '__iter__'):
		pool = Web()
		for primitive in arg:
			pool += web(primitive)
		pool.mergeclose()
		return pool
	else:
		raise TypeError('incompatible data type for Web creation')


class Wire(Container):
	''' Line as continuous suite of points 
		Used to borrow reference of points from a mesh by keeping their original indices

		Attributes:
			points:	    points buffer
			indices:	indices of the line's points in the buffer
			tracks:	    group index for each point in indices
						it can be used to associate groups to points or to edges (if to edges, then take care to still have as many track as indices)
			groups:	data associated to each point (or edge)
	'''
	#__slots__ = 'points', 'indices', 'tracks', 'groups'
	
	def __init__(self, points=None, indices=None, tracks=None, groups=None, options=None):
		self.points = ensure_typedlist(points, vec3)
		self.indices = ensure_typedlist(indices if indices is not None else range(len(self.points)), 'I')
		self.tracks = tracks or None
		self.groups = groups or [None]
		self.options = options or {}
	
	def __len__(self):	return len(self.indices)
	def __iter__(self):	return (self.points[i] for i in self.indices)
	def __getitem__(self, i):
		''' return the ith point of the wire, useful to use the wire in a same way as list of points
		
			equivalent to `self.points[self.indices[i]]` 
		'''
		if isinstance(i, Integral):		return self.points[self.indices[i]]
		elif isinstance(i, slice):	return typedlist((self.points[j] for j in self.indices[i]), dtype=vec3)
		else:						raise TypeError('item index must be int or slice')
		
	def flip(self):
		indices = deepcopy(self.indices)
		indices.reverse()
		if self.tracks:
			tracks = deepcopy(self.tracks[:-1])
			tracks.reverse()
			tracks.append(self.tracks[-1])
		else:
			tracks = None
		return Wire(self.points, indices, tracks, self.groups, self.options)
		
	def close(self):
		if self.indices[-1] != self.indices[0]:
			self.indices.append(self.indices[0])
			if self.tracks:
				self.tracks.append(self.tracks[0])
		return self
		
	def segmented(self, group=None):
		''' return a copy of the mesh with a group each edge 
		
			if group is specified, it will be the new definition put in each groups
		'''
		return Wire(self.points, 
					self.indices,
					typedlist(range(len(self.indices)), dtype='I'),
					[group]*len(self.indices),
					self.options,
					)
	
	def mergeclose(self, limit=None):
		''' merge close points ONLY WHEN they are already linked by an edge.
			the meaning of this method is different than `Web.mergeclose()`
		'''
		if limit is None:	limit = self.precision()
		limit *= limit
		merges = {}
		for i in reversed(range(1, len(self.indices))):
			if distance2(self[i-1], self[i]) <= limit:
				merges[self.indices[i]] = self.indices[i-1]
				self.indices.pop(i)
				if self.tracks:
					self.tracks.pop(i-1)
		if distance2(self[0], self[-1]) < limit:
			merges[self.indices[-1]] = self.indices[0]
			self.indices[-1] = self.indices[0]
			if self.tracks:
				self.tracks[-1] = self.tracks[0]
		return merges
		
	def isvalid(self):
		''' return True if the internal data are consistent '''
		try:				self.check()
		except MeshError:	return False
		else:				return True
	
	def check(self):
		''' raise if the internal data are not consistent '''
		if not (isinstance(self.points, typedlist) and self.points.dtype == vec3):	raise MeshError("points must be a typedlist(dtype=vec3)")
		if not (isinstance(self.indices, typedlist) and self.indices.dtype == 'I'): 	raise MeshError("indices must be a typedlist(dtype='I')")
		if self.tracks and not (isinstance(self.tracks, typedlist) and self.tracks.dtype == 'I'): 	raise MeshError("tracks must be a typedlist(dtype='I')")
		l = len(self.points)
		for i in self.indices:
			if i >= l:	raise MeshError("some indices are greater than the number of points", i, l)
		if self.tracks:
			if len(self.indices) != len(self.tracks):	raise MeshError("tracks list doesn't match indices list length")
			if max(self.tracks) >= len(self.groups):	raise MeshError("some tracks are greater than the number of groups", max(self.tracks), len(self.groups))

	def edge(self, i):
		''' ith edge of the wire '''
		return uvec2(self.indices[i], self.indices[i+1])
	def edges(self):
		''' list of successive edges of the wire '''
		return typedlist((self.edge(i)  for i in range(len(self.indices)-1)), dtype=uvec2)
		
	def edgedirection(self, e):
		''' direction of edge e '''
		if isinstance(e, Integral):	e = self.indices[e], self.indices[e+1]
		return normalize(self.points[e[1]] - self.points[e[0]])
	
	def group(self, groups):
		''' return a new mesh Wire with this one, containing only the indices belonging to the given groups '''
		if not self.tracks:
			return self
		if isinstance(groups, set):			pass
		elif hasattr(groups, '__iter__'):	groups = set(groups)
		else:								groups = (groups,)
		indices = typedlist(dtype=self.indices.dtype)
		tracks = typedlist(dtype=self.tracks.dtype)
		for i,t in zip(self.indices, self.tracks):
			if t in groups:
				indices.append(i)
				tracks.append(t)
		return Wire(self.points, indices, tracks, self.groups, self.options)
		
	
	def length(self):
		''' curviform length of the wire (sum of all edges length) '''
		s = 0
		for i in range(1,len(self.indices)):
			s += distance(self[i-1], self[i])
		return s
		
	def barycenter(self):
		''' curve barycenter '''
		if not self.indices:	return vec3(0)
		if len(self.indices) == 1:	return self.points[self.indices[0]]
		acc = vec3(0)
		tot = 0
		for i in range(1,len(self)):
			a,b = self[i-1], self[i]
			weight = distance(a,b)
			tot += weight
			acc += weight*(a+b)
		return acc / (2*tot)
			
		
	def barycenter_points(self):
		''' barycenter of points used '''
		return sum(self.points[i]	for i in self.indices) / len(self.indices)
	
	def vertexnormals(self, loop=False):
		''' return the opposed direction to the curvature in each point 
			this is called normal because it would be the normal to a surface whose section would be that wire
		'''
		normals = typedlist.full(vec3(0), len(self.indices))
		for i in range(len(self.indices)):
			a,b,c = self.indices[i-2], self.indices[i-1], self.indices[i]
			normals[i-1] = normalize(normalize(self.points[b]-self.points[a]) + normalize(self.points[b]-self.points[c]))
		self._make_loop_consistency(normals, loop)
		return normals
		
	def tangents(self, loop=False):
		''' return approximated tangents to the curve as if it was a surface section.
			if this is not a loop the result is undefined.
		'''
		tangents = typedlist.full(vec3(0), len(self.indices))
		for i in range(len(self.indices)):
			a,b,c = self.indices[i-2], self.indices[i-1], self.indices[i]
			tangents[i-1] = normalize(cross(self.points[b]-self.points[a], self.points[b]-self.points[c]))
		self._make_loop_consistency(tangents, loop)
		return tangents
	
	def _make_loop_consistency(self, normals, loop):
		l = len(self.indices)
		# make normals consistent if asked
		if loop:
			# get an outermost point as it is always well oriented
			dir = self[l//2] - self[0]	# WARNING: if those two points are too close the computation is misleaded
			i = max(self.indices, key=lambda i: dot(self.points[i], dir))
			# propagation reorient
			# WARNING: if there is a cusp in the curve (2 consecutive segments with opposite directions) the final result can be wrong
			for i in range(i+1, i+l):
				j = i%l
				e = normalize(self[j]-self[j-1])
				if dot(noproject(normals[j],e), noproject(normals[j-1],e)) < 0:
					normals[j] = -normals[j]
		# propagate to borders if not loop
		else:
			normals[0] = normals[1]
			normals[-1] = normals[-2]
		# propagate to erase undefined normals
		for _ in range(2):
			for i in range(l):
				if glm.any(isnan(normals[i])):	
					normals[i] = normals[i-1]
	
	def normal(self):
		''' return an approximated normal to the curve as if it was the outline of a flat surface.
			if this is not a loop the result is undefined.
		'''
		area = vec3(0)
		c = self[0]
		for i in range(len(self)):
			area += cross(self[i-1]-c, self[i]-c)
		return normalize(area)
	
	def __add__(self, other):
		''' append the indices and points of the other wire '''
		if isinstance(other, Wire):
			r = Wire(
				self.points if self.points is other.points else self.points[:], 
				self.indices[:], 
				self.tracks[:] if self.tracks else None, 
				self.groups if self.groups is other.groups else self.groups[:],
				)
			r.__iadd__(other)
			return r
		else:
			return NotImplemented
			
	def __iadd__(self, other):
		''' append the indices and points of the other wire '''
		if isinstance(other, Wire):		
			li = len(self.indices)
			
			if self.points is other.points:
				self.indices.extend(other.indices)
			else:
				lp = len(self.points)
				self.points.extend(other.points)
				self.indices.extend(i+lp  for i in other.indices)
			
			if self.groups is other.groups:
				if self.tracks or other.tracks:
					if not self.tracks:
						self.tracks = typedlist.full(0, li, 'I')
					self.tracks.extend(other.tracks or typedlist.full(0, len(other.indices), 'I'))
			else:
				lg = len(self.groups)
				self.groups.extend(other.groups)
				if not self.tracks:	
					self.tracks = typedlist.full(0, li, 'I')
				if other.tracks:
					self.tracks.extend(track+lg	for track in other.tracks)
				else:
					self.tracks.extend(typedlist.full(lg, len(other.indices), 'I'))
			return self
		else:
			return NotImplemented
		
	def strippoints(self):
		''' remove points that are used by no edge, return the reindex list.
			if used is provided, these points will be removed without usage verification
			
			return a table of the reindex made
		'''
		self.points = typedlist((self.points[i]	for i in self.indices), dtype=vec3)
		self.indices = typedlist(range(len(self.points)), dtype='I')
		if self.points[-1] == self.points[0]:	
			self.points.pop()
			self.indices[-1] = 0
	
	def display(self, scene):
		w = web(self)
		w.options = self.options
		return w.display(scene)
	
	def __repr__(self):
		return '<Wire with {} points at 0x{:x}, {} indices>'.format(len(self.points), id(self.points), len(self.indices))
	
	def __str__(self):
		return 'Wire(\n  points={},\n  indices={},\n  tracks={},\n  groups={})'.format(
					reprarray(self.points, 'points'),
					reprarray(self.indices, 'indices'),
					reprarray(self.tracks, 'tracks') if self.tracks else None,
					repr(self.groups))
					
	#def __repr__(self):
		#return '<Wire at {:x} with {} points, {} faces>'.format(id(self), len(self.points), len(self.faces))

def wire(*arg):
	''' Build a Wire object from the other compatible types.
		Supported types are:
		
		:wire:              return it with no copy
		:web:               find the edges to joint, keep the same point buffer
		:primitive:         call its ``.mesh`` method and convert the result to wire
		:iterable:          convert each element to Wire and joint them
		:list of vec3:      reference it and put trivial indices
		:iterable of vec3:  create internal point list from it, and put trivial indices
	'''
	if not arg:	raise TypeError('web take at least one argument')
	if len(arg) == 1:	arg = arg[0]
	if isinstance(arg, Wire):		return arg
	elif isinstance(arg, Web):
		indices = suites(arg.edges)
		if len(indices) > 1:	raise ValueError('the given web has junctions or is discontinuous')
		return Wire(arg.points, indices[0], groups=[None])	# TODO: find a way to get the groups from the Web edges through suites or not
	elif hasattr(arg, 'mesh'):
		return wire(arg.mesh())
	elif isinstance(arg, (typedlist,list,tuple)) and isinstance(arg[0], vec3):
		return Wire(arg)
	elif hasattr(arg, '__iter__'):
		pool = Wire()
		for primitive in arg:
			pool += wire(primitive)
		pool.mergeclose()
		return pool
	else:
		raise TypeError('incompatible data type for Wire creation')
		
# --- common tools ----

class mono(object):
	''' this is a class pretending to be an array
		its __getitem__ and __setitem__ will always answer that its elements are its provided `value`
	'''
	__slots__ = 'value',
	
	def __init__(self, value):
		self.value = value
	def __getitem__(self, index):
		if isinstance(index, Integral):	
			return self.value
		elif isinstance(index, slice):
			return [self.value] * ( (index.stop-index.start) // (index.step or 1) )
	def __setitem__(self, index, value):
		self.value = value
	def __iter__(self):
		while True:
			yield self.value

class jitmap(object):
	''' array like map that supports __getitem__ and __setitem__ '''
	__slots__ = 'func', 'inverse', 'source'	
	def __init__(self, source, func, inverse=None):
		self.func = func
		self.source = source
		self.inverse = inverse
		if not callable(func):		raise TypeError('func must be callable')
		if inverse and not callable(inverse):	raise TypeError('inverse must be callable')
		if not hasattr(source, '__getitem__'):	raise TypeError('source has no __getitem__')
		
	def __getitem__(self, index):
		if isinstance(index, Integral):
			return self.func(self.source[index])
		elif isinstance(index, slice):
			return [func(o)	for o in self.source[index]]
		else:
			raise TypeError('index must be int or slice')
			
	def __setitem__(self, index, value):
		if not self.inverse:
			raise TypeError('inverse function not defined for this jitmap')
		if isinstance(index, Integral):
			self.source[index] = self.inverse(value)
		elif isinstance(index, slice):
			self.source[index] = (self.inverse(o)	for o in value)
			
	def __len__(self):
		return len(self.source)
		
	def __iter__(self):
		return map(self.func, self.source)


# connectivity:
		
def edgekey(a,b):
	''' return a key for a non-directional edge '''
	if a < b:	return (a,b)
	else:		return (b,a)
	
def facekeyo(a,b,c):
	''' return a key for an oriented face '''
	if a < b and b < c:		return (a,b,c)
	elif a < b:				return (c,a,b)
	else:					return (b,c,a)
	
def arrangeface(f, p):
	''' return the face indices rotated the way the `p` is the first one '''
	if   p == f[1]:	return f[1],f[2],f[0]
	elif p == f[2]:	return f[2],f[0],f[1]
	else:			return f
	
def arrangeedge(e, p):
	if p == e[1]:	return e[1], e[0]
	else:			return e

def connpp(ngons):
	''' point to point connectivity 
		input is a list of ngons (tuple of 2 to n indices)
	'''
	conn = {}
	for loop in ngons:
		for i in range(len(loop)):
			for a,b in ((loop[i-1],loop[i]), (loop[i],loop[i-1])):
				if a not in conn:		conn[a] = [b]
				elif b not in conn[a]:	conn[a].append(b)
	return conn
	
def connef(faces):
	''' connectivity dictionnary, from oriented edge to face '''
	conn = {}
	for i,f in enumerate(faces):
		for e in ((f[0],f[1]), (f[1],f[2]), (f[2],f[0])):
			conn[e] = i
	return conn
	
def connpe(edges):
	conn = Asso()
	for i,edge in enumerate(edges):
		for p in edge:
			conn.add(p,i)
	return conn

def connexity(links):
	''' return the number of links referencing each point as a dictionnary {point: num links} '''
	reach = {}
	for l in links:
		for p in l:
			reach[p] = reach.get(p,0) +1
	return reach
		
def strippoints(points, indices):
	used = [False] * len(self.points)
	for index in indices:
		if isinstance(index, int):	
			used[p] = True
		else:
			for p in index:
				used[p] = True
	points = typedlist(dtype=self.points.dtype)
	reindices = typedlist(dtype=indices.dtype)
	reindex = typedlist(dtype='I', reserve=len(self.points))
	for p, u in zip(used, self.points):
		if u:
			reindex.append(len(self.points))
			points.append(p)
		else:
			reindex.append(-1)
	for index, t in zip(index, self.tracks):
		if isinstance(index, int):	
			reindices.append(reindex[index])
		else:
			reindices.append([reindex[i]   for i in index])
	return points, reindices, reindex
	

def lineedges(line, closed=False):
	''' yield the successive couples in line '''
	if isinstance(line, Wire):	
		line = line.indices
	line = iter(line)
	j = first = next(line)
	for i in line:
		yield (j,i)
		j = i
	if closed:	yield (i,first)
	
def line_simplification(web, prec=None):
	''' return a dictionnary of merges to simplify edges when there is points aligned.
	
		This function sort the points to remove on the height of the triangle with adjacent points.
		The returned dictionnary is guaranteed without cycles
	'''
	if not prec:	prec = web.precision()
	pts = web.points
	
	# simplify points when it forms triangles with too small height
	merges = {}
	def process(a,b,c):
		# merge with current merge point if height is not sufficient, use it as new merge point
		height = length(noproject(pts[c]-pts[b], pts[c]-pts[a]))
		if height > prec:
			#scn3D.add(text.Text(pts[b], str(height), 8, (1,0,1), align=('left', 'center')))
			return b
		else:
			merges[b] = a
			return a
	
	for k,line in enumerate(suites(web.edges, oriented=False)):
		s = line[0]
		for i in range(2, len(line)):
			s = process(s, line[i-1], line[i])
		if line[0]==line[-1]: process(s, line[0], line[1])
		
	# remove redundancies in merges (there can't be loops in merges)
	for k,v in merges.items():
		while v in merges and merges[v] != v:
			merges[k] = v = merges[v]
	return merges
	

def suites(lines, oriented=True, cut=True, loop=False):
	''' return a list of the suites that can be formed with lines.
		lines is an iterable of edges
		
		Parameters:
			oriented:      specifies that (a,b) and (c,b) will not be assembled
			cut:           cut suites when they are crossing each others
		
		return a list of the sequences that can be formed
	'''
	lines = list(lines)
	# get contiguous suite of points
	suites = []
	while lines:
		suite = list(lines.pop())
		found = True
		while found:
			found = False
			for i,edge in enumerate(lines):
				if edge[-1] == suite[0]:		suite[0:1] = edge
				elif edge[0] == suite[-1]:		suite[-1:] = edge
				# for unoriented lines
				elif not oriented and edge[0] == suite[0]:		suite[0:1] = reversed(edge)
				elif not oriented and edge[-1] == suite[-1]:	suite[-1:] = reversed(edge)
				else:
					continue
				lines.pop(i)
				found = True
				break
			if loop and suite[-1] == suite[0]:	break
		suites.append(suite)
	# cut at suite intersections (sub suites or crossing suites)
	if cut:
		reach = {}
		for suite in suites:
			for p in suite:
				reach[p] = reach.get(p,0) + 1
		for suite in suites:
			for i in range(1,len(suite)-1):
				if reach[suite[i]] > 1:
					suites.append(suite[i:])
					suite[i+1:] = []
					break
	return suites
	

def distance2_pm(point, mesh) -> '(d, prim)':
	''' squared distance from a point to a mesh
	'''
	if isinstance(mesh, Mesh):
		def analyse():
			for face in mesh.faces:
				f = mesh.facepoints(face)
				n = cross(f[1]-f[0], f[2]-f[0])
				if not n:	continue
				# check if closer to the triangle's edges than to the triangle plane
				plane = True
				for i in range(3):
					d = f[i-1]-f[i-2]
					if dot(cross(n, d), point-f[i-2]) < 0:
						x = dot(point-f[i-2], d) / length2(d)
						# check if closer to the edge points than to the edge axis
						if x < 0:	yield distance2(point, f[i-2]), face[i-2]
						elif x > 1:	yield distance2(point, f[i-1]), face[i-1]
						else:		yield length2(noproject(point - f[i-2], d)), (face[i-2], face[i-1])
						plane = False
						break
				if plane:
					yield dot(point-f[0], n) **2 / length2(n), face
	elif isinstance(mesh, (Web,Wire)):
		def analyse():
			if isinstance(mesh, Web):	edges = mesh.edges
			else:						edges = mesh.edges()
			for edge in edges:
				e = mesh.edgepoints(edge)
				d = e[1]-e[0]
				x = dot(point - e[0], d) / length2(d)
				# check if closer to the edge points than to the edge axis
				if x < 0:	yield distance2(point, e[0]), e[0]
				elif x > 1:	yield distance2(point, e[1]), e[1]
				else:		yield length2(noproject(point - e[0], d)), e
	elif isinstance(mesh, vec3):
		return distance2(point, mesh), 0
	else:
		raise TypeError('cannot evaluate distance from vec3 to {}'.format(type(mesh)))
	return min(analyse(), key=lambda t:t[0])
	
	
def distance2_pm(point, mesh) -> '(d, prim)':
	''' squared distance from a point to a mesh
	'''
	score = inf
	best = None
	if isinstance(mesh, Mesh):
		for face in mesh.faces:
			f = mesh.facepoints(face)
			n = cross(f[1]-f[0], f[2]-f[0])
			if not n:	continue
			# check if closer to the triangle's edges than to the triangle plane
			plane = True
			for i in range(3):
				d = f[i-1]-f[i-2]
				if dot(cross(n, d), point-f[i-2]) < 0:
					x = dot(point-f[i-2], d) / length2(d)
					# check if closer to the edge points than to the edge axis
					if x < 0:	dist, candidate = distance2(point, f[i-2]), face[i-2]
					elif x > 1:	dist, candidate = distance2(point, f[i-1]), face[i-1]
					else:		dist, candidate = length2(noproject(point - f[i-2], d)), (face[i-2], face[i-1])
					plane = False
					break
			if plane:
				dist, candidate = dot(point-f[0], n) **2 / length2(n), face
			if dist < score:
				best, score = candidate, dist
	elif isinstance(mesh, (Web,Wire)):
		if isinstance(mesh, Web):	edges = mesh.edges
		else:						edges = mesh.edges()
		for edge in edges:
			e = mesh.edgepoints(edge)
			d = e[1]-e[0]
			x = dot(point - e[0], d) / length2(d)
			# check if closer to the edge points than to the edge axis
			if x < 0:	dist, candidate = distance2(point, e[0]), edge[0]
			elif x > 1:	dist, candidate = distance2(point, e[1]), edge[1]
			else:		dist, candidate = length2(noproject(point - e[0], d)), edge
			if dist < score:
				best, score = candidate, dist
	elif isinstance(mesh, vec3):
		return distance2(point, mesh), 0
	else:
		raise TypeError('cannot evaluate distance from vec3 to {}'.format(type(mesh)))
	return score, best

def mesh_distance(m0, m1) -> '(d, prim0, prim1)':
	''' minimal distance between elements of meshes 
	
		The result is a tuple `(distance, primitive from m0, primitive from m1)`.
		`primitive` can be:
		
			:int:				index of the closest point
			:(int,int):			indices of the closest edge
			:(int,int,int): 	indices of the closest triangle
	'''
	# compute distance from each points of m to o
	def analyse(m, o):
		# get an iterator over actually used points only
		if isinstance(m, Mesh):
			usage = [False]*len(m.points)
			for f in m.faces:
				for p in f:	usage[p] = True
			it = (i for i,u in enumerate(usage) if u)
		elif isinstance(m, Web):
			usage = [False]*len(m.points)
			for e in m.edges:
				for p in e:	usage[p] = True
			it = (i for i,u in enumerate(usage) if u)
		elif isinstance(m, Wire):
			it = m.indices
		elif isinstance(m, vec3):
			return (*distance2_pm(m, o), 0)
		# comfront to the mesh
		return min((
				(*distance2_pm(m.points[i], o), i)
				for i in it), 
				key=lambda t:t[0])
	# symetrical evaluation
	d0 = analyse(m0, m1)
	d1 = analyse(m1, m0)
	if d0[0] < d1[0]:	return (sqrt(d0[0]), d0[2], d0[1])
	else:				return (sqrt(d1[0]), d1[1], d1[2])
	
		

def mktri(mesh, pts, track=0):
	''' append a triangle '''
	mesh.faces.append(pts)
	mesh.tracks.append(track)

def mkquad(mesh, pts, track=0):
	''' append a quad, choosing the best diagonal '''
	if (	distance2(mesh.points[pts[0]], mesh.points[pts[2]]) 
		<=	distance2(mesh.points[pts[1]], mesh.points[pts[3]]) ):
		mesh.faces.append((pts[:-1]))
		mesh.faces.append((pts[3], pts[0], pts[2]))
	else:
		mesh.faces.append((pts[0], pts[1], pts[3]))
		mesh.faces.append((pts[2], pts[3], pts[1]))
	mesh.tracks.append(track)
	mesh.tracks.append(track)


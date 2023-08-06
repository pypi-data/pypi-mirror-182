import freetype
from dataclasses import dataclass
from .mathutils import *
from .primitives import Segment
from .mesh import Wire, Web, Mesh, web
from .triangulation import triangulation
from . import settings



BezierLinear = Segment

@dataclass
class BezierQuadratic:
	a: vec3
	b: vec3
	c: vec3
	
	def __call__(self, t):
		u = 1-t
		return u**2*self.a + 2*u*t*self.b + t**2*self.c
		
	def mesh(self, resolution=None):
		div = settings.curve_resolution(
			distance(self.a, self.b) + distance(self.b, self.c),
			anglebt(self.b-self.a, self.c-self.b),
			resolution)
		return Wire(self(t)  for t in linrange(0, 1, div=div))
		
	def display(self, scene):
		return self.mesh().display(scene)
	
@dataclass
class BezierCubic:
	a: vec3
	b: vec3
	c: vec3
	d: vec3
	
	def __call__(self, t):
		u = 1-t
		return u**3*self.a + 3*u**2*t*self.b + 3*u*t**2*self.c + t**3*self.d
		
	def mesh(self, resolution=None):
		div = settings.curve_resolution(
			distance(self.a, self.b) + distance(self.b, self.c) + distance(self.c, self.d),
			anglebt(self.b-self.a, self.c-self.b) + angletbt(self.c-self.b, self.d-self.c),
			resolution)
		return Wire(self(t)  for t in linrange(0, 1, div=div))
		
	def display(self, scene):
		return self.mesh().display(scene)
		
cache_fonts = {}

@dataclass
class CharacterCache:
	cbox: Box = None
	web: Web = None
	mesh: Mesh = None


def ft2vec(ft):   return vec3(ft.x, ft.y, 0)

def character_primitives(face):
	primitives = []
	last = [None]

	def move_to(a, ctx):
		last[0] = ft2vec(a)
	def line_to(b, ctx):
		primitives.append(BezierLinear(last[0], ft2vec(b)))
		last[0] = ft2vec(b)
	def conic_to(b, c, ctx):
		primitives.append(BezierQuadratic(last[0], ft2vec(b), ft2vec(c)))
		last[0] = ft2vec(c)
	def cubic_to(b, c, d, ctx):
		primitives.append(BezierCubic(last[0], ft2vec(b), ft2vec(c), ft2vec(d)))
		last[0] = ft2vec(d)
		# in fact there will be no cubic_to because there is no such things in freetype fonts, but just in case for freetype-py
	
	face.glyph.outline.decompose(move_to=move_to, line_to=line_to, conic_to=conic_to, cubic_to=cubic_to)
	return primitives
	
def character_box(face):
	box = face.glyph.outline.get_cbox()
	return Box(
			min=vec3(box.xMin, box.yMin, 0), 
			max=vec3(box.xMax, box.yMax, 0))
	
def character_outline(char, font, resolution=None):
	try:	
		return cache_fonts[font][char]
	except (KeyError, AttributeError):
		if font not in cache_fonts:			cache_fonts[font] = {}
		if char not in cache_fonts[font]:	cache_fonts[font][char] = CharacterCache()
		cache = cache_fonts[font][char]
		
		if isinstance(font, str):
			face = freetype.Face(font)
		else:
			face = font
		scale = 1024
		face.set_char_size(scale)
		face.load_char(char)
		cache.fixed = face.is_fixed_width
		cache.cbox = character_box(face) .transform(1/scale)
		cache.web = result = web(character_primitives(face), resolution=resolution) .transform(1/scale) .mergegroups()
		return cache

def character_surface(char, font, resolution=None):
	try:	
		return cache_fonts[font][char]
	except (KeyError, AttributeError):
		cache = character_outline(char, font, resolution)
		cache.mesh = result = triangulation(cache.web)
		return cache

def text(text, font, size=1, spacing=vec2(0.05, 0.2), fill=True, resolution=None):
	if fill:	
		pool = Mesh()
		character = character_surface
	else:
		pool = Web()
		character = character_outline
	
	face = freetype.Face(font)
	position = vec3(0)
	for char in text:
		if char == ' ':
			position.x += 0.3
		elif char == '\t':
			width = 0.3
			position.x += int(position.x/width) * width
		elif char == '\n':
			position.y -= (1+spacing.y)
			position.x = 0
		else:
			cache = character(char, face, resolution)
			if fill:	part = cache.mesh
			else:		part = cache.web
			pool += part.transform(position-vec3(cache.cbox.min.x,0,0))
			if cache.fixed:
				position.x += 0.5 + spacing.x
			else:
				position.x += cache.cbox.width.x + spacing.x
	return pool.transform(size)

	

def test_character_primitives():
	from .rendering import show
	
	face = freetype.Face('cad/pymadcad/madcad/NotoMono-Regular.ttf')
	face.set_char_size(1024)
	face.load_char('&')
	show([ triangulation(character_primitives(face)) ])

def test_character_cached():
	from .rendering import show
	show([ 
		character_outline('&', 'cad/pymadcad/madcad/NotoMono-Regular.ttf').web,
		character_surface('g', 'cad/pymadcad/madcad/NotoMono-Regular.ttf').mesh.transform(vec3(1,0,0)),
		])
		
def test_text():
	from .rendering import show
	from .generation import extrusion
	part = text('Hello everyone.\nthis is a great font !!', 'cad/pymadcad/madcad/NotoSans-Regular.ttf')
	part = extrusion(vec3(0,0,-1), part.flip())
	show([
		vec3(0),
		part,
		], display_wire=True)

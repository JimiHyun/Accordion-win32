'''OpenGL extension OES.read_format

This module customises the behaviour of the 
OpenGL.raw.GL.OES.read_format to provide a more 
Python-friendly API

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/OES/read_format.txt
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions, wrapper
from OpenGL.GL import glget
import ctypes
from OpenGL.raw.GL.OES.read_format import *
### END AUTOGENERATED SECTION
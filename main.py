import OpenGL.GL as GL
import glfw
import numpy as np
import pyrr
from glutils import *
from ctypes import sizeof, c_float, c_void_p
from objet3d import Objet3D
from primitives import create_plan, create_cube, create_sphere
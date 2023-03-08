import math
from os.path import abspath, basename, splitext
from typing import Sequence

from bpy.ops import mesh, object


def generate_screen_name(file_path: str):
    current_file_name = basename(abspath(file_path))
    return splitext(current_file_name)[0]


def to_radians(*args: Sequence[int]):
    """Degrees to radians."""
    return tuple(map(math.radians, args))


def set_essential_objects():
    """Creates cube, camera and light (Sun) objects."""
    mesh.primitive_cube_add()
    object.camera_add(
        location=(5, 6, 4.5),
        rotation=to_radians(60, 0, 140)
    )
    object.light_add(
        type='SUN', location=(4.5, 2, 6),
        rotation=to_radians(-8, 3, -9)
    )


def set_params(obj, **kwargs):
    """Set key value params to provided object."""
    for k, v in kwargs.items():
        setattr(obj, k, v)

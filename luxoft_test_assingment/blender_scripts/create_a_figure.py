import math
import os

from bpy import data, context
from bpy.ops import mesh, object, render, text, wm
from typing import Sequence

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def to_radians(*args: Sequence[int]):
    return tuple(map(math.radians, args))


def generate_screen_name():
    current_file_name = os.path.basename(os.path.abspath(__file__))
    return os.path.splitext(current_file_name)[0]


# получение аргументов из запускающего скрипта
# запустить скрипт как модуль, чтобы обращаться к его элементам
text.open(filepath=os.path.join(base_dir, "argparser.py"))
argparser = data.texts["argparser.py"].as_module()
args = argparser.parser.parse_args()

# create new empty file
wm.read_homefile(use_empty=True)

# set scene objects, lights, cameras
mesh.primitive_cube_add()
object.camera_add(location=(5, 6, 4.5), rotation=to_radians(60, 0, 140))
object.light_add(
    type='SUN', location=(4.5, 2, 6), rotation=to_radians(-8, 3, -9)
)

# render
scene = context.scene
# bound camera with the scene
scene.camera = data.objects['Camera']
scene.render.resolution_y = args.y_resolution
scene.render.resolution_x = args.x_resolution
screen_name = generate_screen_name()
scene.render.filepath = os.path.join(args.output_path, f'{screen_name}_shot')
render.render(write_still=True)

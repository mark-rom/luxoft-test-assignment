from os.path import abspath, dirname, join

from bpy import context, data
from bpy.ops import render, text, wm

base_dir = dirname(dirname(abspath(__file__)))

text.open(filepath=join(base_dir, "argparser.py"))
argparser = data.texts["argparser.py"].as_module()
args = argparser.parser.parse_args()

text.open(filepath=join(base_dir, 'blender_scripts/scripts_utils/utils.py'))
scripts_utils = data.texts['utils.py'].as_module()
screen_name = scripts_utils.generate_screen_name(__file__)

# create new empty file
wm.read_homefile(use_empty=True)

# set scene objects, lights, cameras
scripts_utils.set_essential_objects()

# render
scene = context.scene
scripts_utils.set_params(scene, camera=data.objects['Camera'])
scripts_utils.set_params(
    scene.render,
    resolution_y=args.y_resolution,
    resolution_x=args.x_resolution,
    filepath=join(args.output_path, f'{screen_name}_shot')
)

render.render(write_still=True)

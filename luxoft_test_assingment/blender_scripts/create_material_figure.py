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
cube = data.objects['Cube']

# создание и применение нового материала на объект
material = data.materials.new('test_material')
material.use_nodes = True
mat_nodes = material.node_tree.nodes["Principled BSDF"]
mat_nodes.inputs[0].default_value = (0.0670657, 0.0529372, 0.8, 1)

if cube.data.materials:
    # assign to 1st material slot
    cube.data.materials[0] = material
else:
    # no slots
    cube.data.materials.append(material)

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

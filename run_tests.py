from os.path import join
from subprocess import run, STDOUT

from luxoft_test_assingment.argparser import parser

from luxoft_test_assingment import utils as u


@u.timer
def run_tests(cli_args, script_path, log_file):
    run(
        args=[
            cli_args.blender_path, '-b',
            '--python', script_path, '--',
            '--output_path', cli_args.output_path,
            '--x_resolution', str(cli_args.x_resolution),
            '--y_resolution', str(cli_args.y_resolution)
        ],
        stdout=log_file,
        stderr=STDOUT
    )


if __name__ == '__main__':

    cli_args = parser.parse_args()

    u.create_dir_if_not_exist(cli_args.output_path)
    u.set_path(cli_args, ('output_path', 'blender_path'))

    scripts_path = u.get_scripts_path('blender_scripts')
    scripts_names = u.get_scripts_names(scripts_path)

    for script in scripts_names:

        script_path = join(scripts_path, script)
        file_name = u.get_filename(script_path)

        log_path = join(cli_args.output_path, f'{file_name}_log.txt')
        json_path = join(cli_args.output_path, f'{file_name}_info.json')

        with open(log_path, 'w') as log_file:
            runtime_data = run_tests(cli_args, script_path, log_file)

        with open(json_path, 'w') as json_file:
            u.create_test_json(script_path, runtime_data, json_file)

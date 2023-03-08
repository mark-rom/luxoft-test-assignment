import json
import platform
from datetime import datetime
from functools import wraps
from os import listdir, mkdir, path
from typing import BinaryIO, List, Optional, Sequence

import psutil


def create_dir_if_not_exist(dir_name: str):
    if not path.isdir(dir_name):
        mkdir(dir_name)


def get_scripts_path(dir_name: str = 'blender_scripts'):
    """Returns path to directory with blender scripts."""
    current_dir = path.dirname(path.abspath(__file__))
    return path.join(current_dir, dir_name)


def get_scripts_names(scrpt_path: str) -> List[str]:
    """Returns list of filenames for given path."""
    scripts_names = []
    for file in listdir(scrpt_path):
        if path.isfile(path.join(scrpt_path, file)):
            scripts_names.append(file)
    return scripts_names


def set_path(cli_args, arg_names):
    for arg in arg_names:
        if arg:
            value = path.abspath(getattr(cli_args, arg))
            setattr(cli_args, arg, value)


def get_filename(file_path: str = None):
    """Returns filename without extention from given path."""
    if file_path is None:
        file_path = __file__
    filename = path.basename(path.abspath(file_path))
    return path.splitext(filename)[0]


def timer(func):
    """Simple decorator to measure execution time for given func.
    Modifies func return to a tuple (start_time, end_time, duration)."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = datetime.now()
        func(*args, **kwargs)
        end_time = datetime.now()
        duration = str(end_time - start_time)
        return str(start_time), str(end_time), duration
    return wrapper


def create_test_json(
    script_path: str, runtime_data: Sequence,
    output_file: Optional[BinaryIO] = None
):
    """Creates a json file with next information about executed test:
    test_name, test_start_datetime, test_end_datetime, test_duration
    and system_data for CPU, RAM, OS."""

    if output_file is None:
        file_path = path.dirname(path.abspath(__file__))
        output_file = open(path.join(
            file_path, f'{get_filename(script_path)}_test_info.json'
        ), 'w')

    uname = platform.uname()

    json.dump(
        {
            'test_name': f'{get_filename(script_path)}_test',
            'test_start_datetime': runtime_data[0],
            'test_end_datetime': runtime_data[1],
            'test_duration': runtime_data[2],
            'system_data': {
                'CPU': f'{uname.processor} {_count_cpu_frequency()} GHz',
                'RAM': f"{_get_ram_info()} GB",
                'OS': f'{uname.system}'
            }
        },
        fp=output_file
    )


def _count_cpu_frequency() -> float:
    """Returns CPU frequency in GHz."""
    return psutil.cpu_freq().max/100


def _get_ram_info() -> int:
    """Returns information about RAM in GBs."""
    value_in_gb = psutil.virtual_memory().total / (1024.0 ** 3)
    return round(value_in_gb)


if __name__ == '__main__':
    data = ("07/03/2023, 16:12:42", "07/03/2023, 16:12:55", "0:00:12.675684")
    create_test_json(data)

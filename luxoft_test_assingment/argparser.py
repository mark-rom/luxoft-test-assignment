import argparse
import sys


class ArgumentParserForBlender(argparse.ArgumentParser):
    """
    This class is identical to its superclass, except for the parse_args
    method (see docstring). It resolves the ambiguity generated when calling
    Blender from the CLI with a python script, and both Blender and the script
    have arguments. E.g., the following call will make Blender crash because
    it will try to process the script's -a and -b flags:
    >>> blender --python my_script.py -a 1 -b 2

    To bypass this issue this class uses the fact that Blender will ignore all
    arguments given after a double-dash ('--'). The approach is that all
    arguments before '--' go to Blender, arguments after go to the script.
    The following calls work fine:
    >>> blender --python my_script.py -- -a 1 -b 2
    >>> blender --python my_script.py --
    """

    def parse_args(self):
        """
        This method is expected to behave identically as in the superclass,
        except that the sys.argv list will be pre-processed using
        _get_argv_after_doubledash before. See the docstring of the class for
        usage examples and details.
        """
        try:
            idx = sys.argv.index("--")
            return super().parse_args(args=sys.argv[idx+1:])
        except ValueError:
            return super().parse_args()


parser = ArgumentParserForBlender()


parser.add_argument(
    "--blender_path",
    action="store",
    help="expects path to a blender file"
)
parser.add_argument(
    '--output_path',
    action="store",
    help="expects path to output_data folder"
)
parser.add_argument(
    '--x_resolution',
    action="store",
    type=int,
    help="expects witdh parameter for rendered pictures"
)
parser.add_argument(
    '--y_resolution',
    action="store",
    type=int,
    help="expects height parameter for rendered pictures"
)

from .exceptions import CommandError
from importlib import import_module
import pathlib

import sys

def print_error_message(error_text: str):
    sys.stderr.write(
        "\n" + error_text + "\n"
    )
    sys.exit(1)


def validate_name(name: str, name_or_dir: str='name'):
        # Check it's a valid directory name.
        if not name.isidentifier():
            error_text = "invalid project name. Your project name must follow the Python\n" \
                "variable naming convention"
            sys.stderr.write(
                "\n" + error_text + "\n"
            )

        # Check it cannot be imported.
        try:
            import_module(name)
        except ImportError:
            pass
        else:
            error_text =  f"'{name}' conflicts with the name of an existing Python " \
                "module and cannot be used as project. Please try " \
                "another name"
            print_error_message(error_text)


def rename_file(old_name: str, new_name: str, base_dir: pathlib.Path):
        (base_dir / old_name).rename(base_dir / new_name)
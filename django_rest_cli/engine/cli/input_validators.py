import sys
from importlib import import_module

from django_rest_cli.engine import print_error_message


def validate_name(name: str, name_or_dir: str='name'):
        # Check it's a valid identifier.
        if not name.isidentifier():
            error_text = "Invalid project name. Check that the project name is a " \
                "valid Python Identifier"
            print_error_message(error_text)

        # Check it cannot be imported.
        try:
            import_module(name)
        except ImportError:
            pass
        else:
            error_text =  f"'{name}' conflicts with the name of an existing Python " \
                "module and cannot be used. Please try " \
                "another name."
            print_error_message(error_text)
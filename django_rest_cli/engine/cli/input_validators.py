from importlib import import_module

from django_rest_cli.engine import raise_error_message
from django_rest_cli.engine.exceptions import ProjectAppNameError


def validate_name(name: str, name_or_dir: str = "name") -> None:
    # Check it's a valid identifier.
    if not name.isidentifier():
        error_text: str = (
            "Invalid project name. Check that the project name is a "
            "valid Python Identifier"
        )
        raise_error_message(error_text, ProjectAppNameError)

    # Check it cannot be imported.
    try:
        import_module(name)
    except ImportError:
        pass
    else:
        error_text: str = (
            f"'{name}' conflicts with the name of an existing Python "
            "module and cannot be used. Please try "
            "another name."
        )
        raise_error_message(error_text, ProjectAppNameError)

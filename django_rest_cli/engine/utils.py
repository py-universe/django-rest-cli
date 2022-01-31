from django_rest_cli.engine import CommandError
from importlib import import_module


def validate_name(name, name_or_dir='name'):
       
        # Check it's a valid directory name.
        if not name.isidentifier():
            raise CommandError("invalid project name. Your project name must follow the Python\n" \
                "variable naming convention")

        # Check it cannot be imported.
        try:
            import_module(name)
        except ImportError:
            pass
        else:
            raise CommandError(
                "'{name}' conflicts with the name of an existing Python "
                "module and cannot be used as project. Please try "
                "another name")
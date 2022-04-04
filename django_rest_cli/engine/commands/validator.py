import os
from pathlib import Path
from pathlib import Path

from django_rest_cli.engine import print_error_message

def is_django_project_directory():
    cwd: Path = Path.cwd()
    file: Path = cwd / 'manage.py'
    
    if file not in cwd.iterdir(): # manage.py file in current directory?
        error_text: str = "Command Failed. Make sure to execute command in a Django project directory"
        print_error_message(error_text)
    else:
        # If command executed within a django project, make the settings.py module 
        # Of the project available to this package
        dir_name: str = Path.cwd().name
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', f"{dir_name}.settings")
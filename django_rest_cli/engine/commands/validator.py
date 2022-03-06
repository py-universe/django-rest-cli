from pathlib import Path

from django_rest_cli.engine import print_error_message

def is_django_project_directory():
    cwd = Path.cwd()
    file = cwd / 'manage.py'
    
    if file not in cwd.iterdir(): # manage.py file in current directory?
        error_text = "Command Failed. Make sure to execute command in a Django project directory"
        print_error_message(error_text)
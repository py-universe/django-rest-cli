import argparse
from .cli_commands import CliCommands

def main():
    parser = argparse.ArgumentParser(prog="drf-cli")
    subparsers = parser.add_subparsers()

    # Start project command parser
    startproject_parser = subparsers.add_parser(
        'startproject'
    ) 
    startproject_parser.add_argument(
        "project_name", 
        type=str, 
        help="a valid python variable"
    )
    startproject_parser.set_defaults(func=CliCommands.start_project)
        
    # Startapp command parser
    startproject_apps = subparsers.add_parser(
        'startapps'
    ) 
    startproject_apps.add_argument(
        "apps", 
        nargs='*',  # Accept multiple app names
        help="name(s) of app(s) to be created'",
    )
    startproject_apps.set_defaults(func=CliCommands.start_apps)

    # Add plugins command parser
    startproject_apps = subparsers.add_parser(
        'add'
    ) 
    startproject_apps.add_argument(
        "plugins", 
        nargs='*' , # Accept multiple app names
        help="name(s) of plugin(s) to be added to project'",
    )
    
    # Generate crud endpoints command parser
    startproject_apps = subparsers.add_parser(
        'add'
    ) 
    startproject_apps.add_argument(
        "plugins", 
        nargs='*' , # Accept multiple plugin names
        help="name(s) of plugin(s) to be added to project'",
    )

    args = parser.parse_args()
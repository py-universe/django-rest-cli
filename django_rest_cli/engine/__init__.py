# import modules to be used in other modules in this project
from distutils.log import error
from django_rest_cli.engine.utils import validate_name, print_error_message
from django_rest_cli.engine.exceptions import CommandError
# ___________________________________________________ end

from django_rest_cli.engine.commands import (
    StartApp,
    StartProject
)
from django_rest_cli.engine.cli_args_parsers import (
    ActionArgsParser, 
)


def main():
    action_parser = ActionArgsParser()
    args = action_parser.args

    if args.action == "startapps":
        if args.apps:
            StartApp.create_multiple_apps(args.apps)
        else:
            error_text = f"'{args.action}' expects one or more app names \n E.g. startapps app_1 app_2 app_3\n"
            print_error_message(error_text)

    elif args.action == "startproject":
            StartProject.start_project()

    elif args.action == "generate-crud-endpoints":
        print("command logic still in the works")

    else:
        error_text = f"'{args.action}' is not a valid action\n" \
             "It should be either 'startapps', 'startproject' or 'generate-crud-endpoints'\n"
        print_error_message(error_text)

import argparse
from calendar import c
from importlib import import_module
import sys

from django_rest_cli.engine.exceptions import CommandError
from django_rest_cli.engine.utils import validate_name

from django_rest_cli.engine.commands import (
    start_project
)
from django_rest_cli.engine.cli_args_parsers import (
    ActionArgsParser, 
    StartprojectArgsParser, 
    CrudengineArgsParser,
    create_apps
)


def main():
    action_parser = ActionArgsParser()
    args = action_parser.args

    if args.action == "startapps":
        if args.apps:
            create_apps(args.apps)
        else:
            sys.stderr.write(
                f"'{args.action}' expects one or more app names \n"
                f"E.g. startapps app_1 app_2 app_3\n"
            )
            sys.exit(1)

    elif args.action == "startproject":
        if args.project_name:
            start_project(args.project_name)
        else:
            sys.stderr.write(
                f"'{args.action}' expects a valid project name \n"
            )
            sys.exit(1)

    elif args.action == "generate-crud-endpoints":
        print("command logic still in the works")

    else:
        sys.stderr.write(
            f"'{args.action}' is not a valid action\n"
            f"It should be either 'startapps', 'startproject' or 'generate-crud-endpoints'\n"
        )
        sys.exit(1)

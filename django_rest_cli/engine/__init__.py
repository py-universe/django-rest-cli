import argparse
from calendar import c
import sys

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
        # start_project(args.name) # project created in the directory where command is invoked
        print("logic for this still in the works")

    elif args.action == "generate-crud-endpoints":
        print("command logic still in the works")
    else:
        sys.stderr.write(
            f"'{args.action}' is not a valid action"
            f"It should be either 'startapps', 'startproject' or 'generate-crud-endpoints'\n"
        )
        sys.exit(1)

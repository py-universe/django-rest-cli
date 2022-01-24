import argparse
import sys

from django_rest_cli.engine.commands import (
    start_apps, start_project
)


parser = argparse.ArgumentParser()

parser.add_argument(
    "what", type=str, help="What is to be started: 'app' for app, 'project' for project"
)
parser.add_argument(
    "name", type=str, help="The name of the app or project to be started"
)
parser.add_argument(
    "directory",
    nargs="?",
    type=str,
    help="Optional base directory to start the app or project in",
    default=None,
)


def main():
    args = parser.parse_args()

    if args.what == "startapps":
        start_apps(args.name, args.directory)
    elif args.what == "startproject":
        start_project(args.name, args.directory)
    else:
        sys.stderr.write(
            f"'{args.what}' is not a valid thing to start. "
            f"It should be either 'startapps' or 'startproject'\n"
        )
        sys.exit(1)

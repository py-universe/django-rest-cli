from argparse import ArgumentParser

from .cli_commands import CliCommands


async def main():
    parser: ArgumentParser = ArgumentParser(prog="drf-cli")
    subparsers = parser.add_subparsers()

    # Start project command parser
    startproject_parser = subparsers.add_parser("startproject")
    startproject_parser.add_argument(
        "project_name", type=str, help="a valid python variable"
    )
    startproject_parser.set_defaults(func=CliCommands.start_project)

    # Startapp command parser
    startproject_apps = subparsers.add_parser("startapps")
    startproject_apps.add_argument(
        "apps",
        nargs="*",  # Accept multiple app names
        help="name(s) of app(s) to be created'",
    )
    startproject_apps.set_defaults(func=CliCommands.start_apps)
    
    args = parser.parse_args()
    # Await asynchronous functions
    if args.func.__name__ == "start_apps" or args.func.__name__ == "start_project":
        await args.func(args)  # Invoke whatever function was selected async
    else:
        args.func(args)  # Sync

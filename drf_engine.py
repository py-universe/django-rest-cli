import sys


def main():
    try:
        from drf_project_builder.engine import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import drf_project_builder."
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()


# this is going to be our entry point for running management commands.
# E.g drf_engine.py [command-- startproject/startapps]
# However when we upload this package to pypi we won't be need this file
# We'd specify the entry point in the setup.cfg file like so:
# [options.entry_points]
# console_scripts =
#    drf-engine = drf_project_builder.engine:execute_from_command_line
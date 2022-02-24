from re import I
from django_rest_cli.engine import main


if __name__ == '__main__':
    main()


# this is going to be our entry point for running management commands.
# E.g dr_cli.py [command-- startproject/startapps]
# However when we upload this package to pypi we won't be needing this file
# We'd specify the entry point in the setup.cfg file like so:
# [options.entry_points]
# console_scripts =
#    dr-cli = drf_project_builder.engine:main
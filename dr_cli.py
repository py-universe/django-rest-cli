import time

from django_rest_cli.engine import entry_point

if __name__ == "__main__":
    start: time = time.perf_counter()
    entry_point()

    interval: time = time.perf_counter() - start
    print(f"Execution Time: {interval}")


# this is going to be our entry point for running management commands.
# E.g dr_cli.py [command-- startproject/startapps]
# However when we upload this package to pypi we won't be needing this file
# We'd specify the entry point in the setup.cfg file like so:
# [options.entry_points]
# console_scripts =
#    dr-cli = django_rest_cli.engine:entry_point

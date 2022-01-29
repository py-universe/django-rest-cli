from typing import List

from django_rest_cli.engine.commands import (
    start_apps
)

def create_apps(apps: List) -> None:
    for app in apps:
        start_apps(app) # apps created in the directory where command is invoked
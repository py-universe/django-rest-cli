from django.conf import settings

from typing import Optional, List
import os
import pathlib

from .base import Base, Startable


class StartApp(Base):

    @staticmethod
    def _update_installed_apps(apps: List) -> None:
        print(getattr(settings, 'INSTALLED_APPS')) 

    @staticmethod
    def _start( name: str, directory: Optional[str] = None) -> None:
        what: Startable = Startable.APP
        directive: str = f'start{what.name.lower()}'
        template: str = f'{what.name}_TEMPLATES_DIR'

        Base.run_cmd_command(
            directive, name, directory, template
        )


    @classmethod
    def create_multiple_apps(cls, apps: List) -> None:
        for app in apps:
            cls._start(app) # apps created in the directory where command is invoked

        cls._update_installed_apps(apps) # Not working
        
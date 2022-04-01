from django.conf import settings

from typing import Optional, List
import os
import pathlib
import asyncio

from .base import Base, Startable


class StartApp(Base):

    @staticmethod
    def _update_installed_apps(apps: List) -> None:
        print(getattr(settings, 'INSTALLED_APPS')) 

    @staticmethod
    async def __start( name: str, directory: Optional[str] = None) -> None:
        what: Startable = Startable.APP
        directive: str = f'start{what.name.lower()}'
        template: str = f'{what.name}_TEMPLATES_DIR'

        await Base.run_cmd_command(
            directive, name, directory, template
        )


    @classmethod
    async def create_multiple_apps(cls, apps: List) -> None:
        funcs = []
        for app in apps:
            funcs.append(
                asyncio.ensure_future(cls.__start(app))
            )
        await asyncio.gather(*funcs)
        
        # response = await asyncio.gather(*funcs)
        # return response
        # for app in apps:
        #     cls._start(app) # apps created in the directory where command is invoked

        # cls._update_installed_apps(apps) # Not working
        
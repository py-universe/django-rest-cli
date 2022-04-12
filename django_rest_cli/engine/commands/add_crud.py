import os
import asyncio
import pathlib
from typing import List

import django

from django_rest_cli.engine import print_exception
from django_rest_cli.engine.exceptions import NoModelsFoundError


class AddCrud:
    @staticmethod
    async def __add(app_label: str) -> None:
        try:
            from django.apps import apps as project_apps
            from django.apps import AppConfig

            if project_apps.ready:
                config: AppConfig = project_apps.get_app_config(app_label)
                app_models: List[str] = [
                    model.__name__ for model in config.get_models()
                ]

                if len(app_models) <= 0:
                    raise NoModelsFoundError(
                        f"No Models Defined in {app_label} App: Make sure to have a models.py file with at least one model class in it."
                    )

        except LookupError as e:
            print_exception(e)
        except ModuleNotFoundError as e:
            print_exception(e)
        except NoModelsFoundError as e:
            print_exception(e)

    @classmethod
    async def addcrud_for_multiple_apps(cls, apps: List) -> None:
        try:
            # Make the current porject within which this command is executed available
            # To the command
            project_name: pathlib.Path = pathlib.Path.cwd().name
            os.environ.setdefault("DJANGO_SETTINGS_MODULE", f"{project_name}.settings")
            django.setup()
        except Exception as e:
            print_exception(e)

        funcs = []
        for app in apps:
            funcs.append(asyncio.ensure_future(cls.__add(app)))
        await asyncio.gather(*funcs)

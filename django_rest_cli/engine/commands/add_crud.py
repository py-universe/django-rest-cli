import os
import asyncio
from typing import List
from pathlib import Path

import django

from django_rest_cli.engine import print_exception, pluralize
from django_rest_cli.engine.exceptions import NoModelsFoundError
from django_rest_cli.engine.templates import (
    serializers_template, view_template, url_template
)
from django_rest_cli.engine import file_api


class AddCrud:
    @staticmethod
    def __generate_serializers(app_name: str, model_name: str) -> None:
        # Build path to app's models.py file for model import
        # app_path: str = Path.cwd().name+ "." +app_name
        
        template = serializers_template.SERIALIZER % {
            "model": model_name
        }
        imports = serializers_template.MODEL_IMPORT % {
            "app": app_name,
            "model": model_name,
        }
       
        serializer_file: Path = Path.cwd() / f"{app_name}" / "serializers.py"
        serializer_head = f"class {model_name}Serializer"

        # If serializers.py file does not exist in app folder, create one
        if not Path.exists(serializer_file):
            file_api.create_file(serializer_file, serializers_template.SETUP)

        if file_api.is_present_in_file(serializer_file, serializer_head):
            return
        head, body = imports, template
        file_api.wrap_file_content(serializer_file, head, body)
    
    @staticmethod
    def __generate_views(app_name: str, model_name: str) -> None:
        viewset_template = view_template.VIEWSET % {"model": model_name}
    
        model_import_template = view_template.MODEL_IMPORT % {
            "app": app_name,
            "model": model_name,
        }
        serializer_import_template = view_template.SERIALIZER_IMPORT % {
            "app": app_name,
            "model": model_name,
        }
        imports = model_import_template + serializer_import_template

        view_file: Path = Path.cwd() / f"{app_name}" / "views.py"
        view_head = f"class {model_name}ViewSet"

        if not Path.exists(view_file):
            file_api.create_file(view_file, view_template.SETUP)

        if file_api.is_present_in_file(view_file, view_head):
            return
        head, body = imports, viewset_template
        file_api.wrap_file_content(view_file, head, body)

    @staticmethod
    def __generate_url_patterns(app_name: str, model_name: str) -> None:
        plural_path = pluralize(model_name.lower())
        template = url_template.URL % {
            "model": model_name,
            "path": plural_path,
        }
        imports = url_template.VIEWSET_IMPORT % {
            "app": app_name,
            "model": model_name,
        }
        # return imports, url_template
        # file = f"{self.api_app_path}/urls.py"
        # chunk = f"{self.model_name}ViewSet)"
        # if file_api.is_present_in_file(file, chunk):
        #     return
        # head, body = self.get_url_parts()
        # if file_api.is_present_in_file(file, url_templates.URL_PATTERNS):
        #     file_api.replace_file_chunk(file, url_templates.URL_PATTERNS, "")
        # body = body + url_templates.URL_PATTERNS
        # file_api.wrap_file_content(file, head, body)
        url_file: Path = Path.cwd() / f"{app_name}" / "urls.py"
        url_head = f"{model_name}ViewSet"

        if not Path.exists(url_file):
            file_api.create_file(url_file, url_template.SETUP)

        if file_api.is_present_in_file(url_file, url_head):
            return
        head, body = imports, template
        if file_api.is_present_in_file(url_file, url_template.URL_PATTERNS):
            file_api.replace_file_chunk(url_file, url_template.URL_PATTERNS, "")
        body = body + url_template.URL_PATTERNS
        file_api.wrap_file_content(url_file, head, body)

    @classmethod
    async def __add(cls, app_label: str) -> None:
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
                for model in app_models:
                    cls.__generate_serializers(app_label, model)
                    cls.__generate_views(app_label, model)
                    cls.__generate_url_patterns(app_label, model)

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
            project_name: Path = Path.cwd().name
            os.environ.setdefault("DJANGO_SETTINGS_MODULE", f"{project_name}.settings")
            django.setup()
        except Exception as e:
            print_exception(e)

        funcs = []
        for app in apps:
            funcs.append(asyncio.ensure_future(cls.__add(app)))
        await asyncio.gather(*funcs)

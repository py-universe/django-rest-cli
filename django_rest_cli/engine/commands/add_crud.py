import asyncio
import os
from pathlib import Path
from typing import List

import django

from django_rest_cli.engine import file_api
from django_rest_cli.engine.utils import (
    pluralize, print_exception, print_info_message, print_success_message
)
from django_rest_cli.engine.exceptions import NoModelsFoundError
from django_rest_cli.engine.templates import (serializers_template,
                                              url_template, view_template)


class BaseGenerator:
    @classmethod
    def _generate_file(cls, file: Path, head: str, imports: str, body: str, setup: str):
        # If file does not exist in app folder, create one
        if not Path.exists(file):
            file_api.create_file(file, setup)

        if file_api.is_present_in_file(file, head):
            return
        file_api.wrap_file_content(file, imports, body)


class SerializerGenerator(BaseGenerator):
    @classmethod
    def _generate_serializers(cls, app_name: str, model_name: str) -> None:
        template = serializers_template.SERIALIZER % {"model": model_name}
        imports = serializers_template.MODEL_IMPORT % {
            "app": app_name,
            "model": model_name,
        }

        serializer_file: Path = Path.cwd() / f"{app_name}" / "serializers.py"
        serializer_head = f"class {model_name}Serializer"

        cls._generate_file(
            serializer_file,
            serializer_head,
            imports,
            template,
            serializers_template.SETUP,
        )


class ViewGenerator(BaseGenerator):
    @classmethod
    def _generate_views(cls, app_name: str, model_name: str) -> None:
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

        cls._generate_file(
            view_file, view_head, imports, viewset_template, view_template.SETUP
        )


class UrlsGenerator:
    @classmethod
    def _generate_url_patterns(cls, app_name: str, model_name: str) -> None:
        plural_path = pluralize(model_name.lower())
        template = url_template.URL % {
            "model": model_name,
            "path": plural_path,
        }
        imports = url_template.VIEWSET_IMPORT % {
            "app": app_name,
            "model": model_name,
        }

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


class AddCrud(SerializerGenerator, ViewGenerator, UrlsGenerator):
    @staticmethod
    async def __sort_app_imports(app_label: str):
        cmd: List[str]
        cmd = ["isort", app_label]

        cmd = " ".join(cmd)
        proc = await asyncio.create_subprocess_shell(
            cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
        )
        stdout, stderr = await proc.communicate()

    @staticmethod
    async def __lint_app_code(app_label: str):
        cmd: List[str]
        cmd = ["black", app_label]

        cmd = " ".join(cmd)
        proc = await asyncio.create_subprocess_shell(
            cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
        )
        stdout, stderr = await proc.communicate()

    @classmethod
    async def __add(cls, app_label: str) -> None:
        try:
            from django.apps import AppConfig
            from django.apps import apps as project_apps

            if project_apps.ready:
                config: AppConfig = project_apps.get_app_config(app_label)
                app_models: List[str] = [
                    model.__name__ for model in config.get_models()
                ]

                if len(app_models) <= 0:
                    raise NoModelsFoundError(
                        f"No Models Defined in {app_label} App: Make sure to have a models.py file with at least one model class in it."
                    )
                else:
                    print_info_message(f"Models Found in {app_label} App: {app_models}")

                print_info_message(f"Generating CRUD endpoints for {app_label} App")  
                for model in app_models:
                    cls._generate_serializers(app_label, model)
                    cls._generate_views(app_label, model)
                    cls._generate_url_patterns(app_label, model)

                await cls.__sort_app_imports(app_label)
                await cls.__lint_app_code(app_label)

                print_success_message(
                    f"all CRUD endpoints for the models found in the {app_label} App successfully added!"
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
            project_name: str = Path.cwd().name
            os.environ.setdefault("DJANGO_SETTINGS_MODULE", f"{project_name}.settings")
            django.setup()
        except Exception as e:
            print_exception(e)

        funcs = []
        for app in apps:
            funcs.append(asyncio.ensure_future(cls.__add(app)))
        await asyncio.gather(*funcs)

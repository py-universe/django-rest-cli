import pathlib


TEMPLATES_DIR: pathlib.Path = (
    pathlib.Path(__file__).resolve(strict=True).parent / "templates"
)
APP_TEMPLATES_DIR: pathlib.Path = TEMPLATES_DIR / "app_template"

PROJECT_TEMPLATE_URL_BASIC: str = (
    "https://github.com/Django-Rest-CLI/basic-template/zipball/master"
)
PROJECT_TEMPLATE_URL_MEDIOR: str = ""
PROJECT_TEMPLATE_URL_ADVANCED: str = ""

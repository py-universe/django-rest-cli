import pathlib


TEMPLATES_DIR: pathlib.Path = pathlib.Path(__file__).resolve(strict=True).parent / 'templates'
APP_TEMPLATES_DIR: pathlib.Path = TEMPLATES_DIR / 'app_template'
PROJECT_TEMPLATES_DIR: pathlib.Path = TEMPLATES_DIR / 'project_template'
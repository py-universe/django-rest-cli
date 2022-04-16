import pytest


@pytest.fixture
def valid_project_name() -> str:
    project_name: str = "demo"
    return project_name


@pytest.fixture
def invalid_project_name() -> str:
    # django expects project names to be valid Python identifiers
    project_name: str = "de-mo"
    return project_name

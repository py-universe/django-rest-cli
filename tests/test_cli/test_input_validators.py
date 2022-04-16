import pytest

from django_rest_cli.engine.cli.input_validators import (
    is_django_project_directory,
    validate_name,
)
from django_rest_cli.engine.exceptions import ProjectAppNameError


@pytest.mark.usefixtures("valid_project_name", "invalid_project_name")
class TestInputValidators:
    def test_raise_exception_for_invalid_project_name(
        self, invalid_project_name: str
    ) -> None:
        with pytest.raises(ProjectAppNameError) as excinfo:
            validate_name(invalid_project_name)
        assert "Invalid project name" in str(excinfo.value)

    def test_raise_exception_when_python_module_used_as_project_name(self) -> None:
        with pytest.raises(ProjectAppNameError) as excinfo:
            validate_name("pathlib")
        assert "conflicts with the name of an existing Python" in str(excinfo.value)

    def test_returns_none_with_valid_project_name(
        self, valid_project_name: str
    ) -> None:
        assert validate_name(valid_project_name) is None

    def test_passes_in_django_project_directory(self) -> None:
        assert is_django_project_directory() is True

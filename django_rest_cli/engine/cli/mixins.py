from examples import custom_style_3
from PyInquirer import prompt


class ProjectConfigMixin(object):
    @staticmethod
    def template_type() -> str:
        template_type: list = [
            {
                "type": "list",
                "name": "user_option",
                "message": "What template do you want to start this project with? Refer to docs for details on what each template comes with",
                "choices": ["Basic", "Medior", "Advanced"],
            }
        ]
        project_style: dict = prompt(template_type, style=custom_style_3)

        return project_style.get("user_option")

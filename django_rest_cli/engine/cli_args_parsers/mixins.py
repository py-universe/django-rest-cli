from PyInquirer import prompt
from examples import custom_style_3


class ProjectConfigMixin(object):

    @staticmethod
    def project_configs():
        presets = [
 
            {
                'type': 'list',
                'name': 'auth',
                'message': 'what authentication scheme? ',
                'choices': [
                    "basic token auth",
                    "jwt",
                    "None"
                ]
            },

            {
                'type': "confirm",
                "name": "pytest",
                "message": "Install and setup django-pytest for writing unit tests with Pytest? ",
            },

            {
                'type': "confirm",
                "name": "dotenv",
                "message": "Install and Setup dotenv for managing secret keys? ",
            },

            {
                'type': "confirm",
                "name": "split_settings",
                "message": "Install and Setup django_split_settings for modularizing the settings.py file? ",
            },

            {
                'type': "confirm",
                "name": "django_rest_swagger",
                "message": "Install and Setup django_rest_swagger for managing docs? ",
            },
        ]
        
        presets = prompt(presets, style=custom_style_3)
        return presets
        
    @staticmethod
    def template_or_manual():
        template_or_manual = [
            {
                'type': 'list',
                'name': 'user_option',
                'message': 'How do you want to start your project: ',
                'choices': [
                    "use default template(It uses the Django-rest-cookietier template. Internet connection required ",
                    "manually select feaures(Offers more flexibility) "
                ]
            }
        ]
        project_style = prompt(template_or_manual, style=custom_style_3)
        
        return project_style.get('user_options')
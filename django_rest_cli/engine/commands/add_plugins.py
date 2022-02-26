from typing import Optional, List
from django_rest_cli.engine.plugins import plugin_trigger


class AddPlugin():
    """
        devs should be able to add dependencies separately through add commands
        E.g drf add dotenv pytest drf_spectacular

        Blocker: How do I add dependencies to a new project
        - adding a dependency entails:
        Approach one:  installing the dependency, adding dependency files, and editing necessary files
        Approach two: store dependency files as sub folders and each time the 
        dependency is selected, pick the dependency files from the folder and add
        it to the project.

        for auth, split-settings, basically packages that reuire multiple files,
        we'd use a template folder. for single file or no file deps, we will create the file
        and make neccessary modifications

        How to add deps to requirements.txt file... pip install the specified dependency
        and pip freeze the requirements to the pip file

        Breaking it down to sub problems. What does adding a dependency entails?
        - Adding the dependency required files.
        - Adding the dependency settings
        - Installing it to the user's virtual env
        - Adding the dependency to the requirements.txt file
       
    """
    @staticmethod
    def _add(name: str) -> None:
        plugin_trigger(name)

    @classmethod
    def add_plugins(cls, plugins: List) -> None:
        # Here first check to see if the plugin command is being invoked within
        # A django project directory
        for plugin in plugins:
            cls._add(plugin) # apps created in the directory where command is invoked
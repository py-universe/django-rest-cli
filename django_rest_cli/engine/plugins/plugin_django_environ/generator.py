from ..base import BasePlugin


class DjangoEnviron(BasePlugin):
    
    def __init__(self) -> None:
        self.generator()

    @staticmethod
    def add_plugin_files():
        pass

    @staticmethod
    def update_settings():
        pass

    @classmethod
    def generator(cls):
        print('django-environ generator invoked')
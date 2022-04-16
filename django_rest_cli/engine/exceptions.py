class CommandError(Exception):
    pass


class ProjectAppNameError(Exception):
    pass


class NoModelsFoundError(Exception):
    pass


class NotDjangoProjectDirectory(Exception):
    pass

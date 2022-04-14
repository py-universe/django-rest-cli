# drf-project-builder
TODO: 
- How can I run subprocesses asynchronously?
- startapps
    - pass a list of apps--create all of them asynchronously, and give users nice looking feedback
- startproject template
  - create project with auth setup-- jwt and social auth
  - create project with env vars management
  - create project django-rest-swagger setup

- addcrud
  - grabs all the models for each app
    - How do I get all the models defined in an app
        - load all project apps: from django.apps import apps as dango_apps
        - Get the config for the app name passed config = django_apps.get_app_config(app_label)
        - Get the models for that app models = config.get_models()
  - creates model serializers for each model
  - creates model viewset based on each serializer
  - creates url patterns for each viewset

 ## why store templates locally and not remote
 - wouldn't require internet connection -- makes it more accessible?
 - faster since no download is required
 - makes it easier for devs to modify the template since they have it locally on their pc

 #### downsides of having the templates local
 - The package will be heavy

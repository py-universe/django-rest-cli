# drf-project-builder
TODO: 
- How can I run subprocesses asynchronously ?
- startapps
    - pass a list of apps--create all of them asynchronously, and give users nice looking feedback
- startproject template
  - create project with auth setup-- jwt and social auth
  - create project with env vars management
  - create project django-rest-swagger setup

- create crud-endpoints
 -- checks the models of the apps passed

 ## why store templates locally and not remote
 - wouldn't require internet connection -- makes it more accessible?
 - faster since no download is required
 - makes it easier for devs to modify the template since they have it locally on their pc

 #### downsides of having the templates local
 - The package will be heavy
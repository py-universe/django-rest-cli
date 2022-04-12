from django.urls import path
from django.conf.urls import include

urlpatterns = [
    path("dj-rest-auth/", include("dj_rest_auth.urls")),
    path("dj-rest-auth/registration/", include("dj_rest_auth.registration.urls")),
    path("account/", include("allauth.urls")),
]

from django.urls import include, path
from rest_framework import routers
from user.views import CustomUserViewSet

router = routers.DefaultRouter()
router.register(r"customusers", CustomUserViewSet)

urlpatterns = [
    path("", include(router.urls)),
]

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import ContactsViewSet

router = DefaultRouter()
router.register("contacts", ContactsViewSet)

urlpatterns = [
    path("", include(router.urls)),
]

from rest_framework.routers import DefaultRouter
from deployee.api.urls import abc_router
from django.urls import path, include
router = DefaultRouter()
router.registry.extend(abc_router.registry)
urlpatterns = [
    path('', include(router.urls))
]
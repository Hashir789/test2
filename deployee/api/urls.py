from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import ABCViewSet

abc_router = DefaultRouter()
abc_router.register(r'abc', ABCViewSet)
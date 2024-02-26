from django.contrib import admin
from django.urls import path, include
from deployee import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('backend.api.urls')),
    path('func/', views.abcc, name="abc"),
    path('', views.home, name="abcd"),
]

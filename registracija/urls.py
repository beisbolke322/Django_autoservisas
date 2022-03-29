from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.VisuDarbuListai.as_view(), name='home'),
    path('<int:id>', views.list, name='list'),
]

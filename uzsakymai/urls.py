from django.urls import path

from . import views

urlpatterns = [
    path('', views.VisiUzsakymai.as_view()),
]

from django.urls import path

from . import views

urlpatterns = [
    path('', views.VisuDarbuListai.as_view(), name='home'),
    path('<int:id>', views.list, name='list'),
    path('ppong/', views.ppong),
]

from django.urls import path, include
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = [
    path('', login_required(views.VisuDarbuListai.as_view()), name='home'),
    path('<int:id>/', views.list, name='list'),
    path('ppong/', views.ppong),
    path("accounts/", include('django.contrib.auth.urls')),
]


# accounts/ login/ [name='login']
# accounts/ logout/ [name='logout']
# accounts/ password_change/ [name='password_change']
# accounts/ password_change/done/ [name='password_change_done']
# accounts/ password_reset/ [name='password_reset']
# accounts/ password_reset/done/ [name='password_reset_done']
# accounts/ reset/<uidb64>/<token>/ [name='password_reset_confirm']
# accounts/ reset/done/ [name='password_reset_complete']
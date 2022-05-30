from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('registracija.urls')),
    path('uzsakymai/', include('uzsakymai.urls'), name='uzsakymai'),
]

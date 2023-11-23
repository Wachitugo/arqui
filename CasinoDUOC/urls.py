
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path("",include("Casino.urls")),
    path('usuarios/', include('usuarios.urls', namespace='usuarios')),
    path('mecanico/', include('mecanico.urls', namespace='mecanico')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

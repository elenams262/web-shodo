"""
URL configuration for Shodo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from web.views import (
    home,
    detalle_trabajo,
    lista_trabajos,
    contacto,
    aviso_legal,
    privacidad,
    cookies,
    crear_admin_emergencia,
)
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home, name="home"),
    path("trabajos/", lista_trabajos, name="lista_trabajos"),
    path("contacto/", contacto, name="contacto"),
    path("trabajo/<int:pk>/", detalle_trabajo, name="detalle_trabajo"),
    path("aviso-legal/", aviso_legal, name="aviso_legal"),
    path("politica-privacidad/", privacidad, name="privacidad"),
    path("politica-cookies/", cookies, name="cookies"),
    path("crear-admin-secreto/", crear_admin_emergencia),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

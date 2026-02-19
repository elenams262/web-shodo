from django.contrib import admin
from .models import Trabajo, MensajeContacto  # Añade MensajeContacto

admin.site.register(Trabajo)
admin.site.register(MensajeContacto)  # <--- Añade esto

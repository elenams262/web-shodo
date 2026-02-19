import os
import django
from django.contrib.auth import get_user_model

# Configura Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Shodo.settings")
django.setup()

User = get_user_model()

username = os.environ.get("DJANGO_SUPERUSER_USERNAME", "admin")
email = os.environ.get("DJANGO_SUPERUSER_EMAIL", "shodomarketingyeventos@gmail.com")
password = os.environ.get("DJANGO_SUPERUSER_PASSWORD", "Raquelsanchez72.")

if not User.objects.filter(username=username).exists():
    print(f"Creando superusuario {username}...")
    User.objects.create_superuser(username, email, password)
    print("Superusuario creado exitosamente.")
else:
    print(
        f"El superusuario {username} ya existe. Intentando actualizar contraseña por seguridad..."
    )
    user = User.objects.get(username=username)
    user.set_password(password)
    user.save()
    print("Contraseña actualizada.")

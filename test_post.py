import os
import sys
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Shodo.settings")
django.setup()

from django.test import Client
import traceback

c = Client(raise_request_exception=True, SERVER_NAME="localhost")
try:
    r = c.post(
        "/",
        {
            "nombre": "test",
            "email": "test@example.com",
            "telefono": "123456",
            "mensaje": "hola",
        },
    )
    print("SUCCESS", r.status_code)
except Exception as e:
    traceback.print_exc()

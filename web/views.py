from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .models import Trabajo, MensajeContacto
from .forms import ContactoForm


def home(request):
    mis_trabajos = Trabajo.objects.all().order_by("-fecha_creacion")[:3]

    if request.method == "POST":
        form = ContactoForm(request.POST)
        if form.is_valid():
            datos = form.cleaned_data

            # 1. GUARDAR EN LA BASE DE DATOS
            MensajeContacto.objects.create(
                nombre=datos["nombre"],
                email=datos["email"],
                telefono=datos.get(
                    "telefono", ""
                ),  # Usamos .get por seguridad si fuera opcional
                mensaje=datos["mensaje"],
            )

            # 2. ENVIAR EMAIL (Cuerpo del mensaje mejorado)
            cuerpo_mensaje = (
                f"Has recibido un nuevo mensaje de contacto:\n\n"
                f"Nombre: {datos['nombre']}\n"
                f"Email: {datos['email']}\n"
                f"Teléfono: {datos['telefono']}\n\n"
                f"Mensaje:\n{datos['mensaje']}"
            )

            send_mail(
                f"Nuevo contacto de {datos['nombre']}",
                cuerpo_mensaje,
                datos["email"],
                ["shodomarketingyeventos@gmail.com"],
                fail_silently=False,
            )

            return redirect("home")
    else:
        form = ContactoForm()

    return render(
        request,
        "home.html",
        {
            "trabajos": mis_trabajos,
            "form": form,
        },
    )


def detalle_trabajo(request, pk):
    trabajo = Trabajo.objects.get(pk=pk)
    return render(request, "detalle.html", {"trabajo": trabajo})


def lista_trabajos(request):
    todos_los_trabajos = Trabajo.objects.all().order_by("-fecha_creacion")
    return render(request, "trabajos.html", {"trabajos": todos_los_trabajos})


def contacto(request):
    if request.method == "POST":
        form = ContactoForm(request.POST)
        if form.is_valid():
            datos = form.cleaned_data
            # Guardamos en DB
            MensajeContacto.objects.create(
                nombre=datos["nombre"],
                email=datos["email"],
                telefono=datos.get("telefono", ""),
                mensaje=datos["mensaje"],
            )
            # Enviamos Email
            send_mail(
                f"Nuevo contacto de {datos['nombre']}",
                f"Nombre: {datos['nombre']}\nEmail: {datos['email']}\nTeléfono: {datos['telefono']}\n\nMensaje:\n{datos['mensaje']}",
                datos["email"],
                ["shodomarketingyeventos@gmail.com"],
            )
            return redirect("home")  # O a una página de gracias
    else:
        form = ContactoForm()

    return render(request, "contacto.html", {"form": form})


def aviso_legal(request):
    return render(request, "aviso_legal.html")


def privacidad(request):
    return render(request, "privacidad.html")


def cookies(request):
    return render(request, "cookies.html")

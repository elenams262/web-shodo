from django import forms


class ContactoForm(forms.Form):
    nombre = forms.CharField(
        label="Tu Nombre",
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Ej: Juan Pérez",
            }
        ),
    )
    email = forms.EmailField(
        label="Tu Email",
        widget=forms.EmailInput(
            attrs={"class": "form-control", "placeholder": "Ej: juanperez@email.com"}
        ),
    )
    telefono = forms.CharField(
        label="Tu Teléfono",
        max_length=20,
        required=False,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Ej: 600 000 000"}
        ),
    )
    mensaje = forms.CharField(
        label="Mensaje",
        widget=forms.Textarea(attrs={"class": "form-control", "rows": 4}),
    )

from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render

from .forms import RegModelForm, ContactForm
from .models import Registrado

def inicio(request):
    titulo = "HOLA"
    form = RegModelForm(request.POST or None)
    context = {"el_form": form, "titulo": titulo}

    if form.is_valid():
        instance = form.save(commit=False)
        nombre = form.cleaned_data.get("nombre")
        email = form.cleaned_data.get("email")
        instance.save()
        context = {"titulo": "Gracias, si quieres registrar otro usuario dale al botón de nuevo"}

    return render(request, "inicio.html", context)

def contact(request):
    form = ContactForm(request.POST or None)
    context = {"form": form}

    if form.is_valid():
        form_email = form.cleaned_data.get("email")
        form_mensaje = form.cleaned_data.get("mensaje")
        form_nombre = form.cleaned_data.get("nombre")
        asunto = 'Form de Contacto'
        email_from = settings.EMAIL_HOST_USER
        email_to = [email_from, "otroemail@gmail.com"]
        email_mensaje = "%s: %s enviado por %s" % (form_nombre, form_mensaje, form_email)
        send_mail(asunto, email_mensaje, email_from, email_to, fail_silently=True)
        context = {"form": form}

    return render(request, "forms.html", context)


from django.shortcuts import render

from .forms import RegForm, RegModelForm
from .models import Registrado
# Create your views here.
def inicio(request):
	titulo = "HOLA"
	form = RegModelForm(request.POST or None)
	context = {"el_form": form, "titulo": titulo,}
	
	if form.is_valid():
		instance = form.save(commit=False)
		nombre = form.cleaned_data.get("nombre")
		email = form.cleaned_data.get("email")
		instance.save()
		
		context = {"titulo": "Gracias, si quieres registrar otro usuario dale al boton de nuevo"}



	return render(request, "inicio.html", context)

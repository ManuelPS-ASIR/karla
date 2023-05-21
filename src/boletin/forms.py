from django import forms

from .models import Registrado

class RegModelForm(forms.ModelForm):
	class Meta:
		model = Registrado
		fields = ["nombre", "email"]
	def clean_email(self):
		email = self.cleaned_data.get("email")
		email_base, proveedor =  email.split("@")
		dominio, extension = proveedor.split(".")
		if dominio != "iesfernandoaguilar" and extension != "es":
			raise forms.ValidationError("Estas utilizando un correo externo al centro")
		return email	
		
class RegForm(forms.Form):
	nombre = forms.CharField(max_length=100)
	email = forms.EmailField()

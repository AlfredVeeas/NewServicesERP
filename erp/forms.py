from django import forms
from .models import FichaNavio, FichaQuimico, FichaVehiculo, FichaHerramientas

class CustomLoginForm(forms.Form):
    email = forms.EmailField(label='E-mail')
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput)

class FichaNavioForm(forms.ModelForm):
    class Meta:
        model = FichaNavio
        fields = '__all__'

#-------

class FichaQuimicoForm(forms.ModelForm):
    class Meta:
        model = FichaQuimico
        fields = '__all__'

class FichaVehiculoForm(forms.ModelForm):
    class Meta:
        model = FichaVehiculo
        fields = '__all__'

class FichaHerramientasForm(forms.ModelForm):
    class Meta:
        model= FichaHerramientas
        fields = '__all__'

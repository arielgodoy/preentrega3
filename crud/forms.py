from django import forms
from django.forms import ModelForm
from .models import Documento,Propiedades,Propietario

class DocForm(ModelForm):
    class Meta:
        model = Documento
        fields = '__all__'
class BuscaDocs(forms.Form):
    titulo = forms.CharField(max_length=100,required=False)


class PropForm(ModelForm):
    class Meta:
        model = Propiedades
        fields = '__all__'
class BuscaProps(forms.Form):
    rol = forms.CharField(max_length=10,required=False)





class PropietarioForm(ModelForm):
    class Meta:
        model = Propietario
        fields = '__all__'
class BuscaPropietario(forms.Form):
    nombre = forms.CharField(max_length=100,required=False)
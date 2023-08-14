from django import forms
from .models import Jugador, Director_Tecnico, Club

class JugadorFormulario(forms.ModelForm):
    class Meta:
        model = Jugador
        fields = '__all__'
    
class DirectorTecnicoFormulario(forms.ModelForm):
    class Meta:
        model = Director_Tecnico
        fields = '__all__'
        
class ClubFormulario(forms.ModelForm):
    class Meta:
        model = Club
        fields = '__all__'
        
class JugadorBusquedaFormulario(forms.Form):
    nombre = forms.CharField(required=False)
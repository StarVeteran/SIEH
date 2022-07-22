from django.db.models import fields
from django.forms import DateTimeInput, ModelForm, TimeInput
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import *


class CrearUsuarioForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ['first_name','last_name','username','email','password1','password2','rol']


class UserForm(ModelForm):
    class Meta:
        model = Usuario
        fields = ['first_name','last_name','email','imagen']


class DateInput(forms.DateInput):
    input_type = 'date'


class PacienteForm(forms.ModelForm):
    disabled_fields = ['responsable']

 
    class Meta:
        model = RegPaciente
        fields = '__all__'
        widgets = {
            'FechaIngreso': forms.DateInput(attrs={'type': 'date'}),
            'FechaEgreso': forms.DateInput(attrs={'type': 'date'}),
            'HoraIngreso': forms.TimeInput(attrs={'type': 'time'}),
            'HoraEgreso': forms.TimeInput(attrs={'type': 'time'}),
            'FechaCirugia': forms.DateInput(attrs={'type': 'date'}),
            'FechaNacimiento': forms.DateInput(attrs={'type': 'date'})
        }


class RegPacienteForm(forms.ModelForm):
    
    class Meta:
        model = RegPaciente
        fields = ['Expediente', 'estatus']

class Expacienteingresoform(forms.ModelForm):

  class Meta:
        model = Expacienteingreso
        fields = ['intnumpaciente', 'dtmfechahoraingreso', 'dtmfechahoraegreso']  

        widget = {
            'intnumpaciente': forms.TextInput(attrs={'class': 'form-control'}),
            'dtmfechahoraingreso': forms.TextInput(attrs={'class': 'form-control'}),
            'dtmfechahoraegreso': forms.TextInput(attrs={'class': 'form-control'}),
        }   




        

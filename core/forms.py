from django import forms
from .models import Medicamento, Prescripcion

class PacienteForm(forms.ModelForm):
    class Meta:
        fields = '__all__'
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'edad': forms.NumberInput(attrs={'class': 'form-control'}),
            'rut': forms.TextInput(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def clean_edad(self):
        edad = self.cleaned_data.get('edad')
        if edad <= 0:
            raise forms.ValidationError("La edad debe ser mayor que 0.")
        return edad


class MedicamentoForm(forms.ModelForm):
    class Meta:
        model = Medicamento
        fields = '__all__'
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control'}),
            'dosis_recomendada': forms.TextInput(attrs={'class': 'form-control'}),
            'laboratorio': forms.TextInput(attrs={'class': 'form-control'}),
        }


class PrescripcionForm(forms.ModelForm):
    class Meta:
        model = Prescripcion
        fields = '__all__'
        widgets = {
            'paciente': forms.TextInput(attrs={'class': 'form-control'}),
            'medicamento': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_inicio': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'fecha_fin': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'indicaciones': forms.Textarea(attrs={'class': 'form-control'}),
        }

from django import forms
from .models import Adopcion

class AdopcionForm(forms.ModelForm):
    class Meta:
        model = Adopcion
        fields = '__all__'  

        widgets = {
            'mascota': forms.Select(attrs={'class': 'form-control'}),
            'adoptante': forms.Select(attrs={'class': 'form-control'}),
            'fecha_adopcion': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }
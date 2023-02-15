from django import forms
from .models import Alvo


class AlvoForm(forms.ModelForm):
    class Meta:
        model = Alvo
        fields = ['nome', 'latitude', 'longitude', 'data_expiracao']
        widgets = {
            'data_expiracao': forms.DateInput(attrs={'type': 'date'}),
        }

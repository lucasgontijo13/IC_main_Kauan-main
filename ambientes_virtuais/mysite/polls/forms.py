from django import forms
from .models import Cliente

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['cpf', 'nome', 'email', 'cnpj']

    def clean(self):
        cleaned_data = super().clean()
        # Realizar validações adicionais se necessário
        return cleaned_data
    
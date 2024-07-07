from django import forms
from .models import Cliente

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['cpf', 'nome', 'email', 'cnpj']

    def clean(self):
        cleaned_data = super().clean()
        nome_completo = cleaned_data.get('nome_completo')
        if nome_completo:
            # Aqui você pode realizar validações adicionais se necessário
            pass
        return cleaned_data
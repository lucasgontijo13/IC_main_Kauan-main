from django import forms
from django.contrib.auth.models import User
from django.utils import timezone

class ClienteForm(forms.ModelForm):
    cpf = forms.CharField(max_length=14, required=False)
    cnpj = forms.CharField(max_length=18, required=False)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'cpf', 'cnpj']

    def clean(self):
        cleaned_data = super().clean()
        # Realize validações adicionais, se necessário
        return cleaned_data

    def save(self, commit=True):
        instance = super().save(commit=False)
        if commit:
            instance.save()
        return instance
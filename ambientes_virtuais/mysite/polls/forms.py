
from django import forms
from .models import Login 

class LoginForm(forms.ModelForm):
    senha_confirmada = forms.CharField(max_length=8, widget=forms.PasswordInput())

    class Meta:
        model = Login
        fields = ['email', 'senha', 'senha_confirmada']

    def clean(self):
        cleaned_data = super().clean()
        senha = cleaned_data.get('senha')
        senha_confirmada = cleaned_data.get('senha_confirmada')

        if senha and senha_confirmada and senha != senha_confirmada:
            raise forms.ValidationError("A senha e a confirmação de senha não correspondem.")

        return cleaned_data

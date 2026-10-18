from django import forms
from django.contrib.auth.forms import PasswordResetForm, UserCreationForm
from .models import User


class CadastroForm(UserCreationForm):
    email = forms.EmailField(label="E-mail", required=True)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "email")
        labels = {"username": "Nome"}

    def clean_email(self):
        email = self.cleaned_data["email"]
        if User.objects.filter(email__iexact=email).exists():
            raise forms.ValidationError("Este e-mail já está cadastrado.")
        return email

class RecuperarSenhaForm(PasswordResetForm):
    nome = forms.CharField(label="Nome", max_length=150)
    field_order = ["nome", "email"]

    def get_users(self, email):
        nome = self.cleaned_data.get("nome", "")
        return (u for u in super().get_users(email) if u.get_username() == nome)
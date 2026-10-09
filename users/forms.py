from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User


class CadastroForm(UserCreationForm):
    nome = forms.CharField(label="Nome completo", max_length=150)
    email = forms.EmailField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("email",)

    def clean_email(self):
        email = self.cleaned_data["email"]
        if User.objects.filter(email__iexact=email).exists():
            raise forms.ValidationError("Este e-mail já está cadastrado.")
        return email

    def save(self, commit=True):
        user = super().save(commit=False)
        primeiro, _, resto = self.cleaned_data["nome"].strip().partition(" ")
        user.first_name = primeiro
        user.last_name = resto
        user.username = self.cleaned_data["email"]
        if commit:
            user.save()
        return user
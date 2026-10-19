from .models import Postagem, Servico
from django import forms

class PostagemForm(forms.ModelForm):

    class Meta:
        model = Postagem
        fields = "__all__"

class ServicoForm(forms.ModelForm):

    class Meta:
        model = Servico
        fields = "__all__"
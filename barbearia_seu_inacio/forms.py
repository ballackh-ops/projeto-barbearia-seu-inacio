from .models import Postagem
from django import forms

class PostagemForm(forms.ModelForm):

    class Meta:
        model = Postagem
        fields = "__all__"
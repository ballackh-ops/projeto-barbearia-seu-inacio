from .models import Postagem, Servico
from django import forms
from django import forms
from .models import Produto
from .models import Aviso

class PostagemForm(forms.ModelForm):

    class Meta:
        model = Postagem
        fields = "__all__"

class ServicoForm(forms.ModelForm):

    class Meta:
        model = Servico
        fields = "__all__"

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ["nome", "descricao", "preco", "estoque", "imagem"]

class AvisoForm(forms.ModelForm):
    class Meta:
        model = Aviso
        fields = ["nome", "descricao", "data"]
        widgets = {
            "data": forms.DateInput(attrs={"type": "date"}, format="%Y-%m-%d"),
        }
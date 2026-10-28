from .models import Postagem, Servico
from django import forms
from django import forms
from .models import Produto

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
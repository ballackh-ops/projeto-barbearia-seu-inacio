# barbearia_seu_inacio/admin.py
from django.contrib import admin
from .models import Postagem, Servico
from django.contrib import admin
from .models import Produto

@admin.register(Postagem)
class PostagemAdmin(admin.ModelAdmin):
    list_display = ("id", "descricao", "data", "imagem")

@admin.register(Servico)
class ServicoAdmin(admin.ModelAdmin):
    list_display = ("id", "descricao", "nome", "duracao_minutos", "imagem", "preco")

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ("id", "nome", "preco", "estoque", "data_criacao")
    search_fields = ("nome",)
    list_filter = ("data_criacao",)
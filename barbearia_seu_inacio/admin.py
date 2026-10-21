# barbearia_seu_inacio/admin.py
from django.contrib import admin
from .models import Postagem, Servico

@admin.register(Postagem)
class PostagemAdmin(admin.ModelAdmin):
    list_display = ("id", "descricao", "data", "imagem")

@admin.register(Servico)
class ServicoAdmin(admin.ModelAdmin):
    list_display = ("id", "descricao", "nome", "duracao_minutos", "imagem", "preco")
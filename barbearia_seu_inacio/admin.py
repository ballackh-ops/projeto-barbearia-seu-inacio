# barbearia_seu_inacio/admin.py
from django.contrib import admin
from .models import Postagem

@admin.register(Postagem)
class PostagemAdmin(admin.ModelAdmin):
    list_display = ("id", "descricao", "data", "imagem")
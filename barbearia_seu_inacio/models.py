from django.db import models
from tinymce.models import HTMLField

class Postagem(models.Model):
    imagem = models.ImageField(upload_to="galeria/")
    descricao = HTMLField()
    data = models.DateField(auto_now=True)

class Servico(models.Model):
    nome = models.CharField(max_length=100)
    imagem = models.ImageField(upload_to="servico/")
    descricao = HTMLField()
    preco = models.DecimalField(max_digits=8, decimal_places=2)
    duracao_minutos = models.PositiveIntegerField(help_text="Duração em minutos")

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    estoque = models.PositiveIntegerField(default=0)
    imagem = models.ImageField(upload_to="produtos/", blank=True, null=True)
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome
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
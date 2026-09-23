from django.db import models
from tinymce.models import HTMLField

class Postagem(models.Model):
    imagem = models.ImageField(upload_to="galeria/")
    descricao = HTMLField()
    data = models.DateField(auto_now=True)
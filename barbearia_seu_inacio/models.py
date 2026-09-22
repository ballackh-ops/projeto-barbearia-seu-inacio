from django.db import models
from tinymce.models import HTMLField
from .models import User

class Postagem(models.Model):
    imagem = models.ImageField(uploud_to="galeria")
    descricao = HTMLField()
    data = models.DateField(auto_now=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
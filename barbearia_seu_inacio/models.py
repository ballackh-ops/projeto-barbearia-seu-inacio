from django.db import models
# from tinymce.models import HTMLField

class servico(models.Model):
    nome = models.CharField(max_length=50)
    imagem = models.ImageField(upload_to="servicos")
    # descricao = HTMLField()
    preco = models.FloatField()

    def __str__(self):
        return self.nome

class Produtos(models.Model):
    nome = models.CharField(max_length=50)
    imagem = models.ImageField(upload_to="produtos")
    # descricao = HTMLField()
    preco = models.FloatField()

    def __str__(self):
            return self.nome

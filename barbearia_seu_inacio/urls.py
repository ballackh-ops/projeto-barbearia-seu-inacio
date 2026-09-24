from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("agenda/", views.agenda, name="agenda"),
    path("contato/", views.contato, name="contato"),
    path("galeria/", views.galeria, name="galeria"),
    path("galeria/<int:id_postagem>/", views.postagem, name="postagem"),
    path("galeria/novo/", views.nova_postagem, name="nova_postagem"),
    path("galeria/<int:id_postagem>/editar/", views.editar_postagem, name="editar_postagem"),
    path("galeria/<int:id_postagem>/remover/", views.remover_postagem, name="remover_postagem"),
    path("servicos/", views.servicos, name="servicos"),
    path("sobre/", views.sobre, name="sobre"),
    path("atendimentos/", views.atendimentos, name="atendimentos"),
    path("loja/", views.loja, name="loja"),
    path("login/", views.login, name="login"),
]
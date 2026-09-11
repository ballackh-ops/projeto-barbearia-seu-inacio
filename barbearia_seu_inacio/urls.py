from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("agenda/", views.agenda, name="agenda"),
    path("contato/", views.contato, name="contato"),
    path("galeria/", views.galeria, name="galeria"),
    path("serviços/", views.servicos, name="serviços"),
    path("sobre/", views.sobre, name="sobre"),
    path("atendimentos/", views.atendimentos, name="atendimentos"),
    path("loja/", views.loja, name="loja"),
]
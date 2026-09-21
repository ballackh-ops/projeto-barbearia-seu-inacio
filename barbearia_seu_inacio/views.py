from django.shortcuts import render

def index(request):
    return render(request, "barbearia_seu_inacio/index.html")

def base(request):
    return render(request, "templates/base.html")

def servicos(request):
    return render(request, "barbearia_seu_inacio/servicos.html")

def contato(request):
    return render(request, "barbearia_seu_inacio/contato.html")

def galeria(request):
    return render(request, "barbearia_seu_inacio/galeria.html")

def agenda(request):
    return render(request, "barbearia_seu_inacio/agenda.html")

def sobre(request):
    return render(request, "barbearia_seu_inacio/sobre.html")

def atendimentos(request):
    return render(request, "barbearia_seu_inacio/atendimentos.html")

def loja(request):
    return render(request, "barbearia_seu_inacio/loja.html")
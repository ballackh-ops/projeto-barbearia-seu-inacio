from django.shortcuts import render

from django.shortcuts import render


def index(request):
    return render(request, "barbearia_seu_inacio/index.html")

def base(request):
    return render(request, "barbearia_seu_inacio/base.html")
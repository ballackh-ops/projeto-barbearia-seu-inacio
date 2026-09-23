from django.shortcuts import render, get_object_or_404, redirect
from .models import Postagem
from .forms import PostagemForm
from django.contrib.auth.decorators import login_required, permission_required

def index(request):
    return render(request, "barbearia_seu_inacio/index.html")

def base(request):
    return render(request, "templates/base.html")

def servicos(request):
    return render(request, "barbearia_seu_inacio/servicos.html")

def contato(request):
    return render(request, "barbearia_seu_inacio/contato.html")

@login_required
@permission_required("barbearia_seu_inacio.view_postagem")
def galeria(request, id_postagem):
    return render(request, "barbearia_seu_inacio/galeria.html", context = {
        "post": get_object_or_404(Postagem, id=id_postagem),
    })

@login_required
@permission_required("barbearia_seu_inacio.add_postagem")
def nova_postagem(request):
    if request.method == "POST":
        form = PostagemForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = PostagemForm()

    return render(request, "blog/form_post.html", context = {
        "form": form,
    })


@login_required
@permission_required("barbearia_seu_inacio.change_postagem")
def editar_postagem(request, id_post):
    post = get_object_or_404(Postagem, id=id_post)
    if request.method == "POST":
        form = PostagemForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = PostagemForm(instance=post)

    return render(request, "blog/form_post.html", context = {
        "form": form,
        "is_editar": True,
    })

@login_required
@permission_required("barbearia_seu_inacio.delete_postagem")
def remover_postagem(request, id_post):
    if request.method == "POST":
        post = get_object_or_404(Post, id=id_post)
        post.delete()
        return redirect("index")
    else:
        return render(request, "blog/confirmar_remocao.html")

def agenda(request):
    return render(request, "barbearia_seu_inacio/agenda.html")

def sobre(request):
    return render(request, "barbearia_seu_inacio/sobre.html")

def atendimentos(request):
    return render(request, "barbearia_seu_inacio/atendimentos.html")

def loja(request):
    return render(request, "barbearia_seu_inacio/loja.html")
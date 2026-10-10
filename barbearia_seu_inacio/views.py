from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Postagem
from .forms import PostagemForm


def index(request):
    return render(request, "barbearia_seu_inacio/index.html")


def base(request):
    return render(request, "templates/base.html")


def servicos(request):
    return render(request, "barbearia_seu_inacio/servicos.html")


def contato(request):
    return render(request, "barbearia_seu_inacio/contato.html")


def galeria(request):
    postagens = Postagem.objects.all()
    return render(request, "barbearia_seu_inacio/galeria.html", context={
        "postagens": postagens,
    })


@login_required
def postagem(request, id_postagem):
    if not request.user.has_perm("barbearia_seu_inacio.view_postagem"):
        messages.error(request, "Você não tem permissão para visualizar esta postagem.")
        return redirect("galeria")

    postagem = get_object_or_404(Postagem, id=id_postagem)
    return render(request, "barbearia_seu_inacio/postagem.html", context={
        "postagem": postagem,
    })


@login_required
def nova_postagem(request):
    if not request.user.has_perm("barbearia_seu_inacio.add_postagem"):
        messages.error(request, "Acesso negado: Você não tem permissão para criar postagens.")
        return redirect("galeria")

    if request.method == "POST":
        form = PostagemForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Postagem criada com sucesso!")
            return redirect("galeria")
    else:
        form = PostagemForm()

    return render(request, "barbearia_seu_inacio/form_postagem.html", context={
        "form": form,
    })


@login_required
def editar_postagem(request, id_postagem):
    if not request.user.has_perm("barbearia_seu_inacio.change_postagem"):
        messages.error(request, "Acesso negado: Você não tem permissão para editar postagens.")
        return redirect("galeria")

    post = get_object_or_404(Postagem, id=id_postagem)
    if request.method == "POST":
        form = PostagemForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, "Postagem atualizada com sucesso!")
            return redirect("galeria")
    else:
        form = PostagemForm(instance=post)

    return render(request, "barbearia_seu_inacio/form_postagem.html", context={
        "form": form,
        "is_editar": True,
    })


@login_required
def remover_postagem(request, id_postagem):
    if not request.user.has_perm("barbearia_seu_inacio.delete_postagem"):
        messages.error(request, "Acesso negado: Você não tem permissão para excluir postagens.")
        return redirect("galeria")

    post = get_object_or_404(Postagem, id=id_postagem)
    if request.method == "POST":
        post.delete()
        messages.success(request, "Postagem removida com sucesso!")
        return redirect("galeria")

    return render(request, "barbearia_seu_inacio/confirmar_remocao.html", context={
        "post": post,
    })


def agenda(request):
    return render(request, "barbearia_seu_inacio/agenda.html")


def sobre(request):
    return render(request, "barbearia_seu_inacio/sobre.html")


def atendimentos(request):
    return render(request, "barbearia_seu_inacio/atendimentos.html")


def loja(request):
    return render(request, "barbearia_seu_inacio/loja.html")
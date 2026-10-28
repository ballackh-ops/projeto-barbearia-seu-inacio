from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Postagem, Servico, Produto
from .forms import PostagemForm, ServicoForm, ProdutoForm
from django.core.paginator import Paginator



def index(request):
    return render(request, "barbearia_seu_inacio/index.html")


def servicos(request):
    servicos = Servico.objects.order_by("-id")
    paginator = Paginator(servicos, 8)
    pagina = paginator.get_page(request.GET.get("pagina"))
    return render(request, "barbearia_seu_inacio/servicos.html", context={
        "servicos": pagina,
        "range_elided": paginator.get_elided_page_range(pagina.number, on_each_side=1, on_ends=1),
    })

@login_required
def servico(request, id_servico):
    if not request.user.has_perm("barbearia_seu_inacio.view_servico"):
        messages.error(request, "Você não tem permissão para visualizar este serviço.")
        return redirect("servicos")

    servico = get_object_or_404(Servico, id=id_servico)
    return render(request, "barbearia_seu_inacio/servico.html", context={
        "servico": servico,
    })

@login_required
def novo_servico(request):
    if not request.user.has_perm("barbearia_seu_inacio.add_servico"):
        messages.error(request, "Acesso negado: Você não tem permissão para criar serviços.")
        return redirect("servicos")

    if request.method == "POST":
        form = ServicoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Serviço cadastrado com sucesso!")
            return redirect("servicos")
    else:
        form = ServicoForm()

    return render(request, "barbearia_seu_inacio/form_servico.html", context={
        "form": form,
    })

@login_required
def editar_servico(request, id_servico):
    if not request.user.has_perm("barbearia_seu_inacio.change_servico"):
        messages.error(request, "Acesso negado: Você não tem permissão para editar serviços.")
        return redirect("servicos")

    servico = get_object_or_404(Servico, id=id_servico)
    if request.method == "POST":
        form = ServicoForm(request.POST, request.FILES, instance=servico)
        if form.is_valid():
            form.save()
            messages.success(request, "Serviço atualizado com sucesso!")
            return redirect("servicos")
    else:
        form = ServicoForm(instance=servico)

    return render(request, "barbearia_seu_inacio/form_servico.html", context={
        "form": form,
        "is_editar": True,
    })

@login_required
def remover_servico(request, id_servico):
    if not request.user.has_perm("barbearia_seu_inacio.delete_servico"):
        messages.error(request, "Acesso negado: Você não tem permissão para excluir serviços.")
        return redirect("servicos")

    servico = get_object_or_404(Servico, id=id_servico)
    if request.method == "POST":
        servico.delete()
        messages.success(request, "Serviço removido com sucesso!")
        return redirect("servicos")

    return render(request, "barbearia_seu_inacio/confirmar_remocao_servico.html", context={
        "servico": servico,
    })

def contato(request):
    return render(request, "barbearia_seu_inacio/contato.html")


def galeria(request):
    postagens = Postagem.objects.order_by("-id")
    paginator = Paginator(postagens, 3)
    pagina = paginator.get_page(request.GET.get("pagina"))
    return render(request, "barbearia_seu_inacio/galeria.html", context={
        "postagens": pagina,
        "range_elided": paginator.get_elided_page_range(pagina.number, on_each_side=1, on_ends=1),
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

    postagem = get_object_or_404(Postagem, id=id_postagem)
    if request.method == "POST":
        form = PostagemForm(request.POST, request.FILES, instance=postagem)
        if form.is_valid():
            form.save()
            messages.success(request, "Postagem atualizada com sucesso!")
            return redirect("galeria")
    else:
        form = PostagemForm(instance=postagem)

    return render(request, "barbearia_seu_inacio/form_postagem.html", context={
        "form": form,
        "is_editar": True,
    })


@login_required
def remover_postagem(request, id_postagem):
    if not request.user.has_perm("barbearia_seu_inacio.delete_postagem"):
        messages.error(request, "Acesso negado: Você não tem permissão para excluir postagens.")
        return redirect("galeria")

    postagem = get_object_or_404(Postagem, id=id_postagem)
    if request.method == "POST":
        postagem.delete()
        messages.success(request, "Postagem removida com sucesso!")
        return redirect("galeria")

    return render(request, "barbearia_seu_inacio/confirmar_remocao_postagem.html", context={
        "postagem": postagem,
    })


def agenda(request):
    return render(request, "barbearia_seu_inacio/agenda.html")


def sobre(request):
    return render(request, "barbearia_seu_inacio/sobre.html")


def atendimentos(request):
    return render(request, "barbearia_seu_inacio/atendimentos.html")


def loja(request):
    return render(request, "barbearia_seu_inacio/loja.html")

def loja(request):
    produtos = Produto.objects.all()
    return render(request, "barbearia_seu_inacio/loja.html", context={
        "produtos": produtos,
    })


@login_required
def novo_produto(request):
    if not request.user.has_perm("barbearia_seu_inacio.add_produto"):
        messages.error(request, "Acesso negado: Você não tem permissão para cadastrar produtos.")
        return redirect("loja")

    if request.method == "POST":
        form = ProdutoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Produto cadastrado com sucesso!")
            return redirect("loja")
    else:
        form = ProdutoForm()

    return render(request, "barbearia_seu_inacio/form_produto.html", context={
        "form": form,
    })


@login_required
def editar_produto(request, id_produto):
    if not request.user.has_perm("barbearia_seu_inacio.change_produto"):
        messages.error(request, "Acesso negado: Você não tem permissão para editar produtos.")
        return redirect("loja")

    produto = get_object_or_404(Produto, id=id_produto)
    if request.method == "POST":
        form = ProdutoForm(request.POST, request.FILES, instance=produto)
        if form.is_valid():
            form.save()
            messages.success(request, "Produto atualizado com sucesso!")
            return redirect("loja")
    else:
        form = ProdutoForm(instance=produto)

    return render(request, "barbearia_seu_inacio/form_produto.html", context={
        "form": form,
        "is_editar": True,
    })


@login_required
def remover_produto(request, id_produto):
    if not request.user.has_perm("barbearia_seu_inacio.delete_produto"):
        messages.error(request, "Acesso negado: Você não tem permissão para excluir produtos.")
        return redirect("loja")

    produto = get_object_or_404(Produto, id=id_produto)
    if request.method == "POST":
        produto.delete()
        messages.success(request, "Produto removido com sucesso!")
        return redirect("loja")

    return render(request, "barbearia_seu_inacio/confirmar_remocao_produto.html", context={
        "produto": produto,
    })
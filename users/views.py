from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages
from .forms import CadastroForm
from django.utils.http import url_has_allowed_host_and_scheme
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import SetPasswordForm

User = get_user_model()

def login(request):
    erro = None
    if request.method == "POST":
        username = request.POST.get("username", "").strip()
        password = request.POST.get("password", "")
        user = authenticate(
            request,
            username=username,
            password=password
        )
        if user is not None:
            auth_login(request, user)
            proximo = request.POST.get("next", "")
            if proximo and url_has_allowed_host_and_scheme(
                proximo,
                allowed_hosts={request.get_host()},
                require_https=request.is_secure(),
            ):
                return redirect(proximo)
            return redirect("index")
        erro = "Nome de usuário ou senha inválidos."
    return render(
        request,
        "registration/login.html",
        {"erro": erro}
    )

def cadastro(request):
    if request.method == "POST":
        form = CadastroForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect("index")
    else:
        form = CadastroForm()
    return render(request, "users/cadastro.html", {"form": form})

def redefinir_senha(request):
    form = None
    erro = None
    usuario = None
    etapa = request.POST.get("etapa", "identificar")

    if request.method == "POST":
        username = request.POST.get("username", "").strip()
        email = request.POST.get("email", "").strip()
        usuario = User.objects.filter(username=username, email__iexact=email).first()

        if usuario and etapa == "identificar":
            form = SetPasswordForm(usuario)
            etapa = "senha"
        elif usuario and etapa == "senha":
            form = SetPasswordForm(usuario, request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, "Senha alterada com sucesso!")
                return redirect("login")
        else:
            erro = "Nome de usuário ou e-mail inválido."

    return render(request, "users/redefinir_senha.html", {
        "form": form,
        "erro": erro,
        "usuario": usuario,
        "etapa": etapa,
    })
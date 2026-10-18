import os

from django.apps import apps as django_apps
from django.contrib.auth.management import create_permissions
from django.contrib.auth.models import Group, Permission
from django.db.models.signals import post_migrate, post_save
from django.dispatch import receiver

from .models import User

NOME_GRUPO_CLIENTE = "Cliente"
NOME_GRUPO_ADMIN = "administradores"

# Conta inicial do barbeiro (defina as variáveis de ambiente para trocar)
NOME_BARBEIRO = os.environ.get("BARBEIRO_NOME", "barbeiro")
EMAIL_BARBEIRO = os.environ.get("BARBEIRO_EMAIL", "barbeiro@seuinacio.com")
SENHA_BARBEIRO = os.environ.get("BARBEIRO_SENHA", "barbeiro123")


@receiver(post_save, sender=User)
def adicionar_novo_usuario_ao_grupo_cliente(sender, instance, created, **kwargs):
    if created:
        grupo, _ = Group.objects.get_or_create(name=NOME_GRUPO_CLIENTE)
        instance.groups.add(grupo)


@receiver(post_migrate)
def criar_grupos_e_barbeiro(sender, **kwargs):
    if sender.name != "users":
        return

    # garante que as permissões do model Postagem já existem
    create_permissions(django_apps.get_app_config("barbearia_seu_inacio"), verbosity=0)

    permissoes = Permission.objects.filter(
        content_type__app_label="barbearia_seu_inacio",
        codename__in=["view_postagem", "add_postagem", "change_postagem", "delete_postagem"],
    )

    cliente, _ = Group.objects.get_or_create(name=NOME_GRUPO_CLIENTE)
    cliente.permissions.add(*permissoes.filter(codename="view_postagem"))

    administradores, _ = Group.objects.get_or_create(name=NOME_GRUPO_ADMIN)
    administradores.permissions.add(*permissoes)

    # o barbeiro só é criado se o grupo ainda não tem ninguém e o nome e o e-mail estão livres
    if (not administradores.user_set.exists()
            and not User.objects.filter(username=NOME_BARBEIRO).exists()
            and not User.objects.filter(email=EMAIL_BARBEIRO).exists()):
        barbeiro = User.objects.create_user(
            username=NOME_BARBEIRO,
            email=EMAIL_BARBEIRO,
            password=SENHA_BARBEIRO,
            first_name="Barbeiro",
        )
        barbeiro.groups.remove(cliente)  # o post_save acima o colocou em "Cliente"
        barbeiro.groups.add(administradores)
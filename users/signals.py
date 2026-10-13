from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import Group
from .models import User

NOME_GRUPO_CLIENTE = "Cliente"  # ajuste se você criou com outro nome/caixa

@receiver(post_save, sender=User)
def adicionar_novo_usuario_ao_grupo_cliente(sender, instance, created, **kwargs):
    if created:
        grupo, _ = Group.objects.get_or_create(name=NOME_GRUPO_CLIENTE)
        instance.groups.add(grupo)
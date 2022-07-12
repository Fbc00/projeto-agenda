from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.


class Categoria(models.Model):
    nome = models.CharField(max_length=255)

    def __str__(self):
        return self.nome


class Contato(models.Model):
    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100, blank=True)
    email = models.EmailField(blank=True)
    telefone = models.CharField(max_length=15)
    descricao = models.TextField(blank=True)
    data_criacao = models.DateTimeField(default=timezone.now)
    categoria = models.ForeignKey('Categoria', on_delete=models.DO_NOTHING)
    mostrar = models.BooleanField(default=True)
    foto = models.ImageField(upload_to='fotos/%Y/%m/%d', blank=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome



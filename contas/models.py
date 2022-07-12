from django.db import models
from contatos.models import Contato
from django import forms
# Create your models here.


class FormContato(forms.ModelForm):
    class Meta:
        model = Contato
        fields = ['nome', 'sobrenome', 'email', 'telefone', 'data_criacao', 'descricao', 'categoria', 'foto']
        exclude = ()
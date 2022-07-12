from django.contrib import admin
from .models import *
# Register your models here.


class ContatoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'sobrenome', 'email', 'telefone', 'descricao', 'data_criacao', 'categoria', 'mostrar','usuario')
    list_filter = ('nome', )
    list_per_page = 10
    search_fields = ('nome', 'sobrenome', 'descricao', 'data_criacao')
    list_editable = ('telefone', 'mostrar', )


class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    list_filter = ('nome',)


admin.site.register(Contato, ContatoAdmin)
admin.site.register(Categoria, CategoriaAdmin)

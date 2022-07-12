from django.urls import path
from contas.views import login
from . import views

urlpatterns = [
    path('', login, name='index'),
    path('<int:contato_id>', views.ver_contato, name='ver_contato'),
    path('busca', views.busca, name='busca'),
]
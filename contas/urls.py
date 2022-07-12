from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='index_login'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('registrer/', views.registrer, name='registrer'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('novo_contato/', views.novo_contato, name='novo_contato'),
]
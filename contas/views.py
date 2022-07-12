from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from contatos.models import Contato
from django.core.paginator import Paginator
from django.contrib import messages, auth
from django.core.validators import validate_email
from django.contrib.auth.models import User
from .models import FormContato

# Create your views here.


def login(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    if request.method != 'POST':
        return render(request, 'contas/login.html')
    usuario = request.POST.get('usuario')
    senha = request.POST.get('senha')
    user = auth.authenticate(request, username=usuario, password=senha)
    if user is None:
        messages.error(request, 'Usuário ou senha inválidos')
        return render(request, 'contas/login.html')
    else:
        auth.login(request, user)
        messages.add_message(request, messages.SUCCESS, 'Bem vindo!')
        return redirect('dashboard')


@login_required(redirect_field_name='login', login_url='/login/')
def dashboard(request):
    contatos = Contato.objects.filter(usuario=request.user, mostrar=True)
    paginator = Paginator(contatos, 2)
    page = request.GET.get('p')
    contatos = paginator.get_page(page)
    return render(request, 'contas/dashboard.html', {'contatos': contatos})


@login_required(redirect_field_name='login', login_url='/login/')
def novo_contato(request):
    form = FormContato(request.POST, request.FILES)
    if request.method != 'POST':
        return render(request, 'contas/novo_contato.html', {'form': form})
    if not form.is_valid():
         return render(request, 'contas/novo_contato.html', {'form': form})
    form.save()
    return redirect('dashboard')


def logout(request):
    auth.logout(request)
    return redirect('login')


def registrer(request):
    # messages.success(request, 'Cadastro realizado com sucesso!')
    if request.method != 'POST':
        return render(request, 'contas/registrer.html')
    nome = request.POST.get('nome')
    sobrenome = request.POST.get('sobrenome')
    email = request.POST.get('email')
    usuario = request.POST.get('usuario')
    senha = request.POST.get('senha')
    senha2 = request.POST.get('senha2')

    if not nome or not sobrenome or not email or not usuario or not senha or not senha2:
        messages.error(request, 'Preencha todos os campos')
        return render(request, 'contas/registrer.html')
    if senha != senha2:
        messages.error(request, 'Senhas não conferem')
        return render(request, 'contas/registrer.html')
    else:
        if len(senha) < 6 and len(usuario) < 6:
            messages.error(request, 'Senha ou usuário muito curto')
            return render(request, 'contas/registrer.html')

    try:
        validate_email(email)
    except:
        messages.error(request, 'Email inválido')
        return render(request, 'contas/registrer.html')

    if User.objects.filter(username=usuario).exists():
        messages.error(request, 'Usuário já existe')
        return render(request, 'contas/registrer.html')

    if User.objects.filter(email=email).exists():
        messages.error(request, 'Email já existe')
        return render(request, 'contas/registrer.html')
    messages.add_message(request, messages.SUCCESS, 'Cadastro realizado com sucesso!')
    user = User.objects.create_user(username=usuario, email=email, password=senha, first_name=nome, last_name=sobrenome)
    user.save()
    return redirect('login')




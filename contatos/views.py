from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from django.contrib.auth.decorators import login_required
from .models import Contato
from django.core.paginator import Paginator
from django.db.models import Q,Value
from django.db.models.functions import Concat
from django.contrib import messages
# Create your views here.


@login_required(redirect_field_name='login', login_url='/login/')
def ver_contato(request, contato_id):
    if not request.user.is_authenticated:
        raise Http404('Usuário não autenticado.')
    contato = get_object_or_404(Contato, id=contato_id)
    if not contato.mostrar:
        raise Http404()
    return render(request, 'contatos/ver_contato.html', {'contato': contato})


def busca(request):
    termo = request.GET.get('termo')
    if termo is None or termo == '':
        messages.add_message(request, messages.ERROR, 'Por favor, digite um termo de busca.')
        return redirect('dashboard')
    campos = Concat('nome', Value(' '), 'sobrenome')
    contatos = Contato.objects.annotate(nomecompleto=campos)

    contatos = contatos.filter(
            Q(nomecompleto__icontains=termo) | Q(telefone__icontains=termo)
        )
    paginator = Paginator(contatos, 1)
    page = request.GET.get('p')
    contatos = paginator.get_page(page)
    return render(request, 'contatos/busca.html', {'contatos': contatos})
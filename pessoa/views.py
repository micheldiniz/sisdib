from typing import Any
from django.shortcuts import render, redirect
from .forms import PessoaFisicaRegistrationForm, EnderecoRegistrationForm, ContatoRegistrationForm, SolicitanteRegistrationForm
from django.contrib.auth.decorators import login_required
from pessoa.models import PessoaFisica
from django.core.paginator import Paginator

# Create your views here.
@login_required
def pessoafisica_registration(request):
    if request.method == 'POST':
        pessoa_fisica_form = PessoaFisicaRegistrationForm(request.POST, prefix='pessoa_fisica')
        endereco_form = EnderecoRegistrationForm(request.POST, prefix='endereco')
        contato_form = ContatoRegistrationForm(request.POST, prefix='contato')
        solicitante_form = SolicitanteRegistrationForm(request.POST, prefix='solicitante')

        if pessoa_fisica_form.is_valid() and endereco_form.is_valid() and contato_form.is_valid():
            pessoa_fisica = pessoa_fisica_form.save()
            endereco = endereco_form.save(commit=False)
            contato = contato_form.save(commit=False)
            solicitante = solicitante_form.save(commit=False)

            endereco.pessoa = pessoa_fisica
            endereco.save()

            contato.pessoa = pessoa_fisica
            contato.save()

            solicitante.pessoa = pessoa_fisica
            solicitante.save()

            return redirect('success_page')

    else:
        pessoa_fisica_form = PessoaFisicaRegistrationForm(prefix='pessoa_fisica')
        endereco_form = EnderecoRegistrationForm(prefix='endereco')
        contato_form = ContatoRegistrationForm(prefix='contato')
    return render(request, 'register_pessoa_fisica.html', {
        'pessoa_fisica_form': pessoa_fisica_form,
        'endereco_form': endereco_form,
        'contato_form': contato_form,
    })

def success_page(request):
    return render(request, 'success.html')

@login_required
def pessoa_all(request):
    pessoas = PessoaFisica.objects.all()
    itens_por_pagina = request.GET.get('itens')    
    if (itens_por_pagina):
        paginator = Paginator(pessoas, itens_por_pagina)
    else:
        paginator = Paginator(pessoas, 50)
    page_number = request.GET.get('page')

    page_obj = paginator.get_page(page_number)
    
    return render(request, "all.html", {"page_obj":page_obj})

@login_required
def deletar_pessoa(request):
    id_pessoa = request.GET.get('id')
    # if request.method == 'POST':
    #     print(id_pessoa)
    pass
from django.shortcuts import render, redirect
from .forms import PessoaFisicaRegistrationForm, EnderecoRegistrationForm, ContatoRegistrationForm, ClienteRegistrationForm

# Create your views here.
def pessoafisica_registration(request):
    if request.method == 'POST':
        pessoa_fisica_form = PessoaFisicaRegistrationForm(request.POST, prefix='pessoa_fisica')
        endereco_form = EnderecoRegistrationForm(request.POST, prefix='endereco')
        contato_form = ContatoRegistrationForm(request.POST, prefix='contato')
        cliente_form = ClienteRegistrationForm(request.POST, prefix='cliente')

        if pessoa_fisica_form.is_valid() and endereco_form.is_valid() and contato_form.is_valid():
            pessoa_fisica = pessoa_fisica_form.save()                       
            endereco = endereco_form.save(commit=False)                        
            contato = contato_form.save(commit=False)
            cliente = cliente_form.save(commit=False)

            endereco.pessoa = pessoa_fisica
            endereco.save()

            contato.pessoa = pessoa_fisica
            contato.save()

            cliente.pessoa = pessoa_fisica
            cliente.save()
            
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
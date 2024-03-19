from django.shortcuts import render
from .forms import MaterialAdaptadoForm
from django.http import HttpResponse

def index(request):
    return HttpResponse("Index Material!")

def cadastrar_Material(request):
    if request.method == 'POST':
        form = MaterialAdaptadoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'success.html')
    else:
        form = MaterialAdaptadoForm()
    return render(request, 'material.html', {'form':form})
    

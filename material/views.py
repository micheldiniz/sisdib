from django.shortcuts import render
from .forms import MaterialAdaptadoForm
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from material.models import Material,MaterialAdaptado

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
    
@login_required
def download_file(request, material_id):
    material = get_object_or_404(Material, id=material_id)
    if material.arquivo_original:
        response = HttpResponse(material.arquivo_original, content_type='application/pdf')
        response['content-Dosposition'] = f'attachment; filename="{material.arquivo_original.name}"'
        return response
    return HttpResponse('File not Found')

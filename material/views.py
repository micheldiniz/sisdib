from django.shortcuts import render
from .forms import MaterialAdaptadoFormSet, MaterialForm
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from material.models import Material,MaterialAdaptado

def index(request):
    return HttpResponse("Index Material!")

def cadastrar_material(request):
    if request.method == 'POST':
        materialAdaptado_form = MaterialAdaptadoFormSet(request.POST, request.FILES)
        material_form = MaterialForm(request.POST, request.FILES)
        
        if materialAdaptado_form.is_valid() and material_form.is_valid():
            material = material_form.save()
            materialAdaptado_form.instance = material
            materialAdaptado_form.save()            
            return render(request, 'success.html')
    else:
        material_form = MaterialForm()
        materialAdaptado_form = MaterialAdaptadoFormSet()
    return render(request, 'material/cadastrar.html', {
        'material_form' : material_form,
        'materialAdaptado_form' : materialAdaptado_form,
    })

def visualizar_material(request):
    pass

@login_required
def download_file(request, material_id):
    material = get_object_or_404(Material, id=material_id)
    if material.arquivo_original:
        response = HttpResponse(material.arquivo_original, content_type='application/pdf')
        response['content-Dosposition'] = f'attachment; filename="{material.arquivo_original.name}"'
        return response
    return HttpResponse('File not Found')

from django.shortcuts import render
from .forms import MaterialAdaptadoFormSet, MaterialForm, MaterialAdaptadoForm
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from material.models import Material,MaterialAdaptado
from django.urls import reverse
from django.shortcuts import redirect

def index(request):
    return HttpResponse("Index Material!")

def cadastrar_material(request):
    if request.method == 'POST':        
        material_form = MaterialForm(request.POST, request.FILES)
  
        if material_form.is_valid():
            material = material_form.save()               
            return redirect(reverse(list_materials))
    else:
        material_form = MaterialForm()        

    return render(request, 'material/cadastrar.html', {
        'form' : material_form,
        'titulo':"Material",
        'subtitulo':"Original",
        'app':'material',
        'app_description':'Material',
    })

def list_materials(request):
    all_materials = Material.objects.all()

    field_names = [field.name for field in Material._meta.fields]

    context = {'objects': all_materials,
            'titulo':"Material",
            'subtitulo':"Original",
            'fields':field_names,
            }
    return render(request, 'material/lista.html', context)

def cadastrar_material_adaptado(request):
    if request.method == 'POST':
        materialAdaptado_form = MaterialAdaptadoForm(request.POST, request.FILES)        
  
        if materialAdaptado_form.is_valid():
            material_adaptado = materialAdaptado_form.save()               
            return redirect(reverse(list_materiais_adaptados))
    else:
        materialAdaptado_form = MaterialAdaptadoForm()

    return render(request, 'material/cadastrar.html', {
        'form' : materialAdaptado_form,
        'titulo':"Material",
        'subtitulo':"Adaptado",
        'app':'material/adaptado',
    })

def list_materiais_adaptados(request):
  all_materiais_adaptados = MaterialAdaptado.objects.all()
  context = {'objects': all_materiais_adaptados,
            'titulo':"Material",
            'subtitulo':"Adaptado",
            'app_description':'Material Adaptado'
            }
  return render(request, 'material/lista.html', context)

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

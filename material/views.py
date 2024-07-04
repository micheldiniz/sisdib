from django.shortcuts import render
from .forms import MaterialAdaptadoFormSet, MaterialForm, MaterialAdaptadoForm
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from material.models import Material,MaterialAdaptado
from django.urls import reverse, reverse_lazy
from django.shortcuts import redirect
from django.views.generic import ListView
from django.core.paginator import Paginator
from django.views.generic.edit import DeleteView

def index(request):
    return redirect(reverse(list_materiais))

def cadastrar_material(request):
    if request.method == 'POST':        
        material_form = MaterialForm(request.POST, request.FILES)
  
        if material_form.is_valid():
            material = material_form.save()               
            return redirect(reverse(list_materiais))
    else:
        material_form = MaterialForm()        

    return render(request, 'material/cadastrar.html', {
        'form' : material_form,
        'titulo':"Material",
        'subtitulo':"Original",
        'app':'material',
        'app_description':'Material',
    })

def list_materiais(request):
    all_materiais = Material.objects.all()
    
    paginator = Paginator(all_materiais, 10)
    
    page_number = request.GET.get("page")

    objects = paginator.get_page(page_number)

    all_materiais = request

    context = {'objects': objects,
            'titulo':"Material",
            'subtitulo':"Original",
            'ths':['ID','Classificacao','Titulo','Autor','Edicao','Editora','Público Alvo','Acervo', 'Tiragem','Qtd Páginas','Arquivo Original','Adaptações'],
            'app':'material',
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
            'app_description':'Material Adaptado',
            'ths':[
                'ID',
                'Material',
                'Tipo',
                'Qtd páginas',
                'Partes',
                'Tamanho (Kg / Mb)',
                'Disponível para pedido?',
                'Arquivo adaptado',
                ],
            }
  return render(request, 'material/lista_adaptado.html', context)

def visualizar_material(request, id):
    
    material = get_object_or_404(Material, id=id)

    return render(request, 'material/view.html', {
        'object': material,
        'titulo':"Material",
        'subtitulo':"Original",
        'app':'material',
        'app_description':'Material',})

def visualizar_material_adaptado(request, id):
    
    material_adaptado = get_object_or_404(MaterialAdaptado, id=id)
    return render(request, 'material/view_adaptado.html', {
        'object': material_adaptado,
        'titulo':"Material",
        'subtitulo':"Adaptado",
        'app':'material',
        'app_description':'Material',})

def editar_material(request, id):
    
    material = get_object_or_404(Material, id=id)

    if request.method == 'POST':
        form = MaterialForm(request.POST, request.FILES, instance=material)
        if form.is_valid():
            form.save()
            return redirect(reverse('visualizar_material', args=[material.id]))
    else:
        form = MaterialForm(instance=material)

    return render(request, 'material/editar.html', {
        'form': form,
        'titulo':"Material",
        'subtitulo':"Original",
        'app':'material',
        'app_description':'Material',})

def editar_material_adaptado(request, id):
    
    material_adaptado = get_object_or_404(MaterialAdaptado, id=id)

    if request.method == 'POST':
        form = MaterialAdaptadoForm(request.POST, request.FILES, instance=material_adaptado)        
        if form.is_valid():
            form.save()
            return redirect(reverse('visualizar_material_adaptado', args=[material_adaptado.id]))        
    else:
        form = MaterialAdaptadoForm(instance=material_adaptado)

    return render(request, 'material/editar_adaptado.html', {
        'form': form,
        'titulo':"Material",
        'subtitulo':"Adaptado",
        'app':'material',
        'app_description':'Material',})

def material_delete(request, material_id):
    obj = get_object_or_404(Material, id=material_id)
    obj.delete()
    return redirect(reverse(list_materiais))

def material_adaptado_delete(request, material_id):
    pass

class MaterialListView(ListView):
    model = Material
    template_name = 'material/lista.html'
    context_object_name = 'material_adaptado'
    paginate_by = 10

    def get_queryset(self):
        return Material.objects.prefetch_related('materiais_adaptados')

@login_required
def download_file(request, material_id):
    material = get_object_or_404(Material, id=material_id)
    if material.arquivo_original:
        response = HttpResponse(material.arquivo_original, content_type='application/pdf')
        response['content-Dosposition'] = f'attachment; filename="{material.arquivo_original.name}"'
        return response
    return HttpResponse('File not Found')



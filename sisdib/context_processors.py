from pessoa.models import Funcionario


def funcionario_loggado(request):
    if request.user.is_authenticated:
        try:
            funcionario = Funcionario.objects.get(user=request.user)
            return {'funcionario_logado':funcionario}
        except Funcionario.DoesNotExist:
            return {'funcionario_logado': None}
    return {'funcionario_logado': None}
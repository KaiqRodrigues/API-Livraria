from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View
from django.http import JsonResponse, HttpResponse
import json, os
from nucleo.models import Categoria


# poderia ser usado funcao com if request == "GET"
@method_decorator(csrf_exempt, name='dispatch')
class CategoriaView(View):
    def get(self, request, id=None):
        if id:          #se recebe Id, pega os dados e responde
            qs = Categoria.objects.get(id=id)
            data = {} 
            data['id'] = qs.id
            data['descricao'] = qs.descricao
            return JsonResponse(data)
        else:
            data = list(Categoria.objects.values())   # pega as categorias       # formata para json
            return JsonResponse(data, safe=False)

        
    def post(self, request):
        json_data = json.loads(request.body)   # ta pegando o dado enviado e transformadno em json
        nova_categoria = Categoria.objects.create(**json_data)    #com kwargs nao precisa listar o dicionario inteiro do json
        dado = {'id': nova_categoria.id, 'descricao': nova_categoria.descricao} 
        return JsonResponse(dado)


    def patch(self, request, id=None):
        json_data = json.loads(request.body)
        qs = Categoria.objects.get(id=id)
        qs.descricao = json_data['descricao']
        qs.save()
        data = {}
        data['id'] = qs.id
        data['descricao'] = qs.descricao
        return JsonResponse(data)
    
    def delete(self, request, id):
        qs = Categoria.objects.get(id=id)
        qs.delete()
        
        return JsonResponse({'Mensagem': 'item excluido'})


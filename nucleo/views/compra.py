from rest_framework.viewsets import ModelViewSet
from nucleo.models import Compra
from drf_spectacular.utils import extend_schema, extend_schema_view, OpenApiResponse, OpenApiExample
from nucleo.serializers import CompraSerializer, CriarEditarCompraSerializer

class CompraViewSet(ModelViewSet):
    queryset = Compra.objects.all()
    # serializer_class = CompraSerializer
    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'retrieve':   #Se for apenas vizualizar é o Basico, se nao, o detalhado
            return CompraSerializer
        return CriarEditarCompraSerializer

    def get_queryset(self):

        usuario = self.request.user
        if usuario.groups.filter(name = 'Adm').exists():      #busca apenas as compras do usuario autenticado
            return Compra.objects.all()
        return Compra.objects.filter(usuario = usuario)
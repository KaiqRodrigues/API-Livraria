from nucleo.models import Categoria
from rest_framework.viewsets import ModelViewSet

from nucleo.serializers import CategoriaSerializer


class CategoriaViewSet(ModelViewSet):

    queryset = Categoria.objects.all()     
    serializer_class = CategoriaSerializer
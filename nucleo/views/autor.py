from nucleo.models import Autor
from rest_framework.viewsets import ModelViewSet
from nucleo.serializers import AutorSerializer


class AutorViewSet(ModelViewSet):
    queryset = Autor.objects.all()     
    serializer_class = AutorSerializer
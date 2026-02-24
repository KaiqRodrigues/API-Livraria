from rest_framework.viewsets import ModelViewSet
from nucleo.models import Editora
from nucleo.serializers import EditoraSerializer

class EditoraViewSet(ModelViewSet):
    queryset = Editora.objects.all()
    serializer_class = EditoraSerializer
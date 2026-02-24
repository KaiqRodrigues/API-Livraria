from nucleo.models import Livro
from rest_framework.viewsets import ModelViewSet
from nucleo.serializers import LivroSerializer, LivroDetailSerializer


class LivroViewSet(ModelViewSet):
    queryset = Livro.objects.all()
    # serializer_class = LivroSerializer
    def get_serializer_class(self):
        if self.action == 'list':
            return LivroDetailSerializer
        elif self.action == 'retrieve':
            return LivroDetailSerializer
        return LivroSerializer

 
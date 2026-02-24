from django.shortcuts import get_object_or_404
from rest_framework.serializers import ModelSerializer

from nucleo.models import Categoria

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from nucleo.serializers import CategoriaSerializer



class CategoriasListGeneric(ListCreateAPIView):
    queryset = Categoria.objects.all()     #DOCUMENTAÇÂO OBRIGA OS NOMES DE VARIAVEL ASSIM
    serializer_class = CategoriaSerializer

class CategoriasDetailGeneric(RetrieveUpdateDestroyAPIView):
    lookup_field = 'id'
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

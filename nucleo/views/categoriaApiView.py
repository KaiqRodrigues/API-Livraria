from rest_framework.views import APIView
from rest_framework.serializers import ModelSerializer
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse, HttpResponse
from django.shortcuts import get_object_or_404

from nucleo.models import Categoria


from nucleo.serializers import CategoriaSerializer


class CategoriasList(APIView):      
    def get(self, request):
        categoria = Categoria.objects.all()
        serializer = CategoriaSerializer(categoria, many=True)  #permite varias categorias no serializer
        return Response(serializer.data)   #responde ja serializado
    
    def post(self, request):
        serializer = CategoriaSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        else:
            return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)
    
class CategoriaDetail(APIView):
    def get(self, request,id):
        categoria = get_object_or_404(Categoria.objects.all(), id=id)   
        serializer = CategoriaSerializer(categoria)
        return Response(serializer.data, status= status.HTTP_201_CREATED)
    
    def put(self, request, id):
        categoria = get_object_or_404(Categoria.objects.all(), id=id)
        serializer = CategoriaSerializer(categoria, data=request.data)
        if serializer.is_valid():
            serializer.save()   
            return Response(serializer.data)
        else:
            return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, id):
        categoria = get_object_or_404(Categoria.objects.all(), id=id)   
        categoria.delete()        
        return Response(status=status.HTTP_204_NO_CONTENT)
    
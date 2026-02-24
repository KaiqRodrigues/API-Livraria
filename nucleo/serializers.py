from rest_framework.serializers import ModelSerializer, SerializerMethodField, CharField
from rest_framework import serializers
from nucleo.models import Categoria, Editora, Autor, Livro, Compra, ItensCompra
from nucleo.services.compra_service import CompraService

class CategoriaSerializer(ModelSerializer):  #deixa nesse modelo
    class Meta:  #define a config do serializer
        model = Categoria
        fields = '__all__'  # pra não precisar colocar campo por campo   

class EditoraSerializer(ModelSerializer):
    class Meta:
        model = Editora
        fields = '__all__'


# EXEMPLO QUE SERIELIZER CUSTOMIZADO
class EditoraSimplesSerializer(ModelSerializer):
    class Meta:
        model = Editora
        fields = ('nome',)

class AutorSerializer(ModelSerializer):
    class Meta:
        model = Autor
        fields ='__all__'

class LivroSerializer(ModelSerializer):
    class Meta:
        model = Livro
        fields = '__all__'

class LivroDetailSerializer(ModelSerializer):
    editora = EditoraSimplesSerializer()    #serializer customizado
    class Meta:
        model = Livro
        fields = '__all__'
        depth = 1



class ItensCompraSerializer(ModelSerializer):
    total = SerializerMethodField()

    class Meta:
        model = ItensCompra
        fields = ('livro', 'quantidade', 'total')
        depth = 2

    def get_total(self, instance):
        return instance.quantidade * instance.livro.preco



class CriarEditarItensCompraSerializer(ModelSerializer):  #SERIALIZER SEM DEPTH
    class Meta:
        model = ItensCompra
        fields = ('livro', 'quantidade')

    def validate(self, data):
        if data['quantidade'] > data['livro'].qtd:
            raise serializers.ValidationError({
                'quantidade': 'Quantidade solicitada não disponível em estoque'
            })
        return data


class CompraSerializer(ModelSerializer):
    usuario = CharField(source='usuario.email')
    status = SerializerMethodField()
    itens = ItensCompraSerializer(many = True)  #pode ter varios itens na mesma compra

    class Meta:
        model = Compra
        fields = ('id', 'usuario', 'status', 'itens', 'total')
        
    def get_status(self, instance):
        return instance.get_status_display()



class CriarEditarCompraSerializer(ModelSerializer):
    itens = CriarEditarItensCompraSerializer(many=True)
    usuario = serializers.HiddenField(default= serializers.CurrentUserDefault())

    class Meta:
        model = Compra
        fields = ('usuario', 'itens')

    def create(self, validated_data):
        itens = validated_data.pop('itens') #itens que vieram dos dados validados (usuario e itens)
        usuario = validated_data.pop("usuario")
        return CompraService.criar_compra(usuario, itens)

    def update(self, instance, validated_data):
        itens = validated_data.pop("itens")
        return CompraService.atualiza_compra(instance, itens)


from django.db import models
from django.db.models import F
from django.contrib.auth.models import User  #utilizar o user do django, pode ser encontrado no painel adm

class Categoria(models.Model):
    descricao = models.CharField(max_length = 255)

    def __str__(self):    # pra devolver a descricao da categoria e nao o obj quando printado
        return self.descricao
    

class Editora(models.Model):
    nome = models.CharField(max_length=255)
    site = models.URLField()

    def __str__(self):
        return self.nome

class Autor(models.Model):
    nome = models.CharField(max_length=255)
    
    def __str__(self):
        return self.nome

class Livro(models.Model):
    titulo = models.CharField(max_length=255)
    isbn = models.CharField(max_length=32)
    qtd = models.IntegerField()
    preco = models.FloatField()
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT, related_name="livros")
    editora = models.ForeignKey(Editora, on_delete=models.PROTECT, related_name="livros")
    autores =  models.ManyToManyField(Autor, related_name="livros")

    def __str__(self):
        return self.titulo


class Compra(models.Model):

    class StatusCompra(models.IntegerChoices):
        CARRINHO = 1,'Carrinho'
        AGUARDANDO_PAGAMENTO = 2, "Aguardando Pagamento"
        PAGO = 3, "Pago"

    usuario = models.ForeignKey(User, on_delete=models.PROTECT, related_name='compras')
    status = models.IntegerField(choices=StatusCompra.choices, default=StatusCompra.CARRINHO)


    @property
    def total(self):
        queryset = self.itens.all().aggregate(
            total = models.Sum(F('quantidade') * F('livro__preco'))
        )
        return queryset['total']





class ItensCompra(models.Model):
    compra = models.ForeignKey(Compra, on_delete=models.CASCADE, related_name='itens')
    livro = models.ForeignKey(Livro, on_delete=models.PROTECT, related_name='vendas')
    quantidade = models.IntegerField()
    
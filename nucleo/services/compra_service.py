from django.db import transaction
from django.db.models import F
from rest_framework.exceptions import ValidationError
from nucleo.models import Compra, ItensCompra, Livro


class CompraService:

 
    #como parte das operações de C e U são iguais, foi generalizado nesse metodo
    def criar_alterar_itens(compra,itens):

        for item in itens:
            #bloqueia o estoque do livro
            livro = Livro.objects.select_for_update().get(pk = item["livro"].pk)
            quantidade = item["quantidade"]

            if livro.qtd < quantidade:
                raise ValidationError(f"Estoque insuficiente do Item {livro.titulo}")

            Livro.objects.filter(pk=livro.pk).update(qtd=F('qtd') - quantidade)
            #cria item compra com o relaiconamento
            ItensCompra.objects.create(
                compra = compra,
                livro = livro,
                quantidade = quantidade
            )
        return compra



    @staticmethod
    @transaction.atomic
    def criar_compra(usuario, itens):
        if not itens:
            raise ValidationError("A compra deve ter pelo menos um item")
        
        compra = Compra.objects.create(usuario = usuario)
        CompraService.criar_alterar_itens(compra, itens)

        return compra


    @staticmethod
    @transaction.atomic
    def atualiza_compra(compra, itens):

        for item in compra.itens.all():
            Livro.objects.filter(pk = item.livro.pk).update(
                qtd = F("qtd") + item.quantidade
            )
        compra.itens.all().delete()

        CompraService.criar_alterar_itens(compra,itens)

        return compra

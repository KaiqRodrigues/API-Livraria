from django.contrib import admin

from nucleo.models import Categoria, Editora, Autor, Livro, Compra, ItensCompra


admin.site.register(Categoria)
admin.site.register(Editora)
admin.site.register(Autor)
admin.site.register(Livro)  


class ItensInline(admin.TabularInline):  # cria uma classe para os itens da compra em forma inline
    model = ItensCompra                  # ItensCompra que possui os valores reais

class CompraAdmin(admin.ModelAdmin):     #inlines recebe a uma tupla de Classes model do ItensCompra
    inlines = (ItensInline, )            #ModelAdmin aplica as regras de comportamento (nesse caso inline)

admin.site.register(Compra, CompraAdmin)  #Registra o model compra e o CompraAdmin que represnta os itens
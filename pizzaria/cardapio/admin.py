from django.contrib import admin
from django.utils.html import format_html
from .models import TipoIngrediente, TipoPizza, Ingrediente, Pizza, IngredientePizza
# Register your models here.

@admin.register(TipoPizza)
class TipoPizzaAdmin(admin.ModelAdmin):
    list_display = ['nome', 'descricao']

@admin.register(TipoIngrediente)
class TipoIngredienteAdmin(admin.ModelAdmin):
    list_display =['nome','icone']

@admin.register(Ingrediente)
class IngredienteAdmin(admin.ModelAdmin):
    list_display=['nome','tipo_ingrediente','preco_formatado', 'disponivel']

    #Filtros
    list_filter = ['tipo_ingrediente','disponivel']

    def preco_formatado(self,obj):
        return f'R$ {obj.preco_por_unidade:.3f}/{obj.unidade_medida}'    
    #Rotulo
    preco_formatado.short_description = 'Preço'

class IngredientePizzaInline(admin.TabularInline):
    #Definir Model
    model = IngredientePizza
    #Adcionar um 1 campo extra
    extra = 1
    #Quais campos eu quero mostrar

    fields = ['ingrediente','quantidade_numerica','quantidade_texto']

    
@admin.register(Pizza)
class PizzaAdmin(admin.ModelAdmin):
    list_display = ['nome','tipo_pizza','preco_total_formatado','tempo_preparo',
                    'ativa']
    list_filter = ['tipo_pizza','ativa']
    inlines = [IngredientePizzaInline]

    def preco_total_formatado(self, obj):
        return f'R$ {obj.preco_total:.2f}'
    
    preco_total_formatado.short_description = 'Preço Total'

admin.site.site_header ="SENAC PIZZA - Administração"
admin.site.site_title = "Pizzaria Admin"
from django.contrib import admin
from catalogo.models import ArregloFloral, ImagenArreglo, Categoria, Etiqueta, CaracteristicasProducto

class CaracteristicasInline(admin.TabularInline):
    model = CaracteristicasProducto
    extra = 1
    max_num = 10
    fields = ['nombre', 'valor']

class ImagenArregloInline(admin.TabularInline):
    model = ImagenArreglo
    extra = 1
    max_num = 6
    fields = ['imagen', 'is_principal']

@admin.register(ArregloFloral)
class ArregloFloralAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'precio', 'disponible', 'categoria']
    inlines = [ImagenArregloInline, CaracteristicasInline]

admin.site.register(Categoria)
admin.site.register(Etiqueta)

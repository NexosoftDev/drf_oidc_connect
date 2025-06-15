from rest_framework import serializers
from catalogo.models import ArregloFloral, ImagenArreglo, Etiqueta, Categoria, CaracteristicasProducto


class CaracteristicasProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CaracteristicasProducto
        fields = ['nombre', 'valor']

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ['nombre']

class EtiquetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Etiqueta
        fields = ['nombre']


class ImagenArregloSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImagenArreglo
        fields = ['imagen', 'is_principal']


class ArregloFloralSerializer(serializers.ModelSerializer):
    imagenes = ImagenArregloSerializer(many=True, read_only=True)
    etiquetas = EtiquetaSerializer(many=True, read_only=True)
    categoria = CategoriaSerializer(read_only=True)
    caracteristicas = CaracteristicasProductoSerializer(many=True, read_only=True)

    class Meta:
        model = ArregloFloral
        fields = '__all__'
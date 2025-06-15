from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"

class Etiqueta(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Etiqueta"
        verbose_name_plural = "Etiquetas"

class ArregloFloral(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    disponible = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, related_name='arreglos')
    etiquetas = models.ManyToManyField(Etiqueta, blank=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Arreglo Floral"
        verbose_name_plural = "Arreglos Florales"

class ImagenArreglo(models.Model):
    arreglo = models.ForeignKey(ArregloFloral, on_delete=models.CASCADE, related_name='imagenes')
    imagen = models.ImageField(upload_to='arreglos/')
    is_principal = models.BooleanField(default=False)

    def __str__(self):
        principal = " (Principal)" if self.is_principal else ""
        return f"Imagen de {self.arreglo.nombre}{principal}"

    class Meta:
        verbose_name = "Imagen de Arreglo"
        verbose_name_plural = "Imagenes de Arreglos"


class CaracteristicasProducto(models.Model):
    nombre = models.CharField(max_length=100, null=True, blank=True)
    valor = models.CharField(max_length=100, null=True, blank=True)
    arreglo = models.ForeignKey('ArregloFloral', on_delete=models.CASCADE, null=True, blank=True,
                                related_name='caracteristicas')



    def __str__(self):
        return self.nombre + " " + self.valor

    class Meta:
        verbose_name = "Caracteristica de Producto"
        verbose_name_plural = "Caracteristicas de los Productos"
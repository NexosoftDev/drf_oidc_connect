from django.db import models
from users.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=150, null=True, blank=True)
    correo = models.EmailField()
    telefono = models.CharField(max_length=150, null=True, blank=True)


    @receiver(post_save, sender=User)
    def create_user_perfile(sender, instance, created, **kwargs):
        if created:
            Perfil.objects.create(
                user=instance,
                username=instance.username,
                correo=instance.email
            )

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "Perfil"
        verbose_name_plural = "Perfiles"


class DomicilioBasico(models.Model):
    perfil = models.OneToOneField(Perfil, on_delete=models.CASCADE, related_name='domicilio')
    estado = models.JSONField(null=True, blank=True, max_length=250)
    municipio = models.JSONField(null=True, blank=True, max_length=250)
    codigo_postal = models.CharField(max_length=5, null=True, blank=True)
    colonia = models.CharField(max_length=255, null=True, blank=True)
    calle = models.CharField(max_length=255, null=True, blank=True)
    numero_exterior = models.CharField(max_length=255, null=True, blank=True)
    numero_interior = models.CharField(max_length=255, null=True, blank=True)


    @receiver(post_save, sender=Perfil)
    def create_domicilio_basico(sender, instance, created, **kwargs):
        if created:
            DomicilioBasico.objects.create(perfil=instance)


    def __str__(self):
        return f'{self.perfil} | {self.colonia} - {self.municipio} - {self.estado}'


    class Meta:
        verbose_name = "Domicilio basico"
        verbose_name_plural = "Domicilios basicos"
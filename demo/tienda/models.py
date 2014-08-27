from django.db import models

# Create your models here.

class Rubro(models.Model):
    nombre = models.CharField(max_length=255)
    def __unicode__(self):
        return self.nombre

class Producto(models.Model):
    cantidad = models.PositiveIntegerField(default=0)
    precio = models.PositiveIntegerField(default=0)
    nombre = models.CharField(max_length=255)
    rubro = models.ForeignKey(Rubro)

    def disponible(self):
        return self.cantidad > 0

    def url(self):
        return "/media/images/producto_" + str(self.id)

    def __unicode__(self):
        return self.nombre


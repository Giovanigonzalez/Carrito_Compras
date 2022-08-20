from django.db import models

# Create your models here.
class Producto(models.Model):
    nombre = models.CharField(max_length=64)
    categoria = models.CharField(max_length=32)
    precio = models.IntegerField()

    def __str__(self):
        txt="{0} {1} {2}".format(self.nombre,self.categoria,self.precio)
        return txt

from django.db import models

# Create your models here.
class Persona(models.Model):
    id= models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=100, verbose_name='Nombre')
    apellido=models.CharField(max_length=100, verbose_name='Apellido')

    def __str__(self):
        return(self.nombre)
from django.db import models

# Create your models here.
class User(models.Model):
    rut = models.CharField(primary_key=True, max_length=10)
    nombre = models.CharField(max_length=20)
    apellido_paterno = models.CharField(max_length=20)
    apellido_materno = models.CharField(max_length=20)
    fecha_nacimiento = models.DateField()
    genero = models.CharField(max_length=20)
    correo = models.EmailField(max_length=100, unique=True, blank=True, null=True)
    contraseña = models.CharField(max_length=30)

    def __str__(self):
        return (
            str(self.nombre)
            + " "
            + str(self.apellido_paterno)
            + " "
            + str(self.apellido_materno)
        )    
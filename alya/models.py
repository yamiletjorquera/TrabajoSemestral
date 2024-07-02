from django.db import models

class User(models.Model):
    rut = models.CharField(primary_key=True, max_length=12)
    nombre = models.CharField(max_length=20)
    apellido_paterno = models.CharField(max_length=20)
    apellido_materno = models.CharField(max_length=20)
    fecha_nacimiento = models.DateField()
    genero = models.CharField(max_length=20)
    correo = models.EmailField(max_length=100, unique=True, blank=True, null=True)
    contraseña = models.CharField(max_length=30)
    activo = models.BooleanField()

    def __str__(self):
        return (
            str(self.nombre)
            + " "
            + str(self.apellido_paterno)
            + " "
            + str(self.apellido_materno)
        )    

class Author(models.Model):
    id = models.CharField(primary_key=True, max_length=10)
    name = models.CharField(max_length=20)
    born_date = models.DateField()
    picture = models.CharField(max_length=10)

    def __str__(self):
        return (str(self.name))
    
class Book(models.Model):
    id = models.CharField(primary_key=True, max_length=10)
    title = models.CharField(max_length=100)
    genre = models.CharField(max_length=20)
    year = models.IntegerField()
    synopsis = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    available = models.BooleanField()
    picture = models.CharField(max_length=10)

    def __str__(self):
        return (str(self.title))
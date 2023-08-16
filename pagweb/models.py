from django.db import models

class Curso(models.Model):
    nombre=models.CharField(max_length=50)
    comision=models.IntegerField()

    def __str__(self) -> str:
        return f"Nombre: {self.nombre} - Comision: {self.comision}"

class Alumno(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)

    def __str__(self) -> str:
        return f"Nombre: {self.nombre} - Apellido: {self.apellido}"    

class Profesor(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)

    def __str__(self) -> str:
        return f"Nombre: {self.nombre} - Apellido: {self.apellido}"
    
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
# Create your models here.

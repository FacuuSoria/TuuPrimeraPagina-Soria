from django.db import models
from django.contrib.auth.models import User, AbstractBaseUser, PermissionsMixin, UserManager
from django.utils import timezone
from ckeditor.fields import RichTextField

class CustomUserManager(UserManager):
    def _create_user(self, email, password,):
        if not email:
            raise ValueError("El email esta mal")
        email = self.normalize_email(email)
        user = self.model(email=email,)
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_user(self, email=None, password=None):
        return self._create_user(email, password)

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
    titulo = models.CharField(max_length=200)
    subtitulo = models.CharField(max_length=200)
    cuerpo = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)
    imagen = models.ImageField(upload_to='avatares/', null=True, blank=True)
    autor = models.CharField(max_length=200)

    def __str__(self):
        return self.titulo

class Avatar(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatares', null=True, blank=True)
    def __str__(self):
        return f"{self.user} - {self.imagen}"

class User(AbstractBaseUser):
    email = models.EmailField(blank=True, default='', unique=True)
    username = models.CharField(max_length=200, blank=True, default='')
    date_joined = models.DateTimeField(default=timezone.now)
    objects = CustomUserManager()
    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []
    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
    def get_full_name(self):
        return self.name
    def get_short_name(self):
        return self.name or self.email.split('@')[0]

# Create your models here.

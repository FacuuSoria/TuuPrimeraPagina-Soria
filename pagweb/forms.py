from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm, UserModel, AuthenticationForm

class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = '__all__'

class AlumnoForm(forms.ModelForm):
    class Meta:
        model = Alumno
        fields = '__all__'

class ProfesorForm(forms.ModelForm):
    class Meta:
        model = Profesor
        fields = '__all__'

class BusquedaCurso(forms.Form):
    nombre = forms.CharField(required=False)

class BusquedaAlumno(forms.Form):
    nombre = forms.CharField(required=False)

class BusquedaProfesor(forms.Form):
    nombre = forms.CharField(required=False)

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']
        
class UserCreationFormCustom(UserCreationForm):
    username=forms.CharField(label="usuario")
    password1=forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2=forms.CharField(label="Repita la Contraseña", widget=forms.PasswordInput)
    class Meta:
        model = UserModel
        fields = ['username', 'password1', 'password2']
        help_texts = {k:"" for k in fields}

class AuthenticationFormCustom(AuthenticationForm):
    username=forms.CharField(label="usuario")
    password=forms.CharField(label="Contraseña", widget=forms.PasswordInput)
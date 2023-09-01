from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm, UserModel, AuthenticationForm, UserChangeForm
from django.contrib.auth import get_user_model

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
        fields = '__all__'
        
class UserCreationFormCustom(UserCreationForm):
    username=forms.CharField(label="usuario")
    password1=forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2=forms.CharField(label="Repita la Contraseña", widget=forms.PasswordInput)
    mail = forms.EmailField(widget=forms.TextInput(attrs={'autofocus': True}))
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
        help_texts = {k:"" for k in fields}

class AuthenticationFormCustom(AuthenticationForm):
    username=forms.CharField(label="usuario")
    password=forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    mail = forms.EmailField(widget=forms.TextInput(attrs={'autofocus': True}))

class UserEditForm(UserChangeForm):
    password=None
    first_name=forms.CharField(label='Nombre')
    last_name=forms.CharField(label='Apellido')
    email=forms.EmailField(label='Mail')
    imagen=forms.ImageField(label='Avatar', required=False)
    class Meta:
        model = User
        fields=['first_name', 'last_name', 'email', 'imagen']
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['password'].widget = forms.PasswordInput()
        def save(self, commit=True):
            user = super().save(commit=False)
            avatar, _ = Avatar.objects.get_or_create(user=user)
            imagen = self.cleaned_data['imagen']
            if imagen:
                avatar.image = imagen
                avatar.save()
            if commit:
                user.save()
            return user
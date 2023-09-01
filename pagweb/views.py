from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import *
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView, PasswordChangeView
from django.contrib.auth.mixins import LoginRequiredMixin
from ckeditor.fields import RichTextField

@login_required
def inicio(request):
    return render(request, 'inicio.html')

def index(request):
    return render(request, 'index.html')

@login_required
def base_datos(request):
    return render(request, 'base_datos.html')

def aboutme(request):
    return render(request, 'aboutme.html')

@login_required
def curso_form(request):
    if request.method == 'POST':
        mi_formulario = CursoForm(request.POST)
        if mi_formulario.is_valid():
            mi_formulario.save()
        return render(request, 'inicio.html')
    else:
        mi_formulario = CursoForm()
        return render(request, 'curso_form.html', {'mi_formulario': mi_formulario})
    
@login_required
def buscar_curso(request):
    curso = []
    form = BusquedaCurso(request.GET)

    if form.is_valid():
        nombre = form.cleaned_data.get('nombre')

        # Realizar la búsqueda en el modelo Curso por nombre
        if nombre:
            curso = Curso.objects.filter(nombre__icontains=nombre)

    return render(request, 'buscar_curso.html', {'form': form, 'curso': curso})
    
class CursoListView(ListView):
    model = Curso
    context_object_name = "curso"
    template_name = 'lista_curso.html'

class CursoUpdateView(UpdateView):
    model = Curso
    template_name = 'editar_curso.html'
    success_url = reverse_lazy('pagweb:lista_curso')
    fields = ['nombre', 'comision']

class CursoDeleteView(DeleteView):
    model = Curso
    template_name = 'eliminar_curso.html'
    success_url = reverse_lazy('pagweb:lista_curso')

@login_required
def alumno_form(request):
    if request.method == 'POST':
        mi_formulario = AlumnoForm(request.POST)
        if mi_formulario.is_valid():
            mi_formulario.save()
        return render(request, 'inicio.html')
    else:
        mi_formulario = AlumnoForm()
        return render(request, 'alumno_form.html', {'mi_formulario': mi_formulario})

@login_required
def buscar_alumno(request):
    alumno = []
    form = BusquedaAlumno(request.GET)

    if form.is_valid():
        nombre = form.cleaned_data.get('nombre')

        if nombre:
            alumno = Alumno.objects.filter(nombre__icontains=nombre)

    return render(request, 'buscar_alumno.html', {'form': form, 'alumno': alumno})

class AlumnoListView(ListView):
    model = Alumno
    context_object_name = "alumno"
    template_name = 'lista_alumno.html'


class AlumnoUpdateView(UpdateView):
    model = Alumno
    template_name = 'editar_alumno.html'
    success_url = reverse_lazy('pagweb:lista_alumno')
    fields = ['nombre', 'apellido']

class AlumnoDeleteView(DeleteView):
    model = Alumno
    template_name = 'eliminar_alumno.html'
    success_url = reverse_lazy('pagweb:lista_alumno')

@login_required  
def profesor_form(request):
    if request.method == 'POST':
        mi_formulario = ProfesorForm(request.POST)
        if mi_formulario.is_valid():
            mi_formulario.save()
        return render(request, 'inicio.html')
    else:
        mi_formulario = ProfesorForm()
        return render(request, 'profesor_form.html', {'mi_formulario': mi_formulario})
    
    def form_valid(self,form):
        form.instance.imagen = self.request.FILES['imagen'].name if 'imagen' in self.request.FILES else None
        return super().form_valid(form)

@login_required
def buscar_profesor(request):
    profesor = []
    form = BusquedaProfesor(request.GET)

    if form.is_valid():
        nombre = form.cleaned_data.get('nombre')

        if nombre:
            profesor = Profesor.objects.filter(nombre__icontains=nombre)

    return render(request, 'buscar_profesor.html', {'form': form, 'profesor': profesor})

class ProfesorListView(ListView):
    model = Profesor
    context_object_name = "profesor"
    template_name = 'lista_profesor.html'

class ProfesorUpdateView(UpdateView):
    model = Profesor
    template_name = 'editar_profesor.html'
    success_url = reverse_lazy('pagweb:lista_profesor')
    fields = ['nombre', 'apellido']

class ProfesorDeleteView(DeleteView):
    model = Profesor
    template_name = 'eliminar_profesor.html'
    success_url = reverse_lazy('pagweb:lista_profesor')
    
def login_request(request):
    if request.method == 'POST':
        form = AuthenticationFormCustom(request, data = request.POST)
        if form.is_valid():
            usuario=form.cleaned_data.get('username')
            contrasena=form.cleaned_data.get('password')
            user = authenticate(username=usuario, password=contrasena)
            login(request,user)
            return render(request, "logincompletado.html", {"mensaje": f'Bienvenido {user.username}'})
    else:
        form = AuthenticationFormCustom()
    return render(request, 'login.html', {'form': form})

def registro(request):
    if request.method == 'POST':
        form = UserCreationFormCustom(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            form.save()
            return render(request,'registrocompletado.html', {'mensaje':'Usuario Creado'})
    else:
        form=UserCreationFormCustom()
    return render(request, 'registro.html', {'form':form})

def editar_perfil(request):
    user=request.user
    if request.method == 'POST':
        miformulario = UserEditForm(request.POST, request.FILES, instance=user)
        if miformulario.is_valid():
            miformulario.save()
            if miformulario.cleaned_data.get('imagen'):
                user.avatar.imagen = miformulario.cleaned_data.get('imagen')
                user.avatar.save()
            return render(request, 'inicio.html')
    else:
        miformulario=UserEditForm(initial={'imagen': user.avatar.imagen}, instance=user)
    return render(request, 'editar_perfil.html', {'miformulario': miformulario, 'usuario': user})

class CambiarContrasena(LoginRequiredMixin, PasswordChangeView):
    template_name = 'cambiar_contrasena.html'
    success_url = reverse_lazy('pagweb:editar_perfil')

class CustomLogoutView(LogoutView):
    next_page = 'pagweb:login'

class PostListView(ListView):
    model = Post
    context_object_name = "post"
    template_name = 'lista_post.html'

class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'editar_post.html'
    success_url = reverse_lazy('pagweb:lista_post')

class PostDeleteView(DeleteView):
    model = Post
    template_name = 'eliminar_post.html'
    success_url = reverse_lazy('pagweb:lista_post')
    
class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'crear_post.html'
    success_url = reverse_lazy('pagweb:lista_post')
# Create your views here.

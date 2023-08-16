from django.urls import path
from pagweb import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('curso_form/', views.curso_form, name='curso_form'),
    path('alumno_form/', views.alumno_form, name='alumno_form'),
    path('profesor_form/', views.profesor_form, name='profesor_form'),
    path('', views.inicio,),
    path('index/', views.index, name='index'),
    path('buscar_curso/', views.buscar_curso, name='buscar_curso'),
    path('buscar_alumno/', views.buscar_alumno, name='buscar_alumno'),
    path('buscar_profesor/', views.buscar_profesor, name='buscar_profesor'),
    path('base_datos/', views.base_datos, name='base_datos'),
    path('lista_curso', views.CursoListView.as_view(), name="lista_curso"),
    path('editar_curso/<int:pk>/', views.CursoUpdateView.as_view(), name="editar_curso"),
    path('eliminar_curso/<int:pk>/', views.CursoDeleteView.as_view(), name="eliminar_curso"),
    path('lista_alumno/', views.AlumnoListView.as_view(), name="lista_alumno"),
    path('editar_alumno/<int:pk>/', views.AlumnoUpdateView.as_view(), name="editar_alumno"),
    path('eliminar_alumno/<int:pk>/', views.AlumnoDeleteView.as_view(), name="eliminar_alumno"),
    path('lista_profesor/', views.ProfesorListView.as_view(), name="lista_profesor"),
    path('editar_profesor/<int:pk>/', views.ProfesorUpdateView.as_view(), name="editar_profesor"),
    path('eliminar_profesor/<int:pk>/', views.ProfesorDeleteView.as_view(), name="eliminar_profesor"),
    path('lista_post/', views.PostListView.as_view(), name="lista_post"),
    path('crear_post/', views.PostCreateView.as_view(), name="crear_post"),
    path('editar_post/<int:pk>/', views.PostUpdateView.as_view(), name="editar_post"),
    path('eliminar_post/<int:pk>/', views.PostDeleteView.as_view(), name="eliminar_post"),
    path('login/', views.login_request, name="login"),
    path('registro/', views.registro, name="registro"),
    path('registrocompletado/', views.registro, name="registrocompletado"),
    path('logout/', views.CustomLogoutView.as_view(), name='logout'),
]
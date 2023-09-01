from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.utils import timezone
from models import Curso, Avatar

### Test con el models Curso ###
class CursoTestCase(TestCase):
    def setUp(self):
        # Crea un usuario de prueba
        self.usuario = User.objects.create_user(username='Test1', password='12345678')
        
        # Crea una instancia de Curso para las pruebas
        self.curso = Curso.objects.create(
            usuario=self.usuario,
            curso='coderhouse',
            comision='123',
        )

    def test_str_method(self):
        # Verifica que el método __str__ del modelo Curso funcione correctamente
        expected_str = f"{self.curso.id} - {self.usuario}"
        self.assertEqual(str(self.curso), expected_str)

    def test_curso_attributes(self):
        # Verifica que los atributos de la instancia de Curso sean correctos
        self.assertEqual(self.curso.usuario, self.usuario)
        self.assertEqual(self.curso.nombre, 'coderhouse')
        self.assertEqual(self.curso.comision, '123')

### Test con el models User ###

class UserTestCase(TestCase):
    def setUp(self):
        # Crea un usuario de prueba
        self.user = get_user_model().objects.create_user(
            email='coder@coder.com',
            password='12345678',
            name='Test2'
        )

    def test_str_method(self):
        # Verifica que el método __str__ del modelo User funcione correctamente
        expected_str = f"{self.user.email} - {self.user.name}"
        self.assertEqual(str(self.user), expected_str)

    def test_user_attributes(self):
        # Verifica los atributos del usuario
        self.assertEqual(self.user.email, 'coder@coder.com')
        self.assertEqual(self.user.name, 'CoderTest')

### Test con el models Avatar ###
class AvatarTestCase(TestCase):
    def setUp(self):
        # Crea un usuario de prueba
        self.user = get_user_model().objects.create_user(
            email='coder2@coder.com',
            password='12345678',
            name='Test3'
        )

        # Crea una instancia de Avatar para las pruebas
        self.avatar = Avatar.objects.create(
            user=self.user,
            image='avatares/test_avatar.png'  # Ruta ficticia a una imagen de avatar
        )

    def test_str_method(self):
        # Verifica que el método __str__ del modelo Avatar funcione correctamente
        expected_str = f"{self.user} - {self.avatar.image}"
        self.assertEqual(str(self.avatar), expected_str)

    def test_avatar_attributes(self):
        # Verifica los atributos del avatar
        self.assertEqual(self.avatar.user, self.user)
        self.assertEqual(self.avatar.image, 'avatares/test_avatar.png')  # Verifica la ruta de la imagen
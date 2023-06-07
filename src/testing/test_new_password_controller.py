import sys
import os

# Agregar el directorio raíz de tu proyecto a la ruta de importación
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from flask import url_for
from app import app

class NewPasswordControllerTestCase(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()

    def test_new_password_controller_get(self):
        response = self.client.get('/auth/new-password')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Bienvenid@ de Nuevo', response.data)
        self.assertIn(b'form', response.data)

    def test_new_password_controller_post(self):
        response = self.client.post('/auth/new-password')
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.location, url_for('login_controller', _external=True))
import sys
import os

# Agregar el directorio raíz de tu proyecto a la ruta de importación
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from flask import url_for
from app import app

class TestRegisterController(unittest.TestCase):
    
    def setUp(self):
        self.app = app.test_client()
        self.app_context = app.app_context()
        self.app_context.push()
        
    def tearDown(self):
        self.app_context.pop()
    
    def test_register_controller(self):
        response = self.app.get('/auth/register')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Registro - Trivias UCV', response.data)
        
        response = self.app.post('/auth/register', data={
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password': 'testpassword',
            'confirm_password': 'testpassword'
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.location, url_for('login_controller', _external=True))
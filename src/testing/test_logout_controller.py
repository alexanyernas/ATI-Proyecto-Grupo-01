import sys
import os

# Agregar el directorio raíz de tu proyecto a la ruta de importación
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from unittest.mock import patch
from flask import url_for
from app import app

class LogoutTestCase(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()

    @patch('app.logout_user')
    def test_logout(self, mock_logout_user):
        response = self.client.get('/logout')
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.location, url_for('login_controller', _external=True))
        mock_logout_user.assert_called_once()
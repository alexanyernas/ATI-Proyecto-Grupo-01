import sys
import os

# Agregar el directorio raíz de tu proyecto a la ruta de importación
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from unittest.mock import patch, MagicMock
from app import app

class GetStoredUsuariosTestCase(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()

    @patch('app.ConexionMongo')
    def test_get_stored_usuarios(self, mock_conexion_mongo):
        mock_db = MagicMock()
        mock_find = MagicMock(return_value=[{
            "id_user": 1,
            "name_user": "Test",
            "alias": "testuser",
            "email": "testuser@example.com",
            "fec_creacion": "2022-01-01",
            "fec_nacimiento": "1990-01-01",
            "facebook": "https://www.facebook.com/testuser",
            "twitter": "https://www.twitter.com/testuser",
            "tipo_usuario": "normal",
            "posicion_ranking": 1,
            "imagen": "",
            "puntaje": 0,
            "ganador_sorteo": False
        }])
        type(mock_db).usuario_tb = mock_find
        mock_conexion_mongo.return_value = mock_db

        response = self.client.get('/usuarios')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"usuarios": [{
            "id_user": 1,
            "name_user": "Test",
            "alias": "testuser",
            "email": "testuser@example.com",
            "fec_creacion": "2022-01-01",
            "fec_nacimiento": "1990-01-01",
            "facebook": "https://www.facebook.com/testuser",
            "twitter": "https://www.twitter.com/testuser",
            "tipo_usuario": "normal",
            "posicion_ranking": 1,
            "imagen": "",
            "puntaje": 0,
            "ganador_sorteo": False
        }]})
        mock_conexion_mongo.assert_called_once()
        mock_db.usuario_tb.find.assert_called_once()
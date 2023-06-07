import sys
import os

# Agregar el directorio raíz de tu proyecto a la ruta de importación
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask_login import UserMixin
from flask import jsonify
from config.mongodb import ConexionMongo

class User():

    db = ConexionMongo()
    mdb = db.connect_mongo()

    def get_stored_usuarios(self):
        _usuarios = self.mdb.usuario_tb.find()
        usuarios = [{"id_user": usuario["id_user"], 
                    "name_user": usuario["name_user"], 
                    "alias": usuario["alias"], 
                    "email": usuario["email"], 
                    "fec_creacion": usuario["fec_creacion"], 
                    "fec_nacimiento": usuario["fec_nacimiento"], 
                    "facebook": usuario["facebook"], 
                    "twitter": usuario["twitter"], 
                    "tipo_usuario": usuario["tipo_usuario"], 
                    "posicion_ranking": usuario["posicion_ranking"], 
                    "imagen": usuario["imagen"], 
                    "puntaje": usuario["puntaje"], 
                    "ganador_sorteo": usuario["ganador_sorteo"]} for usuario in _usuarios]
        return jsonify({"usuarios": usuarios})

    def delete_usuario(self, id):
        try:
            self.mdb.usuario_tb.deleteOne( { "id_user": {id} } )
        except:
            print("Error 002 function delete_usuario")

    def add_user(self, nombre, alias, email, nacimiento, facebook, twitter):
        try:
            _usuarios = self.mdb.usuario_tb.insertOne(
                {
                    "id_user":1,
                    "name_user": {nombre},
                    "alias": {alias},
                    "email": {email},
                    "fec_creacion": "$$NOW",
                    "fec_nacimiento": {nacimiento},
                    "facebook": {facebook},
                    "twitter": {twitter},
                    "tipo_usuario": "Usuario",
                    "posicion_ranking": 0,
                    "imagen": {},
                    "puntaje": [],
                    "ganador_sorteo": []
                })
        except:
            print("Error 001 function add_contacto")
            
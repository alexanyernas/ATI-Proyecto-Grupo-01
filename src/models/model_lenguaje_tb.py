from flask_login import UserMixin, jsonify
from config.mongodb import ConexionMongo

class lenguaje():

    db = ConexionMongo()
    mdb = db.connect_mongo()

    def get_stored_lenguajes(self):
        _lenguajes = self.mdb.lenguaje_tb.find()
        lenguajes = [{"id_lenguaje": lenguaje["id_lenguaje"], 
                    "descripcion": lenguaje["descripcion"], 
                    "texto": lenguaje["texto"]} for lenguaje in _lenguajes]
        return jsonify({"lenguajes": lenguajes})

    def delete_lenguaje(self, id):
        try:
            self.mdb.lenguaje_tb.deleteOne( { "id_lenguaje": {id} } )
        except:
            print("Error 002 function delete_lenguaje")

    def add_lenguaje(self, id_lenguaje, descripcion, texto):
        try:
            _lenguajes = self.mdb.lenguaje_tb.insertOne(
                {
                    "id_lenguaje": {id_lenguaje},
                    "descripcion": {descripcion},
                    "texto": {texto}
                })
        except:
            print("Error 001 function add_contacto")
            
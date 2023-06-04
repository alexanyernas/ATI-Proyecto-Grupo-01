from flask_login import UserMixin, jsonify
from config.mongodb import ConexionMongo

class seccion():

    db = ConexionMongo()
    mdb = db.connect_mongo()

    def get_stored_secciones(self):
        _secciones = self.mdb.seccion_tb.find()
        secciones = [{"id_seccion": seccion["id_seccion"], 
                    "descripcion": seccion["descripcion"], 
                    "texto": seccion["texto"]} for seccion in _secciones]
        return jsonify({"secciones": secciones})

    def delete_seccion(self, id):
        try:
            self.mdb.seccion_tb.deleteOne( { "id_seccion": {id} } )
        except:
            print("Error 002 function delete_seccion")

    def add_seccion(self, id_seccion, descripcion, lenguaje):
        try:
            _secciones = self.mdb.seccion_tb.insertOne(
                {
                    "id_seccion": {id_seccion},
                    "descripcion": {descripcion},
                    "lenguaje": {lenguaje}
                })
        except:
            print("Error 001 function add_contacto")
            
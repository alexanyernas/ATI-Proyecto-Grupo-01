from flask_login import UserMixin, jsonify
from config.mongodb import ConexionMongo

class categoria():

    db = ConexionMongo()
    mdb = db.connect_mongo()

    def get_stored_categorias(self):
        _categorias = self.mdb.categoria_tb.find()
        categorias = [{"id_categoria": categoria["id_categoria"], 
                    "descripcion": categoria["descripcion"], 
                    "trivias": categoria["trivias"]} for categoria in _categorias]
        return jsonify({"categorias": categorias})

    def delete_categoria(self, id):
        try:
            self.mdb.categoria_tb.deleteOne( { "id_categoria": {id} } )
        except:
            print("Error 002 function delete_categoria")

    def add_categoria(self, id_categoria, descripcion, trivias):
        try:
            _categorias = self.mdb.categoria_tb.insertOne(
                {
                    "id_categoria": {id_categoria},
                    "descripcion": {descripcion},
                    "trivias": {trivias}
                })
        except:
            print("Error 001 function add_contacto")
            
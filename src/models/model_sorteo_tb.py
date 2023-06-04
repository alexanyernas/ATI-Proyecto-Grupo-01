from flask_login import UserMixin, jsonify
from config.mongodb import ConexionMongo

class sorteo():

    db = ConexionMongo()
    mdb = db.connect_mongo()

    def get_stored_sorteos(self):
        _sorteos = self.mdb.sorteo_tb.find()
        sorteos = [{"id_sorteo": sorteo["id_sorteo"], 
                    "fec_sorteo": sorteo["fec_sorteo"], 
                    "tipo_sorteo": sorteo["tipo_sorteo"], 
                    "ganadores": sorteo["ganadores"]} for sorteo in _sorteos]
        return jsonify({"sorteos": sorteos})

    def delete_sorteo(self, id):
        try:
            self.mdb.sorteo_tb.deleteOne( { "id_sorteo": {id} } )
        except:
            print("Error 002 function delete_sorteo")

    def add_sorteo(self, id_sorteo, fec_sorteo, tipo_sorteo, ganadores):
        try:
            _sorteos = self.mdb.sorteo_tb.insertOne(
                {
                    "id_sorteo": {id_sorteo},
                    "fec_sorteo": {fec_sorteo},
                    "tipo_sorteo": {tipo_sorteo},
                    "ganadores": {ganadores}
                })
        except:
            print("Error 001 function add_contacto")
            
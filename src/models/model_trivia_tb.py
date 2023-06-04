from flask_login import UserMixin, jsonify
from config.mongodb import ConexionMongo

class trivia():

    db = ConexionMongo()
    mdb = db.connect_mongo()

    def get_stored_trivia(self):
        _trivia = self.mdb.trivia_tb.find()
        trivia = [{"id_trivia": trivia["id_trivia"], 
                    "pregunta": trivia["pregunta"], 
                    "respuestas": trivia["respuestas"], 
                    "imagen": trivia["imagen"]} for trivia in _trivia]
        return jsonify({"trivia": trivia})

    def delete_trivia(self, id):
        try:
            self.mdb.trivia_tb.deleteOne( { "id_trivia": {id} } )
        except:
            print("Error 002 function delete_trivia")

    def add_trivia(self, id_trivia, pregunta, respuestas, imagen):
        try:
            _trivia = self.mdb.trivia_tb.insertOne(
                {
                    "id_trivia": {id_trivia},
                    "pregunta": {pregunta},
                    "respuestas": {respuestas},
                    "imagen": {imagen}
                })
        except:
            print("Error 001 function add_contacto")
            
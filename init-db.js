db = db.getSiblingDB("bd_trivia");

db.usuario_tb.drop();
db.usuario_tb.insertMany([
    {
        "id_user":1,
        "name_user": "Betty Torres",
        "alias": "Betty Torres",
        "email": "bettytores@gmail.com",
        "fec_creacion": "2023-05-11 08:00:00",
        "fec_nacimiento": "17/11/1979",
        "facebook": "",
        "twitter": "",
        "tipo_usuario": "Usuario",
        "posicion_ranking": 0,
        "imagen": {
                    "nombre_archivo": "13852255.png",
                    "formato": "png",
                    "tipo_imagen": "avatar"
                },
        "puntaje": [],
        "ganador_sorteo": []
    },{
        "id_user":2,
        "name_user": "María Paula Herrero",
        "alias": "María Paula Herrero",
        "email": "mpaulaherrero@gmail.com",
        "fec_creacion": "2023-05-11 08:00:00",
        "fec_nacimiento": "18/08/1972",
        "facebook": "",
        "twitter": "",
        "tipo_usuario": "Usuario",
        "posicion_ranking": 0,
        "imagen": {
                    "nombre_archivo": "14444733.jpg",
                    "formato": "jpg",
                    "tipo_imagen": "avatar"
                },
        "puntaje": [],
        "ganador_sorteo": []
    },{
        "id_user":3,
        "name_user": "Fernando Mazzaro",
        "alias": "Fernando Mazzaro",
        "email": "fernando.mazzaro.m@gmail.com",
        "fec_creacion": "2023-05-11 08:00:00",
        "fec_nacimiento": "15/12/1988",
        "facebook": "",
        "twitter": "",
        "tipo_usuario": "Usuario",
        "posicion_ranking": 0,
        "imagen": {
                    "nombre_archivo": "18446241.jpg",
                    "formato": "jpg",
                    "tipo_imagen": "avatar"
                },
        "puntaje": [],
        "ganador_sorteo": []
    },{
        "id_user":4,
        "name_user": "Luz Rico",
        "alias": "Luz Rico",
        "email": "luzrico15@gmail.com",
        "fec_creacion": "2023-05-11 08:00:00",
        "fec_nacimiento": "10/07/1992",
        "facebook": "",
        "twitter": "",
        "tipo_usuario": "Usuario",
        "posicion_ranking": 0,
        "imagen": {
                    "nombre_archivo": "21071997.png",
                    "formato": "png",
                    "tipo_imagen": "avatar"
                },
        "puntaje": [],
        "ganador_sorteo": []
    },{
        "id_user":5,
        "name_user": "Jorge David Contreras Flores",
        "alias": "Jorge David Contreras Flores",
        "email": "Jorgedcontreras.94@gmail.com",
        "fec_creacion": "2023-05-11 08:00:00",
        "fec_nacimiento": "21/01/1994",
        "facebook": "",
        "twitter": "",
        "tipo_usuario": "Usuario",
        "posicion_ranking": 0,
        "imagen": {
                    "nombre_archivo": "23685724.jpeg",
                    "formato": "jpeg",
                    "tipo_imagen": "avatar"
                },
        "puntaje": [],
        "ganador_sorteo": []
    },{
        "id_user":6,
        "name_user": "Ioannis Morakis",
        "alias": "Ioannis Morakis",
        "email": "m.yannis22@gmail.com",
        "fec_creacion": "2023-05-11 08:00:00",
        "fec_nacimiento": "22/09/1995",
        "facebook": "",
        "twitter": "",
        "tipo_usuario": "Usuario",
        "posicion_ranking": 0,
        "imagen": {
                    "nombre_archivo": "24105182.png",
                    "formato": "png",
                    "tipo_imagen": "avatar"
                },
        "puntaje": [],
        "ganador_sorteo": []
    },{
        "id_user":7,
        "name_user": "Victor Daniel Tafuri Vidal",
        "alias": "Victor Daniel Tafuri Vidal",
        "email": "victortafuri2@gmail.com",
        "fec_creacion": "2023-05-11 08:00:00",
        "fec_nacimiento": "09/10/1996",
        "facebook": "",
        "twitter": "",
        "tipo_usuario": "Usuario",
        "posicion_ranking": 0,
        "imagen": {
                    "nombre_archivo": "25504486.jpg",
                    "formato": "jpg",
                    "tipo_imagen": "avatar"
                },
        "puntaje": [],
        "ganador_sorteo": []
    },{
        "id_user":8,
        "name_user": "Maria Fernanda Tejeda Caballero",
        "alias": "Maria Fernanda Tejeda Caballero",
        "email": "mariaf0821@gmail.com",
        "fec_creacion": "2023-05-11 08:00:00",
        "fec_nacimiento": "21/08/1995",
        "facebook": "",
        "twitter": "",
        "tipo_usuario": "Usuario",
        "posicion_ranking": 0,
        "imagen": {
                    "nombre_archivo": "25641163.jpg",
                    "formato": "jpg",
                    "tipo_imagen": "avatar"
                },
        "puntaje": [],
        "ganador_sorteo": []
    },{
        "id_user":9,
        "name_user": "Valentina Contreras",
        "alias": "Valentina Contreras",
        "email": "valexcontreras@gmail.com",
        "fec_creacion": "2023-05-11 08:00:00",
        "fec_nacimiento": "27/06/1998",
        "facebook": "",
        "twitter": "",
        "tipo_usuario": "Usuario",
        "posicion_ranking": 0,
        "imagen": {
                    "nombre_archivo": "26022819.jpg",
                    "formato": "jpg",
                    "tipo_imagen": "avatar"
                },
        "puntaje": [],
        "ganador_sorteo": []
    },{
        "id_user":10,
        "name_user": "Alejandro Graterol",
        "alias": "Alejandro Graterol",
        "email": "alejandro.graterol98@gmail.com",
        "fec_creacion": "2023-05-11 08:00:00",
        "fec_nacimiento": "16/10/1998",
        "facebook": "",
        "twitter": "",
        "tipo_usuario": "Usuario",
        "posicion_ranking": 0,
        "imagen": {
                    "nombre_archivo": "26473471.jpg",
                    "formato": "jpg",
                    "tipo_imagen": "avatar"
                },
        "puntaje": [],
        "ganador_sorteo": []
    },{
        "id_user":11,
        "name_user": "Alexanyer Naranjo",
        "alias": "Alexanyer Naranjo",
        "email": "alexanyernaranjo@gmail.com",
        "fec_creacion": "2023-05-11 08:00:00",
        "fec_nacimiento": "30/10/1998",
        "facebook": "",
        "twitter": "",
        "tipo_usuario": "Usuario",
        "posicion_ranking": 0,
        "imagen": {
                    "nombre_archivo": "26498600.jpg",
                    "formato": "jpg",
                    "tipo_imagen": "avatar"
                },
        "puntaje": [],
        "ganador_sorteo": []
    },{
        "id_user":12,
        "name_user": "David Sanchez",
        "alias": "David Sanchez",
        "email": "luigisperstar7@gmail.com",
        "fec_creacion": "2023-05-11 08:00:00",
        "fec_nacimiento": "18/03/1999",
        "facebook": "",
        "twitter": "",
        "tipo_usuario": "Usuario",
        "posicion_ranking": 0,
        "imagen": {
                    "nombre_archivo": "26573559.jpg",
                    "formato": "jpg",
                    "tipo_imagen": "avatar"
                },
        "puntaje": [],
        "ganador_sorteo": []
    },{
        "id_user":13,
        "name_user": "Carlos Guillen",
        "alias": "Carlos Guillen",
        "email": "cawinosjose4@gmail.com",
        "fec_creacion": "2023-05-11 08:00:00",
        "fec_nacimiento": "28/01/1999",
        "facebook": "",
        "twitter": "",
        "tipo_usuario": "Usuario",
        "posicion_ranking": 0,
        "imagen": {
                    "nombre_archivo": "26619394.jpg",
                    "formato": "jpg",
                    "tipo_imagen": "avatar"
                },
        "puntaje": [],
        "ganador_sorteo": []
    },{
        "id_user":14,
        "name_user": "Alejandra Giannattasio",
        "alias": "Alejandra Giannattasio",
        "email": "alegiannattasioxd@gmail.com",
        "fec_creacion": "2023-05-11 08:00:00",
        "fec_nacimiento": "25/07/1998",
        "facebook": "",
        "twitter": "",
        "tipo_usuario": "Usuario",
        "posicion_ranking": 0,
        "imagen": {
                    "nombre_archivo": "26825960.jpg",
                    "formato": "jpg",
                    "tipo_imagen": "avatar"
                },
        "puntaje": [],
        "ganador_sorteo": []
    },{
        "id_user":15,
        "name_user": "Valeria Acuña",
        "alias": "Valeria Acuña",
        "email": "valeriaa.2608@gmail.com",
        "fec_creacion": "2023-05-11 08:00:00",
        "fec_nacimiento": "26/08/1997",
        "facebook": "",
        "twitter": "",
        "tipo_usuario": "Usuario",
        "posicion_ranking": 0,
        "imagen": {
                    "nombre_archivo": "26915574.jpg",
                    "formato": "jpg",
                    "tipo_imagen": "avatar"
                },
        "puntaje": [],
        "ganador_sorteo": []
    },{
        "id_user":16,
        "name_user": "Gabriel Carrizo",
        "alias": "Gabriel Carrizo",
        "email": "gabo.c.liendo@gmail.com",
        "fec_creacion": "2023-05-11 08:00:00",
        "fec_nacimiento": "25/02/2000",
        "facebook": "",
        "twitter": "",
        "tipo_usuario": "Usuario",
        "posicion_ranking": 0,
        "imagen": {
                    "nombre_archivo": "27031954.jpg",
                    "formato": "jpg",
                    "tipo_imagen": "avatar"
                },
        "puntaje": [],
        "ganador_sorteo": []
    },{
        "id_user":17,
        "name_user": "Carlos Daniel Castillo Orozco",
        "alias": "Carlos Daniel Castillo Orozco",
        "email": "cardacaso@gmail.com",
        "fec_creacion": "2023-05-11 08:00:00",
        "fec_nacimiento": "27/10/1998",
        "facebook": "",
        "twitter": "",
        "tipo_usuario": "Usuario",
        "posicion_ranking": 0,
        "imagen": {
                    "nombre_archivo": "27223295.jpg",
                    "formato": "jpg",
                    "tipo_imagen": "avatar"
                },
        "puntaje": [],
        "ganador_sorteo": []
    },{
        "id_user":18,
        "name_user": "Gabriel Belisario",
        "alias": "Gabriel Belisario",
        "email": "gabrielbelisariof@gmail.com",
        "fec_creacion": "2023-05-11 08:00:00",
        "fec_nacimiento": "16/06/2000",
        "facebook": "",
        "twitter": "",
        "tipo_usuario": "Usuario",
        "posicion_ranking": 0,
        "imagen": {
                    "nombre_archivo": "27246729.jpg",
                    "formato": "jpg",
                    "tipo_imagen": "avatar"
                },
        "puntaje": [],
        "ganador_sorteo": []
    },{
        "id_user":19,
        "name_user": "Leonardo Mendoza",
        "alias": "Leonardo Mendoza",
        "email": "leonardo.rafael.mendoza@gmail.com",
        "fec_creacion": "2023-05-11 08:00:00",
        "fec_nacimiento": "21/01/2000",
        "facebook": "",
        "twitter": "",
        "tipo_usuario": "Usuario",
        "posicion_ranking": 0,
        "imagen": {
                    "nombre_archivo": "27254317.jpg",
                    "formato": "jpg",
                    "tipo_imagen": "avatar"
                },
        "puntaje": [],
        "ganador_sorteo": []
    },{
        "id_user":20,
        "name_user": "Ariana Medina",
        "alias": "Ariana Medina",
        "email": "medina2.ariana9@gmail.com",
        "fec_creacion": "2023-05-11 08:00:00",
        "fec_nacimiento": "02/02/1999",
        "facebook": "",
        "twitter": "",
        "tipo_usuario": "Usuario",
        "posicion_ranking": 0,
        "imagen": {
                    "nombre_archivo": "27371936.jpeg",
                    "formato": "jpeg",
                    "tipo_imagen": "avatar"
                },
        "puntaje": [],
        "ganador_sorteo": []
    },{
        "id_user":21,
        "name_user": "Luis Fernando Peña",
        "alias": "Luis Fernando Peña",
        "email": "lfernandopg26@gmail.com",
        "fec_creacion": "2023-05-11 08:00:00",
        "fec_nacimiento": "26/04/2000",
        "facebook": "",
        "twitter": "",
        "tipo_usuario": "Usuario",
        "posicion_ranking": 0,
        "imagen": {
                    "nombre_archivo": "27377309.jpg",
                    "formato": "jpg",
                    "tipo_imagen": "avatar"
                },
        "puntaje": [],
        "ganador_sorteo": []
    },{
        "id_user":22,
        "name_user": "Hadaya Hadaya",
        "alias": "Hadaya Hadaya",
        "email": "hadaya456@gmail.com",
        "fec_creacion": "2023-05-11 08:00:00",
        "fec_nacimiento": "12/09/2000",
        "facebook": "",
        "twitter": "",
        "tipo_usuario": "Usuario",
        "posicion_ranking": 0,
        "imagen": {
                    "nombre_archivo": "27606502.jpg",
                    "formato": "jpg",
                    "tipo_imagen": "avatar"
                },
        "puntaje": [],
        "ganador_sorteo": []
    },{
        "id_user":23,
        "name_user": "Daniela Ruggiero",
        "alias": "Daniela Ruggiero",
        "email": "Chachy.drs@gmail.com",
        "fec_creacion": "2023-05-11 08:00:00",
        "fec_nacimiento": "10/02/2001",
        "facebook": "",
        "twitter": "",
        "tipo_usuario": "Usuario",
        "posicion_ranking": 0,
        "imagen": {
                    "nombre_archivo": "28126743.jpg",
                    "formato": "jpg",
                    "tipo_imagen": "avatar"
                },
        "puntaje": [],
        "ganador_sorteo": []
    },{
        "id_user":24,
        "name_user": "Jose Miguel Valera",
        "alias": "Jose Miguel Valera",
        "email": "jhoabran@gmail.com",
        "fec_creacion": "2023-05-11 08:00:00",
        "fec_nacimiento": "08/05/2001",
        "facebook": "",
        "twitter": "",
        "tipo_usuario": "Usuario",
        "posicion_ranking": 0,
        "imagen": {
                    "nombre_archivo": "28218108.jpeg",
                    "formato": "jpeg",
                    "tipo_imagen": "avatar"
                },
        "puntaje": [],
        "ganador_sorteo": []
    },
]);

db.seccion_tb.drop();
db.seccion_tb.insertMany([
    {
        "id_seccion": 1,
        "descripcion": "ranking",
        "lenguaje": "es"
    }
]);

db.lenguaje_tb.drop();
db.lenguaje_tb.insertMany([
    {
        "id_lenguaje": "es",
        "descripcion": "Español",
        "texto":[{
                    "descripcion": "",
                    "texto": "",
              }]
    }
]);

db.categoria_tb.drop();
db.categoria_tb.insertMany([
    {
        "id_categoria": 1,
        "descripcion": "Autos",
        "trivias": [1]
    }
]);

db.trivia_tb.drop();
db.trivia_tb.insertMany([
    {
        "id_trivia": 1,
        "pregunta": "Cantidad de puertas de un mustang",
        "respuestas": [{
                        "id_respuesta": 1,
                        "respuesta": "2",
                        "correta": true
                    }],
        "imagen": {
                    "nombre_archivo": "mustang.jpg",
                    "formato": "jpg",
                    "tipo_imagen": "trivia"
                }
    }
]);

db.sorteo_tb.drop();
db.sorteo_tb.insertMany([
    {
        "id_sorteo": 1,
        "fec_sorteo": "2023-05-11 12:00:00",
        "tipo_sorteo": "ranking",
        "ganadores": [{
                        "id_usuario": 1,
                        "premio": "Reloj",
                        "tipo": "Físico"
                   }]
}]);
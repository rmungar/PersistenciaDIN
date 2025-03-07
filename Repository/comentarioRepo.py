import sqlite3

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from Model.Comentario import Comentario


class ComentarioRepo():


    def getComentarios() -> list[Comentario]:
        conn = sqlite3.connect('default.db')
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM COMENTARIO")
        comentariosBD = cursor.fetchall()
        comentarios = []
        for comentarioBD in comentariosBD:
            comentario = Comentario[comentarioBD[0], comentarioBD[1], comentarioBD[2], comentarioBD[3]]
            comentarios.append(comentario)

        return comentarios
    
    def addComentario(self, comentario: Comentario):
        conn = sqlite3.connect('default.db')
        cursor = conn.cursor()

        cursor.execute("INSERT INTO COMENTARIO VALUES (?, ?, ?, ?)", comentario._id, comentario.usuario, comentario.texto, comentario.fecha)
import sqlite3

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import Model.Usuario




class UsuarioRepo():

    def getUsuarios() -> list:
        conn = sqlite3.connect('default.db')
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM USUARIO")
        usuarios = cursor.fetchall()

        return usuarios
    
    def addUsuario(usuario):
        conn = sqlite3.connect('default.db')
        cursor = conn.cursor()

        cursor.execute("INSERT INTO USUARIO VALUES (?, ?, ?, ?)", (usuario.id, usuario.nombre, usuario.email, usuario.password))
        conn.commit()

    def getUsuario(email) -> Model.Usuario.Usuario:
        conn = sqlite3.connect('default.db')
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM USUARIO WHERE email = ?", (email,))
        usuarioBD = cursor.fetchone()

        return Model.Usuario.Usuario(usuarioBD[0], usuarioBD[1], usuarioBD[2], usuarioBD[3], usuarioBD[4], usuarioBD[5], usuarioBD[6], usuarioBD[7])



def Main():
    usuario = UsuarioRepo.getUsuario("raul@gmail.com")
    print(usuario)


if __name__ == '__main__':
    Main()
import sqlite3

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Model.Usuario import Usuario 


class UsuarioRepo():
    """
    Clase que representa un repositorio para manejar operaciones relacionadas con usuarios en la base de datos.
    Proporciona métodos para obtener usuarios, agregar nuevos usuarios y buscar usuarios por correo electrónico.
    """

    def getUsuarios() -> list[Usuario]:
        """
        Obtiene todos los usuarios almacenados en la base de datos.

        Returns:
            list[Usuario]: Una lista de objetos de tipo Usuario.
        """
        conn = sqlite3.connect('_internal/default.db')
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM USUARIO")
        usuariosDB = cursor.fetchall()
        usuarios = []

        for usuarioDB in usuariosDB:
            usuario = Usuario(usuarioDB[0],usuarioDB[1],usuarioDB[2],usuarioDB[3],usuarioDB[4])
            usuarios.append(usuario)

        return usuarios
    
    def addUsuario(usuario):
        """
        Agrega un nuevo usuario a la base de datos.

        Args:
            usuario (Usuario): Objeto de tipo Usuario que se desea agregar.
        """
        conn = sqlite3.connect('_internal/default.db')
        cursor = conn.cursor()

        cursor.execute("INSERT INTO USUARIO VALUES (?, ?, ?)", (usuario.nombre, usuario.email, usuario.password))
        conn.commit()

    def getUsuario(email) -> Usuario:
        """
        Obtiene un usuario específico por su correo electrónico.

        Args:
            email (str): Correo electrónico del usuario que se desea buscar.

        Returns:
            Usuario: Objeto de tipo Usuario correspondiente al correo electrónico proporcionado.
        """
        conn = sqlite3.connect('_internal/default.db')
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM USUARIO WHERE email = ?", (email,))
        usuarioBD = cursor.fetchone()

        return Usuario(usuarioBD[0], usuarioBD[1], usuarioBD[2], usuarioBD[3], usuarioBD[4], usuarioBD[5], usuarioBD[6], usuarioBD[7])

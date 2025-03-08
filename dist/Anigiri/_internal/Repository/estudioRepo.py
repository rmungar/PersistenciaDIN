import sqlite3
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import Model.Estudio

class EstudioRepo():
    """
    Clase que representa un repositorio para manejar operaciones relacionadas con estudios de animación en la base de datos.
    Proporciona métodos para obtener todos los estudios almacenados en la base de datos.
    """

    def getEstudios(self) -> list[Model.Estudio.Estudio]:
        """
        Obtiene todos los estudios de animación almacenados en la base de datos.

        Returns:
            list[Model.Estudio.Estudio]: Una lista de objetos de tipo Estudio.
        """
        conn = sqlite3.connect('_internal/default.db')
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM ESTUDIO")
        estudiosBD = cursor.fetchall()
        estudios = []

        for estudioBD in estudiosBD:
            estudio = Model.Estudio.Estudio(estudioBD[0], estudioBD[1], estudioBD[2], estudioBD[3])
            estudios.append(estudio)

        return estudios
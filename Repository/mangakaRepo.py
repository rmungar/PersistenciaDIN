import sqlite3
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import Model.Mangaka

class MangakaRepo():
    """
    Clase que representa un repositorio para manejar operaciones relacionadas con mangakas en la base de datos.
    Proporciona métodos para obtener todos los mangakas almacenados en la base de datos.
    """
    def getMangakas(self) -> list[Model.Mangaka.Mangaka]:
        """
        Obtiene todos los mangakas almacenados en la base de datos.

        Returns:
            list[Model.Mangaka.Mangaka]: Una lista de objetos de tipo Mangaka.
        """
        conn = sqlite3.connect('default.db')
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM MANGAKA")
        mangakasBD = cursor.fetchall()
        mangakas = []
        for mangakaBD in mangakasBD:
            mangaka = Model.Mangaka.Mangaka(mangakaBD[0], mangakaBD[1], mangakaBD[2], mangakaBD[3], mangakaBD[4], mangakaBD[5])
            mangakas.append(mangaka)

        return mangakas
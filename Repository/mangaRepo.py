import sqlite3
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import Model.Manga

class MangaRepo():
    def getMangas(self) -> list:
        conn = sqlite3.connect('default.db')
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM MANGA")
        mangas = cursor.fetchall()

        return mangas
import sqlite3
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import Model.Anime



class AnimeRepo():
    
    def getAnime(self) -> list:
        conn = sqlite3.connect('default.db')
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM ANIME")
        animes = cursor.fetchall()

        return animes
    
    




import sqlite3
import json

conn = sqlite3.connect('default.db')

cursor = conn.cursor()

# Crear tablas

#cursor.execute("""CREATE TABLE IF NOT EXISTS MANGA (
#    _id VARCHAR(255) PRIMARY KEY,
#    nombre VARCHAR(255) NOT NULL,
#    sinopsis VARCHAR(255) NOT NULL,
#    genero VARCHAR(255) NOT NULL,
#    autor VARCHAR(255) NOT NULL,
#    imagen VARCHAR(255) NOT NULL,
#    tomos INTEGER NOT NULL,
#    capitulos INTEGER NOT NULL,
#    comentarios TEXT
#)""")

# 1 Forma de insertar datos
datosMangas = [
    ('1_One Piece', 'One Piece', 'One Piece es un manga japonés escrito e ilustrado por Eiichirō Oda. Comenzó a publicarse en la revista Weekly Shōnen Jump el 22 de julio de 1997.', 'Aventura, Acción, Comedia, Drama, Fantasía', 'Eiichirō Oda', 'https://www.anime-planet.com/images/manga/covers/one-piece-2-1.jpg', 98, 1000, json.dumps([])),
    ('2_Naruto', 'Naruto', 'Naruto es un manga japonés escrito e ilustrado por Masashi Kishimoto. Comenzó a publicarse en la revista Weekly Shōnen Jump el 21 de septiembre de 1999.', 'Aventura, Acción, Comedia, Drama, Fantasía', 'Masashi Kishimoto', 'https://www.anime-planet.com/images/manga/covers/naruto-2-1.jpg', 72, 700, json.dumps([])),
    ('3_Dragon Ball', 'Dragon Ball', 'Dragon Ball es un manga japonés escrito e ilustrado por Akira Toriyama. Comenzó a publicarse en la revista Weekly Shōnen Jump el 3 de diciembre de 1984.', 'Aventura, Acción, Comedia, Drama, Fantasía', 'Akira Toriyama', 'https://www.anime-planet.com/images/manga/covers/dragon-ball-2-1.jpg', 42, 520, json.dumps([])),
    ('4_Bleach', 'Bleach', 'Bleach es un manga japonés escrito e ilustrado por Tite Kubo. Comenzó a publicarse en la revista Weekly Shōnen Jump el 7 de agosto de 2001.', 'Aventura, Acción, Comedia, Drama, Fantasía', 'Tite Kubo', 'https://www.anime-planet.com/images/manga/covers/bleach-2-1.jpg', 74, 686, json.dumps([])),
]

#cursor.executemany("INSERT INTO MANGA (_id, nombre, sinopsis, genero, autor, imagen, tomos, capitulos, comentarios) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", datosMangas)

cursor.execute("SELECT * FROM MANGA")

mangas = cursor.fetchall()



a = json.dumps(mangas)

print(a)

conn.commit()
conn.close()


















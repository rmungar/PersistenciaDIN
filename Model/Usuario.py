## cursor.execute(
##     """CREATE TABLE IF NOT EXISTS USUARIO (
##     nombre VARCHAR(255) NOT NULL PRIMARY KEY,
##     passwd VARCHAR(255) NOT NULL,
##     email VARCHAR(255) NOT NULL,
##     vistos JSON,
##     empezados JSON,
##     guardados JSON,
##     comentarios JSON,
##     favoritos JSON)"""
## )

from Model import Anime, Comentario, Manga


class Usuario():
    def __init__(self, nombre: str, passwd: str, email: str, comentarios: list, favoritos: list):
        self.nombre = email.split("@")[0]
        self.passwd = passwd
        self.email = email
        self.comentarios = comentarios
        self.favoritos = favoritos

    def updateVistos(self, visto):
        if visto is Manga.Manga():
            self.vistos.append(visto)
        elif visto is Anime.Anime():
            self.vistos.append(visto)
        else:
            print("No se pudo agregar a vistos")


    def updateEmpezados(self, empezado):
        if empezado is Manga.Manga():
            self.empezados.append(empezado)
        elif empezado is Anime.Anime():
            self.empezados.append(empezado)
        else:
            print("No se pudo agregar a empezados")


    def updateGuardados(self, guardado):
        if guardado is Manga.Manga():
            self.guardados.append(guardado)
        elif guardado is Anime.Anime():
            self.guardados.append(guardado)
        else:
            print("No se pudo agregar a guardados")
    

    def updateComentarios(self, comentario):
        if comentario is Comentario:
            self.comentarios.append(comentario)


    def updateFavoritos(self, favorito):
        if favorito is Manga.Manga():
            self.favoritos.append(favorito)
        elif favorito is Anime.Anime():
            self.favoritos.append(favorito)
    

    def __str__(self):
        return f"Usuario: {self.nombre}, {self.email}"
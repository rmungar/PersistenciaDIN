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




class Usuario():
    def __init__(self, nombre: str, passwd: str, email: str, comentarios: list, favoritos: list):
        self.nombre = email.split("@")[0]
        self.passwd = passwd
        self.email = email
        self.comentarios = comentarios
        self.favoritos = favoritos



    def updateComentarios(self, comentario):
        from Model.Comentario import Comentario
        if comentario is Comentario:
            self.comentarios.append(comentario)


    def updateFavoritos(self, favorito):
        from Model.Manga import Manga
        from Model.Anime import Anime
        if favorito is Manga.Manga():
            self.favoritos.append(favorito)
        elif favorito is Anime.Anime():
            self.favoritos.append(favorito)
    

    def __str__(self):
        return f"Usuario: {self.nombre}, {self.email}"
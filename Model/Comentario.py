## cursor.execute(
##     """CREATE TABLE IF NOT EXISTS COMENTARIO (
##     _id VARCHAR(255) PRIMARY KEY, 
##     usuario VARCHAR(255) NOT NULL,
##     anime VARCHAR(255),
##     manga VARCHAR(255),
##     texto TEXT NOT NULL,
##     fecha DATE NOT NULL)"""
## )

class Comentario():
    def __init__(self, _id, usuario, anime, manga, texto, fecha):
        self._id = _id
        self.usuario = usuario
        self.anime = anime
        self.manga = manga
        self.texto = texto
        self.fecha = fecha

    def getAnime(self):
        return self.anime

    def getFecha(self):
        return self.fecha

    def getManga(self):
        return self.manga

    def getTexto(self):
        return self.texto

    def getUsuario(self):
        return self.usuario

    def get_id(self):
        return self._id

    def setAnime(self, anime):
        self.anime = anime

    def setFecha(self, fecha):
        self.fecha = fecha

    def setManga(self, manga):
        self.manga = manga

    def setTexto(self, texto):
        self.texto = texto

    def setUsuario(self, usuario):
        self.usuario = usuario
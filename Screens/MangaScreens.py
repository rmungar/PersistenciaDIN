from datetime import date
import os
from Config.paths import basedir
from PyQt6.QtWidgets import QMainWindow, QListWidgetItem, QMessageBox
from PyQt6.QtGui import QFont, QPixmap, QBrush, QColor
from PyQt6.QtCore import Qt
from PyQt6 import uic


from Model.Comentario import Comentario

class MangaScreen(QMainWindow):

    from Model.Manga import Manga
    from Model.Usuario import Usuario
    from Repository.comentarioRepo import ComentarioRepo
    from Repository.mangaRepo import MangaRepo
    from Utils.Utils import FormularioEmergente


    def __init__(self, stacked_widget, manga: Manga, currentUser: Usuario):
        super(MangaScreen, self).__init__()
        self.currentUser = currentUser
        uic.loadUi(os.path.join(basedir, 'Ui/contentPage.ui'), self)
        self.setWindowTitle("Anigiri")
        self.stacked_widget = stacked_widget
        
        self.homeButton.clicked.connect(lambda: self.toHomeScreen())
        self.userButton.clicked.connect(lambda: self.toUserScreen())
        self.animeButton.clicked.connect(lambda: self.toAllAnimePage())
        self.mangaButton.clicked.connect(lambda: self.toAllMangaPage())
        self.mangakaButton.clicked.connect(lambda: self.toAllMangakaPage())
        self.estudioButton.clicked.connect(lambda: self.toAllEstudioPage())

        if manga is not None:  
            self.favoriteButton.clicked.connect(lambda: self.addFav(currentUser, manga)) 
            self.commentButton.clicked.connect(lambda: self.abrir_formulario(manga, currentUser))
            self.title.setText(manga.nombre)
            self.title.setAlignment(Qt.AlignmentFlag.AlignCenter)
            self.synopsis.setText(manga.sinopsis)
            self.placeholderimage.setPixmap(
                QPixmap(os.path.join(basedir, manga.imagen)).scaled(242, 305, Qt.AspectRatioMode.IgnoreAspectRatio, Qt.TransformationMode.SmoothTransformation)  # Ajusta el tamaño
            )
            self.homeButton.clicked.connect(lambda: self.toHomeScreen())
            self.rankingLabel.setText("RANKING DE MANGAS")
            self.rankingLabel.setAlignment(Qt.AlignmentFlag.AlignHCenter)
            self.updateRanking()
            self.descripcion.setText(f"· Géneros: {manga.genero}\n· Volúmenes: {manga.tomos}\n· Capítulos: {manga.capitulos}\n· Mangaka: {manga.autor}")            
            self.updateComentarios(manga)
            self.comments.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        else:
            self.title.setText("Sin información")
            self.title.setAlignment(Qt.AlignmentFlag.AlignCenter)
            self.synopsis.setText("No se ha seleccionado un manga.")
            self.synopsis.setAlignment(Qt.AlignmentFlag.AlignCenter)
            self.placeholderimage.clear()
            self.descripcion.setText("Información no disponible.")
            self.descripcion.setAlignment(Qt.AlignmentFlag.AlignCenter)
            self.comments.setText("COMENTARIOS")
            self.comments.setAlignment(Qt.AlignmentFlag.AlignHCenter)
            self.rankingLabel.setText("RANKING DE ANIMES")
            self.rankingLabel.setAlignment(Qt.AlignmentFlag.AlignHCenter)

    def addFav(self, usuario: Usuario, manga: Manga):
        usuario.updateFavoritos(manga)
        self.mostrar_notificacion("Favoritos actualizados")
        


    def updateRanking(self):
        cont = 1
        mangaRepo = self.MangaRepo()
        mangaList = mangaRepo.getMangas()
        for manga in mangaList:
            item = QListWidgetItem(f"{cont} - {manga.nombre}")
            font = QFont()
            font.setPointSize(12)
            item.setFont(font)
            item.setForeground(QBrush(QColor(0, 0, 0)))
            self.ranking.addItem(item)
            cont += 1

    def abrir_formulario(self, manga:Manga, usuario:Usuario):
        dialogo = self.FormularioEmergente()
        resultado = dialogo.exec()

        if resultado == 1:
            datos = dialogo.obtener_datos()

            comentarioRepo = self.ComentarioRepo()
            comentarioRepo.addComentarioToAnime(
                self.Comentario(
                    f"M-{manga.nombre}-{usuario.nombre}",
                    usuario.email,
                    datos["Comentario"],
                    f"{date.today()}"
                )   
            )
            self.updateComentarios(manga)
            self.mostrar_notificacion("Comentario añadido")
    

    def mostrar_notificacion(self, mensaje):
        
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Icon.Information)
        msg.setWindowTitle("Notificación")
        msg.setText(mensaje)
        msg.setStandardButtons(QMessageBox.StandardButton.Ok)
        msg.exec()


    def updateComentarios(self, manga: Manga):
        text = "COMENTARIOS\n"
        comentarioRepo = self.ComentarioRepo()
        comments: list[Comentario] = comentarioRepo.getComentarios()
        for comentario in comments:
            if comentario._id.split("-")[0] == "M" and comentario._id.split("-")[1] == manga.nombre:
                text += "{}: {}\n".format(comentario.usuario.split("@")[0], comentario.texto)
        self.comments.setText(text)

    def toAllAnimePage(self):
        from Screens.AllAnimeScreen import AllAnimeScreen
        allAnimePage = AllAnimeScreen(self.stacked_widget, self.currentUser)
        self.stacked_widget.addWidget(allAnimePage)
        self.stacked_widget.setCurrentWidget(allAnimePage) 

    def toAllMangaPage(self):
        from Screens.AllMangaScreen import AllMangaScreen
        allMangaPage = AllMangaScreen(self.stacked_widget, self.currentUser)
        self.stacked_widget.addWidget(allMangaPage)
        self.stacked_widget.setCurrentWidget(allMangaPage)  

    def toAllEstudioPage(self):
        from Screens.AllEstudioScreen import AllEstudioScreen
        allEstudioPage = AllEstudioScreen(self.stacked_widget, self.currentUser)
        self.stacked_widget.addWidget(allEstudioPage)
        self.stacked_widget.setCurrentWidget(allEstudioPage)  

    def toAllMangakaPage(self):
        from Screens.AllMangakaScreen import AllMangakaScreen
        allMangakaPage = AllMangakaScreen(self.stacked_widget, self.currentUser)
        self.stacked_widget.addWidget(allMangakaPage)
        self.stacked_widget.setCurrentWidget(allMangakaPage) 

    def toHomeScreen(self):
        from Screens.HomeScreen import HomeScreen
        homeScreen = HomeScreen(self.stacked_widget, self.currentUser)
        self.stacked_widget.addWidget(homeScreen)
        self.stacked_widget.setCurrentWidget(homeScreen)

    def toUserScreen(self):
        from Screens.UserScreen import UserScreen
        userScreen = UserScreen(self.stacked_widget, self.currentUser)
        self.stacked_widget.addWidget(userScreen)
        self.stacked_widget.setCurrentWidget(userScreen)
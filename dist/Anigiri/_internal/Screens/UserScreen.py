import os
from Config.paths import basedir
from PyQt6.QtWidgets import QMainWindow, QListWidgetItem
from PyQt6.QtGui import QFont, QPixmap, QBrush, QColor
from PyQt6.QtCore import Qt
from PyQt6 import uic



class UserScreen(QMainWindow):

    from Model.Usuario import Usuario
    from Repository.comentarioRepo import ComentarioRepo
    
    def __init__(self, stacked_widget, usuario: Usuario):
        super(UserScreen, self).__init__()
        self.currentUser = usuario
        uic.loadUi(os.path.join(basedir, 'Ui/userUi.ui'), self)
        self.setWindowTitle("Anigiri")
        self.homeButton.clicked.connect(lambda: self.toHomeScreen())
        self.animeButton.clicked.connect(lambda: self.toAllAnimePage())
        self.mangaButton.clicked.connect(lambda: self.toAllMangaPage())
        self.mangakaButton.clicked.connect(lambda: self.toAllMangakaPage())
        self.estudioButton.clicked.connect(lambda: self.toAllEstudioPage())
        self.stacked_widget = stacked_widget

        if usuario is not None:
            self.setComentarios(usuario)
            self.nombre.setText(usuario.nombre)
            self.email.setText(usuario.email)
            self.favoritos.setText(f"{len(usuario.favoritos)}")
            ruta_imagen = os.path.join(basedir, "Resources/User/userImage.png")
            pixmap = QPixmap(ruta_imagen)
            self.userImg.setPixmap(QPixmap(pixmap).scaled(191,191, Qt.AspectRatioMode.IgnoreAspectRatio, Qt.TransformationMode.SmoothTransformation))
        else:
            self.nombre.setText("Sin información")
            self.email.setText("Sin información")


    def setComentarios(self, usuario: Usuario):
        comentarioRepo = self.ComentarioRepo()
        comments = comentarioRepo.getComentariosByUser(usuario)

        self.comentariosList.clear()  # Limpiar lista antes de agregar nuevos comentarios

        for comentario in comments:
            # Formatear el texto del comentario
            texto_comentario = f"{comentario.fecha} - {comentario._id.split('-')[1]}: {comentario.texto}"

            # Crear el item y añadirlo al QListWidget
            item = QListWidgetItem(texto_comentario)
            font = QFont()  # Crear un objeto de tipo QFont
            font.setPointSize(12)  # Aumentar el tamaño de la fuente (ajusta el número según lo que necesites)
            item.setFont(font)
            item.setForeground(QBrush(QColor(0, 0, 0)))
            self.comentariosList.addItem(item)


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
        self.stacked_widget.setCurrentIndex(1)
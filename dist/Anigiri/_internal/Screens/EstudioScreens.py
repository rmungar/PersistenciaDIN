import os
from Config.paths import basedir
from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt
from PyQt6 import uic




class EstudioScreen(QMainWindow):
    from Model.Usuario import Usuario
    from Model.Estudio import Estudio
    
    def __init__(self, stacked_widget, estudio: Estudio, currentUser: Usuario):
        super(EstudioScreen, self).__init__()
        self.currentUser = currentUser
        self.stacked_widget = stacked_widget
        uic.loadUi(os.path.join(basedir, 'Ui/creatorsPage.ui'), self)
        self.setWindowTitle("Anigiri")

        self.homeButton.clicked.connect(lambda: self.toHomeScreen())
        self.userButton.clicked.connect(lambda: self.toUserScreen())
        self.animeButton.clicked.connect(lambda: self.toAllAnimePage())
        self.mangaButton.clicked.connect(lambda: self.toAllMangaPage())
        self.mangakaButton.clicked.connect(lambda: self.toAllMangakaPage())
        self.estudioButton.clicked.connect(lambda: self.toAllEstudioPage())

        if estudio is not None:
            self.title.setText(estudio.nombre)
            self.title.setAlignment(Qt.AlignmentFlag.AlignCenter)
            self.biographyvalue.setText(f"· País: {estudio.pais}")
            self.placeholderimage.setPixmap(QPixmap(os.path.join(basedir, estudio.imagen)).scaled(500, 600, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation))  # Ajusta el tamaño
            self.obras.setText(f"Animes: {estudio.animes}")
        else:
            self.title.setText("Sin información")
            self.title.setAlignment(Qt.AlignmentFlag.AlignCenter)
            self.biographyvalue.setText("No se ha seleccionado un estudio.")
            self.biographyvalue.setAlignment(Qt.AlignmentFlag.AlignCenter)
            self.placeholderimage.clear()
            self.obras.setText("Información no disponible.")
            self.obras.setAlignment(Qt.AlignmentFlag.AlignCenter)

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
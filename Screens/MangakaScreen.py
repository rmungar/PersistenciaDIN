import os
from Config.paths import basedir
from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt
from PyQt6 import uic

from Model import Mangaka, Usuario


class MangakaScreen(QMainWindow):
    def __init__(self, stacked_widget, mangaka: Mangaka, currentUser: Usuario):
        super(MangakaScreen, self).__init__()
        self.currentUser = currentUser
        uic.loadUi(os.path.join(basedir, 'Ui/creatorsPage.ui'), self)
        self.setWindowTitle("Anigiri")
        self.stacked_widget = stacked_widget
        self.homeButton.clicked.connect(lambda: self.toHomeScreen())
        self.userButton.clicked.connect(lambda: self.toUserScreen())
        self.animeButton.clicked.connect(lambda: self.toAllAnimePage())
        self.mangaButton.clicked.connect(lambda: self.toAllMangaPage())
        self.mangakaButton.clicked.connect(lambda: self.toAllMangakaPage())
        self.estudioButton.clicked.connect(lambda: self.toAllEstudioPage())

        if mangaka is not None:
            self.title.setText(mangaka.nombre)
            self.title.setAlignment(Qt.AlignmentFlag.AlignCenter)
            self.biographyvalue.setText(f"· Nacimiento: {mangaka.nacimiento}\n· Nacionalidad: {mangaka.nacionalidad}")
            self.placeholderimage.setPixmap(
                QPixmap(os.path.join(basedir, mangaka.imagen)).scaled(300, 400, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)  # Ajusta el tamaño
            )
            self.obras.setText(f"Obras: {mangaka.obras}")
        else:
            self.title.setText("Sin información")
            self.title.setAlignment(Qt.AlignmentFlag.AlignCenter)
            self.biographyvalue.setText("No se ha seleccionado un mangaka.")
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
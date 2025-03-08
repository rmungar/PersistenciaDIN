import os
from Config.paths import basedir
from PyQt6.QtWidgets import QMainWindow, QListWidget, QListWidgetItem
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt, QSize
from PyQt6 import uic

from Model import Usuario

from Repository.mangakaRepo import MangakaRepo
from Screens import MangakaScreen, UserScreen
from Screens.AnimeScreens import AllAnimeScreen
from Screens.EstudioScreens import AllEstudioScreen
from Screens.MangaScreens import AllMangaScreen

class AllMangakaScreen(QMainWindow):
    def __init__(self, stacked_widget, currentUser: Usuario):
        super(AllMangakaScreen, self).__init__()
        self.currentUser = currentUser
        uic.loadUi(os.path.join(basedir, 'Ui/allTemplate.ui'), self)
        self.setWindowTitle("Anigiri")
        self.stacked_widget = stacked_widget
        self.homeButton.clicked.connect(lambda: self.toHomeScreen())
        self.userButton.clicked.connect(lambda: self.toUserScreen())
        self.animeButton.clicked.connect(lambda: self.toAllAnimePage())
        self.mangaButton.clicked.connect(lambda: self.toAllMangaPage())
        self.mangakaButton.clicked.connect(lambda: self.toAllMangakaPage())
        self.estudioButton.clicked.connect(lambda: self.toAllEstudioPage())
        self.listWidget = self.findChild(QListWidget, "listWidget")  # Asegurar acceso

        if self.listWidget is None:
            print("Error: listWidget no encontrado en la UI.")
            return  # Evita fallos si el widget no se encuentra
        
        mangakaRepo = MangakaRepo()
        self.mangakaList = mangakaRepo.getMangakas()

        self.displayMangakaList()

    def displayMangakaList(self):
        """Muestra los animes en el QListWidget"""
        self.listWidget.clear()  # Limpia la lista antes de agregar nuevos elementos

        for mangaka in self.mangakaList:
            font = QFont()
            font.setPointSize(16)  # Cambia 16 por el tamaño que desees
            item = QListWidgetItem(mangaka.nombre)  # Asigna el icono y el nombre
            item.setData(1, mangaka)  # Guarda el objeto para referencia futura
            item.setFont(font)
            item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            item.setSizeHint(QSize(100, 100))
            self.listWidget.addItem(item)

        print("Número de elementos en listWidget:", self.listWidget.count())

        self.listWidget.update()
        self.listWidget.repaint()

        self.listWidget.itemClicked.connect(self.onMangakaClicked)

    def onMangakaClicked(self, item):
        mangaka = item.data(1)
        mangakaScreen = MangakaScreen(self.stacked_widget, mangaka, self.currentUser)
        self.stacked_widget.addWidget(mangakaScreen)
        self.stacked_widget.setCurrentWidget(mangakaScreen)

    def toAllAnimePage(self):
        allAnimePage = AllAnimeScreen(self.stacked_widget, self.currentUser)
        self.stacked_widget.addWidget(allAnimePage)
        self.stacked_widget.setCurrentWidget(allAnimePage) 

    def toAllMangaPage(self):
        allMangaPage = AllMangaScreen(self.stacked_widget, self.currentUser)
        self.stacked_widget.addWidget(allMangaPage)
        self.stacked_widget.setCurrentWidget(allMangaPage)  

    def toAllEstudioPage(self):
        allEstudioPage = AllEstudioScreen(self.stacked_widget, self.currentUser)
        self.stacked_widget.addWidget(allEstudioPage)
        self.stacked_widget.setCurrentWidget(allEstudioPage)  

    def toAllMangakaPage(self):
        allMangakaPage = AllMangakaScreen(self.stacked_widget, self.currentUser)
        self.stacked_widget.addWidget(allMangakaPage)
        self.stacked_widget.setCurrentWidget(allMangakaPage) 

    def toHomeScreen(self):
        self.stacked_widget.setCurrentIndex(1)

    def toUserScreen(self):
        userScreen = UserScreen(self.stacked_widget, self.currentUser)
        self.stacked_widget.addWidget(userScreen)
        self.stacked_widget.setCurrentWidget(userScreen)
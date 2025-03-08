import os
from Config.paths import basedir
from PyQt6.QtWidgets import QMainWindow, QListWidget, QListWidgetItem
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt, QSize
from PyQt6 import uic



class AllMangakaScreen(QMainWindow):

    from Model.Usuario import Usuario
    from Repository.mangakaRepo import MangakaRepo
    

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
        
        mangakaRepo = self.MangakaRepo()
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
        from Screens.MangakaScreen import MangakaScreen
        mangaka = item.data(1)
        mangakaScreen = MangakaScreen(self.stacked_widget, mangaka, self.currentUser)
        self.stacked_widget.addWidget(mangakaScreen)
        self.stacked_widget.setCurrentWidget(mangakaScreen)

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
        allMangakaPage = AllMangakaScreen(self.stacked_widget, self.currentUser)
        self.stacked_widget.addWidget(allMangakaPage)
        self.stacked_widget.setCurrentWidget(allMangakaPage) 

    def toHomeScreen(self):
        self.stacked_widget.setCurrentIndex(1)

    def toUserScreen(self):
        from Screens.UserScreen import UserScreen
        userScreen = UserScreen(self.stacked_widget, self.currentUser)
        self.stacked_widget.addWidget(userScreen)
        self.stacked_widget.setCurrentWidget(userScreen)
import os
from Config.paths import basedir
from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import QSize
from PyQt6 import uic






class HomeScreen(QMainWindow):

    from Model.Anime import Anime
    from Model.Estudio import Estudio
    from Model.Manga import Manga
    from Model.Mangaka import Mangaka
    from Model.Usuario import Usuario
    from Repository.animeRepo import AnimeRepo
    from Repository.estudioRepo import EstudioRepo
    from Repository.mangaRepo import MangaRepo
    from Repository.mangakaRepo import MangakaRepo
    from Repository.usuarioRepo import UsuarioRepo

    def __init__(self, stacked_widget, currentUser: Usuario):
        from Screens.LoginScreen import LoginScreen
        super(HomeScreen, self).__init__()
        self.currentUser = currentUser
        self.login_screen = LoginScreen(stacked_widget)

        uic.loadUi(os.path.join(basedir, 'Ui/homePage.ui'), self)
        self.setWindowTitle("Anigiri")
        self.stacked_widget = stacked_widget
        self.userButton.clicked.connect(lambda: self.toUserScreen())
        self.animeButton.clicked.connect(lambda: self.toAllAnimePage())
        self.mangaButton.clicked.connect(lambda: self.toAllMangaPage())
        self.mangakaButton.clicked.connect(lambda: self.toAllMangakaPage())
        self.estudioButton.clicked.connect(lambda: self.toAllEstudioPage())

        mangaRepo = self.MangaRepo()
        animeRepo = self.AnimeRepo()
        mangakaRepo = self.MangakaRepo()
        estudioRepo = self.EstudioRepo()

        # Obtener listas de datos
        self.animeList = animeRepo.getAnime()
        self.mangaList = mangaRepo.getMangas()
        self.mangakaList = mangakaRepo.getMangakas()
        self.estudioList = estudioRepo.getEstudios()

        # Índices para rastrear la posición de cada imagen
        self.anime_indices = [0, 1, 2]  # [izquierda (top2), centro (top1), derecha (top3)]
        self.manga_indices = [0, 1, 2]
        self.mangaka_indices = [0, 1, 2]
        self.estudio_indices = [0, 1, 2]

        # Configurar imágenes en UI
        self.setImagenes(self.animeTop1, self.animeTop2, self.animeTop3, 
                         self.anime_indices, self.animeList, self.toAnimePage)

        self.setImagenes(self.mangaTop1, self.mangaTop2, self.mangaTop3, 
                         self.manga_indices, self.mangaList, self.toMangaPage)

        self.setImagenes(self.mangakaTop1, self.mangakaTop2, self.mangakaTop3, 
                         self.mangaka_indices, self.mangakaList, self.toMangakaPage)

        self.setImagenes(self.estudiosTop1, self.estudiosTop2, self.estudiosTop3, 
                         self.estudio_indices, self.estudioList, self.toEstudioPage)

    def configurarBoton(self, boton, imagen):
        """Configura un botón con la imagen proporcionada"""
        boton.setText("")
        boton.setStyleSheet("background: transparent; border: none;")
        boton.setIcon(QIcon(imagen))
        boton.setIconSize(QSize(370, 400))

    def setImagenes(self, btn_centro, btn_izq, btn_der, indices, lista, funcion_navegar):
        """Configura los botones de imágenes con sus eventos de navegación y rotación"""
        self.configurarBoton(btn_centro, os.path.join(basedir, lista[indices[1]].imagen))  # Centro (top1)
        self.configurarBoton(btn_izq, os.path.join(basedir, lista[indices[0]].imagen))  # Izquierda (top2)
        self.configurarBoton(btn_der, os.path.join(basedir, lista[indices[2]].imagen))  # Derecha (top3)

        # Asignar navegación correcta al botón central
        btn_centro.clicked.connect(lambda: funcion_navegar(lista[indices[1]]))  # top1 lleva a la info correcta

        # Asignar eventos de rotación
        btn_izq.clicked.connect(lambda: self.moverImagen(indices, lista, btn_centro, btn_izq, btn_der, funcion_navegar, -1))
        btn_der.clicked.connect(lambda: self.moverImagen(indices, lista, btn_centro, btn_izq, btn_der, funcion_navegar, 1))

    def moverImagen(self, indices, lista, btn_centro, btn_izq, btn_der, funcion_navegar, direccion):
        """Rota las imágenes manteniendo la disposición correcta"""
        if direccion == 1:  # Si se presiona top3
            indices[:] = [indices[1], indices[2], indices[0]]  # top3 → top1, top2 → top3, top1 → top2
        elif direccion == -1:  # Si se presiona top2
            indices[:] = [indices[2], indices[0], indices[1]]  # top2 → top1, top1 → top3, top3 → top2

        # Actualizar imágenes en los botones
        self.configurarBoton(btn_centro, os.path.join(basedir, lista[indices[1]].imagen))  # Centro (top1)
        self.configurarBoton(btn_izq, os.path.join(basedir, lista[indices[0]].imagen))  # Izquierda (top2)
        self.configurarBoton(btn_der, os.path.join(basedir, lista[indices[2]].imagen))  # Derecha (top3)

        # Actualizar el evento del botón central para que lleve a la página correcta
        btn_centro.clicked.connect(lambda: funcion_navegar(lista[indices[1]]))  # Siempre top1 lleva a la página correcta

    def toMangaPage(self, manga: Manga):
        from Screens.MangaScreens import MangaScreen
        manga_screen = MangaScreen(self.stacked_widget, manga, self.currentUser)
        self.stacked_widget.addWidget(manga_screen)
        self.stacked_widget.setCurrentWidget(manga_screen)   

    def toAnimePage(self, anime: Anime):
        """Actualiza AnimeScreen y cambia de ventana"""
        from Screens.AnimeScreens import AnimeScreen
        animeScreen = AnimeScreen(self.stacked_widget, anime, self.currentUser)
        self.stacked_widget.addWidget(animeScreen)
        self.stacked_widget.setCurrentWidget(animeScreen)   
    
    def toMangakaPage(self, mangaka: Mangaka):  
        """Actualiza MangakaScreen y cambia de ventana"""
        from Screens.MangakaScreen import MangakaScreen
        mangakaScreen = MangakaScreen(self.stacked_widget, mangaka, self.currentUser)
        self.stacked_widget.addWidget(mangakaScreen)
        self.stacked_widget.setCurrentWidget(mangakaScreen)   

    def toEstudioPage(self, estudio: Estudio):
        """Actualiza EstudioScreen y cambia de ventana"""
        from Screens.EstudioScreens import EstudioScreen
        estudioScreen = EstudioScreen(self.stacked_widget, estudio, self.currentUser)
        self.stacked_widget.addWidget(estudioScreen)
        self.stacked_widget.setCurrentWidget(estudioScreen)   

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

    def toUserScreen(self):
        from Screens.UserScreen import UserScreen
        userScreen = UserScreen(self.stacked_widget, self.currentUser)
        self.stacked_widget.addWidget(userScreen)
        self.stacked_widget.setCurrentWidget(userScreen)    
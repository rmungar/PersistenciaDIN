# -*- coding: utf-8 -*-

# prueba@gmail.com
# passwordPrueba


import sys
import os
import pyrebase
from PyQt6.QtWidgets import QApplication, QMainWindow, QStackedWidget, QErrorMessage, QLineEdit
from PyQt6.QtCore import QSize, Qt
from PyQt6 import uic
from PyQt6.QtGui import QIcon, QPixmap, QFont
from Model import Anime, Estudio, Manga, Mangaka
from Model.Usuario import Usuario
from Repository.animeRepo import AnimeRepo
from Repository.estudioRepo import EstudioRepo
from Repository.mangaRepo import MangaRepo
from Repository.mangakaRepo import MangakaRepo
from Repository.usuarioRepo import UsuarioRepo

basedir = os.path.dirname(__file__)

config = {
    "apiKey": "AIzaSyB7fn2d5cm8YtiBrelexmoxleAezCNiU9E",
    "authDomain": "anigiri-353a4.firebaseapp.com",
    "projectId": "anigiri-353a4",
    "storageBucket": "anigiri-353a4.firebasestorage.app",
    "databaseURL": "",
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
userLogged = auth.current_user

class LoginScreen(QMainWindow):
    def __init__(self, stacked_widget):

        
        super(LoginScreen, self).__init__()
        uic.loadUi(os.path.join(basedir, 'Ui/login.ui'), self)
        self.setWindowTitle("Anigiri")
        font = QFont()
        font.setPointSize(16)
        self.emailText.setFont(font)
        self.stacked_widget = stacked_widget  # Referencia al `QStackedWidget
        self.loginButton.clicked.connect(self.login)
        self.registerButton.clicked.connect(self.register)


    def login(self):
        email = self.emailText.toPlainText()
        password = self.passwordText.toPlainText()

        try:
            user = auth.sign_in_with_email_and_password(email, password)  
            print("Login exitoso:", user)

            # Cambia a la pantalla de inicio
            self.stacked_widget.addWidget(HomeScreen(stacked_widget))
            self.stacked_widget.setCurrentIndex(1)
        except:
            QErrorMessage(self).showMessage("Usuario o contraseña incorrectos")

    def register(self):
        email = self.emailText.toPlainText()
        password = self.passwordText.toPlainText()

        try:
            user = auth.create_user_with_email_and_password(email, password)
            print("Usuario registrado:", user)
        except:
            QErrorMessage(self).showMessage("Usuario ya registrado")


class MangaScreen(QMainWindow):
    def __init__(self, stacked_widget, manga):
        super(MangaScreen, self).__init__()
        
        uic.loadUi(os.path.join(basedir, 'Ui/mangaPage.ui'), self)
        self.setWindowTitle("Anigiri")
        self.stacked_widget = stacked_widget
        if manga is not None:
            self.title.setText(manga.nombre)
            self.synopsisvalue.setText(manga.sinopsis)
            self.placeholderimage.setPixmap(QPixmap(os.path.join(basedir, manga.imagen)).size())
            
            self.information.setText(f"Generos: {manga.genero}\nVolúmenes: {manga.tomos}\nCapítulos: {manga.capitulos}\nMangaka: {manga.autor}")
        else:
            self.title.setText("Sin información")
            self.synopsisvalue.setText("No se ha seleccionado un manga.")
            self.placeholderimage.clear()  # Limpia la imagen
            self.information.setText("Información no disponible.")


class AnimeScreen(QMainWindow):
    def __init__(self, stacked_widget, anime):
        super(AnimeScreen, self).__init__()

        uic.loadUi(os.path.join(basedir, 'Ui/animePage.ui'), self)
        self.setWindowTitle("Anigiri")
        self.stacked_widget = stacked_widget
        if anime is not None:
            self.title.setText(anime.nombre)
            self.synopsisvalue.setText(anime.sinopsis)
            self.placeholderimage.setPixmap(QPixmap(os.path.join(basedir, anime.imagen)))
            self.information.setText(f"Generos: {anime.genero}\nTemporadas: {anime.temporadas}\nCapítulos: {anime.capitulos}\nEstudio: {anime.estudio}")
        else:
            self.title.setText("Sin información")
            self.synopsisvalue.setText("No se ha seleccionado un manga.")
            self.placeholderimage.clear()  # Limpia la imagen
            self.information.setText("Información no disponible.")


class MangakaScreen(QMainWindow):
    def __init__(self, stacked_widget, mangaka):
        super(MangakaScreen, self).__init__()

        uic.loadUi(os.path.join(basedir, 'Ui/mangakaPage.ui'), self)
        self.setWindowTitle("Anigiri")
        self.stacked_widget = stacked_widget
        if mangaka is not None:
            self.title.setText(mangaka.nombre)
            self.biographyvalue.setText(f"Nacimiento: {mangaka.nacimiento}\nNacionalidad: {mangaka.nacionalidad}")
            self.placeholderimage.setPixmap(QPixmap(os.path.join(basedir, mangaka.imagen)))
            self.mangas.setText(f"Obras: {mangaka.obras}")
        else:
            self.title.setText("Sin información")
            self.biographyvalue.setText("No se ha seleccionado un mangaka.")
            self.placeholderimage.clear()  # Limpia la imagen
            self.mangas.setText("Información no disponible.")


class EstudioScreen(QMainWindow):
    def __init__(self, stacked_widget, estudio):
        super(EstudioScreen, self).__init__()

        uic.loadUi(os.path.join(basedir, 'Ui/estudioPage.ui'), self)
        self.setWindowTitle("Anigiri")
        self.stacked_widget = stacked_widget
        if estudio is not None:
            self.title.setText(estudio.nombre)
            self.detailsvalue.setText(f"País: {estudio.pais}")
            self.placeholderimage.setPixmap(QPixmap(os.path.join(basedir, estudio.imagen)))
            self.animes.setText(f"Animes: {estudio.animes}")
        else:
            self.title.setText("Sin información")
            self.detailsvalue.setText("No se ha seleccionado un estudio.")
            self.placeholderimage.clear()  # Limpia la imagen
            self.anime.setText("Información no disponible.")


class HomeScreen(QMainWindow):
    def __init__(self, stacked_widget):
        super(HomeScreen, self).__init__()

        self.login_screen = LoginScreen(stacked_widget)

        uic.loadUi(os.path.join(basedir, 'Ui/homePage.ui'), self)
        self.setWindowTitle("Anigiri")
        self.stacked_widget = stacked_widget

        usuarioRepo = UsuarioRepo()
        mangaRepo = MangaRepo()
        animeRepo = AnimeRepo()
        mangakaRepo = MangakaRepo()
        estudioRepo = EstudioRepo()

        # Obtener listas de datos
        self.mangaList = mangaRepo.getMangas()
        self.animeList = animeRepo.getAnime()
        self.mangakaList = mangakaRepo.getMangakas()
        self.estudioList = estudioRepo.getEstudios()

        # Listas de imágenes (ajustadas según la disposición)
        self.image_paths_anime = [
            os.path.join(basedir, self.animeList[0].imagen),  # Izquierda
            os.path.join(basedir, self.animeList[1].imagen),  # Centro
            os.path.join(basedir, self.animeList[2].imagen)   # Derecha
        ]

        self.image_paths_manga = [
            os.path.join(basedir, self.mangaList[0].imagen),  # Centro
            os.path.join(basedir, self.mangaList[1].imagen),  # Izquierda
            os.path.join(basedir, self.mangaList[2].imagen)   # Derecha
        ]

        self.image_paths_mangaka = [
            os.path.join(basedir, self.mangakaList[0].imagen),
            os.path.join(basedir, self.mangakaList[1].imagen),
            os.path.join(basedir, self.mangakaList[2].imagen)
        ]

        self.image_paths_estudio = [
            os.path.join(basedir, self.estudioList[0].imagen),
            os.path.join(basedir, self.estudioList[1].imagen),
            os.path.join(basedir, self.estudioList[2].imagen)
        ]

        # Configurar imágenes en UI
        self.setImagenesAnime()
        self.setImagenesManga()
        self.setImagenesMangaka()
        self.setImagenesEstudio()

    def setImagenesAnime(self):
        """Configura los botones de anime con imágenes y eventos de rotación"""
        self.configurarBoton(self.animeTop1, self.image_paths_anime[1])
        self.configurarBoton(self.animeTop2, self.image_paths_anime[0])
        self.configurarBoton(self.animeTop3, self.image_paths_anime[2])

        self.animeTop1.clicked.connect(lambda: self.toAnimePage(self.animeList[0]))
        self.animeTop2.clicked.connect(lambda: self.moverImagen(self.image_paths_anime, self.animeTop1, self.animeTop2, self.animeTop3, 2))
        self.animeTop3.clicked.connect(lambda: self.moverImagen(self.image_paths_anime, self.animeTop1, self.animeTop2, self.animeTop3, 3))

    def setImagenesManga(self):
        """Configura los botones de manga con imágenes y eventos de rotación"""
        self.configurarBoton(self.mangaTop1, self.image_paths_manga[0])
        self.configurarBoton(self.mangaTop2, self.image_paths_manga[1])
        self.configurarBoton(self.mangaTop3, self.image_paths_manga[2])

        self.mangaTop1.clicked.connect(lambda: self.toMangaPage(self.mangaList[0]))
        self.mangaTop2.clicked.connect(lambda: self.moverImagen(self.image_paths_manga, self.mangaTop1, self.mangaTop2, self.mangaTop3, 2))
        self.mangaTop3.clicked.connect(lambda: self.moverImagen(self.image_paths_manga, self.mangaTop1, self.mangaTop2, self.mangaTop3, 3))

    def setImagenesMangaka(self):
        """Configura los botones de mangaka con imágenes"""
        self.configurarBoton(self.mangakaTop1, self.image_paths_mangaka[0])
        self.configurarBoton(self.mangakaTop2, self.image_paths_mangaka[1])
        self.configurarBoton(self.mangakaTop3, self.image_paths_mangaka[2])

        self.mangakaTop1.clicked.connect(lambda: self.toMangakaPage(self.mangakaList[0]))
        self.mangakaTop2.clicked.connect(lambda: self.moverImagen(self.image_paths_mangaka, self.mangakaTop1, self.mangakaTop2, self.mangakaTop3, 2))
        self.mangakaTop3.clicked.connect(lambda: self.moverImagen(self.image_paths_mangaka, self.mangakaTop1, self.mangakaTop2, self.mangakaTop3, 3))

    def setImagenesEstudio(self):
        """Configura los botones de estudio con imágenes"""
        self.configurarBoton(self.estudiosTop1, self.image_paths_estudio[0])
        self.configurarBoton(self.estudiosTop2, self.image_paths_estudio[1])
        self.configurarBoton(self.estudiosTop3, self.image_paths_estudio[2])

        self.estudiosTop1.clicked.connect(lambda: self.toEstudioPage(self.estudioList[0]))
        self.estudiosTop2.clicked.connect(lambda: self.moverImagen(self.image_paths_estudio, self.estudiosTop1, self.estudiosTop2, self.estudiosTop3, 2))
        self.estudiosTop3.clicked.connect(lambda: self.moverImagen(self.image_paths_estudio, self.estudiosTop1, self.estudiosTop2, self.estudiosTop3, 3))

    def configurarBoton(self, boton, imagen):
        """Configura un botón con la imagen proporcionada"""
        boton.setText("")
        boton.setStyleSheet("background: transparent; border: none;")
        boton.setIcon(QIcon(imagen))
        boton.setIconSize(QSize(370, 400))

    def moverImagen(self, image_paths, boton_centro, boton_izq, boton_der, boton_presionado):
        """Rota las imágenes en la dirección correspondiente"""
        if boton_presionado == 2:  # Rotación a la derecha
            image_paths[:] = [image_paths[1], image_paths[2], image_paths[0]]
        elif boton_presionado == 3:  # Rotación a la izquierda
            image_paths[:] = [image_paths[2], image_paths[0], image_paths[1]]

        # Aplicar los nuevos iconos
        boton_centro.setIcon(QIcon(image_paths[0]))
        boton_izq.setIcon(QIcon(image_paths[1]))
        boton_der.setIcon(QIcon(image_paths[2]))

    def toMangaPage(self, manga: Manga.Manga):
        manga_screen = MangaScreen(stacked_widget, manga)
        stacked_widget.addWidget(manga_screen)
        stacked_widget.setCurrentWidget(manga_screen)   

    def toAnimePage(self, anime: Anime.Anime):
        """Actualiza AnimeScreen y cambia de ventana"""
        animeScreen = AnimeScreen(self.stacked_widget, anime)
        stacked_widget.addWidget(animeScreen)
        stacked_widget.setCurrentWidget(animeScreen)   
    
    def toMangakaPage(self, mangaka: Mangaka.Mangaka):  
        """Actualiza MangakaScreen y cambia de ventana"""
        mangakaScreen = MangakaScreen(self.stacked_widget, mangaka)
        stacked_widget.addWidget(mangakaScreen)
        stacked_widget.setCurrentWidget(mangakaScreen)   

    def toEstudioPage(self, estudio: Estudio.Estudio):
        """Actualiza EstudioScreen y cambia de ventana"""
        estudioScreen = EstudioScreen(self.stacked_widget, estudio)
        stacked_widget.addWidget(estudioScreen)
        stacked_widget.setCurrentWidget(estudioScreen)   
    

if __name__ == '__main__':
    app = QApplication(sys.argv)

    # Crear el QStackedWidget
    stacked_widget = QStackedWidget()
    loginScreen = LoginScreen(stacked_widget)
    # Iniciar en la pantalla de Login
    stacked_widget.addWidget(loginScreen)
    stacked_widget.setCurrentIndex(0)
    stacked_widget.show()

    app.exec()

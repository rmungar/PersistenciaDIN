# -*- coding: utf-8 -*-

# prueba@gmail.com
# passwordPrueba


import sys
import os
import pyrebase
from PyQt6.QtWidgets import QApplication, QMainWindow, QStackedWidget, QErrorMessage
from PyQt6.QtCore import QSize
from PyQt6 import uic
from PyQt6.QtGui import QIcon
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

class Login(QMainWindow):
    def __init__(self, stacked_widget):
        super(Login, self).__init__()
        uic.loadUi(os.path.join(basedir, 'Ui/login.ui'), self)
        self.setWindowTitle("Anigiri")
        
        self.stacked_widget = stacked_widget  # Referencia al `QStackedWidget`
        
        self.loginButton.clicked.connect(self.login)
        self.registerButton.clicked.connect(self.register)


    def login(self):
        email = self.emailText.toPlainText()
        password = self.passwordText.toPlainText()

        try:
            user = auth.sign_in_with_email_and_password(email, password)  
            print("Login exitoso:", user)

            # Cambia a la pantalla de inicio
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


class HomeScreen(QMainWindow):
    def __init__(self, stacked_widget):
        super(HomeScreen, self).__init__()

        uic.loadUi(os.path.join(basedir, 'Ui/homePage.ui'), self)
        self.setWindowTitle("Anigiri")
        self.stacked_widget = stacked_widget

        usuarioRepo = UsuarioRepo()
        mangaRepo = MangaRepo()
        animeRepo = AnimeRepo()
        mangakaRepo = MangakaRepo()
        estudioRepo = EstudioRepo()

        # Obtener listas de datos
        mangaList = mangaRepo.getMangas()
        animeList = animeRepo.getAnime()
        mangakaList = mangakaRepo.getMangakas()
        estudioList = estudioRepo.getEstudios()

        # Listas de imágenes (ajustadas según la disposición)
        self.image_paths_anime = [
            os.path.join(basedir, animeList[1].imagen),  # Izquierda
            os.path.join(basedir, animeList[0].imagen),  # Centro
            os.path.join(basedir, animeList[2].imagen)   # Derecha
        ]

        self.image_paths_manga = [
            os.path.join(basedir, mangaList[0].imagen),  # Centro
            os.path.join(basedir, mangaList[1].imagen),  # Izquierda
            os.path.join(basedir, mangaList[2].imagen)   # Derecha
        ]

        self.image_paths_mangaka = [
            os.path.join(basedir, mangakaList[0].imagen),
            os.path.join(basedir, mangakaList[1].imagen),
            os.path.join(basedir, mangakaList[2].imagen)
        ]

        self.image_paths_estudio = [
            os.path.join(basedir, estudioList[0].imagen),
            os.path.join(basedir, estudioList[1].imagen),
            os.path.join(basedir, estudioList[2].imagen)
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

        self.animeTop2.clicked.connect(lambda: self.moverImagen(self.image_paths_anime, self.animeTop1, self.animeTop2, self.animeTop3, 2))
        self.animeTop3.clicked.connect(lambda: self.moverImagen(self.image_paths_anime, self.animeTop1, self.animeTop2, self.animeTop3, 3))

    def setImagenesManga(self):
        """Configura los botones de manga con imágenes y eventos de rotación"""
        self.configurarBoton(self.mangaTop1, self.image_paths_manga[0])
        self.configurarBoton(self.mangaTop2, self.image_paths_manga[1])
        self.configurarBoton(self.mangaTop3, self.image_paths_manga[2])

        self.mangaTop2.clicked.connect(lambda: self.moverImagen(self.image_paths_manga, self.mangaTop1, self.mangaTop2, self.mangaTop3, 2))
        self.mangaTop3.clicked.connect(lambda: self.moverImagen(self.image_paths_manga, self.mangaTop1, self.mangaTop2, self.mangaTop3, 3))

    def setImagenesMangaka(self):
        """Configura los botones de mangaka con imágenes"""
        self.configurarBoton(self.mangakaTop1, self.image_paths_mangaka[0])
        self.configurarBoton(self.mangakaTop2, self.image_paths_mangaka[1])
        self.configurarBoton(self.mangakaTop3, self.image_paths_mangaka[2])

        self.mangakaTop2.clicked.connect(lambda: self.moverImagen(self.image_paths_mangaka, self.mangakaTop1, self.mangakaTop2, self.mangakaTop3, 2))
        self.mangakaTop3.clicked.connect(lambda: self.moverImagen(self.image_paths_mangaka, self.mangakaTop1, self.mangakaTop2, self.mangakaTop3, 3))

    def setImagenesEstudio(self):
        """Configura los botones de estudio con imágenes"""
        self.configurarBoton(self.estudiosTop1, self.image_paths_estudio[0])
        self.configurarBoton(self.estudiosTop2, self.image_paths_estudio[1])
        self.configurarBoton(self.estudiosTop3, self.image_paths_estudio[2])

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

    


if __name__ == '__main__':
    app = QApplication(sys.argv)

    # Creamos un QStackedWidget para manejar las pantallas
    stacked_widget = QStackedWidget()

    # Creamos las pantallas y las agregamos al QStackedWidget
    login_screen = Login(stacked_widget)
    home_screen = HomeScreen(stacked_widget)

    stacked_widget.addWidget(login_screen)  # Índice 0
    stacked_widget.addWidget(home_screen)   # Índice 1

    stacked_widget.setCurrentIndex(0)  # Empezamos en la pantalla de Login
    stacked_widget.show()

    app.exec()

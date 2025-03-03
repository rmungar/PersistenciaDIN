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
from Repository.mangaRepo import MangaRepo
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
        mangaList = mangaRepo.getMangas()
        animeRepo = AnimeRepo()
        animeList = animeRepo.getAnime()
        ## estudioRepo = EstudioRepo()
        ## mangakaRepo = MangakaRepo()

        self.animeImagePaths = [
            os.path.join(basedir, animeList[0][5]),
            os.path.join(basedir, animeList[1][5]),
            os.path.join(basedir, animeList[2][5])
        ]

        self.mangaImagePaths = [
            os.path.join(basedir, mangaList[0][5]),
            os.path.join(basedir, mangaList[1][5]),
            os.path.join(basedir, mangaList[2][5])
        ]


        
        self.animeTop1.setText("")
        self.animeTop1.setStyleSheet("background: transparent; border: none;")
        self.animeTop1.setIcon(QIcon(self.animeImagePaths[0]))
        self.animeTop1.setIconSize(QSize(370, 400))

        self.animeTop2.setText("")
        self.animeTop2.setStyleSheet("background: transparent; border: none;")
        self.animeTop2.setIcon(QIcon(self.animeImagePaths[1]))
        self.animeTop2.setIconSize(QSize(370, 400))

        self.animeTop3.setText("")
        self.animeTop3.setStyleSheet("background: transparent; border: none;")
        self.animeTop3.setIcon(QIcon(self.animeImagePaths[2]))
        self.animeTop3.setIconSize(QSize(370, 400))

        
        self.animeTop2.clicked.connect(lambda: self.moverImagenAnime(2))
        self.animeTop3.clicked.connect(lambda: self.moverImagenAnime(3))



        self.mangaTop1.setText("")
        self.mangaTop1.setStyleSheet("background: transparent; border: none;")
        self.mangaTop1.setIcon(QIcon(self.mangaImagePaths[0]))
        self.mangaTop1.setIconSize(QSize(370, 400))

        self.mangaTop2.setText("")
        self.mangaTop2.setStyleSheet("background: transparent; border: none;")
        self.mangaTop2.setIcon(QIcon(self.mangaImagePaths[1]))
        self.mangaTop2.setIconSize(QSize(370, 400))

        self.mangaTop3.setText("")
        self.mangaTop3.setStyleSheet("background: transparent; border: none;")
        self.mangaTop3.setIcon(QIcon(self.mangaImagePaths[2]))
        self.mangaTop3.setIconSize(QSize(370, 400))

        self.mangaTop2.clicked.connect(lambda: self.moverImagenManga(2))
        self.mangaTop3.clicked.connect(lambda: self.moverImagenManga(3))
                    
    def moverImagenAnime(self, boton_presionado):
        
        if boton_presionado == 2:  # Si se presiona el de la izquierda, rotar a la derecha
            self.animeImagePaths = [self.animeImagePaths[1], self.animeImagePaths[2], self.animeImagePaths[0]]
        elif boton_presionado == 3:  # Si se presiona el de la derecha, rotar a la izquierda
            self.animeImagePaths = [self.animeImagePaths[2], self.animeImagePaths[0], self.animeImagePaths[1]]
        
        # Actualizar los iconos con la nueva rotación
        self.animeTop1.setIcon(QIcon(self.animeImagePaths[0]))
        self.animeTop2.setIcon(QIcon(self.animeImagePaths[1]))
        self.animeTop3.setIcon(QIcon(self.animeImagePaths[2]))

    def moverImagenManga(self, boton_presionado):
        
        if boton_presionado == 2:  # Si se presiona el de la izquierda, rotar a la derecha
            self.mangaImagePaths = [self.mangaImagePaths[1], self.mangaImagePaths[2], self.mangaImagePaths[0]]
        elif boton_presionado == 3:  # Si se presiona el de la derecha, rotar a la izquierda
            self.mangaImagePaths = [self.mangaImagePaths[2], self.mangaImagePaths[0], self.mangaImagePaths[1]]

        # Actualizar los iconos con la nueva rotación
        self.mangaTop1.setIcon(QIcon(self.mangaImagePaths[0]))
        self.mangaTop2.setIcon(QIcon(self.mangaImagePaths[1]))
        self.mangaTop3.setIcon(QIcon(self.mangaImagePaths[2]))
    


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

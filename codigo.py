# -*- coding: utf-8 -*-

import sys
import os
import pyrebase
from PyQt6.QtWidgets import QApplication, QMainWindow, QStackedWidget, QErrorMessage
from PyQt6 import uic

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


class Login(QMainWindow):
    def __init__(self, stacked_widget):
        super(Login, self).__init__()
        uic.loadUi(os.path.join(basedir, 'login.ui'), self)
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
        uic.loadUi(os.path.join(basedir, 'homePage.ui'), self)
        self.setWindowTitle("Anigiri")
        self.stacked_widget = stacked_widget


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

# -*- coding: utf-8 -*-

#importamos las librerías necesarias
import sys
from PyQt6.QtWidgets import * 
from PyQt6 import uic  
from PyQt6.QtCore import Qt
from pathlib import Path
import re
import math as Math
from PyQt6.QtGui import QIcon
import os
import pyrebase as pyrebase

config = {
    "apiKey": "AIzaSyB7fn2d5cm8YtiBrelexmoxleAezCNiU9E",
    "authDomain": "anigiri-353a4.firebaseapp.com",
    "projectId": "anigiri-353a4",
    "storageBucket": "anigiri-353a4.firebasestorage.app",
    "databaseURL": "",
}

firebase = pyrebase.initialize_app(config)


basedir = os.path.dirname(__file__)

#Carga la interfaz gráfica y conecta los botones
class Ventana(QMainWindow):
    #Inicializamos la ventana y conectamos los botones
    def __init__(self):

        super(Ventana, self).__init__() 
        
        self.isResult = False

        uic.loadUi(os.path.join(basedir, 'login.ui'),self)
        self.setWindowTitle("Anigiri") 


        self.loginButton.clicked.connect(self.login)
        self.registerButton.clicked.connect(self.register)

        self.history = dict()

        # Conectamos los botones
    
    def login(self):
        email = self.emailText.toPlainText()
        password = self.passwordText.toPlainText()

        auth = firebase.auth()
        try:
            user = auth.sign_in_with_email_and_password(email, password)
            self.user = user
            print(user)
            
        except:
            QErrorMessage(self).showMessage("Usuario o contraseña incorrectos")
        
    def register(self):
        email = self.emailText.toPlainText()
        password = self.passwordText.toPlainText()

        auth = firebase.auth()
        try:
            user = auth.create_user_with_email_and_password(email, password)
            self.user = user
            print(user)
            
        except:
            QErrorMessage(self).showMessage("Usuario ya registrado")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Ventana()
    window.show()
    app.exec() 
from logging import config
import os

import pyrebase
from Config.paths import basedir
from PyQt6.QtWidgets import QMainWindow, QErrorMessage
from PyQt6.QtGui import QFont
from PyQt6 import uic



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

    from Model.Usuario import Usuario
    from Repository.usuarioRepo import UsuarioRepo
    
    
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
    
    def getUsuario(self, email: str, psswd: str) -> Usuario:
        usuarios = self.UsuarioRepo.getUsuarios()
        print("Usuarios en la base de datos:")
        for u in usuarios:
            print(f"Email: '{u.email}', Password: '{u.passwd}'")  # DEBUG

        for usuario in usuarios:
            print(f"Comparando: '{usuario.email.strip()}' == '{email.strip()}' y '{usuario.passwd.strip()}' == '{psswd.strip()}'")  # DEBUG
            if usuario.email.strip() == email.strip() and usuario.passwd.strip() == psswd.strip():
                print("Usuario encontrado ✅")  # Mensaje de éxito
                return usuario  # Devuelve el usuario si lo encuentra

        print("❌ Usuario no encontrado")  # Mensaje de error si no se encuentra
        raise Exception("Usuario no encontrado")


    def login(self):
        from Screens.HomeScreen import HomeScreen
        email = self.emailText.toPlainText()
        password = self.passwordText.toPlainText()

        
        auth.sign_in_with_email_and_password(email, password)  
        currentUser = self.getUsuario(email, password)
        print(f"Usuario logueado: {currentUser.email}")

        # Cambia a la pantalla de inicio
        homeScreen = HomeScreen(self.stacked_widget, currentUser)
        self.stacked_widget.addWidget(homeScreen)
        self.stacked_widget.setCurrentWidget(homeScreen)
        

    def register(self):
        email = self.emailText.toPlainText()
        password = self.passwordText.toPlainText()
        usuarioRepo = self.UsuarioRepo()
        try:
            auth.create_user_with_email_and_password(email, password)
            usuarioRepo.addUsuario(self.Usuario("",password, email, [], []))
        except:
            QErrorMessage(self).showMessage("Usuario ya registrado")

# -*- coding: utf-8 -*-

# prueba@gmail.com
# passwordPrueba

import sys
from PyQt6.QtWidgets import QApplication, QStackedWidget
from Model.Usuario import Usuario
from Repository.usuarioRepo import UsuarioRepo




if __name__ == '__main__':

    from Screens.LoginScreen import LoginScreen
    app = QApplication(sys.argv)

    # Crear el QStackedWidget
    stacked_widget = QStackedWidget()
    loginScreen = LoginScreen(stacked_widget)

    # Iniciar en la pantalla de Login
    stacked_widget.addWidget(loginScreen)
    stacked_widget.setCurrentIndex(0)
    stacked_widget.show()

    app.exec()

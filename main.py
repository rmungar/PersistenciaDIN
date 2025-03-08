# -*- coding: utf-8 -*-

# prueba@gmail.com
# passwordPrueba
import os
import sys
from PyQt6.QtWidgets import QApplication, QStackedWidget
from PyQt6.QtGui import QIcon
import ctypes

if __name__ == '__main__':

    from Screens.LoginScreen import LoginScreen
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon(f"{os.getcwd()}/_internal/Resources/LogoAnigiri.ico"))
    myappid = 'Anigiri.2dam'
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
    # Crear el QStackedWidget
    stacked_widget = QStackedWidget()
    loginScreen = LoginScreen(stacked_widget)

    # Iniciar en la pantalla de Login
    stacked_widget.addWidget(loginScreen)
    stacked_widget.setCurrentIndex(0)
    stacked_widget.show()

    app.exec()

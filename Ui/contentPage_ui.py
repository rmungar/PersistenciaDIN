# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'contentPage.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(903, 821)
        MainWindow.setMinimumSize(QSize(903, 821))
        MainWindow.setMaximumSize(QSize(903, 821))
        MainWindow.setStyleSheet(u"background-color: rgb(21, 32, 60);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_5, 17, 1, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_4, 18, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 0, 3, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_3, 19, 1, 1, 1)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_6, 16, 1, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 3, 1, 1, 1)

        self.mangaButton = QPushButton(self.centralwidget)
        self.mangaButton.setObjectName(u"mangaButton")
        self.mangaButton.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.mangaButton, 6, 1, 1, 1)

        self.animeButton = QPushButton(self.centralwidget)
        self.animeButton.setObjectName(u"animeButton")
        self.animeButton.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.animeButton, 5, 1, 1, 1)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"")
        self.gridLayout_2 = QGridLayout(self.widget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.placeholderimage = QLabel(self.widget)
        self.placeholderimage.setObjectName(u"placeholderimage")
        self.placeholderimage.setMinimumSize(QSize(242, 305))
        self.placeholderimage.setMaximumSize(QSize(242, 305))
        self.placeholderimage.setStyleSheet(u"background-color: rgb(170, 170, 170);")

        self.gridLayout_2.addWidget(self.placeholderimage, 1, 1, 1, 1)

        self.comments = QLabel(self.widget)
        self.comments.setObjectName(u"comments")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comments.sizePolicy().hasHeightForWidth())
        self.comments.setSizePolicy(sizePolicy)
        self.comments.setMinimumSize(QSize(242, 305))
        self.comments.setMaximumSize(QSize(242, 305))
        self.comments.setStyleSheet(u"background-color:rgb(227, 227, 227);\n"
"color: rgb(0, 0, 0);\n"
"font: 14pt \"Segoe UI Symbol\";")
        self.comments.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.gridLayout_2.addWidget(self.comments, 2, 0, 1, 1)

        self.synopsis = QLabel(self.widget)
        self.synopsis.setObjectName(u"synopsis")
        sizePolicy.setHeightForWidth(self.synopsis.sizePolicy().hasHeightForWidth())
        self.synopsis.setSizePolicy(sizePolicy)
        self.synopsis.setMinimumSize(QSize(242, 305))
        self.synopsis.setMaximumSize(QSize(242, 305))
        self.synopsis.setStyleSheet(u"background-color:rgb(227, 227, 227);\n"
"color: rgb(0, 0, 0);\n"
"font: 14pt \"Segoe UI Symbol\";")
        self.synopsis.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.synopsis.setWordWrap(True)
        self.synopsis.setMargin(10)

        self.gridLayout_2.addWidget(self.synopsis, 1, 0, 1, 1)

        self.descripcion = QLabel(self.widget)
        self.descripcion.setObjectName(u"descripcion")
        sizePolicy.setHeightForWidth(self.descripcion.sizePolicy().hasHeightForWidth())
        self.descripcion.setSizePolicy(sizePolicy)
        self.descripcion.setMinimumSize(QSize(242, 305))
        self.descripcion.setMaximumSize(QSize(242, 305))
        self.descripcion.setStyleSheet(u"background-color:rgb(227, 227, 227);\n"
"color: rgb(0, 0, 0);\n"
"font: 14pt \"Segoe UI Symbol\";")
        self.descripcion.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.descripcion.setWordWrap(True)
        self.descripcion.setMargin(10)

        self.gridLayout_2.addWidget(self.descripcion, 2, 1, 1, 1)

        self.title = QLabel(self.widget)
        self.title.setObjectName(u"title")
        self.title.setMinimumSize(QSize(0, 0))
        self.title.setMaximumSize(QSize(903, 100))
        self.title.setStyleSheet(u"background-color: rgb(0, 85, 127);\n"
"font: 700 26pt \"Trebuchet MS\";")
        self.title.setWordWrap(True)

        self.gridLayout_2.addWidget(self.title, 0, 0, 1, 3)

        self.ranking = QLabel(self.widget)
        self.ranking.setObjectName(u"ranking")
        self.ranking.setMinimumSize(QSize(243, 616))
        self.ranking.setMaximumSize(QSize(243, 616))
        self.ranking.setStyleSheet(u"background-color:rgb(227, 227, 227);\n"
"color: rgb(0, 0, 0);\n"
"font: 14pt \"Segoe UI Symbol\";")
        self.ranking.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.ranking.setWordWrap(True)
        self.ranking.setMargin(10)

        self.gridLayout_2.addWidget(self.ranking, 1, 2, 2, 1)


        self.gridLayout_3.addWidget(self.widget, 0, 0, 1, 1)


        self.gridLayout.addLayout(self.gridLayout_3, 3, 2, 18, 3)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 20, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 1, 3, 1, 1)

        self.userButton = QPushButton(self.centralwidget)
        self.userButton.setObjectName(u"userButton")
        self.userButton.setMinimumSize(QSize(55, 55))
        self.userButton.setStyleSheet(u"QPushButton {\n"
"    border-radius: 25px; \n"
"    background-color: rgb(20, 90, 182); \n"
"    color: white; \n"
"    border: none; \n"
"    font-size: 14px;\n"
"}")
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.UserAvailable))
        self.userButton.setIcon(icon)
        self.userButton.setIconSize(QSize(30, 30))

        self.gridLayout.addWidget(self.userButton, 0, 4, 2, 1)

        self.mangakaButton = QPushButton(self.centralwidget)
        self.mangakaButton.setObjectName(u"mangakaButton")
        self.mangakaButton.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.mangakaButton, 8, 1, 1, 1)

        self.estudioButton = QPushButton(self.centralwidget)
        self.estudioButton.setObjectName(u"estudioButton")
        self.estudioButton.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.estudioButton, 7, 1, 1, 1)

        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setStyleSheet(u"QPushButton {\n"
"    background: transparent; \n"
"    border: none;\n"
"    color: white; \n"
"	font: 24pt \"Pinky Show\";\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: transparent; \n"
"}")

        self.gridLayout.addWidget(self.pushButton, 0, 1, 2, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.mangaButton.setText(QCoreApplication.translate("MainWindow", u"Mangas", None))
        self.animeButton.setText(QCoreApplication.translate("MainWindow", u"Animes", None))
        self.placeholderimage.setText("")
        self.comments.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"justify\"><br/></p></body></html>", None))
        self.synopsis.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"justify\"><br/></p></body></html>", None))
        self.descripcion.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"justify\"><br/></p></body></html>", None))
        self.title.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
        self.ranking.setText("")
        self.userButton.setText("")
        self.mangakaButton.setText(QCoreApplication.translate("MainWindow", u"Mangakas", None))
        self.estudioButton.setText(QCoreApplication.translate("MainWindow", u"Estudios", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"ANIGIRI", None))
    # retranslateUi


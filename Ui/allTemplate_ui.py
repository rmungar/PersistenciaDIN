# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'allTemplate.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1216, 868)
        MainWindow.setStyleSheet(u"background-color: #15203c")
        self.contentwidget = QWidget(MainWindow)
        self.contentwidget.setObjectName(u"contentwidget")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.contentwidget.sizePolicy().hasHeightForWidth())
        self.contentwidget.setSizePolicy(sizePolicy)
        self.gridLayout_4 = QGridLayout(self.contentwidget)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridContenido = QGridLayout()
        self.gridContenido.setObjectName(u"gridContenido")

        self.gridLayout_4.addLayout(self.gridContenido, 2, 2, 1, 1)

        self.gridEndpoints = QGridLayout()
        self.gridEndpoints.setObjectName(u"gridEndpoints")
        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridEndpoints.addItem(self.verticalSpacer_4, 7, 0, 1, 1)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridEndpoints.addItem(self.horizontalSpacer_7, 5, 1, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridEndpoints.addItem(self.horizontalSpacer_5, 5, 3, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridEndpoints.addItem(self.horizontalSpacer_4, 5, 5, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridEndpoints.addItem(self.verticalSpacer_2, 0, 0, 1, 1)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridEndpoints.addItem(self.horizontalSpacer_6, 5, 6, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridEndpoints.addItem(self.horizontalSpacer_3, 5, 7, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridEndpoints.addItem(self.verticalSpacer_3, 8, 0, 1, 1)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridEndpoints.addItem(self.verticalSpacer_6, 5, 0, 1, 1)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridEndpoints.addItem(self.horizontalSpacer_8, 5, 4, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridEndpoints.addItem(self.verticalSpacer, 9, 0, 1, 1)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridEndpoints.addItem(self.verticalSpacer_5, 6, 0, 1, 1)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridEndpoints.addItem(self.horizontalSpacer_9, 5, 2, 1, 1)

        self.animeAPI = QPushButton(self.contentwidget)
        self.animeAPI.setObjectName(u"animeAPI")

        self.gridEndpoints.addWidget(self.animeAPI, 1, 0, 1, 4)

        self.mangaAPI = QPushButton(self.contentwidget)
        self.mangaAPI.setObjectName(u"mangaAPI")

        self.gridEndpoints.addWidget(self.mangaAPI, 2, 0, 1, 4)

        self.pushButton_4 = QPushButton(self.contentwidget)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.gridEndpoints.addWidget(self.pushButton_4, 3, 0, 1, 4)

        self.pushButton_3 = QPushButton(self.contentwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.gridEndpoints.addWidget(self.pushButton_3, 4, 0, 1, 4)


        self.gridLayout_4.addLayout(self.gridEndpoints, 2, 0, 1, 2)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer, 1, 2, 1, 1)

        self.pushButton = QPushButton(self.contentwidget)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout_4.addWidget(self.pushButton, 1, 0, 1, 1)

        MainWindow.setCentralWidget(self.contentwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.animeAPI.setText(QCoreApplication.translate("MainWindow", u"Animes", None))
        self.mangaAPI.setText(QCoreApplication.translate("MainWindow", u"Mangas", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Estudios", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Mangakas", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Anigiri", None))
    # retranslateUi


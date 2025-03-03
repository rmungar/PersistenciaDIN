# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'homePage.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(785, 693)
        MainWindow.setStyleSheet(u"background-color: rgb(21, 32, 60);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_5, 17, 1, 1, 1)

        self.pushButton_4 = QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.gridLayout.addWidget(self.pushButton_4, 7, 1, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_4, 18, 1, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 20, 1, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_3, 19, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 1, 3, 1, 1)

        self.mangaAPI = QPushButton(self.centralwidget)
        self.mangaAPI.setObjectName(u"mangaAPI")

        self.gridLayout.addWidget(self.mangaAPI, 6, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 0, 3, 1, 1)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_6, 16, 1, 1, 1)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"font: 24pt \"Pinky Show\";")

        self.gridLayout.addWidget(self.label, 0, 1, 2, 1)

        self.animeAPI = QPushButton(self.centralwidget)
        self.animeAPI.setObjectName(u"animeAPI")

        self.gridLayout.addWidget(self.animeAPI, 5, 1, 1, 1)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"background-color: rgb(127, 127, 127);")
        self.gridLayout_2 = QGridLayout(self.widget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.label_3, 4, 0, 1, 1)

        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)

        self.line_4 = QFrame(self.widget)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.Shape.HLine)
        self.line_4.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_2.addWidget(self.line_4, 1, 0, 1, 1)

        self.line = QFrame(self.widget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_2.addWidget(self.line, 5, 0, 1, 1)

        self.widget_2 = QWidget(self.widget)
        self.widget_2.setObjectName(u"widget_2")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy)
        self.widget_2.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.gridLayout_5 = QGridLayout(self.widget_2)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.pushButton_31 = QPushButton(self.widget_2)
        self.pushButton_31.setObjectName(u"pushButton_31")
        self.pushButton_31.setStyleSheet(u"background-color: rgb(108, 199, 255);")

        self.gridLayout_5.addWidget(self.pushButton_31, 0, 0, 1, 1)

        self.pushButton_42 = QPushButton(self.widget_2)
        self.pushButton_42.setObjectName(u"pushButton_42")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pushButton_42.sizePolicy().hasHeightForWidth())
        self.pushButton_42.setSizePolicy(sizePolicy1)
        self.pushButton_42.setStyleSheet(u"background-color: rgb(108, 199, 255);")

        self.gridLayout_5.addWidget(self.pushButton_42, 0, 1, 1, 1)

        self.pushButton_33 = QPushButton(self.widget_2)
        self.pushButton_33.setObjectName(u"pushButton_33")
        self.pushButton_33.setStyleSheet(u"background-color: rgb(108, 199, 255);")

        self.gridLayout_5.addWidget(self.pushButton_33, 0, 2, 1, 1)


        self.gridLayout_2.addWidget(self.widget_2, 6, 0, 1, 1)

        self.line_3 = QFrame(self.widget)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.Shape.HLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_2.addWidget(self.line_3, 7, 0, 1, 1)

        self.widget1 = QWidget(self.widget)
        self.widget1.setObjectName(u"widget1")
        sizePolicy.setHeightForWidth(self.widget1.sizePolicy().hasHeightForWidth())
        self.widget1.setSizePolicy(sizePolicy)
        self.widget1.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.gridLayout_4 = QGridLayout(self.widget1)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.pushButton_37 = QPushButton(self.widget1)
        self.pushButton_37.setObjectName(u"pushButton_37")
        self.pushButton_37.setStyleSheet(u"background-color: rgb(108, 199, 255);")

        self.gridLayout_4.addWidget(self.pushButton_37, 0, 0, 1, 1)

        self.pushButton_38 = QPushButton(self.widget1)
        self.pushButton_38.setObjectName(u"pushButton_38")
        sizePolicy1.setHeightForWidth(self.pushButton_38.sizePolicy().hasHeightForWidth())
        self.pushButton_38.setSizePolicy(sizePolicy1)
        self.pushButton_38.setStyleSheet(u"background-color: rgb(108, 199, 255);")

        self.gridLayout_4.addWidget(self.pushButton_38, 0, 1, 1, 1)

        self.pushButton_39 = QPushButton(self.widget1)
        self.pushButton_39.setObjectName(u"pushButton_39")
        self.pushButton_39.setStyleSheet(u"background-color: rgb(108, 199, 255);")

        self.gridLayout_4.addWidget(self.pushButton_39, 0, 2, 1, 1)


        self.gridLayout_2.addWidget(self.widget1, 2, 0, 1, 1)


        self.gridLayout_3.addWidget(self.widget, 0, 0, 1, 1)


        self.gridLayout.addLayout(self.gridLayout_3, 3, 2, 18, 2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 3, 1, 1, 1)

        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.gridLayout.addWidget(self.pushButton_3, 8, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Estudios", None))
        self.mangaAPI.setText(QCoreApplication.translate("MainWindow", u"Mangas", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Anigiri</p></body></html>", None))
        self.animeAPI.setText(QCoreApplication.translate("MainWindow", u"Animes", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt;\">Mangas</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt;\">Animes</span></p></body></html>", None))
        self.pushButton_31.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_42.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_33.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_37.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_38.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_39.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Mangakas", None))
    # retranslateUi


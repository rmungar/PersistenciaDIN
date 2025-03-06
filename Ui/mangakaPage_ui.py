# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mangakaPage.ui'
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


        self.gridLayout_4.addLayout(self.gridEndpoints, 1, 0, 1, 2)

        self.gridContenido = QGridLayout()
        self.gridContenido.setObjectName(u"gridContenido")
        self.placeholderimage = QLabel(self.contentwidget)
        self.placeholderimage.setObjectName(u"placeholderimage")
        self.placeholderimage.setStyleSheet(u"background-color: #cccac6")
        self.placeholderimage.setPixmap(QPixmap(u"../../../../kynrh/Downloads/frierenMangaka.png"))
        self.placeholderimage.setScaledContents(True)

        self.gridContenido.addWidget(self.placeholderimage, 1, 1, 1, 1)

        self.title = QLabel(self.contentwidget)
        self.title.setObjectName(u"title")
        self.title.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.title.sizePolicy().hasHeightForWidth())
        self.title.setSizePolicy(sizePolicy1)
        self.title.setFocusPolicy(Qt.FocusPolicy.TabFocus)
        self.title.setStyleSheet(u"background-color: #cccac6")

        self.gridContenido.addWidget(self.title, 0, 0, 1, 3)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridContenido.addItem(self.horizontalSpacer_2, 1, 3, 1, 1)

        self.information = QLabel(self.contentwidget)
        self.information.setObjectName(u"information")
        self.information.setStyleSheet(u"background-color: #cccac6")

        self.gridContenido.addWidget(self.information, 2, 1, 1, 1)

        self.biographyvalue = QLabel(self.contentwidget)
        self.biographyvalue.setObjectName(u"biographyvalue")
        self.biographyvalue.setStyleSheet(u"background-color: #cccac6")

        self.gridContenido.addWidget(self.biographyvalue, 1, 0, 1, 1)

        self.mangas = QLabel(self.contentwidget)
        self.mangas.setObjectName(u"mangas")
        self.mangas.setStyleSheet(u"background-color: #cccac6")

        self.gridContenido.addWidget(self.mangas, 2, 0, 1, 1)

        self.gridContenido.setRowStretch(0, 1)

        self.gridLayout_4.addLayout(self.gridContenido, 1, 2, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer, 0, 2, 1, 1)

        self.pushButton = QPushButton(self.contentwidget)
        self.pushButton.setObjectName(u"pushButton")
        font = QFont()
        font.setFamilies([u"Pinky Show"])
        font.setPointSize(24)
        self.pushButton.setFont(font)

        self.gridLayout_4.addWidget(self.pushButton, 0, 0, 1, 2)

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
        self.placeholderimage.setText("")
        self.title.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt; font-weight:700;\">MANGAKA: BEYOND MANGA'S END</span></p></body></html>", None))
        self.information.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:700;\">Information</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"post-title-t3_li8zpf\"></a><span style=\" font-family:'-apple-system','BlinkMacSystemFont','Segoe UI','Roboto','Helvetica Neue','Arial','Apple Color Emoji','Segoe UI Emoji','Segoe UI Symbol','sans"
                        "-serif'; font-size:xx-large; font-weight:600; color:#000000;\">\u00af</span><span style=\" font-family:'-apple-system','BlinkMacSystemFont','Segoe UI','Roboto','Helvetica Neue','Arial','Apple Color Emoji','Segoe UI Emoji','Segoe UI Symbol','sans-serif'; font-size:xx-large; font-weight:600; color:#000000;\">\u00af\u00af\u00af\u00af\u00af\u00af\u00af\u00af\u00af\u00af\u00af</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.biographyvalue.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; font-weight:700;\">Biography</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"post-title-t3_li8zpf\"></a><span style=\" font-family:'-apple-system','BlinkMacSystemFont','Segoe UI','Roboto','Helvetica Neue','Arial','Apple Color Emoji','Segoe"
                        " UI Emoji','Segoe UI Symbol','sans-serif'; font-size:xx-large; font-weight:600; color:#000000;\">\u00af</span><span style=\" font-family:'-apple-system','BlinkMacSystemFont','Segoe UI','Roboto','Helvetica Neue','Arial','Apple Color Emoji','Segoe UI Emoji','Segoe UI Symbol','sans-serif'; font-size:xx-large; font-weight:600; color:#000000;\">\u00af\u00af\u00af\u00af\u00af\u00af\u00af\u00af\u00af\u00af\u00af\u00af</span><a name=\"post-title-t3_li8zpf\"></a><span style=\" font-family:'-apple-system','BlinkMacSystemFont','Segoe UI','Roboto','Helvetica Neue','Arial','Apple Color Emoji','Segoe UI Emoji','Segoe UI Symbol','sans-serif'; font-size:xx-large; font-weight:600; color:#000000;\">\u00af</span><span style=\" font-family:'-apple-system','BlinkMacSystemFont','Segoe UI','Roboto','Helvetica Neue','Arial','Apple Color Emoji','Segoe UI Emoji','Segoe UI Symbol','sans-serif'; font-size:xx-large; font-weight:600; color:#000000;\">\u00af\u00af\u00af\u00af\u00af\u00af\u00af\u00af\u00af\u00af</span></p>\n"
"<p align=\"jus"
                        "tify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:24pt;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"> text look at me I'm such a good anime oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo oooooooooooooooo oooooooo oooooooo oooooooooooo oooooooooooooooooooooooooooooooo oooooooooooo oooooooooooooooooooo oooooooooooo</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.mangas.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; font-weight:700;\">Manga</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"post-title-t3_li8zpf\"></a><span style=\" font-family:'-apple-system','BlinkMacSystemFont','Segoe UI','Roboto','Helvetica Neue','Arial','Apple Color Emoji','Segoe UI Emoji','Segoe UI Symbol','sans-serif"
                        "'; font-size:xx-large; font-weight:600; color:#000000;\">\u00af</span><span style=\" font-family:'-apple-system','BlinkMacSystemFont','Segoe UI','Roboto','Helvetica Neue','Arial','Apple Color Emoji','Segoe UI Emoji','Segoe UI Symbol','sans-serif'; font-size:xx-large; font-weight:600; color:#000000;\">\u00af\u00af\u00af\u00af\u00af\u00af\u00af\u00af\u00af\u00af\u00af\u00af</span><a name=\"post-title-t3_li8zpf\"></a><span style=\" font-family:'-apple-system','BlinkMacSystemFont','Segoe UI','Roboto','Helvetica Neue','Arial','Apple Color Emoji','Segoe UI Emoji','Segoe UI Symbol','sans-serif'; font-size:xx-large; font-weight:600; color:#000000;\">\u00af</span><span style=\" font-family:'-apple-system','BlinkMacSystemFont','Segoe UI','Roboto','Helvetica Neue','Arial','Apple Color Emoji','Segoe UI Emoji','Segoe UI Symbol','sans-serif'; font-size:xx-large; font-weight:600; color:#000000;\">\u00af\u00af\u00af\u00af\u00af\u00af\u00af\u00af\u00af\u00af</span></p></body></html>", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"ANIGIRI", None))
    # retranslateUi


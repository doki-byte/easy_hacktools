'''
Author: 沐寒
Date: 2023-03-13 20:54:09
LastEditors: 最后编辑
LastEditTime: 2023-03-18 12:02:09
url: https://www.anquanclub.com
'''
# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Hunter.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
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
from PySide6.QtWidgets import (QApplication, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)
import UI.rc_pic

class Ui_Hunter(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(538, 140)
        icon = QIcon()
        icon.addFile(u":/icon/img/favicon.ico", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.hunter_key = QLineEdit(self.centralwidget)
        self.hunter_key.setObjectName(u"hunter_key")
        self.hunter_key.setMinimumSize(QSize(0, 30))
        self.hunter_key.setStyleSheet(u"border : 1px solid;\n"
"border-color : rgb(0, 170, 255);\n"
"")

        self.verticalLayout.addWidget(self.hunter_key)

        self.hunter_cookie = QLineEdit(self.centralwidget)
        self.hunter_cookie.setObjectName(u"hunter_cookie")
        self.hunter_cookie.setMinimumSize(QSize(0, 30))
        self.hunter_cookie.setStyleSheet(u"border : 1px solid;\n"
"border-color : rgb(0, 170, 255);\n"
"")

        self.verticalLayout.addWidget(self.hunter_cookie)

        self.hunter_save = QPushButton(self.centralwidget)
        self.hunter_save.setObjectName(u"hunter_save")
        self.hunter_save.setStyleSheet(u"font-size:18px;\n"
"background-color: rgb(108, 118, 255);\n"
"color: rgb(255, 255, 255);")

        self.verticalLayout.addWidget(self.hunter_save)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Hunter\u914d\u7f6e", None))
        self.hunter_key.setText("")
        self.hunter_key.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u586b\u5199hunter\u7684api-key", None))
        self.hunter_cookie.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u586b\u5199\u7ecf\u8fc7base64\u52a0\u5bc6\u540e\u7684hunter.qianxin.com\u7684cookie (\u6ce8\u610f\u53bb\u6389\u672b\u5c3e\u7684\u7b49\u53f7)", None))
        self.hunter_save.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58", None))
    # retranslateUi


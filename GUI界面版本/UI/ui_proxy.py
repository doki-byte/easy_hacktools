'''
Author: 沐寒
Date: 2023-03-15 16:59:47
LastEditors: 最后编辑
LastEditTime: 2023-03-18 12:02:07
url: https://www.anquanclub.com
'''
# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'proxy.ui'
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

class Ui_Proxy(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(367, 177)
        icon = QIcon()
        icon.addFile(u":/icon/img/favicon.ico", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.host = QLineEdit(self.centralwidget)
        self.host.setObjectName(u"host")
        self.host.setMinimumSize(QSize(0, 30))
        self.host.setStyleSheet(u"border : 1px solid;\n"
"border-color : rgb(0, 170, 255);\n"
"")

        self.verticalLayout.addWidget(self.host)

        self.port = QLineEdit(self.centralwidget)
        self.port.setObjectName(u"port")
        self.port.setMinimumSize(QSize(0, 30))
        self.port.setStyleSheet(u"border : 1px solid;\n"
"border-color : rgb(0, 170, 255);\n"
"")

        self.verticalLayout.addWidget(self.port)

        self.proxy_save = QPushButton(self.centralwidget)
        self.proxy_save.setObjectName(u"proxy_save")
        self.proxy_save.setStyleSheet(u"font-size:18px;\n"
"background-color: rgb(108, 118, 255);\n"
"color: rgb(255, 255, 255);")

        self.verticalLayout.addWidget(self.proxy_save)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u4ee3\u7406\u8bbe\u7f6e", None))
        self.host.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u4ee3\u7406\u4e3b\u673aip (eg:127.0.0.1)", None))
        self.port.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u4ee3\u7406\u7aef\u53e3port (eg:10808)", None))
        self.proxy_save.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58", None))
    # retranslateUi


'''
Author: 沐寒
Date: 2023-03-13 20:51:04
LastEditors: 最后编辑
LastEditTime: 2023-03-18 12:02:01
url: https://www.anquanclub.com
'''
# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Fofa.ui'
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

class Ui_Fofa(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(437, 202)
        icon = QIcon()
        icon.addFile(u":/icon/img/favicon.ico", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.fofa_email = QLineEdit(self.centralwidget)
        self.fofa_email.setObjectName(u"fofa_email")
        self.fofa_email.setMinimumSize(QSize(0, 30))
        self.fofa_email.setStyleSheet(u"border : 1px solid;\n"
"border-color : rgb(0, 170, 255);\n"
"")

        self.verticalLayout.addWidget(self.fofa_email)

        self.fofa_key = QLineEdit(self.centralwidget)
        self.fofa_key.setObjectName(u"fofa_key")
        self.fofa_key.setMinimumSize(QSize(0, 30))
        self.fofa_key.setStyleSheet(u"border : 1px solid;\n"
"border-color : rgb(0, 170, 255);\n"
"")

        self.verticalLayout.addWidget(self.fofa_key)

        self.fofa_save = QPushButton(self.centralwidget)
        self.fofa_save.setObjectName(u"fofa_save")
        self.fofa_save.setStyleSheet(u"font-size:18px;\n"
"background-color: rgb(108, 118, 255);\n"
"color: rgb(255, 255, 255);")

        self.verticalLayout.addWidget(self.fofa_save)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Fofa\u914d\u7f6e", None))
        self.fofa_email.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u586b\u6ce8\u518cfofa\u7684email", None))
        self.fofa_key.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u586bemail\u5bf9\u5e94\u7684key", None))
        self.fofa_save.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58", None))
    # retranslateUi


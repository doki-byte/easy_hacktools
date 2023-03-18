# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QGroupBox, QHBoxLayout,
    QLineEdit, QMainWindow, QMenu, QMenuBar,
    QPushButton, QSizePolicy, QSpacerItem, QTabWidget,
    QTextBrowser, QTextEdit, QToolBox, QVBoxLayout,
    QWidget)
import UI.rc_pic

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1624, 803)
        icon = QIcon()
        icon.addFile(u":/icon/img/favicon.ico", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.actionFofa = QAction(MainWindow)
        self.actionFofa.setObjectName(u"actionFofa")
        self.actionHunter = QAction(MainWindow)
        self.actionHunter.setObjectName(u"actionHunter")
        self.actionShodan = QAction(MainWindow)
        self.actionShodan.setObjectName(u"actionShodan")
        self.actionProxy = QAction(MainWindow)
        self.actionProxy.setObjectName(u"actionProxy")
        self.action_ClearUrl = QAction(MainWindow)
        self.action_ClearUrl.setObjectName(u"action_ClearUrl")
        self.action_About = QAction(MainWindow)
        self.action_About.setObjectName(u"action_About")
        self.action_Auther = QAction(MainWindow)
        self.action_Auther.setObjectName(u"action_Auther")
        self.action_Issea = QAction(MainWindow)
        self.action_Issea.setObjectName(u"action_Issea")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setMinimumSize(QSize(0, 0))
        self.tabWidget.setStyleSheet(u"")
        self.tabWidget.setTabShape(QTabWidget.Rounded)
        self.fofa = QWidget()
        self.fofa.setObjectName(u"fofa")
        self.fofa.setStyleSheet(u"")
        self.horizontalLayout = QHBoxLayout(self.fofa)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(5, 8, 5, 0)
        self.groupBox = QGroupBox(self.fofa)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setStyleSheet(u"QGroupBox\n"
"{\n"
"border : 2px solid;\n"
"border-color : rgb(223, 148, 255);\n"
"font  : 13px;\n"
"}")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(5, 20, 5, 0)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.Fofayufa = QLineEdit(self.groupBox)
        self.Fofayufa.setObjectName(u"Fofayufa")
        self.Fofayufa.setMinimumSize(QSize(0, 30))
        self.Fofayufa.setContextMenuPolicy(Qt.NoContextMenu)
        self.Fofayufa.setStyleSheet(u"border : 1px solid;\n"
"border-color : rgb(0, 170, 255);\n"
"")

        self.horizontalLayout_2.addWidget(self.Fofayufa)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.fofanumber = QLineEdit(self.groupBox)
        self.fofanumber.setObjectName(u"fofanumber")
        self.fofanumber.setMinimumSize(QSize(0, 30))
        self.fofanumber.setContextMenuPolicy(Qt.NoContextMenu)
        self.fofanumber.setStyleSheet(u"border : 1px solid;\n"
"border-color : rgb(0, 170, 255);\n"
"")

        self.horizontalLayout_2.addWidget(self.fofanumber)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

        self.fofaso = QPushButton(self.groupBox)
        self.fofaso.setObjectName(u"fofaso")
        self.fofaso.setMinimumSize(QSize(0, 30))
        self.fofaso.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.fofaso.setStyleSheet(u"font-size:18px;\n"
"background-color: rgb(255, 170, 0);\n"
"color: rgb(255, 255, 255);")

        self.horizontalLayout_2.addWidget(self.fofaso)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.horizontalLayout_2.setStretch(0, 4)
        self.horizontalLayout_2.setStretch(2, 3)
        self.horizontalLayout_2.setStretch(4, 2)

        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.fofatips = QTextBrowser(self.groupBox)
        self.fofatips.setObjectName(u"fofatips")
        self.fofatips.setContextMenuPolicy(Qt.NoContextMenu)

        self.verticalLayout_2.addWidget(self.fofatips)


        self.horizontalLayout.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.fofa)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setStyleSheet(u"QGroupBox\n"
"{\n"
"border : 2px solid;\n"
"border-color : rgb(223, 148, 255);\n"
"font  : 13px;\n"
"}")
        self.verticalLayout_3 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(5, 20, 5, 0)
        self.fofacankao = QTextBrowser(self.groupBox_2)
        self.fofacankao.setObjectName(u"fofacankao")
        self.fofacankao.setContextMenuPolicy(Qt.NoContextMenu)

        self.verticalLayout_3.addWidget(self.fofacankao)


        self.horizontalLayout.addWidget(self.groupBox_2)

        self.horizontalLayout.setStretch(0, 3)
        self.horizontalLayout.setStretch(1, 2)
        self.tabWidget.addTab(self.fofa, "")
        self.Hunter = QWidget()
        self.Hunter.setObjectName(u"Hunter")
        self.horizontalLayout_14 = QHBoxLayout(self.Hunter)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.groupBox_9 = QGroupBox(self.Hunter)
        self.groupBox_9.setObjectName(u"groupBox_9")
        self.groupBox_9.setStyleSheet(u"QGroupBox\n"
"{\n"
"border : 2px solid;\n"
"border-color : rgb(255, 170, 127);\n"
"font  : 13px;\n"
"}")
        self.verticalLayout_14 = QVBoxLayout(self.groupBox_9)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(5, 20, 5, 0)
        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.hunter_yufa = QLineEdit(self.groupBox_9)
        self.hunter_yufa.setObjectName(u"hunter_yufa")
        self.hunter_yufa.setMinimumSize(QSize(0, 30))
        self.hunter_yufa.setContextMenuPolicy(Qt.NoContextMenu)
        self.hunter_yufa.setStyleSheet(u"border : 1px solid;\n"
"border-color : rgb(0, 170, 255);\n"
"")

        self.horizontalLayout_15.addWidget(self.hunter_yufa)

        self.hunter_num = QLineEdit(self.groupBox_9)
        self.hunter_num.setObjectName(u"hunter_num")
        self.hunter_num.setMinimumSize(QSize(0, 30))
        self.hunter_num.setContextMenuPolicy(Qt.NoContextMenu)
        self.hunter_num.setStyleSheet(u"border : 1px solid;\n"
"border-color : rgb(0, 170, 255);\n"
"")

        self.horizontalLayout_15.addWidget(self.hunter_num)

        self.hunter_zichan = QLineEdit(self.groupBox_9)
        self.hunter_zichan.setObjectName(u"hunter_zichan")
        self.hunter_zichan.setMinimumSize(QSize(0, 30))
        self.hunter_zichan.setContextMenuPolicy(Qt.NoContextMenu)
        self.hunter_zichan.setStyleSheet(u"border : 1px solid;\n"
"border-color : rgb(0, 170, 255);\n"
"")

        self.horizontalLayout_15.addWidget(self.hunter_zichan)

        self.horizontalLayout_15.setStretch(0, 1)
        self.horizontalLayout_15.setStretch(1, 1)
        self.horizontalLayout_15.setStretch(2, 3)

        self.verticalLayout_13.addLayout(self.horizontalLayout_15)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.hunter_status = QLineEdit(self.groupBox_9)
        self.hunter_status.setObjectName(u"hunter_status")
        self.hunter_status.setMinimumSize(QSize(0, 30))
        self.hunter_status.setContextMenuPolicy(Qt.NoContextMenu)
        self.hunter_status.setStyleSheet(u"border : 1px solid;\n"
"border-color : rgb(0, 170, 255);\n"
"")

        self.horizontalLayout_16.addWidget(self.hunter_status)

        self.hunter_start_time = QLineEdit(self.groupBox_9)
        self.hunter_start_time.setObjectName(u"hunter_start_time")
        self.hunter_start_time.setMinimumSize(QSize(0, 30))
        self.hunter_start_time.setContextMenuPolicy(Qt.NoContextMenu)
        self.hunter_start_time.setStyleSheet(u"border : 1px solid;\n"
"border-color : rgb(0, 170, 255);\n"
"")

        self.horizontalLayout_16.addWidget(self.hunter_start_time)

        self.hunter_end_time = QLineEdit(self.groupBox_9)
        self.hunter_end_time.setObjectName(u"hunter_end_time")
        self.hunter_end_time.setMinimumSize(QSize(0, 30))
        self.hunter_end_time.setContextMenuPolicy(Qt.NoContextMenu)
        self.hunter_end_time.setStyleSheet(u"border : 1px solid;\n"
"border-color : rgb(0, 170, 255);\n"
"")

        self.horizontalLayout_16.addWidget(self.hunter_end_time)

        self.horizontalSpacer_47 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_47)

        self.hunterso = QPushButton(self.groupBox_9)
        self.hunterso.setObjectName(u"hunterso")
        self.hunterso.setMinimumSize(QSize(0, 30))
        self.hunterso.setStyleSheet(u"font-size:18px;\n"
"background-color: rgb(170, 170, 255);\n"
"color: rgb(255, 255, 255);\n"
"")

        self.horizontalLayout_16.addWidget(self.hunterso)

        self.horizontalLayout_16.setStretch(0, 1)
        self.horizontalLayout_16.setStretch(1, 1)
        self.horizontalLayout_16.setStretch(2, 1)
        self.horizontalLayout_16.setStretch(4, 1)

        self.verticalLayout_13.addLayout(self.horizontalLayout_16)

        self.huntertips = QTextBrowser(self.groupBox_9)
        self.huntertips.setObjectName(u"huntertips")
        self.huntertips.setContextMenuPolicy(Qt.NoContextMenu)

        self.verticalLayout_13.addWidget(self.huntertips)

        self.groupBox_11 = QGroupBox(self.groupBox_9)
        self.groupBox_11.setObjectName(u"groupBox_11")
        self.groupBox_11.setStyleSheet(u"QGroupBox\n"
"{\n"
"border : 2px solid;\n"
"border-color : rgb(248, 157, 255);\n"
"font  : 13px;\n"
"}")
        self.textBrowser_2 = QTextBrowser(self.groupBox_11)
        self.textBrowser_2.setObjectName(u"textBrowser_2")
        self.textBrowser_2.setGeometry(QRect(180, 40, 256, 192))

        self.verticalLayout_13.addWidget(self.groupBox_11)


        self.verticalLayout_14.addLayout(self.verticalLayout_13)

        self.hunter_jifentips = QTextBrowser(self.groupBox_9)
        self.hunter_jifentips.setObjectName(u"hunter_jifentips")
        self.hunter_jifentips.setContextMenuPolicy(Qt.NoContextMenu)

        self.verticalLayout_14.addWidget(self.hunter_jifentips)

        self.verticalLayout_14.setStretch(0, 2)
        self.verticalLayout_14.setStretch(1, 1)

        self.horizontalLayout_14.addWidget(self.groupBox_9)

        self.groupBox_10 = QGroupBox(self.Hunter)
        self.groupBox_10.setObjectName(u"groupBox_10")
        self.groupBox_10.setStyleSheet(u"QGroupBox\n"
"{\n"
"border : 2px solid;\n"
"border-color : rgb(1, 81, 255);\n"
"font  : 13px;\n"
"}")
        self.horizontalLayout_17 = QHBoxLayout(self.groupBox_10)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(5, 20, 5, 0)
        self.HunteryufaLine = QTextBrowser(self.groupBox_10)
        self.HunteryufaLine.setObjectName(u"HunteryufaLine")
        self.HunteryufaLine.setContextMenuPolicy(Qt.NoContextMenu)

        self.horizontalLayout_17.addWidget(self.HunteryufaLine)


        self.horizontalLayout_14.addWidget(self.groupBox_10)

        self.horizontalLayout_14.setStretch(0, 4)
        self.horizontalLayout_14.setStretch(1, 1)
        self.tabWidget.addTab(self.Hunter, "")
        self.Shodan = QWidget()
        self.Shodan.setObjectName(u"Shodan")
        self.horizontalLayout_5 = QHBoxLayout(self.Shodan)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(5, 8, 5, 0)
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.groupBox_3 = QGroupBox(self.Shodan)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setStyleSheet(u"QGroupBox\n"
"{\n"
"border : 2px solid;\n"
"border-color : rgb(10, 210, 255);\n"
"font  : 13px;\n"
"}")
        self.verticalLayout_4 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(5, 20, 5, 0)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.Shodanyufa = QLineEdit(self.groupBox_3)
        self.Shodanyufa.setObjectName(u"Shodanyufa")
        self.Shodanyufa.setMinimumSize(QSize(0, 30))
        self.Shodanyufa.setContextMenuPolicy(Qt.NoContextMenu)
        self.Shodanyufa.setStyleSheet(u"border : 1px solid;\n"
"border-color : rgb(0, 170, 255);\n"
"")

        self.horizontalLayout_3.addWidget(self.Shodanyufa)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_4)

        self.Shodannumber = QLineEdit(self.groupBox_3)
        self.Shodannumber.setObjectName(u"Shodannumber")
        self.Shodannumber.setMinimumSize(QSize(0, 30))
        self.Shodannumber.setContextMenuPolicy(Qt.NoContextMenu)
        self.Shodannumber.setStyleSheet(u"border : 1px solid;\n"
"border-color : rgb(0, 170, 255);\n"
"")

        self.horizontalLayout_3.addWidget(self.Shodannumber)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_5)

        self.Shodanso = QPushButton(self.groupBox_3)
        self.Shodanso.setObjectName(u"Shodanso")
        self.Shodanso.setMinimumSize(QSize(0, 30))
        self.Shodanso.setStyleSheet(u"font-size:18px;\n"
"background-color: rgb(255, 170, 0);\n"
"color: rgb(255, 255, 255);")

        self.horizontalLayout_3.addWidget(self.Shodanso)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_6)

        self.horizontalLayout_3.setStretch(0, 4)
        self.horizontalLayout_3.setStretch(2, 3)
        self.horizontalLayout_3.setStretch(4, 2)

        self.verticalLayout_4.addLayout(self.horizontalLayout_3)

        self.Shodantips = QTextBrowser(self.groupBox_3)
        self.Shodantips.setObjectName(u"Shodantips")
        self.Shodantips.setContextMenuPolicy(Qt.NoContextMenu)

        self.verticalLayout_4.addWidget(self.Shodantips)


        self.horizontalLayout_4.addWidget(self.groupBox_3)

        self.groupBox_4 = QGroupBox(self.Shodan)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setStyleSheet(u"QGroupBox\n"
"{\n"
"border : 2px solid;\n"
"border-color : rgb(223, 148, 255);\n"
"font  : 13px;\n"
"}")
        self.verticalLayout_5 = QVBoxLayout(self.groupBox_4)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(5, 20, 5, 0)
        self.Shodancankao = QTextBrowser(self.groupBox_4)
        self.Shodancankao.setObjectName(u"Shodancankao")
        self.Shodancankao.setContextMenuPolicy(Qt.NoContextMenu)

        self.verticalLayout_5.addWidget(self.Shodancankao)


        self.horizontalLayout_4.addWidget(self.groupBox_4)

        self.horizontalLayout_4.setStretch(0, 3)
        self.horizontalLayout_4.setStretch(1, 2)

        self.horizontalLayout_5.addLayout(self.horizontalLayout_4)

        self.tabWidget.addTab(self.Shodan, "")
        self.addtoBase64 = QWidget()
        self.addtoBase64.setObjectName(u"addtoBase64")
        self.horizontalLayout_6 = QHBoxLayout(self.addtoBase64)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(5, 8, 5, 0)
        self.groupBox_5 = QGroupBox(self.addtoBase64)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setContextMenuPolicy(Qt.PreventContextMenu)
        self.groupBox_5.setStyleSheet(u"QGroupBox\n"
"{\n"
"border : 2px solid;\n"
"border-color : rgb(255, 99, 94);\n"
"font  : 13px;\n"
"}")
        self.verticalLayout_6 = QVBoxLayout(self.groupBox_5)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(5, 25, 5, 0)
        self.base64Line = QLineEdit(self.groupBox_5)
        self.base64Line.setObjectName(u"base64Line")
        self.base64Line.setMinimumSize(QSize(0, 40))
        self.base64Line.setContextMenuPolicy(Qt.NoContextMenu)
        self.base64Line.setStyleSheet(u"border : 1px solid;\n"
"border-color : rgb(0, 170, 255);\n"
"")

        self.verticalLayout_6.addWidget(self.base64Line)

        self.base64add = QPushButton(self.groupBox_5)
        self.base64add.setObjectName(u"base64add")
        self.base64add.setStyleSheet(u"font-size:18px;\n"
"background-color: rgb(108, 118, 255);\n"
"color: rgb(255, 255, 255);")

        self.verticalLayout_6.addWidget(self.base64add)

        self.base64tips = QTextBrowser(self.groupBox_5)
        self.base64tips.setObjectName(u"base64tips")
        self.base64tips.setContextMenuPolicy(Qt.NoContextMenu)

        self.verticalLayout_6.addWidget(self.base64tips)


        self.horizontalLayout_6.addWidget(self.groupBox_5)

        self.groupBox_6 = QGroupBox(self.addtoBase64)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.groupBox_6.setStyleSheet(u"QGroupBox\n"
"{\n"
"border : 2px solid;\n"
"border-color : rgb(85, 170, 255);\n"
"font  : 13px;\n"
"}")
        self.verticalLayout_7 = QVBoxLayout(self.groupBox_6)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(5, 25, 5, 0)
        self.base64demo = QTextBrowser(self.groupBox_6)
        self.base64demo.setObjectName(u"base64demo")
        self.base64demo.setContextMenuPolicy(Qt.NoContextMenu)

        self.verticalLayout_7.addWidget(self.base64demo)


        self.horizontalLayout_6.addWidget(self.groupBox_6)

        self.horizontalLayout_6.setStretch(0, 2)
        self.horizontalLayout_6.setStretch(1, 3)
        self.tabWidget.addTab(self.addtoBase64, "")
        self.Ndaytools = QWidget()
        self.Ndaytools.setObjectName(u"Ndaytools")
        self.verticalLayout_8 = QVBoxLayout(self.Ndaytools)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.toolBox = QToolBox(self.Ndaytools)
        self.toolBox.setObjectName(u"toolBox")
        self.toolBox.setStyleSheet(u"QToolBox\n"
"{\n"
"border : 2px solid;;\n"
"font-size:20px;\n"
"border-color: rgb(255, 170, 127);\n"
"}")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.page.setGeometry(QRect(0, 0, 1561, 638))
        self.page.setStyleSheet(u"")
        self.verticalLayout_12 = QVBoxLayout(self.page)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalSpacer_26 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_26, 0, 5, 1, 1)

        self.horizontalSpacer_25 = QSpacerItem(40, 40, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_25, 0, 1, 1, 1)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_8, 0, 3, 1, 1)

        self.pushButton_3 = QPushButton(self.page)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setStyleSheet(u"border : 2px solid;\n"
"border-color: rgb(255, 170, 0);\n"
"font-size:18px;\n"
"background-color: rgb(255, 170, 0);\n"
"color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.pushButton_3, 0, 4, 1, 1)

        self.pushButton = QPushButton(self.page)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setStyleSheet(u"border : 2px solid;\n"
"border-color: rgb(255, 170, 0);\n"
"font-size:18px;\n"
"background-color: rgb(255, 170, 0);\n"
"color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.pushButton, 0, 2, 1, 1)

        self.pushButton_4 = QPushButton(self.page)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setStyleSheet(u"border : 2px solid;\n"
"border-color: rgb(255, 170, 0);\n"
"font-size:18px;\n"
"background-color: rgb(255, 170, 0);\n"
"color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.pushButton_4, 0, 0, 1, 1)


        self.verticalLayout_11.addLayout(self.gridLayout)

        self.gridLayout_14 = QGridLayout()
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.horizontalSpacer_145 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_14.addItem(self.horizontalSpacer_145, 0, 5, 1, 1)

        self.pushButton_126 = QPushButton(self.page)
        self.pushButton_126.setObjectName(u"pushButton_126")
        self.pushButton_126.setStyleSheet(u"border : 2px solid;\n"
"border-color:rgb(85, 170, 0);\n"
"font-size:18px;\n"
"background-color: rgb(85, 170, 0);\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_14.addWidget(self.pushButton_126, 0, 4, 1, 1)

        self.pushButton_118 = QPushButton(self.page)
        self.pushButton_118.setObjectName(u"pushButton_118")
        self.pushButton_118.setStyleSheet(u"border : 2px solid;\n"
"border-color:rgb(85, 170, 0);\n"
"font-size:18px;\n"
"background-color: rgb(85, 170, 0);\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_14.addWidget(self.pushButton_118, 0, 0, 1, 1)

        self.horizontalSpacer_139 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_14.addItem(self.horizontalSpacer_139, 0, 3, 1, 1)

        self.horizontalSpacer_144 = QSpacerItem(40, 40, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_14.addItem(self.horizontalSpacer_144, 0, 1, 1, 1)

        self.pushButton_123 = QPushButton(self.page)
        self.pushButton_123.setObjectName(u"pushButton_123")
        self.pushButton_123.setStyleSheet(u"border : 2px solid;\n"
"border-color:rgb(85, 170, 0);\n"
"font-size:18px;\n"
"background-color: rgb(85, 170, 0);\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_14.addWidget(self.pushButton_123, 0, 2, 1, 1)


        self.verticalLayout_11.addLayout(self.gridLayout_14)

        self.gridLayout_17 = QGridLayout()
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.pushButton_150 = QPushButton(self.page)
        self.pushButton_150.setObjectName(u"pushButton_150")
        self.pushButton_150.setStyleSheet(u"border : 2px solid;\n"
"border-color: rgb(126, 255, 223);\n"
"font-size:18px;\n"
"background-color: rgb(126, 255, 223);\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_17.addWidget(self.pushButton_150, 0, 2, 1, 1)

        self.horizontalSpacer_166 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_17.addItem(self.horizontalSpacer_166, 0, 3, 1, 1)

        self.horizontalSpacer_172 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_17.addItem(self.horizontalSpacer_172, 0, 5, 1, 1)

        self.horizontalSpacer_171 = QSpacerItem(40, 40, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_17.addItem(self.horizontalSpacer_171, 0, 1, 1, 1)

        self.pushButton_153 = QPushButton(self.page)
        self.pushButton_153.setObjectName(u"pushButton_153")
        self.pushButton_153.setStyleSheet(u"border : 2px solid;\n"
"border-color: rgb(126, 255, 223);\n"
"font-size:18px;\n"
"background-color: rgb(126, 255, 223);\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_17.addWidget(self.pushButton_153, 0, 4, 1, 1)

        self.pushButton_145 = QPushButton(self.page)
        self.pushButton_145.setObjectName(u"pushButton_145")
        self.pushButton_145.setStyleSheet(u"border : 2px solid;\n"
"border-color: rgb(126, 255, 223);\n"
"font-size:18px;\n"
"background-color: rgb(126, 255, 223);\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_17.addWidget(self.pushButton_145, 0, 0, 1, 1)


        self.verticalLayout_11.addLayout(self.gridLayout_17)

        self.gridLayout_15 = QGridLayout()
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.pushButton_127 = QPushButton(self.page)
        self.pushButton_127.setObjectName(u"pushButton_127")
        self.pushButton_127.setStyleSheet(u"border : 2px solid;\n"
"border-color: rgb(255, 230, 38);\n"
"font-size:18px;\n"
"background-color: rgb(255, 230, 38);\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_15.addWidget(self.pushButton_127, 0, 0, 1, 1)

        self.horizontalSpacer_153 = QSpacerItem(40, 40, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_15.addItem(self.horizontalSpacer_153, 0, 1, 1, 1)

        self.pushButton_132 = QPushButton(self.page)
        self.pushButton_132.setObjectName(u"pushButton_132")
        self.pushButton_132.setStyleSheet(u"border : 2px solid;\n"
"border-color: rgb(255, 230, 38);\n"
"font-size:18px;\n"
"background-color: rgb(255, 230, 38);\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_15.addWidget(self.pushButton_132, 0, 2, 1, 1)

        self.pushButton_135 = QPushButton(self.page)
        self.pushButton_135.setObjectName(u"pushButton_135")
        self.pushButton_135.setStyleSheet(u"border : 2px solid;\n"
"border-color: rgb(255, 230, 38);\n"
"font-size:18px;\n"
"background-color: rgb(255, 230, 38);\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_15.addWidget(self.pushButton_135, 0, 4, 1, 1)

        self.horizontalSpacer_152 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_15.addItem(self.horizontalSpacer_152, 0, 5, 1, 1)

        self.horizontalSpacer_148 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_15.addItem(self.horizontalSpacer_148, 0, 3, 1, 1)


        self.verticalLayout_11.addLayout(self.gridLayout_15)

        self.gridLayout_23 = QGridLayout()
        self.gridLayout_23.setObjectName(u"gridLayout_23")
        self.pushButton_202 = QPushButton(self.page)
        self.pushButton_202.setObjectName(u"pushButton_202")
        self.pushButton_202.setStyleSheet(u"border : 2px solid;\n"
"border-color: rgb(223, 148, 255);\n"
"font-size:18px;\n"
"background-color: rgb(223, 148, 255);\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_23.addWidget(self.pushButton_202, 0, 10, 1, 1)

        self.horizontalSpacer_220 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_23.addItem(self.horizontalSpacer_220, 0, 9, 1, 1)

        self.horizontalSpacer_219 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_23.addItem(self.horizontalSpacer_219, 0, 5, 1, 1)

        self.horizontalSpacer_222 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_23.addItem(self.horizontalSpacer_222, 0, 3, 1, 1)

        self.pushButton_207 = QPushButton(self.page)
        self.pushButton_207.setObjectName(u"pushButton_207")
        self.pushButton_207.setStyleSheet(u"border : 2px solid;\n"
"border-color: rgb(223, 148, 255);\n"
"font-size:18px;\n"
"background-color: rgb(223, 148, 255);\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_23.addWidget(self.pushButton_207, 0, 2, 1, 1)

        self.pushButton_203 = QPushButton(self.page)
        self.pushButton_203.setObjectName(u"pushButton_203")
        self.pushButton_203.setStyleSheet(u"border : 2px solid;\n"
"border-color: rgb(223, 148, 255);\n"
"font-size:18px;\n"
"background-color: rgb(223, 148, 255);\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_23.addWidget(self.pushButton_203, 0, 8, 1, 1)

        self.pushButton_200 = QPushButton(self.page)
        self.pushButton_200.setObjectName(u"pushButton_200")
        self.pushButton_200.setStyleSheet(u"border : 2px solid;\n"
"border-color: rgb(223, 148, 255);\n"
"font-size:18px;\n"
"background-color: rgb(223, 148, 255);\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_23.addWidget(self.pushButton_200, 0, 6, 1, 1)

        self.horizontalSpacer_223 = QSpacerItem(40, 40, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_23.addItem(self.horizontalSpacer_223, 0, 1, 1, 1)

        self.pushButton_199 = QPushButton(self.page)
        self.pushButton_199.setObjectName(u"pushButton_199")
        self.pushButton_199.setStyleSheet(u"border : 2px solid;\n"
"border-color: rgb(223, 148, 255);\n"
"font-size:18px;\n"
"background-color: rgb(223, 148, 255);\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_23.addWidget(self.pushButton_199, 0, 4, 1, 1)

        self.horizontalSpacer_224 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_23.addItem(self.horizontalSpacer_224, 0, 7, 1, 1)

        self.pushButton_204 = QPushButton(self.page)
        self.pushButton_204.setObjectName(u"pushButton_204")
        self.pushButton_204.setStyleSheet(u"border : 2px solid;\n"
"border-color: rgb(223, 148, 255);\n"
"font-size:18px;\n"
"background-color: rgb(223, 148, 255);\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_23.addWidget(self.pushButton_204, 0, 0, 1, 1)


        self.verticalLayout_11.addLayout(self.gridLayout_23)

        self.gridLayout_19 = QGridLayout()
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.horizontalSpacer_186 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_19.addItem(self.horizontalSpacer_186, 0, 3, 1, 1)

        self.horizontalSpacer_183 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_19.addItem(self.horizontalSpacer_183, 0, 5, 1, 1)

        self.pushButton_168 = QPushButton(self.page)
        self.pushButton_168.setObjectName(u"pushButton_168")
        self.pushButton_168.setStyleSheet(u"border : 2px solid;\n"
"border-color: rgb(223, 148, 255);\n"
"font-size:18px;\n"
"background-color: rgb(223, 148, 255);\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_19.addWidget(self.pushButton_168, 0, 0, 1, 1)

        self.pushButton_164 = QPushButton(self.page)
        self.pushButton_164.setObjectName(u"pushButton_164")
        self.pushButton_164.setStyleSheet(u"border : 2px solid;\n"
"border-color: rgb(223, 148, 255);\n"
"font-size:18px;\n"
"background-color: rgb(223, 148, 255);\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_19.addWidget(self.pushButton_164, 0, 6, 1, 1)

        self.pushButton_167 = QPushButton(self.page)
        self.pushButton_167.setObjectName(u"pushButton_167")
        self.pushButton_167.setStyleSheet(u"border : 2px solid;\n"
"border-color: rgb(223, 148, 255);\n"
"font-size:18px;\n"
"background-color: rgb(223, 148, 255);\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_19.addWidget(self.pushButton_167, 0, 8, 1, 1)

        self.pushButton_163 = QPushButton(self.page)
        self.pushButton_163.setObjectName(u"pushButton_163")
        self.pushButton_163.setStyleSheet(u"border : 2px solid;\n"
"border-color: rgb(223, 148, 255);\n"
"font-size:18px;\n"
"background-color: rgb(223, 148, 255);\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_19.addWidget(self.pushButton_163, 0, 4, 1, 1)

        self.horizontalSpacer_188 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_19.addItem(self.horizontalSpacer_188, 0, 7, 1, 1)

        self.pushButton_171 = QPushButton(self.page)
        self.pushButton_171.setObjectName(u"pushButton_171")
        self.pushButton_171.setStyleSheet(u"border : 2px solid;\n"
"border-color: rgb(223, 148, 255);\n"
"font-size:18px;\n"
"background-color: rgb(223, 148, 255);\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_19.addWidget(self.pushButton_171, 0, 2, 1, 1)

        self.pushButton_166 = QPushButton(self.page)
        self.pushButton_166.setObjectName(u"pushButton_166")
        self.pushButton_166.setStyleSheet(u"border : 2px solid;\n"
"border-color: rgb(223, 148, 255);\n"
"font-size:18px;\n"
"background-color: rgb(223, 148, 255);\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_19.addWidget(self.pushButton_166, 0, 10, 1, 1)

        self.horizontalSpacer_187 = QSpacerItem(40, 40, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_19.addItem(self.horizontalSpacer_187, 0, 1, 1, 1)

        self.horizontalSpacer_184 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_19.addItem(self.horizontalSpacer_184, 0, 9, 1, 1)


        self.verticalLayout_11.addLayout(self.gridLayout_19)

        self.gridLayout_22 = QGridLayout()
        self.gridLayout_22.setObjectName(u"gridLayout_22")
        self.horizontalSpacer_210 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_22.addItem(self.horizontalSpacer_210, 0, 5, 1, 1)

        self.pushButton_193 = QPushButton(self.page)
        self.pushButton_193.setObjectName(u"pushButton_193")
        self.pushButton_193.setStyleSheet(u"border : 2px solid;\n"
"border-color: rgb(223, 148, 255);\n"
"font-size:18px;\n"
"background-color: rgb(223, 148, 255);\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_22.addWidget(self.pushButton_193, 0, 10, 1, 1)

        self.horizontalSpacer_211 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_22.addItem(self.horizontalSpacer_211, 0, 9, 1, 1)

        self.horizontalSpacer_213 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_22.addItem(self.horizontalSpacer_213, 0, 3, 1, 1)

        self.horizontalSpacer_214 = QSpacerItem(40, 40, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_22.addItem(self.horizontalSpacer_214, 0, 1, 1, 1)

        self.pushButton_198 = QPushButton(self.page)
        self.pushButton_198.setObjectName(u"pushButton_198")
        self.pushButton_198.setStyleSheet(u"border : 2px solid;\n"
"border-color: rgb(223, 148, 255);\n"
"font-size:18px;\n"
"background-color: rgb(223, 148, 255);\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_22.addWidget(self.pushButton_198, 0, 2, 1, 1)

        self.pushButton_190 = QPushButton(self.page)
        self.pushButton_190.setObjectName(u"pushButton_190")
        self.pushButton_190.setStyleSheet(u"border : 2px solid;\n"
"border-color: rgb(223, 148, 255);\n"
"font-size:18px;\n"
"background-color: rgb(223, 148, 255);\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_22.addWidget(self.pushButton_190, 0, 4, 1, 1)

        self.pushButton_195 = QPushButton(self.page)
        self.pushButton_195.setObjectName(u"pushButton_195")
        self.pushButton_195.setStyleSheet(u"border : 2px solid;\n"
"border-color: rgb(223, 148, 255);\n"
"font-size:18px;\n"
"background-color: rgb(223, 148, 255);\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_22.addWidget(self.pushButton_195, 0, 0, 1, 1)

        self.pushButton_194 = QPushButton(self.page)
        self.pushButton_194.setObjectName(u"pushButton_194")
        self.pushButton_194.setStyleSheet(u"border : 2px solid;\n"
"border-color: rgb(223, 148, 255);\n"
"font-size:18px;\n"
"background-color: rgb(223, 148, 255);\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_22.addWidget(self.pushButton_194, 0, 8, 1, 1)

        self.pushButton_191 = QPushButton(self.page)
        self.pushButton_191.setObjectName(u"pushButton_191")
        self.pushButton_191.setStyleSheet(u"border : 2px solid;\n"
"border-color: rgb(223, 148, 255);\n"
"font-size:18px;\n"
"background-color: rgb(223, 148, 255);\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_22.addWidget(self.pushButton_191, 0, 6, 1, 1)

        self.horizontalSpacer_215 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_22.addItem(self.horizontalSpacer_215, 0, 7, 1, 1)


        self.verticalLayout_11.addLayout(self.gridLayout_22)

        self.gridLayout_21 = QGridLayout()
        self.gridLayout_21.setObjectName(u"gridLayout_21")
        self.horizontalSpacer_205 = QSpacerItem(40, 40, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_21.addItem(self.horizontalSpacer_205, 0, 1, 1, 1)

        self.pushButton_184 = QPushButton(self.page)
        self.pushButton_184.setObjectName(u"pushButton_184")
        self.pushButton_184.setStyleSheet(u"border : 2px solid;\n"
"border-color: rgb(223, 148, 255);\n"
"font-size:18px;\n"
"background-color: rgb(223, 148, 255);\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_21.addWidget(self.pushButton_184, 0, 10, 1, 1)

        self.horizontalSpacer_201 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_21.addItem(self.horizontalSpacer_201, 0, 5, 1, 1)

        self.horizontalSpacer_204 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_21.addItem(self.horizontalSpacer_204, 0, 3, 1, 1)

        self.horizontalSpacer_206 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_21.addItem(self.horizontalSpacer_206, 0, 7, 1, 1)

        self.pushButton_181 = QPushButton(self.page)
        self.pushButton_181.setObjectName(u"pushButton_181")
        self.pushButton_181.setStyleSheet(u"border : 2px solid;\n"
"border-color: rgb(223, 148, 255);\n"
"font-size:18px;\n"
"background-color: rgb(223, 148, 255);\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_21.addWidget(self.pushButton_181, 0, 4, 1, 1)

        self.pushButton_186 = QPushButton(self.page)
        self.pushButton_186.setObjectName(u"pushButton_186")
        self.pushButton_186.setStyleSheet(u"border : 2px solid;\n"
"border-color: rgb(223, 148, 255);\n"
"font-size:18px;\n"
"background-color: rgb(223, 148, 255);\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_21.addWidget(self.pushButton_186, 0, 0, 1, 1)

        self.pushButton_185 = QPushButton(self.page)
        self.pushButton_185.setObjectName(u"pushButton_185")
        self.pushButton_185.setStyleSheet(u"border : 2px solid;\n"
"border-color: rgb(223, 148, 255);\n"
"font-size:18px;\n"
"background-color: rgb(223, 148, 255);\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_21.addWidget(self.pushButton_185, 0, 8, 1, 1)

        self.horizontalSpacer_202 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_21.addItem(self.horizontalSpacer_202, 0, 9, 1, 1)

        self.pushButton_189 = QPushButton(self.page)
        self.pushButton_189.setObjectName(u"pushButton_189")
        self.pushButton_189.setStyleSheet(u"border : 2px solid;\n"
"border-color: rgb(223, 148, 255);\n"
"font-size:18px;\n"
"background-color: rgb(223, 148, 255);\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_21.addWidget(self.pushButton_189, 0, 2, 1, 1)

        self.pushButton_182 = QPushButton(self.page)
        self.pushButton_182.setObjectName(u"pushButton_182")
        self.pushButton_182.setStyleSheet(u"border : 2px solid;\n"
"border-color: rgb(223, 148, 255);\n"
"font-size:18px;\n"
"background-color: rgb(223, 148, 255);\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_21.addWidget(self.pushButton_182, 0, 6, 1, 1)


        self.verticalLayout_11.addLayout(self.gridLayout_21)

        self.gridLayout_13 = QGridLayout()
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.horizontalSpacer_134 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_13.addItem(self.horizontalSpacer_134, 0, 5, 1, 1)

        self.pushButton_117 = QPushButton(self.page)
        self.pushButton_117.setObjectName(u"pushButton_117")
        self.pushButton_117.setStyleSheet(u"border : 2px solid;\n"
"border-color: rgb(223, 148, 255);\n"
"font-size:18px;\n"
"background-color: rgb(223, 148, 255);\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_13.addWidget(self.pushButton_117, 0, 4, 1, 1)

        self.horizontalSpacer_136 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_13.addItem(self.horizontalSpacer_136, 0, 9, 1, 1)

        self.pushButton_115 = QPushButton(self.page)
        self.pushButton_115.setObjectName(u"pushButton_115")
        self.pushButton_115.setStyleSheet(u"border : 2px solid;\n"
"border-color: rgb(223, 148, 255);\n"
"font-size:18px;\n"
"background-color: rgb(223, 148, 255);\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_13.addWidget(self.pushButton_115, 0, 6, 1, 1)

        self.pushButton_113 = QPushButton(self.page)
        self.pushButton_113.setObjectName(u"pushButton_113")
        self.pushButton_113.setStyleSheet(u"border : 2px solid;\n"
"border-color: rgb(223, 148, 255);\n"
"font-size:18px;\n"
"background-color: rgb(223, 148, 255);\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_13.addWidget(self.pushButton_113, 0, 10, 1, 1)

        self.pushButton_110 = QPushButton(self.page)
        self.pushButton_110.setObjectName(u"pushButton_110")
        self.pushButton_110.setStyleSheet(u"border : 2px solid;\n"
"border-color: rgb(223, 148, 255);\n"
"font-size:18px;\n"
"background-color: rgb(223, 148, 255);\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_13.addWidget(self.pushButton_110, 0, 8, 1, 1)

        self.horizontalSpacer_130 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_13.addItem(self.horizontalSpacer_130, 0, 3, 1, 1)

        self.pushButton_114 = QPushButton(self.page)
        self.pushButton_114.setObjectName(u"pushButton_114")
        self.pushButton_114.setStyleSheet(u"border : 2px solid;\n"
"border-color: rgb(223, 148, 255);\n"
"font-size:18px;\n"
"background-color: rgb(223, 148, 255);\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_13.addWidget(self.pushButton_114, 0, 2, 1, 1)

        self.pushButton_109 = QPushButton(self.page)
        self.pushButton_109.setObjectName(u"pushButton_109")
        self.pushButton_109.setStyleSheet(u"border : 2px solid;\n"
"border-color: rgb(223, 148, 255);\n"
"font-size:18px;\n"
"background-color: rgb(223, 148, 255);\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_13.addWidget(self.pushButton_109, 0, 0, 1, 1)

        self.horizontalSpacer_135 = QSpacerItem(40, 40, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_13.addItem(self.horizontalSpacer_135, 0, 1, 1, 1)

        self.horizontalSpacer_129 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_13.addItem(self.horizontalSpacer_129, 0, 7, 1, 1)


        self.verticalLayout_11.addLayout(self.gridLayout_13)

        self.gridLayout_18 = QGridLayout()
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.pushButton_159 = QPushButton(self.page)
        self.pushButton_159.setObjectName(u"pushButton_159")
        self.pushButton_159.setStyleSheet(u"border : 2px solid;\n"
"border-color: rgb(223, 148, 255);\n"
"font-size:18px;\n"
"background-color: rgb(223, 148, 255);\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_18.addWidget(self.pushButton_159, 0, 0, 1, 1)

        self.horizontalSpacer_179 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_18.addItem(self.horizontalSpacer_179, 0, 7, 1, 1)

        self.pushButton_158 = QPushButton(self.page)
        self.pushButton_158.setObjectName(u"pushButton_158")
        self.pushButton_158.setStyleSheet(u"border : 2px solid;\n"
"border-color: rgb(223, 148, 255);\n"
"font-size:18px;\n"
"background-color: rgb(223, 148, 255);\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_18.addWidget(self.pushButton_158, 0, 8, 1, 1)

        self.horizontalSpacer_174 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_18.addItem(self.horizontalSpacer_174, 0, 5, 1, 1)

        self.horizontalSpacer_178 = QSpacerItem(40, 40, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_18.addItem(self.horizontalSpacer_178, 0, 1, 1, 1)

        self.horizontalSpacer_177 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_18.addItem(self.horizontalSpacer_177, 0, 3, 1, 1)

        self.pushButton_162 = QPushButton(self.page)
        self.pushButton_162.setObjectName(u"pushButton_162")
        self.pushButton_162.setStyleSheet(u"border : 2px solid;\n"
"border-color: rgb(223, 148, 255);\n"
"font-size:18px;\n"
"background-color: rgb(223, 148, 255);\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_18.addWidget(self.pushButton_162, 0, 2, 1, 1)

        self.pushButton_157 = QPushButton(self.page)
        self.pushButton_157.setObjectName(u"pushButton_157")
        self.pushButton_157.setStyleSheet(u"border : 2px solid;\n"
"border-color: rgb(223, 148, 255);\n"
"font-size:18px;\n"
"background-color: rgb(223, 148, 255);\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_18.addWidget(self.pushButton_157, 0, 10, 1, 1)

        self.pushButton_155 = QPushButton(self.page)
        self.pushButton_155.setObjectName(u"pushButton_155")
        self.pushButton_155.setStyleSheet(u"border : 2px solid;\n"
"border-color: rgb(223, 148, 255);\n"
"font-size:18px;\n"
"background-color: rgb(223, 148, 255);\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_18.addWidget(self.pushButton_155, 0, 6, 1, 1)

        self.horizontalSpacer_175 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_18.addItem(self.horizontalSpacer_175, 0, 9, 1, 1)

        self.pushButton_154 = QPushButton(self.page)
        self.pushButton_154.setObjectName(u"pushButton_154")
        self.pushButton_154.setStyleSheet(u"border : 2px solid;\n"
"border-color: rgb(223, 148, 255);\n"
"font-size:18px;\n"
"background-color: rgb(223, 148, 255);\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_18.addWidget(self.pushButton_154, 0, 4, 1, 1)


        self.verticalLayout_11.addLayout(self.gridLayout_18)

        self.gridLayout_20 = QGridLayout()
        self.gridLayout_20.setObjectName(u"gridLayout_20")
        self.pushButton_176 = QPushButton(self.page)
        self.pushButton_176.setObjectName(u"pushButton_176")
        self.pushButton_176.setStyleSheet(u"border : 2px solid;\n"
"border-color: rgb(223, 148, 255);\n"
"font-size:18px;\n"
"background-color: rgb(223, 148, 255);\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_20.addWidget(self.pushButton_176, 0, 8, 1, 1)

        self.horizontalSpacer_195 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_20.addItem(self.horizontalSpacer_195, 0, 3, 1, 1)

        self.horizontalSpacer_192 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_20.addItem(self.horizontalSpacer_192, 0, 5, 1, 1)

        self.pushButton_177 = QPushButton(self.page)
        self.pushButton_177.setObjectName(u"pushButton_177")
        self.pushButton_177.setStyleSheet(u"border : 2px solid;\n"
"border-color: rgb(223, 148, 255);\n"
"font-size:18px;\n"
"background-color: rgb(223, 148, 255);\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_20.addWidget(self.pushButton_177, 0, 0, 1, 1)

        self.horizontalSpacer_196 = QSpacerItem(40, 40, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_20.addItem(self.horizontalSpacer_196, 0, 1, 1, 1)

        self.pushButton_180 = QPushButton(self.page)
        self.pushButton_180.setObjectName(u"pushButton_180")
        self.pushButton_180.setStyleSheet(u"border : 2px solid;\n"
"border-color: rgb(223, 148, 255);\n"
"font-size:18px;\n"
"background-color: rgb(223, 148, 255);\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_20.addWidget(self.pushButton_180, 0, 2, 1, 1)

        self.pushButton_172 = QPushButton(self.page)
        self.pushButton_172.setObjectName(u"pushButton_172")
        self.pushButton_172.setStyleSheet(u"border : 2px solid;\n"
"border-color: rgb(223, 148, 255);\n"
"font-size:18px;\n"
"background-color: rgb(223, 148, 255);\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_20.addWidget(self.pushButton_172, 0, 4, 1, 1)

        self.horizontalSpacer_193 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_20.addItem(self.horizontalSpacer_193, 0, 9, 1, 1)

        self.pushButton_173 = QPushButton(self.page)
        self.pushButton_173.setObjectName(u"pushButton_173")
        self.pushButton_173.setStyleSheet(u"border : 2px solid;\n"
"border-color: rgb(223, 148, 255);\n"
"font-size:18px;\n"
"background-color: rgb(223, 148, 255);\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_20.addWidget(self.pushButton_173, 0, 6, 1, 1)

        self.pushButton_175 = QPushButton(self.page)
        self.pushButton_175.setObjectName(u"pushButton_175")
        self.pushButton_175.setStyleSheet(u"border : 2px solid;\n"
"border-color: rgb(223, 148, 255);\n"
"font-size:18px;\n"
"background-color: rgb(223, 148, 255);\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_20.addWidget(self.pushButton_175, 0, 10, 1, 1)

        self.horizontalSpacer_197 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_20.addItem(self.horizontalSpacer_197, 0, 7, 1, 1)


        self.verticalLayout_11.addLayout(self.gridLayout_20)

        self.gridLayout_24 = QGridLayout()
        self.gridLayout_24.setObjectName(u"gridLayout_24")
        self.horizontalSpacer_228 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_24.addItem(self.horizontalSpacer_228, 0, 5, 1, 1)

        self.pushButton_209 = QPushButton(self.page)
        self.pushButton_209.setObjectName(u"pushButton_209")
        self.pushButton_209.setStyleSheet(u"border : 2px solid;\n"
"border-color: rgb(223, 148, 255);\n"
"font-size:18px;\n"
"background-color: rgb(223, 148, 255);\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_24.addWidget(self.pushButton_209, 0, 6, 1, 1)

        self.pushButton_213 = QPushButton(self.page)
        self.pushButton_213.setObjectName(u"pushButton_213")
        self.pushButton_213.setStyleSheet(u"border : 2px solid;\n"
"border-color: rgb(223, 148, 255);\n"
"font-size:18px;\n"
"background-color: rgb(223, 148, 255);\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_24.addWidget(self.pushButton_213, 0, 0, 1, 1)

        self.horizontalSpacer_229 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_24.addItem(self.horizontalSpacer_229, 0, 9, 1, 1)

        self.horizontalSpacer_233 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_24.addItem(self.horizontalSpacer_233, 0, 7, 1, 1)

        self.pushButton_208 = QPushButton(self.page)
        self.pushButton_208.setObjectName(u"pushButton_208")
        self.pushButton_208.setStyleSheet(u"border : 2px solid;\n"
"border-color: rgb(223, 148, 255);\n"
"font-size:18px;\n"
"background-color: rgb(223, 148, 255);\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_24.addWidget(self.pushButton_208, 0, 4, 1, 1)

        self.horizontalSpacer_232 = QSpacerItem(40, 40, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_24.addItem(self.horizontalSpacer_232, 0, 1, 1, 1)

        self.pushButton_212 = QPushButton(self.page)
        self.pushButton_212.setObjectName(u"pushButton_212")
        self.pushButton_212.setStyleSheet(u"border : 2px solid;\n"
"border-color: rgb(223, 148, 255);\n"
"font-size:18px;\n"
"background-color: rgb(223, 148, 255);\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_24.addWidget(self.pushButton_212, 0, 8, 1, 1)

        self.horizontalSpacer_231 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_24.addItem(self.horizontalSpacer_231, 0, 3, 1, 1)

        self.pushButton_216 = QPushButton(self.page)
        self.pushButton_216.setObjectName(u"pushButton_216")
        self.pushButton_216.setStyleSheet(u"border : 2px solid;\n"
"border-color: rgb(223, 148, 255);\n"
"font-size:18px;\n"
"background-color: rgb(223, 148, 255);\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_24.addWidget(self.pushButton_216, 0, 2, 1, 1)

        self.pushButton_211 = QPushButton(self.page)
        self.pushButton_211.setObjectName(u"pushButton_211")
        self.pushButton_211.setStyleSheet(u"border : 2px solid;\n"
"border-color: rgb(223, 148, 255);\n"
"font-size:18px;\n"
"background-color: rgb(223, 148, 255);\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_24.addWidget(self.pushButton_211, 0, 10, 1, 1)


        self.verticalLayout_11.addLayout(self.gridLayout_24)

        self.gridLayout_25 = QGridLayout()
        self.gridLayout_25.setObjectName(u"gridLayout_25")
        self.horizontalSpacer_241 = QSpacerItem(40, 40, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_25.addItem(self.horizontalSpacer_241, 0, 1, 1, 1)

        self.horizontalSpacer_237 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_25.addItem(self.horizontalSpacer_237, 0, 5, 1, 1)

        self.pushButton_218 = QPushButton(self.page)
        self.pushButton_218.setObjectName(u"pushButton_218")
        self.pushButton_218.setStyleSheet(u"border : 2px solid;\n"
"border-color: rgb(223, 148, 255);\n"
"font-size:18px;\n"
"background-color: rgb(223, 148, 255);\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_25.addWidget(self.pushButton_218, 0, 6, 1, 1)

        self.horizontalSpacer_240 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_25.addItem(self.horizontalSpacer_240, 0, 3, 1, 1)

        self.horizontalSpacer_242 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_25.addItem(self.horizontalSpacer_242, 0, 7, 1, 1)

        self.pushButton_225 = QPushButton(self.page)
        self.pushButton_225.setObjectName(u"pushButton_225")
        self.pushButton_225.setStyleSheet(u"border : 2px solid;\n"
"border-color: rgb(223, 148, 255);\n"
"font-size:18px;\n"
"background-color: rgb(223, 148, 255);\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_25.addWidget(self.pushButton_225, 0, 2, 1, 1)

        self.pushButton_221 = QPushButton(self.page)
        self.pushButton_221.setObjectName(u"pushButton_221")
        self.pushButton_221.setStyleSheet(u"border : 2px solid;\n"
"border-color: rgb(223, 148, 255);\n"
"font-size:18px;\n"
"background-color: rgb(223, 148, 255);\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_25.addWidget(self.pushButton_221, 0, 8, 1, 1)

        self.pushButton_220 = QPushButton(self.page)
        self.pushButton_220.setObjectName(u"pushButton_220")
        self.pushButton_220.setStyleSheet(u"border : 2px solid;\n"
"border-color: rgb(223, 148, 255);\n"
"font-size:18px;\n"
"background-color: rgb(223, 148, 255);\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_25.addWidget(self.pushButton_220, 0, 10, 1, 1)

        self.pushButton_217 = QPushButton(self.page)
        self.pushButton_217.setObjectName(u"pushButton_217")
        self.pushButton_217.setStyleSheet(u"border : 2px solid;\n"
"border-color: rgb(223, 148, 255);\n"
"font-size:18px;\n"
"background-color: rgb(223, 148, 255);\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_25.addWidget(self.pushButton_217, 0, 4, 1, 1)

        self.pushButton_222 = QPushButton(self.page)
        self.pushButton_222.setObjectName(u"pushButton_222")
        self.pushButton_222.setStyleSheet(u"border : 2px solid;\n"
"border-color: rgb(223, 148, 255);\n"
"font-size:18px;\n"
"background-color: rgb(223, 148, 255);\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_25.addWidget(self.pushButton_222, 0, 0, 1, 1)

        self.horizontalSpacer_238 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_25.addItem(self.horizontalSpacer_238, 0, 9, 1, 1)


        self.verticalLayout_11.addLayout(self.gridLayout_25)


        self.verticalLayout_12.addLayout(self.verticalLayout_11)

        self.toolBox.addItem(self.page, u"\u6f0f\u6d1ePoc\u96c6\u5408")
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2.setGeometry(QRect(0, 0, 100, 30))
        self.toolBox.addItem(self.page_2, u"\u6f0f\u6d1eExp\u96c6\u5408")

        self.verticalLayout_8.addWidget(self.toolBox)

        self.tabWidget.addTab(self.Ndaytools, "")
        self.IptoDomain = QWidget()
        self.IptoDomain.setObjectName(u"IptoDomain")
        self.horizontalLayout_7 = QHBoxLayout(self.IptoDomain)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.groupBox_7 = QGroupBox(self.IptoDomain)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.groupBox_7.setStyleSheet(u"QGroupBox\n"
"{\n"
"border : 2px solid;\n"
"border-color : rgb(223, 148, 255);\n"
"font  : 13px;\n"
"}")
        self.verticalLayout_9 = QVBoxLayout(self.groupBox_7)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalSpacer = QSpacerItem(20, 30, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_9.addItem(self.verticalSpacer)

        self.iptodomain = QPushButton(self.groupBox_7)
        self.iptodomain.setObjectName(u"iptodomain")
        self.iptodomain.setStyleSheet(u"font-size:18px;\n"
"background-color: rgb(108, 118, 255);\n"
"color: rgb(255, 255, 255);")

        self.verticalLayout_9.addWidget(self.iptodomain)

        self.clear_iptodomain = QPushButton(self.groupBox_7)
        self.clear_iptodomain.setObjectName(u"clear_iptodomain")
        self.clear_iptodomain.setStyleSheet(u"font-size:16px;\n"
"background-color: rgb(108, 118, 255);\n"
"color: rgb(255, 255, 255);")

        self.verticalLayout_9.addWidget(self.clear_iptodomain)

        self.iptodomain_tips = QTextEdit(self.groupBox_7)
        self.iptodomain_tips.setObjectName(u"iptodomain_tips")
        self.iptodomain_tips.setContextMenuPolicy(Qt.NoContextMenu)

        self.verticalLayout_9.addWidget(self.iptodomain_tips)

        self.verticalLayout_9.setStretch(1, 1)
        self.verticalLayout_9.setStretch(3, 3)

        self.horizontalLayout_7.addWidget(self.groupBox_7)

        self.groupBox_8 = QGroupBox(self.IptoDomain)
        self.groupBox_8.setObjectName(u"groupBox_8")
        self.groupBox_8.setStyleSheet(u"QGroupBox\n"
"{\n"
"border : 2px solid;\n"
"border-color : rgb(255, 159, 24);\n"
"font  : 13px;\n"
"}")
        self.verticalLayout_10 = QVBoxLayout(self.groupBox_8)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalSpacer_2 = QSpacerItem(20, 30, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_10.addItem(self.verticalSpacer_2)

        self.domaintorank = QPushButton(self.groupBox_8)
        self.domaintorank.setObjectName(u"domaintorank")
        self.domaintorank.setStyleSheet(u"font-size:18px;\n"
"background-color: rgb(120, 255, 131);\n"
"color: rgb(255, 255, 255);\n"
"")

        self.verticalLayout_10.addWidget(self.domaintorank)

        self.domaintorank_tips = QTextEdit(self.groupBox_8)
        self.domaintorank_tips.setObjectName(u"domaintorank_tips")
        self.domaintorank_tips.setContextMenuPolicy(Qt.NoContextMenu)

        self.verticalLayout_10.addWidget(self.domaintorank_tips)

        self.verticalLayout_10.setStretch(1, 1)
        self.verticalLayout_10.setStretch(2, 3)

        self.horizontalLayout_7.addWidget(self.groupBox_8)

        self.tabWidget.addTab(self.IptoDomain, "")

        self.verticalLayout.addWidget(self.tabWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1624, 22))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        self.menu_2 = QMenu(self.menubar)
        self.menu_2.setObjectName(u"menu_2")
        self.menu_3 = QMenu(self.menubar)
        self.menu_3.setObjectName(u"menu_3")
        self.menu_4 = QMenu(self.menubar)
        self.menu_4.setObjectName(u"menu_4")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())
        self.menubar.addAction(self.menu_4.menuAction())
        self.menu.addAction(self.actionFofa)
        self.menu.addAction(self.actionHunter)
        self.menu.addAction(self.actionShodan)
        self.menu_2.addAction(self.actionProxy)
        self.menu_2.addAction(self.action_ClearUrl)
        self.menu_3.addAction(self.action_About)
        self.menu_3.addAction(self.action_Auther)
        self.menu_4.addAction(self.action_Issea)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)
        self.toolBox.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Easy_hacktools \u3010Nday\u6f0f\u6d1e\u96c6\u5408\u5c0f\u5de5\u5177\u3011 \u4f5c\u8005\uff1aMuhan Blog\uff1awww.anquanclub.com  \u61d2\u4eba\u5fc5\u5907 \u7b80\u7b80\u5355\u5355 \u5feb\u901f\u9a8c\u8bc1 \u9010\u6b65\u5b8c\u5584 \u6301\u7eed\u66f4\u65b0", None))
        self.actionFofa.setText(QCoreApplication.translate("MainWindow", u"Fofa\u914d\u7f6e", None))
        self.actionHunter.setText(QCoreApplication.translate("MainWindow", u"Hunter\u914d\u7f6e", None))
        self.actionShodan.setText(QCoreApplication.translate("MainWindow", u"Shodan\u914d\u7f6e", None))
        self.actionProxy.setText(QCoreApplication.translate("MainWindow", u"\u4ee3\u7406\u8bbe\u7f6e", None))
        self.action_ClearUrl.setText(QCoreApplication.translate("MainWindow", u"\u6e05\u7406\u91c7\u96c6\u6587\u4ef6", None))
        self.action_About.setText(QCoreApplication.translate("MainWindow", u"\u5173\u4e8e", None))
        self.action_Auther.setText(QCoreApplication.translate("MainWindow", u"\u4f5c\u8005", None))
        self.action_Issea.setText(QCoreApplication.translate("MainWindow", u"\u53cd\u9988", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Fofa\u641c\u7d22\u6a21\u5757", None))
        self.Fofayufa.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u586b\u5199base64\u52a0\u5bc6\u540e\u7684fofa\u547d\u4ee4", None))
        self.fofanumber.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u586b\u5199\u67e5\u8be2\u6b21\u6570(\u9700\u8981\u67e5\u770b\u81ea\u5df1\u4f1a\u5458\u7b49\u7ea7)", None))
        self.fofaso.setText(QCoreApplication.translate("MainWindow", u"\u67e5\u8be2", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Fofa\u641c\u7d22\u53c2\u8003", None))
        self.fofacankao.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Microsoft YaHei UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ff0000;\">title=&quot;beijing&quot;         		\u4ece\u6807\u9898\u4e2d\u641c\u7d22\u201c\u5317\u4eac\u201d</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ff0000;\">header=&quot;elastic&quot;        		\u4ecehttp\u5934\u4e2d\u641c\u7d22\u201celastic\u201d</span><"
                        "/p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ff0000;\">body=&quot;\u7f51\u7edc\u7a7a\u95f4\u6d4b\u7ed8&quot;      		\u4ecehtml\u6b63\u6587\u4e2d\u641c\u7d22\u201c\u7f51\u7edc\u7a7a\u95f4\u6d4b\u7ed8\u201d</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ff0000;\">fid=&quot;sSXXGNUO2FefBTcCLIT/2Q==&quot;  	\u67e5\u627e\u76f8\u540c\u7684\u7f51\u7ad9\u6307\u7eb9</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ff0000;\">domain=&quot;qq.com&quot;             		\u641c\u7d22\u6839\u57df\u540d\u5e26\u6709qq.com\u7684\u7f51\u7ad9</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">icp=&quot;\u4eacICP\u8bc1030173\u53f7"
                        "&quot;        	\u67e5\u627e\u5907\u6848\u53f7\u4e3a\u201c\u4eacICP\u8bc1030173\u53f7\u201d\u7684\u7f51\u7ad9</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">js_name=&quot;js/jquery.js&quot;      		\u67e5\u627e\u7f51\u7ad9\u6b63\u6587\u4e2d\u5305\u542bjs/jquery.js\u7684\u8d44\u4ea7</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">js_md5=&quot;82ac3f14327a8b7ba49baa208d4eaa15&quot;   \u67e5\u627ejs\u6e90\u7801\u4e0e\u4e4b\u5339\u914d\u7684\u8d44\u4ea7</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">cname=&quot;ap21.siteforce.com&quot;     	\u67e5\u627ecname\u4e3a&quot;ap21.siteforce.com&quot;\u7684\u7f51\u7ad9</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">cname_domain=&quot;siteforce.com&quot;"
                        "        	\u67e5\u627ecname\u5305\u542b\u201csiteforce.com\u201d\u7684\u7f51\u7ad9</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">cloud_name=&quot;Aliyundun&quot;              	\u901a\u8fc7\u4e91\u670d\u52a1\u540d\u79f0\u641c\u7d22\u8d44\u4ea7</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">product=&quot;NGINX&quot;                     	\u641c\u7d22\u6b64\u4ea7\u54c1\u7684\u8d44\u4ea7</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">category=&quot;\u670d\u52a1&quot;                     	\u641c\u7d22\u6b64\u4ea7\u54c1\u5206\u7c7b\u7684\u8d44\u4ea7</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">sdk_hash==&quot;Mkb4Ms4R96glv/T6TRzwPWh3UDatBqeF&quot;    \u641c\u7d22\u4f7f\u7528\u6b64sdk\u7684\u8d44"
                        "\u4ea7</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ff0000;\">icon_hash=&quot;247388890&quot;               	\u641c\u7d22\u4f7f\u7528\u6b64 icon \u7684\u8d44\u4ea7</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ff0000;\">host=&quot;.gov.cn&quot;                      	\u4eceurl\u4e2d\u641c\u7d22\u201d.gov.cn\u201d</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ff0000;\">port=&quot;6379&quot;                         	\u67e5\u627e\u5bf9\u5e94\u201c6379\u201d\u7aef\u53e3\u7684\u8d44\u4ea7</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ff0000;\">ip=&quot;1.1.1.1&quot;                 "
                        "       		\u4eceip\u4e2d\u641c\u7d22\u5305\u542b\u201c1.1.1.1\u201d\u7684\u7f51\u7ad9</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ff0000;\">ip=&quot;220.181.111.1/24&quot;               	\u67e5\u8be2IP\u4e3a\u201c220.181.111.1\u201d\u7684C\u7f51\u6bb5\u8d44\u4ea7</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">status_code=&quot;402&quot;                   	\u67e5\u8be2\u670d\u52a1\u5668\u72b6\u6001\u4e3a\u201c402\u201d\u7684\u8d44\u4ea7</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">protocol=&quot;quic&quot;                     	\u67e5\u8be2quic\u534f\u8bae\u8d44\u4ea7</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ff0000;\">count"
                        "ry=&quot;CN&quot;                        	\u641c\u7d22\u6307\u5b9a\u56fd\u5bb6(\u7f16\u7801)\u7684\u8d44\u4ea7</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">region=&quot;Xinjiang Uyghur Autonomous Region&quot;  \u641c\u7d22\u6307\u5b9a\u884c\u653f\u533a\u7684\u8d44\u4ea7</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">city=&quot;\u00dcr\u00fcmqi&quot;                       	\u641c\u7d22\u6307\u5b9a\u57ce\u5e02\u7684\u8d44\u4ea7</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">cert=&quot;baidu&quot;                        		\u641c\u7d22\u8bc1\u4e66\u4e2d\u5e26\u6709baidu\u7684\u8d44\u4ea7</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">cert.subject=&quot;Oracle Corporation&quot;   	\u641c"
                        "\u7d22\u8bc1\u4e66\u6301\u6709\u8005\u662fOracle Corporation\u7684\u8d44\u4ea7</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">cert.issuer=&quot;DigiCert&quot;              	\u641c\u7d22\u8bc1\u4e66\u9881\u53d1\u8005\u4e3aDigiCert Inc\u7684\u8d44\u4ea7</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">cert.is_valid=true                  	\u9a8c\u8bc1\u8bc1\u4e66\u662f\u5426\u6709\u6548\uff0ctrue\u6709\u6548\uff0cfalse\u65e0\u6548</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">jarm=&quot;2ad...83e81&quot;                  	\u641c\u7d22JARM\u6307\u7eb9</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">banner=&quot;users&quot; &amp;&amp; protocol=&quot;ftp&quot;    	\u641c\u7d22FTP\u534f\u8bae\u4e2d"
                        "\u5e26\u6709users\u6587\u672c\u7684\u8d44\u4ea7</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">type=&quot;service&quot;                      	\u652f\u6301subdomain\u548cservice\u4e24\u79cd</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ff0000;\">os=&quot;centos&quot;                         		\u641c\u7d22CentOS\u8d44\u4ea7</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">server==&quot;MicrosoftIIS/10&quot;           	\u641c\u7d22IIS 10\u670d\u52a1\u5668</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">app=&quot;MicrosoftExchange&quot;             	\u641c\u7d22MicrosoftExchange\u8bbe\u5907</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; marg"
                        "in-right:0px; -qt-block-indent:0; text-indent:0px;\">after=&quot;2017&quot; &amp;&amp; before=&quot;20171001&quot;   	\u65f6\u95f4\u8303\u56f4\u6bb5\u641c\u7d22</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">asn=&quot;19551&quot;                         	\u641c\u7d22\u6307\u5b9aasn\u7684\u8d44\u4ea7</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">org=&quot;LLC Baxet&quot;                     	\u641c\u7d22\u6307\u5b9aorg(\u7ec4\u7ec7)\u7684\u8d44\u4ea7</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">base_protocol=&quot;udp&quot;                 	\u641c\u7d22\u6307\u5b9audp\u534f\u8bae\u7684\u8d44\u4ea7</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">is_fraud=false                      		\u6392"
                        "\u9664\u4eff\u5192/\u6b3a\u8bc8\u6570\u636e</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">is_honeypot=false                   	\u6392\u9664\u871c\u7f50\u6570\u636e</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">is_ipv6=true                        		\u641c\u7d22ipv6\u7684\u8d44\u4ea7</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">is_domain=true                      	\u641c\u7d22\u57df\u540d\u7684\u8d44\u4ea7</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">is_cloud=true                       	\u7b5b\u9009\u4f7f\u7528\u4e86\u4e91\u670d\u52a1\u7684\u8d44\u4ea7</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">port_"
                        "size=&quot;6&quot;                       	\u67e5\u8be2\u5f00\u653e\u7aef\u53e3\u6570\u91cf\u7b49\u4e8e&quot;6&quot;\u7684\u8d44\u4ea7</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">port_size_gt=&quot;6&quot;                    	\u67e5\u8be2\u5f00\u653e\u7aef\u53e3\u6570\u91cf\u5927\u4e8e&quot;6&quot;\u7684\u8d44\u4ea7</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">port_size_lt=&quot;12&quot;                   	\u67e5\u8be2\u5f00\u653e\u7aef\u53e3\u6570\u91cf\u5c0f\u4e8e&quot;12&quot;\u7684\u8d44\u4ea7</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">ip_ports=&quot;80,161&quot;                   	\u641c\u7d22\u540c\u65f6\u5f00\u653e80\u548c161\u7aef\u53e3\u7684ip</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; "
                        "text-indent:0px;\"><span style=\" color:#ff0000;\">ip_country=&quot;CN&quot;                     	\u641c\u7d22\u4e2d\u56fd\u7684ip\u8d44\u4ea7(\u4ee5ip\u4e3a\u5355\u4f4d\u7684\u8d44\u4ea7\u6570\u636e)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ff0000;\">ip_region=&quot;Zhejiang&quot;                	\u641c\u7d22\u6307\u5b9a\u884c\u653f\u533a\u7684ip\u8d44\u4ea7</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ff0000;\">ip_city=&quot;Hangzhou&quot;                  	\u641c\u7d22\u6307\u5b9a\u57ce\u5e02\u7684ip\u8d44\u4ea7</span></p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.fofa), QCoreApplication.translate("MainWindow", u"Fofa\u641c\u7d22", None))
        self.groupBox_9.setTitle(QCoreApplication.translate("MainWindow", u"Hunter\u641c\u7d22\u6a21\u5757", None))
        self.hunter_yufa.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u586b\u5199\u52a0\u5bc6\u540e\u7684hunter\u8bed\u53e5", None))
        self.hunter_num.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u586b\u5199\u60f3\u8981\u67e5\u8be2\u6570\u636e\u7684\u6761\u6570", None))
        self.hunter_zichan.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u586b\u5199\u8d44\u4ea7\u7c7b\u578b\uff0c1\u4ee3\u8868\u201dweb\u8d44\u4ea7\u201c\uff0c2\u4ee3\u8868\u201d\u975eweb\u8d44\u4ea7\u201c\uff0c3\u4ee3\u8868\u201d\u5168\u90e8\u201c", None))
        self.hunter_status.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u72b6\u6001\u7801\u5217\u8868\uff0c\u4ee5\u9017\u53f7\u5206\u9694\uff0c\u5982\u201d200\u201c", None))
        self.hunter_start_time.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb\u65f6\u95f4\uff0c\u683c\u5f0f\u4e3a2023-03-12 00:00:00", None))
        self.hunter_end_time.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u7ed3\u675f\u65f6\u95f4\uff0c\u683c\u5f0f\u4e3a2022-07-17 00:00:00", None))
        self.hunterso.setText(QCoreApplication.translate("MainWindow", u"\u67e5\u8be2", None))
        self.groupBox_11.setTitle(QCoreApplication.translate("MainWindow", u"Hunter\u79ef\u5206\u660e\u7ec6", None))
        self.groupBox_10.setTitle(QCoreApplication.translate("MainWindow", u"Hunter\u67e5\u8be2\u8bed\u6cd5\u53c2\u8003", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Hunter), QCoreApplication.translate("MainWindow", u"Hunter\u641c\u7d22", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Shodan\u641c\u7d22\u6a21\u5757", None))
        self.Shodanyufa.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u76f4\u63a5\u586b\u5199shodan\u8bed\u6cd5\uff08\u4e0d\u9700\u8981\u52a0\u5bc6\uff09", None))
        self.Shodannumber.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u586b\u5199\u67e5\u8be2\u6b21\u6570(\u9700\u8981\u67e5\u770b\u81ea\u5df1\u4f1a\u5458\u7b49\u7ea7)", None))
        self.Shodanso.setText(QCoreApplication.translate("MainWindow", u"\u67e5\u8be2", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"Shodan\u641c\u7d22\u53c2\u8003", None))
        self.Shodancankao.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Microsoft YaHei UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">------\u9650\u5b9a\u56fd\u5bb6\u548c\u57ce\u5e02</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u9650\u5b9a\u56fd\u5bb6country:&quot;CN&quot;</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u9650\u5b9a\u57ce\u5e02city:&quot;Shang"
                        "Hai&quot;</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">------\u9650\u5b9a\u4e3b\u673a\u540d\u6216\u57df\u540d</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">hostname:.org</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">hostname:&quot;google&quot;</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">hostname:baidu.com</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin"
                        "-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">------\u9650\u5b9a\u7ec4\u7ec7\u6216\u673a\u6784</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">org:&quot;alibaba&quot;</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">------\u9650\u5b9a\u7cfb\u7edfOS\u7248\u672c</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">os:&quot;Windows Server 2008 R2&quot;</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">os:&quot;Windows 7 or 8&quot;</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-"
                        "block-indent:0; text-indent:0px;\">os:&quot;Linux 2.6.x&quot;</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">------\u9650\u5b9a\u7aef\u53e3</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">port:22</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">port:80</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">------\u6307\u5b9a\u7f51\u6bb5</p>\n"
"<p style=\" margin-top:0px; margin-bott"
                        "om:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">net:&quot;59.56.19.0/24&quot;</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">------\u6307\u5b9a\u4f7f\u7528\u7684\u8f6f\u4ef6\u6216\u4ea7\u54c1</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">product:&quot;Apache httpd&quot;</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">product:&quot;nginx&quot;</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">product:&quot;Microsoft IIS httpd&quot;</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px"
                        "; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">product:&quot;mysql&quot;</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">------\u6307\u5b9aCVE\u6f0f\u6d1e\u7f16\u53f7</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">vuln:&quot;CVE-2014-0723&quot;</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">------\u6307\u5b9a\u7f51\u9875\u5185\u5bb9</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; t"
                        "ext-indent:0px;\">http.html:&quot;hello world&quot;</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">------\u6307\u5b9a\u7f51\u9875\u6807\u9898</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">http.title:&quot;hello&quot;</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">------\u6307\u5b9a\u8fd4\u56de\u54cd\u5e94\u7801</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">http.status:20"
                        "0</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">------\u6307\u5b9a\u8fd4\u56de\u4e2d\u7684server\u7c7b\u578b</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">http.server:Apache/2.4.7</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">http.server:PHP</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">------\u6307\u5b9a\u5730\u7406\u4f4d\u7f6e</p>\n"
"<p style=\" margin-top:0px; marg"
                        "in-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">geo:&quot;31.25,121.44&quot;</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">------\u6307\u5b9aISP\u4f9b\u5e94\u5546</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">isp:&quot;China Telecom&quot;</p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Shodan), QCoreApplication.translate("MainWindow", u"Shodan\u641c\u7d22", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"Base64\u52a0\u5bc6\u6a21\u5757", None))
        self.base64Line.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u586b\u5199\u60a8\u8981\u52a0\u5bc6\u7684\u5185\u5bb9", None))
        self.base64add.setText(QCoreApplication.translate("MainWindow", u"\u52a0\u5bc6", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("MainWindow", u"Base64\u52a0\u5bc6\u6f14\u793a", None))
        self.base64demo.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Microsoft YaHei UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">\u3010app=&quot;MSA/1.0&quot;\u3011\u7684\u52a0\u5bc6\u7ed3\u679c\u4e3aYXBwPSJNU0EvMS4wIg==</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">\u3010title=&quot;Vigor 2960&quot;\u3011\u7684\u52a0\u5bc6\u7ed3\u679c\u4e3adGl0bGU9IlZpZ29yIDI5NjAi"
                        "</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">\u3010app=&quot;D_Link-DCS-2530L&quot;\u3011\u7684\u52a0\u5bc6\u7ed3\u679c\u4e3aYXBwPSJEX0xpbmstRENTLTI1MzBMIg==</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">\u3010title=&quot;\u5b5a\u76df\u4e91 &quot;\u3011\u7684\u52a0\u5bc6\u7ed3\u679c\u4e3adGl0bGU9IuWtmuebn+S6kSAi</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">\u3010app=&quot;VOS-VOS3000&quot;\u3011\u7684\u52a0\u5bc6\u7ed3\u679c\u4e3aYXBwPSJWT1MtVk9TMzAwMCI=</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">\u3010body=&quot;kkFileVi"
                        "ew&quot;\u3011\u7684\u52a0\u5bc6\u7ed3\u679c\u4e3aYm9keT0ia2tGaWxlVmlldyI=</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">\u3010title=&quot;WSO2 Management Console&quot;\u3011\u7684\u52a0\u5bc6\u7ed3\u679c\u4e3adGl0bGU9IldTTzIgTWFuYWdlbWVudCBDb25zb2xlIg==</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">\u3010body=&quot;SolarView Compact&quot; &amp;&amp; title==&quot;Top&quot;\u3011\u7684\u52a0\u5bc6\u7ed3\u679c\u4e3aYm9keT0iU29sYXJWaWV3IENvbXBhY3QiICYmIHRpdGxlPT0iVG9wIg==</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">\u3010body=&quot;FortiToken clock drift detected&quot;\u3011\u7684\u52a0\u5bc6\u7ed3\u679c\u4e3aYm9keT0iRm9ydGlUb2tlbiBjbG9jayBkcmlmdCBk"
                        "ZXRlY3RlZCI=</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">\u3010app=&quot;Microsoft-Exchange&quot;\u3011\u7684\u52a0\u5bc6\u7ed3\u679c\u4e3aYXBwPSJNaWNyb3NvZnQtRXhjaGFuZ2Ui</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">\u3010app=&quot;Ruijie-EG\u6613\u7f51\u5173&quot;\u3011\u7684\u52a0\u5bc6\u7ed3\u679c\u4e3aYXBwPSJSdWlqaWUtRUfmmJPnvZHlhbMi</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">\u3010title==&quot;Tenda | Login&quot;\u3011\u7684\u52a0\u5bc6\u7ed3\u679c\u4e3adGl0bGU9PSJUZW5kYSB8IExvZ2luIg==</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" fo"
                        "nt-size:10pt;\">\u3010app=&quot;Sapido-\u8def\u7531\u5668&quot;\u3011\u7684\u52a0\u5bc6\u7ed3\u679c\u4e3aYXBwPSJTYXBpZG8t6Lev55Sx5ZmoIg==</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">\u3010title=&quot;USG FLEX&quot;\u3011\u7684\u52a0\u5bc6\u7ed3\u679c\u4e3adGl0bGU9IlVTRyBGTEVYIg==</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">\u3010app=&quot;APACHE-hadoop-YARN&quot;\u3011\u7684\u52a0\u5bc6\u7ed3\u679c\u4e3aYXBwPSJBUEFDSEUtaGFkb29wLVlBUk4i</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">\u3010&quot;Simple File List&quot;\u3011\u7684\u52a0\u5bc6\u7ed3\u679c\u4e3aIlNpbXBsZSBGaWxlIExpc3Qi</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; mar"
                        "gin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">\u3010&quot;VoIPmonitor&quot;\u3011\u7684\u52a0\u5bc6\u7ed3\u679c\u4e3aIlZvSVBtb25pdG9yIg==</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">\u3010&quot;ClickHouse&quot; &amp;&amp; body=&quot;ok&quot;\u3011\u7684\u52a0\u5bc6\u7ed3\u679c\u4e3aIkNsaWNrSG91c2UiICYmIGJvZHk9Im9rIg==</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">\u3010app=&quot;\u6cdb\u5fae-\u534f\u540c\u529e\u516cOA&quot;\u3011\u7684\u52a0\u5bc6\u7ed3\u679c\u4e3aYXBwPSLms5vlvq4t5Y2P5ZCM5Yqe5YWsT0Ei</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">\u3010app=&quot;\u6cdb\u5fae-E-Weaver&quot;\u3011"
                        "\u7684\u52a0\u5bc6\u7ed3\u679c\u4e3aYXBwPSLms5vlvq4tRS1XZWF2ZXIi</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">\u3010title=&quot;Ruby On Rails&quot;\u3011\u7684\u52a0\u5bc6\u7ed3\u679c\u4e3adGl0bGU9IlJ1YnkgT24gUmFpbHMi</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">\u3010app=&quot;Landray-OA\u7cfb\u7edf&quot;\u3011\u7684\u52a0\u5bc6\u7ed3\u679c\u4e3aYXBwPSJMYW5kcmF5LU9B57O757ufIg==</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">\u3010app=&quot;\u5c0f\u7c73\u8def\u7531\u5668&quot;\u3011\u7684\u52a0\u5bc6\u7ed3\u679c\u4e3aYXBwPSLlsI/nsbPot6/nlLHlmagi</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-bl"
                        "ock-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">\u3010body=&quot;DAP-1360&quot; &amp;&amp; body=&quot;6.05&quot;\u3011\u7684\u52a0\u5bc6\u7ed3\u679c\u4e3aYm9keT0iREFQLTEzNjAiICYmIGJvZHk9IjYuMDUi</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">\u3010&quot;Franklin Fueling Systems&quot;\u3011\u7684\u52a0\u5bc6\u7ed3\u679c\u4e3aIkZyYW5rbGluIEZ1ZWxpbmcgU3lzdGVtcyI=</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">\u3010app=&quot;ZABBIX-\u76d1\u63a7\u7cfb\u7edf&quot;\u3011\u7684\u52a0\u5bc6\u7ed3\u679c\u4e3aYXBwPSJaQUJCSVgt55uR5o6n57O757ufIg==</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">\u3010app=&quot;ZABBIX-\u76d1\u63a7\u7cfb\u7edf&quot"
                        "; &amp;&amp; body=&quot;saml&quot;\u3011\u7684\u52a0\u5bc6\u7ed3\u679c\u4e3aYXBwPSJaQUJCSVgt55uR5o6n57O757ufIiAmJiBib2R5PSJzYW1sIg==</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">\u3010title=&quot;Spark Master at&quot;\u3011\u7684\u52a0\u5bc6\u7ed3\u679c\u4e3adGl0bGU9IlNwYXJrIE1hc3RlciBhdCI=</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">\u3010app=&quot;Doccms&quot;\u3011\u7684\u52a0\u5bc6\u7ed3\u679c\u4e3aYXBwPSJEb2NjbXMi</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">\u3010&quot;Fikker\u7ba1\u7406\u5e73\u53f0&quot;\u3011\u7684\u52a0\u5bc6\u7ed3\u679c\u4e3aIkZpa2tlcueuoeeQhuW5s+WPsCI=</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; mar"
                        "gin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">\u3010app=&quot;IceWarp-\u516c\u53f8\u4ea7\u54c1&quot;\u3011\u7684\u52a0\u5bc6\u7ed3\u679c\u4e3aYXBwPSJJY2VXYXJwLeWFrOWPuOS6p+WTgSI=</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">\u3010title=&quot;Node-RED&quot;\u3011\u7684\u52a0\u5bc6\u7ed3\u679c\u4e3adGl0bGU9Ik5vZGUtUkVEIg==</span></p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.addtoBase64), QCoreApplication.translate("MainWindow", u"Base64\u52a0\u5bc6", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"               \u7f51\u5eb7\u4e0b\u4e00\u4ee3\u9632\u706b\u5899 getshell              ", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"              \u91d1\u8776OA Apusic\u5e94\u7528\u670d\u52a1\u5668(\u4e2d\u95f4\u4ef6) server_file \u76ee\u5f55\u904d\u5386\u6f0f\u6d1e              ", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"               x-ui\u9762\u677f\u722c\u866b\u722c\u53d6\u53ca\u767b\u9646\u5206\u4eab              ", None))
        self.pushButton_126.setText(QCoreApplication.translate("MainWindow", u"      ClickHouse API \u6570\u636e\u5e93\u63a5\u53e3\u672a\u6388\u6743\u8bbf\u95ee\u6f0f\u6d1e      ", None))
        self.pushButton_118.setText(QCoreApplication.translate("MainWindow", u"      Apache Hadoop Yarn RPC \u8fdc\u7a0b\u547d\u4ee4\u6267\u884c\u6f0f\u6d1e      ", None))
        self.pushButton_123.setText(QCoreApplication.translate("MainWindow", u"      Apache Spark \u8fdc\u7a0b\u547d\u4ee4\u6267\u884c\u6f0f\u6d1e(CVE-2022-33891)\u4e00\u628a\u68ad      ", None))
        self.pushButton_150.setText(QCoreApplication.translate("MainWindow", u"DrayTek\u4f01\u4e1a\u7f51\u7edc\u8bbe\u5907\u8fdc\u7a0b\u547d\u4ee4\u6267\u884c\u6f0f\u6d1e(CVE_2022_8515)", None))
        self.pushButton_153.setText(QCoreApplication.translate("MainWindow", u"VMware\u670d\u52a1\u7aef\u6a21\u677f\u6ce8\u5165\u6f0f\u6d1e(CVE-2022-22954)\u4e00\u628a\u68ad", None))
        self.pushButton_145.setText(QCoreApplication.translate("MainWindow", u"D-Link DCS\u7cfb\u5217\u76d1\u63a7 \u8d26\u53f7\u5bc6\u7801\u4fe1\u606f\u6cc4\u9732\u6f0f\u6d1e(CVE_2020_25078)", None))
        self.pushButton_127.setText(QCoreApplication.translate("MainWindow", u"DedeCMS v5.7.87 SQL\u6ce8\u5165\u6f0f\u6d1e(CVE-2022-23337)\u4e00\u628a\u68ad", None))
        self.pushButton_132.setText(QCoreApplication.translate("MainWindow", u"WSO2\u8fdc\u7a0b\u547d\u4ee4\u6267\u884c\u6f0f\u6d1e(CVE-2022-29464)\u4e00\u628a\u68ad", None))
        self.pushButton_135.setText(QCoreApplication.translate("MainWindow", u"D-LINK DAP-2020 webproc \u4efb\u610f\u6587\u4ef6\u8bfb\u53d6\u6f0f\u6d1e(CVE-2021-27250)\u4e00\u628a\u68ad", None))
        self.pushButton_202.setText(QCoreApplication.translate("MainWindow", u"      \u5f85\u6dfb\u52a0      ", None))
        self.pushButton_207.setText(QCoreApplication.translate("MainWindow", u"      \u5f85\u6dfb\u52a0      ", None))
        self.pushButton_203.setText(QCoreApplication.translate("MainWindow", u"      \u5f85\u6dfb\u52a0      ", None))
        self.pushButton_200.setText(QCoreApplication.translate("MainWindow", u"      \u5f85\u6dfb\u52a0      ", None))
        self.pushButton_199.setText(QCoreApplication.translate("MainWindow", u"      \u5f85\u6dfb\u52a0      ", None))
        self.pushButton_204.setText(QCoreApplication.translate("MainWindow", u"      \u5f85\u6dfb\u52a0      ", None))
        self.pushButton_168.setText(QCoreApplication.translate("MainWindow", u"      \u5f85\u6dfb\u52a0      ", None))
        self.pushButton_164.setText(QCoreApplication.translate("MainWindow", u"      \u5f85\u6dfb\u52a0      ", None))
        self.pushButton_167.setText(QCoreApplication.translate("MainWindow", u"      \u5f85\u6dfb\u52a0      ", None))
        self.pushButton_163.setText(QCoreApplication.translate("MainWindow", u"      \u5f85\u6dfb\u52a0      ", None))
        self.pushButton_171.setText(QCoreApplication.translate("MainWindow", u"      \u5f85\u6dfb\u52a0      ", None))
        self.pushButton_166.setText(QCoreApplication.translate("MainWindow", u"      \u5f85\u6dfb\u52a0      ", None))
        self.pushButton_193.setText(QCoreApplication.translate("MainWindow", u"      \u5f85\u6dfb\u52a0      ", None))
        self.pushButton_198.setText(QCoreApplication.translate("MainWindow", u"      \u5f85\u6dfb\u52a0      ", None))
        self.pushButton_190.setText(QCoreApplication.translate("MainWindow", u"      \u5f85\u6dfb\u52a0      ", None))
        self.pushButton_195.setText(QCoreApplication.translate("MainWindow", u"      \u5f85\u6dfb\u52a0      ", None))
        self.pushButton_194.setText(QCoreApplication.translate("MainWindow", u"      \u5f85\u6dfb\u52a0      ", None))
        self.pushButton_191.setText(QCoreApplication.translate("MainWindow", u"      \u5f85\u6dfb\u52a0      ", None))
        self.pushButton_184.setText(QCoreApplication.translate("MainWindow", u"      \u5f85\u6dfb\u52a0      ", None))
        self.pushButton_181.setText(QCoreApplication.translate("MainWindow", u"      \u5f85\u6dfb\u52a0      ", None))
        self.pushButton_186.setText(QCoreApplication.translate("MainWindow", u"      \u5f85\u6dfb\u52a0      ", None))
        self.pushButton_185.setText(QCoreApplication.translate("MainWindow", u"      \u5f85\u6dfb\u52a0      ", None))
        self.pushButton_189.setText(QCoreApplication.translate("MainWindow", u"      \u5f85\u6dfb\u52a0      ", None))
        self.pushButton_182.setText(QCoreApplication.translate("MainWindow", u"      \u5f85\u6dfb\u52a0      ", None))
        self.pushButton_117.setText(QCoreApplication.translate("MainWindow", u"      \u5f85\u6dfb\u52a0      ", None))
        self.pushButton_115.setText(QCoreApplication.translate("MainWindow", u"      \u5f85\u6dfb\u52a0      ", None))
        self.pushButton_113.setText(QCoreApplication.translate("MainWindow", u"      \u5f85\u6dfb\u52a0      ", None))
        self.pushButton_110.setText(QCoreApplication.translate("MainWindow", u"      \u5f85\u6dfb\u52a0      ", None))
        self.pushButton_114.setText(QCoreApplication.translate("MainWindow", u"      \u5f85\u6dfb\u52a0      ", None))
        self.pushButton_109.setText(QCoreApplication.translate("MainWindow", u"      \u5f85\u6dfb\u52a0      ", None))
        self.pushButton_159.setText(QCoreApplication.translate("MainWindow", u"      \u5f85\u6dfb\u52a0      ", None))
        self.pushButton_158.setText(QCoreApplication.translate("MainWindow", u"      \u5f85\u6dfb\u52a0      ", None))
        self.pushButton_162.setText(QCoreApplication.translate("MainWindow", u"      \u5f85\u6dfb\u52a0      ", None))
        self.pushButton_157.setText(QCoreApplication.translate("MainWindow", u"      \u5f85\u6dfb\u52a0      ", None))
        self.pushButton_155.setText(QCoreApplication.translate("MainWindow", u"      \u5f85\u6dfb\u52a0      ", None))
        self.pushButton_154.setText(QCoreApplication.translate("MainWindow", u"      \u5f85\u6dfb\u52a0      ", None))
        self.pushButton_176.setText(QCoreApplication.translate("MainWindow", u"      \u5f85\u6dfb\u52a0      ", None))
        self.pushButton_177.setText(QCoreApplication.translate("MainWindow", u"      \u5f85\u6dfb\u52a0      ", None))
        self.pushButton_180.setText(QCoreApplication.translate("MainWindow", u"      \u5f85\u6dfb\u52a0      ", None))
        self.pushButton_172.setText(QCoreApplication.translate("MainWindow", u"      \u5f85\u6dfb\u52a0      ", None))
        self.pushButton_173.setText(QCoreApplication.translate("MainWindow", u"      \u5f85\u6dfb\u52a0      ", None))
        self.pushButton_175.setText(QCoreApplication.translate("MainWindow", u"      \u5f85\u6dfb\u52a0      ", None))
        self.pushButton_209.setText(QCoreApplication.translate("MainWindow", u"      \u5f85\u6dfb\u52a0      ", None))
        self.pushButton_213.setText(QCoreApplication.translate("MainWindow", u"      \u5f85\u6dfb\u52a0      ", None))
        self.pushButton_208.setText(QCoreApplication.translate("MainWindow", u"      \u5f85\u6dfb\u52a0      ", None))
        self.pushButton_212.setText(QCoreApplication.translate("MainWindow", u"      \u5f85\u6dfb\u52a0      ", None))
        self.pushButton_216.setText(QCoreApplication.translate("MainWindow", u"      \u5f85\u6dfb\u52a0      ", None))
        self.pushButton_211.setText(QCoreApplication.translate("MainWindow", u"      \u5f85\u6dfb\u52a0      ", None))
        self.pushButton_218.setText(QCoreApplication.translate("MainWindow", u"      \u5f85\u6dfb\u52a0      ", None))
        self.pushButton_225.setText(QCoreApplication.translate("MainWindow", u"      \u5f85\u6dfb\u52a0      ", None))
        self.pushButton_221.setText(QCoreApplication.translate("MainWindow", u"      \u5f85\u6dfb\u52a0      ", None))
        self.pushButton_220.setText(QCoreApplication.translate("MainWindow", u"      \u5f85\u6dfb\u52a0      ", None))
        self.pushButton_217.setText(QCoreApplication.translate("MainWindow", u"      \u5f85\u6dfb\u52a0      ", None))
        self.pushButton_222.setText(QCoreApplication.translate("MainWindow", u"      \u5f85\u6dfb\u52a0      ", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), QCoreApplication.translate("MainWindow", u"\u6f0f\u6d1ePoc\u96c6\u5408", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), QCoreApplication.translate("MainWindow", u"\u6f0f\u6d1eExp\u96c6\u5408", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Ndaytools), QCoreApplication.translate("MainWindow", u"Nday\u96c6\u5408", None))
        self.groupBox_7.setTitle(QCoreApplication.translate("MainWindow", u"IP\u53cd\u67e5\u57df\u540d", None))
        self.iptodomain.setText(QCoreApplication.translate("MainWindow", u"\u67e5\u8be2", None))
        self.clear_iptodomain.setText(QCoreApplication.translate("MainWindow", u"\u6e05\u9664\u67e5\u8be2\u7ed3\u679c", None))
        self.groupBox_8.setTitle(QCoreApplication.translate("MainWindow", u"\u57df\u540d\u67e5\u8be2\u6743\u91cd", None))
        self.domaintorank.setText(QCoreApplication.translate("MainWindow", u"\u67e5\u8be2", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.IptoDomain), QCoreApplication.translate("MainWindow", u"IP\u53cd\u67e5\u57df\u540d&&\u6743\u91cd\u67e5\u8be2", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u8f6f\u4ef6\u8bbe\u7f6e", None))
        self.menu_2.setTitle(QCoreApplication.translate("MainWindow", u"\u64cd\u4f5c", None))
        self.menu_3.setTitle(QCoreApplication.translate("MainWindow", u"\u5e2e\u52a9", None))
        self.menu_4.setTitle(QCoreApplication.translate("MainWindow", u"\u95ee\u9898", None))
    # retranslateUi


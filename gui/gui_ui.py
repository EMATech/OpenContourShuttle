# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gui.ui'
##
## Created by: Qt User Interface Compiler version 6.0.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_GUI(object):
    def setupUi(self, GUI):
        if not GUI.objectName():
            GUI.setObjectName(u"GUI")
        GUI.resize(600, 643)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(GUI.sizePolicy().hasHeightForWidth())
        GUI.setSizePolicy(sizePolicy)
        GUI.setMinimumSize(QSize(600, 643))
        self.centralwidget = QWidget(GUI)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setEnabled(True)
        self.centralwidget.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setStyleSheet(u"background: url(images/ShuttleXpress_Black.png);\n"
                                         "                    background-repeat:no-repeat;\n"
                                         "                ")
        self.dial = QDial(self.centralwidget)
        self.dial.setObjectName(u"dial")
        self.dial.setGeometry(QRect(190, 170, 230, 230))
        self.dial.setStyleSheet(u"background-color: black;")
        self.dial.setMaximum(255)
        self.dial.setSliderPosition(128)
        self.wheel_pos1 = QRadioButton(self.centralwidget)
        self.wheel_pos1.setObjectName(u"wheel_pos1")
        self.wheel_pos1.setGeometry(QRect(340, 155, 16, 20))
        self.wheel_pos1.setStyleSheet(u"color: white;")
        self.wheel_neg3 = QRadioButton(self.centralwidget)
        self.wheel_neg3.setObjectName(u"wheel_neg3")
        self.wheel_neg3.setGeometry(QRect(182, 215, 16, 20))
        self.wheel_neg3.setStyleSheet(u"color: white;")
        self.wheel_pos7 = QRadioButton(self.centralwidget)
        self.wheel_pos7.setObjectName(u"wheel_pos7")
        self.wheel_pos7.setGeometry(QRect(384, 382, 16, 20))
        self.wheel_pos7.setStyleSheet(u"background: #000000ff;\n"
                                      "                        color: white;\n"
                                      "                    ")
        self.wheel_neg4 = QRadioButton(self.centralwidget)
        self.wheel_neg4.setObjectName(u"wheel_neg4")
        self.wheel_neg4.setGeometry(QRect(166, 257, 16, 20))
        self.wheel_neg4.setStyleSheet(u"background: #000000ff;\n"
                                      "                        color: white;\n"
                                      "                    ")
        self.wheel_neg6 = QRadioButton(self.centralwidget)
        self.wheel_neg6.setObjectName(u"wheel_neg6")
        self.wheel_neg6.setGeometry(QRect(181, 345, 16, 20))
        self.wheel_neg6.setStyleSheet(u"color: white;")
        self.wheel_neg5 = QRadioButton(self.centralwidget)
        self.wheel_neg5.setObjectName(u"wheel_neg5")
        self.wheel_neg5.setGeometry(QRect(166, 300, 16, 20))
        self.wheel_neg5.setStyleSheet(u"color: white;")
        self.wheel_neg1 = QRadioButton(self.centralwidget)
        self.wheel_neg1.setObjectName(u"wheel_neg1")
        self.wheel_neg1.setGeometry(QRect(251, 155, 16, 20))
        self.wheel_neg1.setStyleSheet(u"background: #000000ff;\n"
                                      "                        color: white;\n"
                                      "                    ")
        self.wheel_pos2 = QRadioButton(self.centralwidget)
        self.wheel_pos2.setObjectName(u"wheel_pos2")
        self.wheel_pos2.setGeometry(QRect(380, 178, 16, 20))
        self.wheel_pos2.setStyleSheet(u"background: #000000ff;\n"
                                      "                        color: white;\n"
                                      "                    ")
        self.wheel_pos6 = QRadioButton(self.centralwidget)
        self.wheel_pos6.setObjectName(u"wheel_pos6")
        self.wheel_pos6.setGeometry(QRect(413, 345, 16, 20))
        self.wheel_pos6.setStyleSheet(u"background: #000000ff;\n"
                                      "                        color: white;\n"
                                      "                    ")
        self.button_1 = QCheckBox(self.centralwidget)
        self.button_1.setObjectName(u"button_1")
        self.button_1.setGeometry(QRect(60, 270, 75, 24))
        self.button_1.setStyleSheet(u"background: #000000ff;\n"
                                    "                        color: white;\n"
                                    "                    ")
        self.wheel_pos4 = QRadioButton(self.centralwidget)
        self.wheel_pos4.setObjectName(u"wheel_pos4")
        self.wheel_pos4.setGeometry(QRect(428, 257, 16, 20))
        self.wheel_pos4.setStyleSheet(u"background: #000000ff;\n"
                                      "                        color: white;\n"
                                      "                    ")
        self.wheel_pos5 = QRadioButton(self.centralwidget)
        self.wheel_pos5.setObjectName(u"wheel_pos5")
        self.wheel_pos5.setGeometry(QRect(427, 300, 16, 20))
        self.wheel_pos5.setStyleSheet(u"background: #000000ff;\n"
                                      "                        color: white;\n"
                                      "                    ")
        self.wheel_neg2 = QRadioButton(self.centralwidget)
        self.wheel_neg2.setObjectName(u"wheel_neg2")
        self.wheel_neg2.setGeometry(QRect(210, 178, 16, 20))
        self.wheel_neg2.setStyleSheet(u"background: #000000ff;\n"
                                      "                        color: white;\n"
                                      "                    ")
        self.wheel_cent0 = QRadioButton(self.centralwidget)
        self.wheel_cent0.setObjectName(u"wheel_cent0")
        self.wheel_cent0.setGeometry(QRect(297, 147, 16, 20))
        self.wheel_cent0.setStyleSheet(u"background: #000000ff;\n"
                                       "                        color: white;\n"
                                       "                    ")
        self.wheel_cent0.setChecked(True)
        self.wheel_pos3 = QRadioButton(self.centralwidget)
        self.wheel_pos3.setObjectName(u"wheel_pos3")
        self.wheel_pos3.setGeometry(QRect(413, 215, 16, 20))
        self.wheel_pos3.setStyleSheet(u"background: #000000ff;\n"
                                      "                        color: white;\n"
                                      "                    ")
        self.wheel_neg7 = QRadioButton(self.centralwidget)
        self.wheel_neg7.setObjectName(u"wheel_neg7")
        self.wheel_neg7.setGeometry(QRect(210, 382, 16, 20))
        self.wheel_neg7.setStyleSheet(u"color: white;")
        self.button_2 = QCheckBox(self.centralwidget)
        self.button_2.setObjectName(u"button_2")
        self.button_2.setGeometry(QRect(130, 120, 75, 24))
        self.button_2.setStyleSheet(u"background: #000000ff;\n"
                                    "                        color: white;\n"
                                    "                    ")
        self.button_4 = QCheckBox(self.centralwidget)
        self.button_4.setObjectName(u"button_4")
        self.button_4.setGeometry(QRect(400, 120, 75, 24))
        self.button_4.setStyleSheet(u"background: #000000ff;\n"
                                    "                        color: white;\n"
                                    "                    ")
        self.button_5 = QCheckBox(self.centralwidget)
        self.button_5.setObjectName(u"button_5")
        self.button_5.setGeometry(QRect(470, 270, 75, 24))
        self.button_5.setStyleSheet(u"background: #000000ff;\n"
                                    "                        color: white;\n"
                                    "                    ")
        self.button_3 = QCheckBox(self.centralwidget)
        self.button_3.setObjectName(u"button_3")
        self.button_3.setGeometry(QRect(270, 70, 75, 24))
        self.button_3.setStyleSheet(u"background: #000000ff;\n"
                                    "                        color: white;\n"
                                    "                    ")
        GUI.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(GUI)
        self.statusbar.setObjectName(u"statusbar")
        GUI.setStatusBar(self.statusbar)
        self.menubar = QMenuBar(GUI)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 600, 22))
        GUI.setMenuBar(self.menubar)
        QWidget.setTabOrder(self.button_1, self.button_2)
        QWidget.setTabOrder(self.button_2, self.button_3)
        QWidget.setTabOrder(self.button_3, self.button_4)
        QWidget.setTabOrder(self.button_4, self.button_5)
        QWidget.setTabOrder(self.button_5, self.wheel_neg7)
        QWidget.setTabOrder(self.wheel_neg7, self.wheel_neg6)
        QWidget.setTabOrder(self.wheel_neg6, self.wheel_neg5)
        QWidget.setTabOrder(self.wheel_neg5, self.wheel_neg4)
        QWidget.setTabOrder(self.wheel_neg4, self.wheel_neg3)
        QWidget.setTabOrder(self.wheel_neg3, self.wheel_neg2)
        QWidget.setTabOrder(self.wheel_neg2, self.wheel_neg1)
        QWidget.setTabOrder(self.wheel_neg1, self.wheel_cent0)
        QWidget.setTabOrder(self.wheel_cent0, self.wheel_pos1)
        QWidget.setTabOrder(self.wheel_pos1, self.wheel_pos2)
        QWidget.setTabOrder(self.wheel_pos2, self.wheel_pos3)
        QWidget.setTabOrder(self.wheel_pos3, self.wheel_pos4)
        QWidget.setTabOrder(self.wheel_pos4, self.wheel_pos5)
        QWidget.setTabOrder(self.wheel_pos5, self.wheel_pos6)
        QWidget.setTabOrder(self.wheel_pos6, self.wheel_pos7)
        QWidget.setTabOrder(self.wheel_pos7, self.dial)

        self.retranslateUi(GUI)

        QMetaObject.connectSlotsByName(GUI)
    # setupUi

    def retranslateUi(self, GUI):
        GUI.setWindowTitle(QCoreApplication.translate("GUI", u"GUI", None))
        self.wheel_pos1.setText("")
        self.wheel_neg3.setText("")
        self.wheel_pos7.setText("")
        self.wheel_neg4.setText(QCoreApplication.translate("GUI", u"-", None))
        self.wheel_neg6.setText("")
        self.wheel_neg5.setText("")
        self.wheel_neg1.setText("")
        self.wheel_pos2.setText("")
        self.wheel_pos6.setText("")
        self.button_1.setText(QCoreApplication.translate("GUI", u"Button 1", None))
        self.wheel_pos4.setText("")
        self.wheel_pos5.setText("")
        self.wheel_neg2.setText("")
        self.wheel_cent0.setText("")
        self.wheel_pos3.setText("")
        self.wheel_neg7.setText("")
        self.button_2.setText(QCoreApplication.translate("GUI", u"Button 2", None))
        self.button_4.setText(QCoreApplication.translate("GUI", u"Button 4", None))
        self.button_5.setText(QCoreApplication.translate("GUI", u"Button 5", None))
        self.button_3.setText(QCoreApplication.translate("GUI", u"Button 3", None))
    # retranslateUi


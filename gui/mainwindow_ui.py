# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.2.2
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QDial, QDockWidget,
    QFrame, QMainWindow, QPushButton, QRadioButton,
    QSizePolicy, QStatusBar, QTabWidget, QTextEdit,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowModality(Qt.ApplicationModal)
        MainWindow.resize(600, 600)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(600, 600))
        MainWindow.setMaximumSize(QSize(600, 600))
        MainWindow.setBaseSize(QSize(600, 600))
        font = QFont()
        font.setPointSize(12)
        font.setKerning(True)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"")
        MainWindow.setDocumentMode(False)
        MainWindow.setTabShape(QTabWidget.Rounded)
        MainWindow.setDockOptions(QMainWindow.AllowTabbedDocks|QMainWindow.AnimatedDocks)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.action_Quit = QAction(MainWindow)
        self.action_Quit.setObjectName(u"action_Quit")
        self.main_widget = QWidget(MainWindow)
        self.main_widget.setObjectName(u"main_widget")
        self.main_widget.setEnabled(True)
        self.main_widget.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.main_widget.setAutoFillBackground(False)
        self.main_widget.setStyleSheet(u"QWidget#main_widget {background: url(images/ShuttleXpress_Black.png);\n"
"     background-repeat:no-repeat;}\n"
"    ")
        self.dial = QDial(self.main_widget)
        self.dial.setObjectName(u"dial")
        self.dial.setGeometry(QRect(197, 178, 216, 216))
        self.dial.setAutoFillBackground(False)
        self.dial.setStyleSheet(u"background-color: black;")
        self.dial.setMaximum(9)
        self.dial.setPageStep(9)
        self.dial.setSliderPosition(2)
        self.dial.setInvertedAppearance(False)
        self.dial.setInvertedControls(False)
        self.dial.setWrapping(True)
        self.dial.setNotchTarget(3.700000000000000)
        self.dial.setNotchesVisible(False)
        self.wheel_pos1 = QRadioButton(self.main_widget)
        self.wheel_pos1.setObjectName(u"wheel_pos1")
        self.wheel_pos1.setGeometry(QRect(332, 151, 24, 24))
        self.wheel_pos1.setStyleSheet(u"color: white;")
        self.wheel_neg3 = QRadioButton(self.main_widget)
        self.wheel_neg3.setObjectName(u"wheel_neg3")
        self.wheel_neg3.setGeometry(QRect(174, 211, 24, 24))
        self.wheel_neg3.setStyleSheet(u"color: white;")
        self.wheel_pos7 = QRadioButton(self.main_widget)
        self.wheel_pos7.setObjectName(u"wheel_pos7")
        self.wheel_pos7.setGeometry(QRect(376, 378, 24, 24))
        self.wheel_pos7.setStyleSheet(u"background: #000000ff;\n"
"      color: white;\n"
"     ")
        self.wheel_neg4 = QRadioButton(self.main_widget)
        self.wheel_neg4.setObjectName(u"wheel_neg4")
        self.wheel_neg4.setGeometry(QRect(158, 253, 24, 24))
        self.wheel_neg4.setStyleSheet(u"background: #000000ff;\n"
"      color: white;\n"
"     ")
        self.wheel_neg6 = QRadioButton(self.main_widget)
        self.wheel_neg6.setObjectName(u"wheel_neg6")
        self.wheel_neg6.setGeometry(QRect(173, 341, 24, 24))
        self.wheel_neg6.setStyleSheet(u"color: white;")
        self.wheel_neg5 = QRadioButton(self.main_widget)
        self.wheel_neg5.setObjectName(u"wheel_neg5")
        self.wheel_neg5.setGeometry(QRect(158, 296, 24, 24))
        self.wheel_neg5.setStyleSheet(u"color: white;")
        self.wheel_neg1 = QRadioButton(self.main_widget)
        self.wheel_neg1.setObjectName(u"wheel_neg1")
        self.wheel_neg1.setGeometry(QRect(243, 151, 24, 24))
        self.wheel_neg1.setStyleSheet(u"background: #000000ff;\n"
"      color: white;\n"
"     ")
        self.wheel_pos2 = QRadioButton(self.main_widget)
        self.wheel_pos2.setObjectName(u"wheel_pos2")
        self.wheel_pos2.setGeometry(QRect(372, 174, 24, 24))
        self.wheel_pos2.setStyleSheet(u"background: #000000ff;\n"
"      color: white;\n"
"     ")
        self.wheel_pos6 = QRadioButton(self.main_widget)
        self.wheel_pos6.setObjectName(u"wheel_pos6")
        self.wheel_pos6.setGeometry(QRect(405, 341, 24, 24))
        self.wheel_pos6.setStyleSheet(u"background: #000000ff;\n"
"      color: white;\n"
"     ")
        self.button_1 = QCheckBox(self.main_widget)
        self.button_1.setObjectName(u"button_1")
        self.button_1.setGeometry(QRect(80, 266, 24, 24))
        font1 = QFont()
        font1.setPointSize(12)
        self.button_1.setFont(font1)
        self.button_1.setStyleSheet(u"background: #000000ff;\n"
"      color: white;\n"
"     ")
        self.wheel_pos4 = QRadioButton(self.main_widget)
        self.wheel_pos4.setObjectName(u"wheel_pos4")
        self.wheel_pos4.setGeometry(QRect(420, 253, 24, 24))
        self.wheel_pos4.setStyleSheet(u"background: #000000ff;\n"
"      color: white;\n"
"     ")
        self.wheel_pos5 = QRadioButton(self.main_widget)
        self.wheel_pos5.setObjectName(u"wheel_pos5")
        self.wheel_pos5.setGeometry(QRect(419, 296, 24, 24))
        self.wheel_pos5.setStyleSheet(u"background: #000000ff;\n"
"      color: white;\n"
"     ")
        self.wheel_neg2 = QRadioButton(self.main_widget)
        self.wheel_neg2.setObjectName(u"wheel_neg2")
        self.wheel_neg2.setGeometry(QRect(202, 174, 24, 24))
        self.wheel_neg2.setStyleSheet(u"background: #000000ff;\n"
"      color: white;\n"
"     ")
        self.wheel_cent0 = QRadioButton(self.main_widget)
        self.wheel_cent0.setObjectName(u"wheel_cent0")
        self.wheel_cent0.setGeometry(QRect(289, 143, 24, 24))
        self.wheel_cent0.setStyleSheet(u"background: #000000ff;\n"
"      color: white;\n"
"     ")
        self.wheel_cent0.setChecked(True)
        self.wheel_pos3 = QRadioButton(self.main_widget)
        self.wheel_pos3.setObjectName(u"wheel_pos3")
        self.wheel_pos3.setGeometry(QRect(405, 211, 24, 24))
        self.wheel_pos3.setStyleSheet(u"background: #000000ff;\n"
"      color: white;\n"
"     ")
        self.wheel_neg7 = QRadioButton(self.main_widget)
        self.wheel_neg7.setObjectName(u"wheel_neg7")
        self.wheel_neg7.setGeometry(QRect(202, 378, 24, 24))
        self.wheel_neg7.setStyleSheet(u"color: white;")
        self.button_2 = QCheckBox(self.main_widget)
        self.button_2.setObjectName(u"button_2")
        self.button_2.setGeometry(QRect(156, 122, 24, 24))
        self.button_2.setFont(font1)
        self.button_2.setStyleSheet(u"background: #000000ff;\n"
"      color: white;\n"
"     ")
        self.button_4 = QCheckBox(self.main_widget)
        self.button_4.setObjectName(u"button_4")
        self.button_4.setGeometry(QRect(430, 122, 24, 24))
        self.button_4.setFont(font1)
        self.button_4.setLayoutDirection(Qt.RightToLeft)
        self.button_4.setAutoFillBackground(False)
        self.button_4.setStyleSheet(u"background: #000000ff;\n"
"      color: white;\n"
"     ")
        self.button_5 = QCheckBox(self.main_widget)
        self.button_5.setObjectName(u"button_5")
        self.button_5.setGeometry(QRect(498, 266, 24, 24))
        self.button_5.setFont(font1)
        self.button_5.setLayoutDirection(Qt.RightToLeft)
        self.button_5.setStyleSheet(u"background: #000000ff;\n"
"      color: white;\n"
"     ")
        self.button_3 = QCheckBox(self.main_widget)
        self.button_3.setObjectName(u"button_3")
        self.button_3.setGeometry(QRect(290, 72, 24, 24))
        self.button_3.setFont(font1)
        self.button_3.setStyleSheet(u"background: #000000ff;\n"
"      color: white;\n"
"     ")
        self.button_3.setTristate(True)
        self.about_button = QPushButton(self.main_widget)
        self.about_button.setObjectName(u"about_button")
        self.about_button.setGeometry(QRect(576, 0, 24, 24))
        font2 = QFont()
        font2.setPointSize(9)
        font2.setBold(True)
        self.about_button.setFont(font2)
        self.about_button.setCursor(QCursor(Qt.WhatsThisCursor))
        self.about_button.setCheckable(False)
        self.about_button.setFlat(True)
        MainWindow.setCentralWidget(self.main_widget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.about_widget = QDockWidget(MainWindow)
        self.about_widget.setObjectName(u"about_widget")
        self.about_widget.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.about_widget.sizePolicy().hasHeightForWidth())
        self.about_widget.setSizePolicy(sizePolicy1)
        self.about_widget.setMinimumSize(QSize(580, 574))
        self.about_widget.setFloating(False)
        self.about_widget.setFeatures(QDockWidget.DockWidgetClosable)
        self.about_widget.setAllowedAreas(Qt.RightDockWidgetArea)
        self.about_widget_contents = QWidget()
        self.about_widget_contents.setObjectName(u"about_widget_contents")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.about_widget_contents.sizePolicy().hasHeightForWidth())
        self.about_widget_contents.setSizePolicy(sizePolicy2)
        self.about_widget_contents.setAutoFillBackground(False)
        self.about_text = QTextEdit(self.about_widget_contents)
        self.about_text.setObjectName(u"about_text")
        self.about_text.setGeometry(QRect(0, 0, 560, 550))
        self.about_text.setFocusPolicy(Qt.WheelFocus)
        self.about_text.setAcceptDrops(False)
        self.about_text.setStyleSheet(u"color: white;")
        self.about_text.setFrameShape(QFrame.NoFrame)
        self.about_text.setFrameShadow(QFrame.Plain)
        self.about_text.setUndoRedoEnabled(False)
        self.about_text.setReadOnly(True)
        self.about_text.setAcceptRichText(True)
        self.about_widget.setWidget(self.about_widget_contents)
        MainWindow.addDockWidget(Qt.RightDockWidgetArea, self.about_widget)
        self.about_widget.raise_()
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

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Contour ShuttleXpress", None))
        self.action_Quit.setText(QCoreApplication.translate("MainWindow", u"&Quit", None))
        self.wheel_pos1.setText("")
        self.wheel_neg3.setText("")
        self.wheel_pos7.setText("")
        self.wheel_neg4.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.wheel_neg6.setText("")
        self.wheel_neg5.setText("")
        self.wheel_neg1.setText("")
        self.wheel_pos2.setText("")
        self.wheel_pos6.setText("")
        self.button_1.setText("")
        self.wheel_pos4.setText("")
        self.wheel_pos5.setText("")
        self.wheel_neg2.setText("")
        self.wheel_cent0.setText("")
        self.wheel_pos3.setText("")
        self.wheel_neg7.setText("")
        self.button_2.setText("")
        self.button_4.setText("")
        self.button_5.setText("")
        self.button_3.setText("")
        self.about_button.setText(QCoreApplication.translate("MainWindow", u"?", None))
    # retranslateUi


# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
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
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QSlider, QSpinBox, QVBoxLayout,
    QWidget)
import ui.resources

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(510, 416)
        icon = QIcon()
        icon.addFile(u":/icons/key_FILL0_wght400_GRAD0_opsz24.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"QWidget {\n"
"    background-color: #393e46;\n"
"    color: white;\n"
"    font-family: Verdana;\n"
"    font-size: 16pt;\n"
"    margin: 10px;\n"
"}\n"
"\n"
"QPushButton {\n"
"    border: 2px solid orangered;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton#btn_lowercase,\n"
"#btn_highercase, \n"
"#btn_nums, \n"
"#btn_specialsymbols {\n"
"    padding: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border-color: #364F6B;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    border: 4px solid #364F6B;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    border: 4px solid #002753;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    background-color: #002753;\n"
"    border-color: #364F6B;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"QWidget {\n"
"    background-color: #393e46;\n"
"    color: white;\n"
"    font-family: Verdana;\n"
"    font-size: 16pt;\n"
"    margin: 10px;\n"
"}\n"
"\n"
"QPushButton {\n"
"    border: 2px solid orangered;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton#btn_lowercase,\n"
"#btn_highercase, \n"
"#btn_nums, \n"
"#btn_specialsymbols {\n"
"    padding: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border-color: #364F6B;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    border: 4px solid #364F6B;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    border: 4px solid #002753;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    background-color: #002753;\n"
"    border-color: #364F6B;\n"
"}")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.icon_lock = QPushButton(self.centralwidget)
        self.icon_lock.setObjectName(u"icon_lock")
        self.icon_lock.setEnabled(False)
        self.icon_lock.setStyleSheet(u"border: none")
        icon1 = QIcon()
        icon1.addFile(u":/icons/lock_FILL0_wght400_GRAD0_opsz24.svg", QSize(), QIcon.Disabled, QIcon.On)
        self.icon_lock.setIcon(icon1)
        self.icon_lock.setIconSize(QSize(100, 100))

        self.verticalLayout.addWidget(self.icon_lock)

        self.layout_password = QHBoxLayout()
        self.layout_password.setObjectName(u"layout_password")
        self.frame_password = QFrame(self.centralwidget)
        self.frame_password.setObjectName(u"frame_password")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_password.sizePolicy().hasHeightForWidth())
        self.frame_password.setSizePolicy(sizePolicy)
        self.frame_password.setStyleSheet(u"QFrame {\n"
"    border: 2px solid orangered;\n"
"    border-radius: 5px;\n"
"    margin-right: 0;\n"
"}\n"
"\n"
"QFrame:hover {\n"
"    border-color: #364F6B;\n"
"    border-radius: 5px;\n"
"    margin-right: 0;\n"
"}")
        self.frame_password.setFrameShape(QFrame.StyledPanel)
        self.frame_password.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_password)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.line_password = QLineEdit(self.frame_password)
        self.line_password.setObjectName(u"line_password")
        self.line_password.setStyleSheet(u"QLineEdit {\n"
"    border: none;\n"
"    margin: 0;\n"
"    font-size: 20pt;\n"
"}")

        self.horizontalLayout_2.addWidget(self.line_password)

        self.btn_visibility = QPushButton(self.frame_password)
        self.btn_visibility.setObjectName(u"btn_visibility")
        self.btn_visibility.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_visibility.setStyleSheet(u"QPushButton { \n"
"    border: none;\n"
"    margin: 0;\n"
"    background-color: transparent;\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/icons/visibility_off_FILL0_wght400_GRAD0_opsz24.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon2.addFile(u":/icons/visibility_FILL0_wght400_GRAD0_opsz24.svg", QSize(), QIcon.Normal, QIcon.On)
        self.btn_visibility.setIcon(icon2)
        self.btn_visibility.setIconSize(QSize(30, 30))
        self.btn_visibility.setCheckable(True)

        self.horizontalLayout_2.addWidget(self.btn_visibility)


        self.layout_password.addWidget(self.frame_password)

        self.btn_refresh = QPushButton(self.centralwidget)
        self.btn_refresh.setObjectName(u"btn_refresh")
        self.btn_refresh.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_refresh.setStyleSheet(u"QPushButton {\n"
"    margin-right: 0;\n"
"    margin-left: 0;\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/icons/refresh_FILL0_wght400_GRAD0_opsz24.svg", QSize(), QIcon.Normal, QIcon.On)
        self.btn_refresh.setIcon(icon3)
        self.btn_refresh.setIconSize(QSize(52, 52))

        self.layout_password.addWidget(self.btn_refresh)

        self.btn_copy = QPushButton(self.centralwidget)
        self.btn_copy.setObjectName(u"btn_copy")
        self.btn_copy.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_copy.setStyleSheet(u"QPushButton {\n"
"    padding: 5px;\n"
"    margin-left: 0;\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u":/icons/content_copy_FILL0_wght400_GRAD0_opsz24.svg", QSize(), QIcon.Normal, QIcon.On)
        self.btn_copy.setIcon(icon4)
        self.btn_copy.setIconSize(QSize(42, 42))

        self.layout_password.addWidget(self.btn_copy)


        self.verticalLayout.addLayout(self.layout_password)

        self.layout_info = QHBoxLayout()
        self.layout_info.setObjectName(u"layout_info")
        self.lbl_strength = QLabel(self.centralwidget)
        self.lbl_strength.setObjectName(u"lbl_strength")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lbl_strength.sizePolicy().hasHeightForWidth())
        self.lbl_strength.setSizePolicy(sizePolicy1)
        self.lbl_strength.setAlignment(Qt.AlignCenter)

        self.layout_info.addWidget(self.lbl_strength)

        self.lbl_entropy = QLabel(self.centralwidget)
        self.lbl_entropy.setObjectName(u"lbl_entropy")
        sizePolicy1.setHeightForWidth(self.lbl_entropy.sizePolicy().hasHeightForWidth())
        self.lbl_entropy.setSizePolicy(sizePolicy1)
        self.lbl_entropy.setAlignment(Qt.AlignCenter)

        self.layout_info.addWidget(self.lbl_entropy)


        self.verticalLayout.addLayout(self.layout_info)

        self.layout_length = QHBoxLayout()
        self.layout_length.setObjectName(u"layout_length")
        self.slider_length = QSlider(self.centralwidget)
        self.slider_length.setObjectName(u"slider_length")
        self.slider_length.setCursor(QCursor(Qt.PointingHandCursor))
        self.slider_length.setStyleSheet(u"QSlider::groove:horizontal {\n"
"    background-color: transparent;\n"
"    height: 5px;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"    background-color: orangered;\n"
"}\n"
"\n"
"QSlider::add-page:horizontal {\n"
"    background-color: #364F6B;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background-color: white;\n"
"    width: 22px;\n"
"    border-radius: 10px;\n"
"    margin-top: -8px;\n"
"    margin-bottom: -8px;\n"
"}")
        self.slider_length.setMaximum(100)
        self.slider_length.setValue(12)
        self.slider_length.setOrientation(Qt.Horizontal)

        self.layout_length.addWidget(self.slider_length)

        self.spinbox_length = QSpinBox(self.centralwidget)
        self.spinbox_length.setObjectName(u"spinbox_length")
        self.spinbox_length.setCursor(QCursor(Qt.PointingHandCursor))
        self.spinbox_length.setStyleSheet(u"QSpinBox {\n"
"    border: 2px solid orangered;\n"
"    border-radius: 5px;\n"
"    background: transparent;\n"
"    padding: 2px;\n"
"}\n"
"\n"
"QSpinBox:hover {\n"
"    border-color: #364F6B;\n"
"}")
        self.spinbox_length.setAlignment(Qt.AlignCenter)
        self.spinbox_length.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.spinbox_length.setMaximum(100)
        self.spinbox_length.setValue(12)

        self.layout_length.addWidget(self.spinbox_length)


        self.verticalLayout.addLayout(self.layout_length)

        self.layout_characters = QHBoxLayout()
        self.layout_characters.setObjectName(u"layout_characters")
        self.btn_lowercase = QPushButton(self.centralwidget)
        self.btn_lowercase.setObjectName(u"btn_lowercase")
        self.btn_lowercase.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_lowercase.setCheckable(True)
        self.btn_lowercase.setChecked(False)

        self.layout_characters.addWidget(self.btn_lowercase)

        self.btn_highercase = QPushButton(self.centralwidget)
        self.btn_highercase.setObjectName(u"btn_highercase")
        self.btn_highercase.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_highercase.setCheckable(True)
        self.btn_highercase.setChecked(False)

        self.layout_characters.addWidget(self.btn_highercase)

        self.btn_nums = QPushButton(self.centralwidget)
        self.btn_nums.setObjectName(u"btn_nums")
        self.btn_nums.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_nums.setCheckable(True)
        self.btn_nums.setChecked(False)

        self.layout_characters.addWidget(self.btn_nums)

        self.btn_specialsymbols = QPushButton(self.centralwidget)
        self.btn_specialsymbols.setObjectName(u"btn_specialsymbols")
        self.btn_specialsymbols.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_specialsymbols.setCheckable(True)

        self.layout_characters.addWidget(self.btn_specialsymbols)


        self.verticalLayout.addLayout(self.layout_characters)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Password Generator", None))
        self.icon_lock.setText("")
        self.btn_visibility.setText("")
        self.btn_refresh.setText("")
        self.btn_copy.setText("")
        self.lbl_strength.setText("")
        self.lbl_entropy.setText("")
        self.btn_lowercase.setText(QCoreApplication.translate("MainWindow", u"a-z", None))
        self.btn_highercase.setText(QCoreApplication.translate("MainWindow", u"A-Z", None))
        self.btn_nums.setText(QCoreApplication.translate("MainWindow", u"0-9", None))
        self.btn_specialsymbols.setText(QCoreApplication.translate("MainWindow", u"#$%", None))
    # retranslateUi


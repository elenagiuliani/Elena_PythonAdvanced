# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'arUtil.ui'
##
## Created by: Qt User Interface Compiler version 6.10.0
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QLayout, QLineEdit, QPushButton, QRadioButton,
    QSizePolicy, QSpacerItem, QStackedWidget, QVBoxLayout,
    QWidget)
import app_imgs_rc

class Ui_arUtil(object):
    def setupUi(self, arUtil):
        if not arUtil.objectName():
            arUtil.setObjectName(u"arUtil")
        arUtil.resize(654, 450)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(arUtil.sizePolicy().hasHeightForWidth())
        arUtil.setSizePolicy(sizePolicy)
        icon = QIcon()
        icon.addFile(u":/images/icons/logo_store.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        arUtil.setWindowIcon(icon)
        arUtil.setStyleSheet(u"/* \n"
"my_white     = rgb(240, 240, 240);\n"
"my_black     = rgb(24, 25, 28);\n"
"dark_green  = rgb(31, 49, 0);\n"
"light_green  = rgb(71, 89, 30);\n"
" */\n"
"\n"
"QWidget {\n"
"color: rgb(240, 240, 240);  /* push btn text color */\n"
"background-color: rgb(24, 25, 28);  /* widgets background color */\n"
"}\n"
"\n"
"/* push btn */\n"
"QPushButton:hover {background-color: rgb(31, 49, 0); }\n"
"QPushButton:checked {background-color: rgb(71, 89, 30);}\n"
"QPushButton:disabled {color: rgb(100, 100, 100);} /* push btn text color, when disabled*/\n"
"QPushButton { color: rgb(240, 240, 240);}\n"
"\n"
"/* tabs */\n"
"QTabBar::tab:hover {background-color: rgb(31, 49, 0); }\n"
"QTabBar::tab:selected  {background-color: rgb(71, 89, 30);}\n"
"\n"
"/* line \n"
"4 is for horizontal line (5 for vertical line)*/\n"
"QFrame[frameShape=\"4\"]{\n"
"background-color: rgb(240, 240, 240);\n"
"max-height: 1px;\n"
"border: none;\n"
"}\n"
"QFrame[frameShape=\"5\"]{\n"
"background-color: rgb(240, 240, 240);\n"
"max-width: 1px;\n"
"bo"
                        "rder: none;\n"
"}\n"
"\n"
"/* scroll bar */\n"
"QScrollBar:vertical {\n"
"    background: transparent;\n"
"    width: 15px;\n"
"}\n"
"\n"
"/* list widget */\n"
"QListWidget::item:disabled {color: rgb(100, 100, 100); }\n"
"\n"
"/* RADIO BUTTONS */\n"
"QRadioButton::indicator {\n"
"width: 14px;\n"
"height: 14px;\n"
"}\n"
"/* Unchecked circle */\n"
"QRadioButton::indicator:unchecked {\n"
"border: 1px solid #666;\n"
"border-radius: 7px;\n"
"background: none;\n"
"}\n"
"/* Checked dot */\n"
"QRadioButton::indicator:checked {\n"
"border: 1px solid #666;\n"
"border-radius: 7px;\n"
"background-color: rgb(71, 89, 30);  /* DOT COLOR HERE */\n"
"}\n"
"\n"
"")
        self.gridLayout = QGridLayout(arUtil)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setVerticalSpacing(10)
        self.gridLayout.setContentsMargins(0, 7, 0, 0)
        self.wgFooter = QWidget(arUtil)
        self.wgFooter.setObjectName(u"wgFooter")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.wgFooter.sizePolicy().hasHeightForWidth())
        self.wgFooter.setSizePolicy(sizePolicy1)
        self.wgFooter.setMinimumSize(QSize(0, 0))
        self.wgFooter.setMaximumSize(QSize(16777215, 40))
        self.wgFooter.setStyleSheet(u"/* \n"
"my_white     = rgb(240, 240, 240);\n"
"my_black     = rgb(24, 25, 28);\n"
"dark_green  = rgb(31, 49, 0);\n"
"light_green  = rgb(71, 89, 30);\n"
" */\n"
"\n"
"QWidget {background-color: rgb(34, 35, 38) ;\n"
"				border-top: 2px solid  rgb(50, 50, 50);\n"
"}\n"
"")
        self.verticalLayout_3 = QVBoxLayout(self.wgFooter)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 3, 0, 0)
        self.widget = QWidget(self.wgFooter)
        self.widget.setObjectName(u"widget")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy2)
        self.widget.setMaximumSize(QSize(16777215, 40))
        self.widget.setStyleSheet(u"QWidget { border: none;}")
        self.gridLayout_2 = QGridLayout(self.widget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(9, 0, 9, 0)
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        sizePolicy1.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setPointSize(8)
        self.label_2.setFont(font)

        self.horizontalLayout_4.addWidget(self.label_2)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)

        self.btnCgtraderLink = QPushButton(self.widget)
        self.btnCgtraderLink.setObjectName(u"btnCgtraderLink")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.btnCgtraderLink.sizePolicy().hasHeightForWidth())
        self.btnCgtraderLink.setSizePolicy(sizePolicy3)
        self.btnCgtraderLink.setMinimumSize(QSize(30, 30))
        self.btnCgtraderLink.setMaximumSize(QSize(30, 30))
        self.btnCgtraderLink.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/images/icons/cgtrader_logo.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnCgtraderLink.setIcon(icon1)
        self.btnCgtraderLink.setIconSize(QSize(20, 20))

        self.horizontalLayout_4.addWidget(self.btnCgtraderLink)

        self.btnFabLink = QPushButton(self.widget)
        self.btnFabLink.setObjectName(u"btnFabLink")
        sizePolicy3.setHeightForWidth(self.btnFabLink.sizePolicy().hasHeightForWidth())
        self.btnFabLink.setSizePolicy(sizePolicy3)
        self.btnFabLink.setMinimumSize(QSize(30, 30))
        self.btnFabLink.setMaximumSize(QSize(30, 30))
        self.btnFabLink.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/images/icons/fab_logo.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnFabLink.setIcon(icon2)
        self.btnFabLink.setIconSize(QSize(20, 20))

        self.horizontalLayout_4.addWidget(self.btnFabLink)

        self.btnHelp = QPushButton(self.widget)
        self.btnHelp.setObjectName(u"btnHelp")
        sizePolicy3.setHeightForWidth(self.btnHelp.sizePolicy().hasHeightForWidth())
        self.btnHelp.setSizePolicy(sizePolicy3)
        self.btnHelp.setMinimumSize(QSize(30, 30))
        self.btnHelp.setMaximumSize(QSize(30, 30))
        self.btnHelp.setSizeIncrement(QSize(0, 0))
        self.btnHelp.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnHelp.setToolTipDuration(-1)
        self.btnHelp.setStyleSheet(u"border:0px;")
        self.btnHelp.setIconSize(QSize(25, 25))

        self.horizontalLayout_4.addWidget(self.btnHelp)


        self.gridLayout_2.addLayout(self.horizontalLayout_4, 0, 0, 1, 1)


        self.verticalLayout_3.addWidget(self.widget)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)


        self.gridLayout.addWidget(self.wgFooter, 5, 0, 1, 1)

        self.wgMain = QWidget(arUtil)
        self.wgMain.setObjectName(u"wgMain")
        sizePolicy2.setHeightForWidth(self.wgMain.sizePolicy().hasHeightForWidth())
        self.wgMain.setSizePolicy(sizePolicy2)
        self.wgMain.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout_6 = QVBoxLayout(self.wgMain)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(-1, 0, -1, 0)
        self._2 = QHBoxLayout()
        self._2.setSpacing(0)
        self._2.setObjectName(u"_2")
        self._2.setContentsMargins(-1, 0, -1, -1)
        self.stkTypeManageCreate = QStackedWidget(self.wgMain)
        self.stkTypeManageCreate.setObjectName(u"stkTypeManageCreate")
        self.pageMain = QWidget()
        self.pageMain.setObjectName(u"pageMain")
        self.gridLayout_5 = QGridLayout(self.pageMain)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.layMain = QVBoxLayout()
        self.layMain.setObjectName(u"layMain")

        self.gridLayout_5.addLayout(self.layMain, 0, 0, 1, 1)

        self.stkTypeManageCreate.addWidget(self.pageMain)
        self.pageManageProjects = QWidget()
        self.pageManageProjects.setObjectName(u"pageManageProjects")
        self.gridLayout_7 = QGridLayout(self.pageManageProjects)
        self.gridLayout_7.setSpacing(6)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.widget_8 = QWidget(self.pageManageProjects)
        self.widget_8.setObjectName(u"widget_8")
        sizePolicy1.setHeightForWidth(self.widget_8.sizePolicy().hasHeightForWidth())
        self.widget_8.setSizePolicy(sizePolicy1)
        self.widget_8.setMaximumSize(QSize(16777215, 30))
        self.horizontalLayout_3 = QHBoxLayout(self.widget_8)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(9, 0, 9, 0)
        self.label = QLabel(self.widget_8)
        self.label.setObjectName(u"label")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy4)
        self.label.setMinimumSize(QSize(170, 0))

        self.horizontalLayout_3.addWidget(self.label)

        self.linRootPath = QLineEdit(self.widget_8)
        self.linRootPath.setObjectName(u"linRootPath")

        self.horizontalLayout_3.addWidget(self.linRootPath)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_5)

        self.btnChangeRootPath = QPushButton(self.widget_8)
        self.btnChangeRootPath.setObjectName(u"btnChangeRootPath")

        self.horizontalLayout_3.addWidget(self.btnChangeRootPath)


        self.gridLayout_7.addWidget(self.widget_8, 1, 0, 1, 1)

        self.widget_9 = QWidget(self.pageManageProjects)
        self.widget_9.setObjectName(u"widget_9")
        self.gridLayout_8 = QGridLayout(self.widget_9)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.layTypeManage = QHBoxLayout()
        self.layTypeManage.setObjectName(u"layTypeManage")

        self.gridLayout_8.addLayout(self.layTypeManage, 0, 0, 1, 1)


        self.gridLayout_7.addWidget(self.widget_9, 3, 0, 1, 1)

        self.widget_4 = QWidget(self.pageManageProjects)
        self.widget_4.setObjectName(u"widget_4")
        sizePolicy1.setHeightForWidth(self.widget_4.sizePolicy().hasHeightForWidth())
        self.widget_4.setSizePolicy(sizePolicy1)
        self.widget_4.setMaximumSize(QSize(16777215, 30))
        self.horizontalLayout_10 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(-1, 0, -1, 0)
        self.label_6 = QLabel(self.widget_4)
        self.label_6.setObjectName(u"label_6")
        sizePolicy3.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy3)
        self.label_6.setMinimumSize(QSize(170, 0))
        self.label_6.setMaximumSize(QSize(170, 16777215))
        self.label_6.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.label_6.setWordWrap(False)

        self.horizontalLayout_10.addWidget(self.label_6)

        self.linMarketplaceName = QLineEdit(self.widget_4)
        self.linMarketplaceName.setObjectName(u"linMarketplaceName")

        self.horizontalLayout_10.addWidget(self.linMarketplaceName)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_8)

        self.btnChangeMarketplaceName = QPushButton(self.widget_4)
        self.btnChangeMarketplaceName.setObjectName(u"btnChangeMarketplaceName")

        self.horizontalLayout_10.addWidget(self.btnChangeMarketplaceName)


        self.gridLayout_7.addWidget(self.widget_4, 2, 0, 1, 1)

        self.stkTypeManageCreate.addWidget(self.pageManageProjects)
        self.pageCreateProject = QWidget()
        self.pageCreateProject.setObjectName(u"pageCreateProject")
        self.pageCreateProject.setStyleSheet(u"")
        self.gridLayout_9 = QGridLayout(self.pageCreateProject)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.gridLayout_4.setVerticalSpacing(16)
        self.gridLayout_4.setContentsMargins(12, 12, 12, 12)
        self.pushButton_2 = QPushButton(self.pageCreateProject)
        self.pushButton_2.setObjectName(u"pushButton_2")
        sizePolicy3.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy3)
        self.pushButton_2.setBaseSize(QSize(0, 0))
        self.pushButton_2.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.pushButton_2.setStyleSheet(u"")

        self.gridLayout_4.addWidget(self.pushButton_2, 5, 2, 1, 1)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")

        self.gridLayout_4.addLayout(self.horizontalLayout_7, 5, 1, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 30, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout_4.addItem(self.verticalSpacer_3, 0, 1, 1, 1)

        self.widget_3 = QWidget(self.pageCreateProject)
        self.widget_3.setObjectName(u"widget_3")
        sizePolicy1.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy1)
        self.horizontalLayout_5 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_6)

        self.radioButton_4 = QRadioButton(self.widget_3)
        self.radioButton_4.setObjectName(u"radioButton_4")
        self.radioButton_4.setChecked(True)

        self.horizontalLayout_5.addWidget(self.radioButton_4)

        self.radioButton_3 = QRadioButton(self.widget_3)
        self.radioButton_3.setObjectName(u"radioButton_3")

        self.horizontalLayout_5.addWidget(self.radioButton_3)

        self.radioButton_2 = QRadioButton(self.widget_3)
        self.radioButton_2.setObjectName(u"radioButton_2")

        self.horizontalLayout_5.addWidget(self.radioButton_2)

        self.radioButton = QRadioButton(self.widget_3)
        self.radioButton.setObjectName(u"radioButton")

        self.horizontalLayout_5.addWidget(self.radioButton)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_7)


        self.gridLayout_4.addWidget(self.widget_3, 1, 1, 1, 1)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.linFilesName = QLineEdit(self.pageCreateProject)
        self.linFilesName.setObjectName(u"linFilesName")
        sizePolicy3.setHeightForWidth(self.linFilesName.sizePolicy().hasHeightForWidth())
        self.linFilesName.setSizePolicy(sizePolicy3)
        self.linFilesName.setMaximumSize(QSize(400, 16777215))
        self.linFilesName.setStyleSheet(u"")
        self.linFilesName.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_8.addWidget(self.linFilesName)


        self.gridLayout_4.addLayout(self.horizontalLayout_8, 3, 1, 1, 1)

        self.label_5 = QLabel(self.pageCreateProject)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_4.addWidget(self.label_5, 3, 0, 1, 1)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.linProjectName = QLineEdit(self.pageCreateProject)
        self.linProjectName.setObjectName(u"linProjectName")
        sizePolicy3.setHeightForWidth(self.linProjectName.sizePolicy().hasHeightForWidth())
        self.linProjectName.setSizePolicy(sizePolicy3)
        self.linProjectName.setMaximumSize(QSize(400, 16777215))
        self.linProjectName.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_9.addWidget(self.linProjectName)


        self.gridLayout_4.addLayout(self.horizontalLayout_9, 2, 1, 1, 1)

        self.label_3 = QLabel(self.pageCreateProject)
        self.label_3.setObjectName(u"label_3")
        sizePolicy1.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy1)
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_4.addWidget(self.label_3, 1, 0, 1, 1)

        self.label_4 = QLabel(self.pageCreateProject)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_4.addWidget(self.label_4, 2, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer_2, 4, 0, 1, 1)


        self.gridLayout_9.addLayout(self.gridLayout_4, 0, 0, 1, 1)

        self.stkTypeManageCreate.addWidget(self.pageCreateProject)

        self._2.addWidget(self.stkTypeManageCreate)


        self.verticalLayout_6.addLayout(self._2)


        self.gridLayout.addWidget(self.wgMain, 4, 0, 1, 1)

        self.wgUpper = QWidget(arUtil)
        self.wgUpper.setObjectName(u"wgUpper")
        self.verticalLayout_5 = QVBoxLayout(self.wgUpper)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(9, -1, 9, -1)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(12, -1, 12, -1)
        self.btnProject = QPushButton(self.wgUpper)
        self.btnProject.setObjectName(u"btnProject")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.btnProject.sizePolicy().hasHeightForWidth())
        self.btnProject.setSizePolicy(sizePolicy5)
        self.btnProject.setMinimumSize(QSize(40, 0))
        self.btnProject.setMaximumSize(QSize(16777215, 16777215))
        font1 = QFont()
        font1.setUnderline(False)
        self.btnProject.setFont(font1)
        self.btnProject.setAutoFillBackground(False)
        self.btnProject.setStyleSheet(u"QPushButton {\n"
"    border: 0px;\n"
"	text-align: left;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    /*color: rgb(151, 169, 0);*/\n"
"    background-color: transparent;\n"
"	text-decoration: underline;\n"
"}\n"
"\n"
"\n"
"")
        self.btnProject.setFlat(False)

        self.horizontalLayout.addWidget(self.btnProject)

        self.horizontalSpacer = QSpacerItem(20, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.btnManageProjects = QPushButton(self.wgUpper)
        self.btnManageProjects.setObjectName(u"btnManageProjects")
        sizePolicy3.setHeightForWidth(self.btnManageProjects.sizePolicy().hasHeightForWidth())
        self.btnManageProjects.setSizePolicy(sizePolicy3)
        self.btnManageProjects.setMaximumSize(QSize(100, 16777215))
        self.btnManageProjects.setCheckable(True)

        self.horizontalLayout.addWidget(self.btnManageProjects)

        self.btnCreateProject = QPushButton(self.wgUpper)
        self.btnCreateProject.setObjectName(u"btnCreateProject")
        sizePolicy3.setHeightForWidth(self.btnCreateProject.sizePolicy().hasHeightForWidth())
        self.btnCreateProject.setSizePolicy(sizePolicy3)
        self.btnCreateProject.setMaximumSize(QSize(100, 16777215))
        self.btnCreateProject.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btnCreateProject.setCheckable(True)

        self.horizontalLayout.addWidget(self.btnCreateProject)


        self.verticalLayout_4.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.btnBack = QPushButton(self.wgUpper)
        self.btnBack.setObjectName(u"btnBack")
        self.btnBack.setEnabled(False)
        self.btnBack.setStyleSheet(u"")
        icon3 = QIcon()
        icon3.addFile(u":/images/icons/btn_back.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnBack.setIcon(icon3)
        self.btnBack.setFlat(False)

        self.horizontalLayout_2.addWidget(self.btnBack)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)


        self.verticalLayout_4.addLayout(self.horizontalLayout_2)


        self.verticalLayout_5.addLayout(self.verticalLayout_4)


        self.gridLayout.addWidget(self.wgUpper, 0, 0, 1, 1)


        self.retranslateUi(arUtil)

        self.stkTypeManageCreate.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(arUtil)
    # setupUi

    def retranslateUi(self, arUtil):
        arUtil.setWindowTitle(QCoreApplication.translate("arUtil", u"Pixels and Crafts Pipeline", None))
        self.label_2.setText(QCoreApplication.translate("arUtil", u"Pixels and Crafts Pipeline", None))
        self.btnCgtraderLink.setText("")
        self.btnFabLink.setText("")
#if QT_CONFIG(tooltip)
        self.btnHelp.setToolTip(QCoreApplication.translate("arUtil", u"Open wiki", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.btnHelp.setStatusTip("")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.btnHelp.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.btnHelp.setText(QCoreApplication.translate("arUtil", u"?", None))
        self.label.setText(QCoreApplication.translate("arUtil", u"Root path:", None))
        self.btnChangeRootPath.setText(QCoreApplication.translate("arUtil", u"Change path", None))
        self.label_6.setText(QCoreApplication.translate("arUtil", u"Marketplace folder name:", None))
        self.btnChangeMarketplaceName.setText(QCoreApplication.translate("arUtil", u"Change Name", None))
        self.pushButton_2.setText(QCoreApplication.translate("arUtil", u"Create", None))
        self.radioButton_4.setText(QCoreApplication.translate("arUtil", u"Environment", None))
        self.radioButton_3.setText(QCoreApplication.translate("arUtil", u"Props", None))
        self.radioButton_2.setText(QCoreApplication.translate("arUtil", u"3D scans", None))
        self.radioButton.setText(QCoreApplication.translate("arUtil", u"Characters", None))
#if QT_CONFIG(tooltip)
        self.linFilesName.setToolTip(QCoreApplication.translate("arUtil", u"If possible choose one word.\n"
"It will be the name for the files", None))
#endif // QT_CONFIG(tooltip)
        self.label_5.setText(QCoreApplication.translate("arUtil", u"Files' name:", None))
        self.label_3.setText(QCoreApplication.translate("arUtil", u"Type of project:", None))
        self.label_4.setText(QCoreApplication.translate("arUtil", u"Name of the project:", None))
#if QT_CONFIG(tooltip)
        self.btnProject.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.btnProject.setText(QCoreApplication.translate("arUtil", u"Project name", None))
        self.btnManageProjects.setText(QCoreApplication.translate("arUtil", u"Manage projects", None))
        self.btnCreateProject.setText(QCoreApplication.translate("arUtil", u"Create project", None))
        self.btnBack.setText("")
    # retranslateUi


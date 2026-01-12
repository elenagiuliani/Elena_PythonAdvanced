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
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)
import app_imgs_rc

class Ui_arUtil(object):
    def setupUi(self, arUtil):
        if not arUtil.objectName():
            arUtil.setObjectName(u"arUtil")
        arUtil.resize(623, 552)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(arUtil.sizePolicy().hasHeightForWidth())
        arUtil.setSizePolicy(sizePolicy)
        icon = QIcon()
        icon.addFile(u":/images/icons/logo_store.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        arUtil.setWindowIcon(icon)
        arUtil.setStyleSheet(u"")
        self.gridLayout = QGridLayout(arUtil)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(10)
        self.gridLayout.setVerticalSpacing(0)
        self.gridLayout.setContentsMargins(0, 7, 0, 0)
        self.wgtFooter = QWidget(arUtil)
        self.wgtFooter.setObjectName(u"wgtFooter")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.wgtFooter.sizePolicy().hasHeightForWidth())
        self.wgtFooter.setSizePolicy(sizePolicy1)
        self.wgtFooter.setMinimumSize(QSize(0, 0))
        self.wgtFooter.setMaximumSize(QSize(16777215, 40))
        self.wgtFooter.setStyleSheet(u"QWidget {border-top: 2px solid  rgb(50, 50, 50);\n"
"}")
        self.verticalLayout_3 = QVBoxLayout(self.wgtFooter)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.main_widget = QWidget(self.wgtFooter)
        self.main_widget.setObjectName(u"main_widget")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.main_widget.sizePolicy().hasHeightForWidth())
        self.main_widget.setSizePolicy(sizePolicy2)
        self.main_widget.setMaximumSize(QSize(16777215, 40))
        self.main_widget.setStyleSheet(u"QWidget { border: none;}")
        self.gridLayout_2 = QGridLayout(self.main_widget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(9, 0, 9, 0)
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_2 = QLabel(self.main_widget)
        self.label_2.setObjectName(u"label_2")
        sizePolicy1.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setPointSize(7)
        self.label_2.setFont(font)

        self.horizontalLayout_4.addWidget(self.label_2)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)

        self.btnCgtraderLink = QPushButton(self.main_widget)
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

        self.btnFabLink = QPushButton(self.main_widget)
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

        self.btnHelp = QPushButton(self.main_widget)
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

        self.btnReloadApp = QPushButton(self.main_widget)
        self.btnReloadApp.setObjectName(u"btnReloadApp")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.btnReloadApp.sizePolicy().hasHeightForWidth())
        self.btnReloadApp.setSizePolicy(sizePolicy4)
        self.btnReloadApp.setMinimumSize(QSize(25, 25))
        self.btnReloadApp.setMaximumSize(QSize(25, 25))
        icon3 = QIcon()
        icon3.addFile(u":/images/icons/btn_reload_app.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnReloadApp.setIcon(icon3)

        self.horizontalLayout_4.addWidget(self.btnReloadApp)


        self.gridLayout_2.addLayout(self.horizontalLayout_4, 0, 1, 1, 1)


        self.verticalLayout_3.addWidget(self.main_widget)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)


        self.gridLayout.addWidget(self.wgtFooter, 6, 0, 1, 1)

        self.lblFeedback = QLabel(arUtil)
        self.lblFeedback.setObjectName(u"lblFeedback")
        font1 = QFont()
        font1.setPointSize(9)
        self.lblFeedback.setFont(font1)
        self.lblFeedback.setStyleSheet(u"padding-left: 25px;\n"
"padding-bottom: 8px;\n"
"padding-top: 5px;")

        self.gridLayout.addWidget(self.lblFeedback, 5, 0, 1, 1)

        self.wgUpper = QWidget(arUtil)
        self.wgUpper.setObjectName(u"wgUpper")
        self.verticalLayout_5 = QVBoxLayout(self.wgUpper)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(9, -1, 9, -1)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, -1, 5, -1)
        self.btnOpenProjectFolder = QPushButton(self.wgUpper)
        self.btnOpenProjectFolder.setObjectName(u"btnOpenProjectFolder")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.btnOpenProjectFolder.sizePolicy().hasHeightForWidth())
        self.btnOpenProjectFolder.setSizePolicy(sizePolicy5)
        self.btnOpenProjectFolder.setMinimumSize(QSize(40, 0))
        self.btnOpenProjectFolder.setMaximumSize(QSize(16777215, 16777215))
        font2 = QFont()
        font2.setUnderline(False)
        self.btnOpenProjectFolder.setFont(font2)
        self.btnOpenProjectFolder.setAutoFillBackground(False)
        self.btnOpenProjectFolder.setStyleSheet(u"QPushButton {\n"
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
        self.btnOpenProjectFolder.setFlat(False)

        self.horizontalLayout.addWidget(self.btnOpenProjectFolder)

        self.horizontalSpacer = QSpacerItem(20, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.btnManageProjectsMenu = QPushButton(self.wgUpper)
        self.btnManageProjectsMenu.setObjectName(u"btnManageProjectsMenu")
        sizePolicy3.setHeightForWidth(self.btnManageProjectsMenu.sizePolicy().hasHeightForWidth())
        self.btnManageProjectsMenu.setSizePolicy(sizePolicy3)
        self.btnManageProjectsMenu.setMaximumSize(QSize(100, 16777215))
        self.btnManageProjectsMenu.setCheckable(True)

        self.horizontalLayout.addWidget(self.btnManageProjectsMenu)

        self.btnCreateProjectMenu = QPushButton(self.wgUpper)
        self.btnCreateProjectMenu.setObjectName(u"btnCreateProjectMenu")
        sizePolicy3.setHeightForWidth(self.btnCreateProjectMenu.sizePolicy().hasHeightForWidth())
        self.btnCreateProjectMenu.setSizePolicy(sizePolicy3)
        self.btnCreateProjectMenu.setMaximumSize(QSize(100, 16777215))
        self.btnCreateProjectMenu.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btnCreateProjectMenu.setCheckable(True)

        self.horizontalLayout.addWidget(self.btnCreateProjectMenu)

        self.horizontalSpacer_4 = QSpacerItem(10, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_4)

        self.btnBack = QPushButton(self.wgUpper)
        self.btnBack.setObjectName(u"btnBack")
        self.btnBack.setEnabled(False)
        self.btnBack.setStyleSheet(u"")
        icon4 = QIcon()
        icon4.addFile(u":/images/icons/btn_back.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnBack.setIcon(icon4)
        self.btnBack.setFlat(False)

        self.horizontalLayout.addWidget(self.btnBack)


        self.verticalLayout_4.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)


        self.verticalLayout_4.addLayout(self.horizontalLayout_2)


        self.verticalLayout_5.addLayout(self.verticalLayout_4)


        self.gridLayout.addWidget(self.wgUpper, 0, 0, 1, 1)

        self.wgMain = QWidget(arUtil)
        self.wgMain.setObjectName(u"wgMain")
        sizePolicy2.setHeightForWidth(self.wgMain.sizePolicy().hasHeightForWidth())
        self.wgMain.setSizePolicy(sizePolicy2)
        self.wgMain.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout_6 = QVBoxLayout(self.wgMain)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(-1, 0, -1, 0)
        self.layMain = QVBoxLayout()
        self.layMain.setObjectName(u"layMain")

        self.verticalLayout_6.addLayout(self.layMain)


        self.gridLayout.addWidget(self.wgMain, 4, 0, 1, 1)


        self.retranslateUi(arUtil)

        QMetaObject.connectSlotsByName(arUtil)
    # setupUi

    def retranslateUi(self, arUtil):
        arUtil.setWindowTitle(QCoreApplication.translate("arUtil", u"Pixels and Crafts Pipeline", None))
        self.label_2.setText(QCoreApplication.translate("arUtil", u"PackForge Pipeline", None))
#if QT_CONFIG(tooltip)
        self.btnCgtraderLink.setToolTip(QCoreApplication.translate("arUtil", u"Link to CgTrader marketplace", None))
#endif // QT_CONFIG(tooltip)
        self.btnCgtraderLink.setText("")
#if QT_CONFIG(tooltip)
        self.btnFabLink.setToolTip(QCoreApplication.translate("arUtil", u"Link to Fab marketplace", None))
#endif // QT_CONFIG(tooltip)
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
#if QT_CONFIG(tooltip)
        self.btnReloadApp.setToolTip(QCoreApplication.translate("arUtil", u"Reload app", None))
#endif // QT_CONFIG(tooltip)
        self.btnReloadApp.setText("")
        self.lblFeedback.setText("")
#if QT_CONFIG(tooltip)
        self.btnOpenProjectFolder.setToolTip(QCoreApplication.translate("arUtil", u"Current loaded project", None))
#endif // QT_CONFIG(tooltip)
        self.btnOpenProjectFolder.setText(QCoreApplication.translate("arUtil", u"Project name", None))
        self.btnManageProjectsMenu.setText(QCoreApplication.translate("arUtil", u"Manage projects", None))
        self.btnCreateProjectMenu.setText(QCoreApplication.translate("arUtil", u"Create project", None))
        self.btnBack.setText("")
    # retranslateUi


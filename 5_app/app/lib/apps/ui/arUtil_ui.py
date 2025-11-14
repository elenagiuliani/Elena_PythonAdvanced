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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QHeaderView, QLabel, QLayout, QPushButton,
    QSizePolicy, QSpacerItem, QStackedWidget, QTabWidget,
    QTreeWidget, QTreeWidgetItem, QVBoxLayout, QWidget)
import app_imgs_rc

class Ui_arUtil(object):
    def setupUi(self, arUtil):
        if not arUtil.objectName():
            arUtil.setObjectName(u"arUtil")
        arUtil.resize(770, 544)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(arUtil.sizePolicy().hasHeightForWidth())
        arUtil.setSizePolicy(sizePolicy)
        arUtil.setStyleSheet(u"background-color: rgb(33, 33, 33);\n"
"\n"
"selection-background-color: rgb(230, 230, 230);\n"
"\n"
"")
        self.gridLayout = QGridLayout(arUtil)
        self.gridLayout.setObjectName(u"gridLayout")
        self.wgMain = QWidget(arUtil)
        self.wgMain.setObjectName(u"wgMain")
        self.verticalLayout_6 = QVBoxLayout(self.wgMain)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(-1, 10, -1, -1)
        self.tabWidget = QTabWidget(self.wgMain)
        self.tabWidget.setObjectName(u"tabWidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy1)
        self.tabWidget.setMinimumSize(QSize(300, 0))
        self.tabWidget.setMaximumSize(QSize(3000, 16777215))
        self.tabWidget.setSizeIncrement(QSize(0, 0))
        self.tabWidget.setBaseSize(QSize(0, 0))
        self.tabWidget.setFocusPolicy(Qt.FocusPolicy.TabFocus)
        self.tabWidget.setTabPosition(QTabWidget.TabPosition.West)
        self.tabWidget.setTabShape(QTabWidget.TabShape.Triangular)
        self.tabWidget.setElideMode(Qt.TextElideMode.ElideNone)
        self.tabArchitectural = QWidget()
        self.tabArchitectural.setObjectName(u"tabArchitectural")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.tabArchitectural.sizePolicy().hasHeightForWidth())
        self.tabArchitectural.setSizePolicy(sizePolicy2)
        self.tabArchitectural.setMinimumSize(QSize(200, 0))
        self.verticalLayout_2 = QVBoxLayout(self.tabArchitectural)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_3)

        self.pushButton_2 = QPushButton(self.tabArchitectural)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout_7.addWidget(self.pushButton_2)

        self.pushButton = QPushButton(self.tabArchitectural)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout_7.addWidget(self.pushButton)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_4)


        self.verticalLayout_2.addLayout(self.horizontalLayout_7)

        self.stackedWidget = QStackedWidget(self.tabArchitectural)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.pageAssets = QWidget()
        self.pageAssets.setObjectName(u"pageAssets")
        self.verticalLayout_8 = QVBoxLayout(self.pageAssets)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.widget = QWidget(self.pageAssets)
        self.widget.setObjectName(u"widget")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(1)
        sizePolicy3.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy3)
        self.widget.setMaximumSize(QSize(16777215, 120))
        self.gridLayout_2 = QGridLayout(self.widget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.imgAsset = QPushButton(self.widget)
        self.imgAsset.setObjectName(u"imgAsset")
        self.imgAsset.setEnabled(True)
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.imgAsset.sizePolicy().hasHeightForWidth())
        self.imgAsset.setSizePolicy(sizePolicy4)
        self.imgAsset.setMaximumSize(QSize(150, 16777215))
        self.imgAsset.setBaseSize(QSize(0, 0))

        self.horizontalLayout_6.addWidget(self.imgAsset)

        self.lblAsset = QLabel(self.widget)
        self.lblAsset.setObjectName(u"lblAsset")
        self.lblAsset.setMargin(20)

        self.horizontalLayout_6.addWidget(self.lblAsset)


        self.gridLayout_2.addLayout(self.horizontalLayout_6, 0, 0, 1, 1)


        self.verticalLayout_8.addWidget(self.widget)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer)

        self.stackedWidget.addWidget(self.pageAssets)
        self.pageFiles = QWidget()
        self.pageFiles.setObjectName(u"pageFiles")
        self.treeWidget = QTreeWidget(self.pageFiles)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setText(0, u"1");
        self.treeWidget.setHeaderItem(__qtreewidgetitem)
        self.treeWidget.setObjectName(u"treeWidget")
        self.treeWidget.setGeometry(QRect(20, 30, 256, 192))
        self.stackedWidget.addWidget(self.pageFiles)

        self.verticalLayout_2.addWidget(self.stackedWidget)

        self.tabWidget.addTab(self.tabArchitectural, "")
        self.tabProps = QWidget()
        self.tabProps.setObjectName(u"tabProps")
        self.verticalLayout_4 = QVBoxLayout(self.tabProps)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.tabWidget.addTab(self.tabProps, "")
        self.tabLamps = QWidget()
        self.tabLamps.setObjectName(u"tabLamps")
        self.verticalLayout_5 = QVBoxLayout(self.tabLamps)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.tabWidget.addTab(self.tabLamps, "")

        self.horizontalLayout_5.addWidget(self.tabWidget)

        self.widget_2 = QWidget(self.wgMain)
        self.widget_2.setObjectName(u"widget_2")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Expanding)
        sizePolicy5.setHorizontalStretch(1)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy5)
        self.widget_2.setMaximumSize(QSize(250, 16777215))
        self.gridLayout_3 = QGridLayout(self.widget_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, -1, 9, -1)
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.verticalLayout_3.setContentsMargins(0, -1, 0, -1)
        self.label_2 = QLabel(self.widget_2)
        self.label_2.setObjectName(u"label_2")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(1)
        sizePolicy6.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy6)
        self.label_2.setMaximumSize(QSize(600, 30))

        self.verticalLayout_3.addWidget(self.label_2)

        self.line = QFrame(self.widget_2)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_3.addWidget(self.line)

        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label_9 = QLabel(self.widget_2)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_4.addWidget(self.label_9, 0, 0, 1, 1)

        self.label_11 = QLabel(self.widget_2)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout_4.addWidget(self.label_11, 1, 0, 1, 1)

        self.lblUniqueMeshes = QLabel(self.widget_2)
        self.lblUniqueMeshes.setObjectName(u"lblUniqueMeshes")
        self.lblUniqueMeshes.setMargin(5)

        self.gridLayout_4.addWidget(self.lblUniqueMeshes, 0, 1, 1, 1)

        self.lblInteractiveMeshes = QLabel(self.widget_2)
        self.lblInteractiveMeshes.setObjectName(u"lblInteractiveMeshes")
        self.lblInteractiveMeshes.setMargin(5)

        self.gridLayout_4.addWidget(self.lblInteractiveMeshes, 1, 1, 1, 1)


        self.verticalLayout_3.addLayout(self.gridLayout_4)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)

        self.imgRef = QPushButton(self.widget_2)
        self.imgRef.setObjectName(u"imgRef")
        sizePolicy7 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(1)
        sizePolicy7.setHeightForWidth(self.imgRef.sizePolicy().hasHeightForWidth())
        self.imgRef.setSizePolicy(sizePolicy7)
        self.imgRef.setMaximumSize(QSize(100, 100))

        self.verticalLayout_3.addWidget(self.imgRef)


        self.gridLayout_3.addLayout(self.verticalLayout_3, 0, 0, 1, 1)


        self.horizontalLayout_5.addWidget(self.widget_2)


        self.verticalLayout_6.addLayout(self.horizontalLayout_5)


        self.gridLayout.addWidget(self.wgMain, 2, 0, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.horizontalLayout_3.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, -1, 0, -1)
        self.btnStoreLink = QPushButton(arUtil)
        self.btnStoreLink.setObjectName(u"btnStoreLink")
        self.btnStoreLink.setEnabled(False)
        self.btnStoreLink.setMaximumSize(QSize(50, 50))
        icon = QIcon()
        icon.addFile(u":/images/icons/PixelsAndCrafts_logo_oct2025.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnStoreLink.setIcon(icon)
        self.btnStoreLink.setIconSize(QSize(40, 40))
        self.btnStoreLink.setCheckable(False)

        self.horizontalLayout_2.addWidget(self.btnStoreLink)

        self.lblNameApp = QLabel(arUtil)
        self.lblNameApp.setObjectName(u"lblNameApp")

        self.horizontalLayout_2.addWidget(self.lblNameApp)


        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)

        self.btnHelp = QPushButton(arUtil)
        self.btnHelp.setObjectName(u"btnHelp")
        sizePolicy8 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.btnHelp.sizePolicy().hasHeightForWidth())
        self.btnHelp.setSizePolicy(sizePolicy8)
        self.btnHelp.setMaximumSize(QSize(25, 25))
        icon1 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.HelpFaq))
        self.btnHelp.setIcon(icon1)

        self.horizontalLayout_4.addWidget(self.btnHelp)


        self.horizontalLayout_3.addLayout(self.horizontalLayout_4)


        self.gridLayout.addLayout(self.horizontalLayout_3, 3, 0, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, -1, -1, -1)
        self.btnProject = QPushButton(arUtil)
        self.btnProject.setObjectName(u"btnProject")

        self.horizontalLayout.addWidget(self.btnProject)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.btnManageProjects = QPushButton(arUtil)
        self.btnManageProjects.setObjectName(u"btnManageProjects")
        sizePolicy8.setHeightForWidth(self.btnManageProjects.sizePolicy().hasHeightForWidth())
        self.btnManageProjects.setSizePolicy(sizePolicy8)
        self.btnManageProjects.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout.addWidget(self.btnManageProjects)

        self.btnCreateProject = QPushButton(arUtil)
        self.btnCreateProject.setObjectName(u"btnCreateProject")
        sizePolicy8.setHeightForWidth(self.btnCreateProject.sizePolicy().hasHeightForWidth())
        self.btnCreateProject.setSizePolicy(sizePolicy8)
        self.btnCreateProject.setMaximumSize(QSize(100, 16777215))
        self.btnCreateProject.setLayoutDirection(Qt.LayoutDirection.LeftToRight)

        self.horizontalLayout.addWidget(self.btnCreateProject)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.gridLayout.addLayout(self.verticalLayout, 1, 0, 1, 1)


        self.retranslateUi(arUtil)

        self.tabWidget.setCurrentIndex(0)
        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(arUtil)
    # setupUi

    def retranslateUi(self, arUtil):
        arUtil.setWindowTitle(QCoreApplication.translate("arUtil", u"Pixels and Crafts Pipeline", None))
        self.pushButton_2.setText(QCoreApplication.translate("arUtil", u"Assets", None))
        self.pushButton.setText(QCoreApplication.translate("arUtil", u"Files", None))
        self.imgAsset.setText(QCoreApplication.translate("arUtil", u"screenshot", None))
        self.lblAsset.setText(QCoreApplication.translate("arUtil", u"Asset name", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabArchitectural), QCoreApplication.translate("arUtil", u"Architectural", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabProps), QCoreApplication.translate("arUtil", u"Props", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabLamps), QCoreApplication.translate("arUtil", u"Lamps", None))
        self.label_2.setText(QCoreApplication.translate("arUtil", u"Details", None))
        self.label_9.setText(QCoreApplication.translate("arUtil", u"Unique meshes", None))
        self.label_11.setText(QCoreApplication.translate("arUtil", u"Interactive meshes", None))
        self.lblUniqueMeshes.setText(QCoreApplication.translate("arUtil", u"0", None))
        self.lblInteractiveMeshes.setText(QCoreApplication.translate("arUtil", u"0", None))
        self.imgRef.setText("")
        self.btnStoreLink.setText("")
        self.lblNameApp.setText(QCoreApplication.translate("arUtil", u"Pixels and Crafts", None))
        self.btnHelp.setText("")
        self.btnProject.setText(QCoreApplication.translate("arUtil", u"Project name", None))
        self.btnManageProjects.setText(QCoreApplication.translate("arUtil", u"Manage projects", None))
        self.btnCreateProject.setText(QCoreApplication.translate("arUtil", u"Create project", None))
    # retranslateUi


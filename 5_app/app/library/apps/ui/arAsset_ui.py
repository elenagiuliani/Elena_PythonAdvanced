# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'arAsset.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QPushButton,
    QSizePolicy, QSpacerItem, QStackedWidget, QVBoxLayout,
    QWidget)
import app_imgs_rc

class Ui_arAsset(object):
    def setupUi(self, arAsset):
        if not arAsset.objectName():
            arAsset.setObjectName(u"arAsset")
        arAsset.setEnabled(True)
        arAsset.resize(561, 78)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(arAsset.sizePolicy().hasHeightForWidth())
        arAsset.setSizePolicy(sizePolicy)
        arAsset.setMinimumSize(QSize(0, 0))
        arAsset.setStyleSheet(u"text-align: left;\n"
"/*padding: 9px;")
        self.verticalLayout = QVBoxLayout(arAsset)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.stkAssetsBlueprints = QStackedWidget(arAsset)
        self.stkAssetsBlueprints.setObjectName(u"stkAssetsBlueprints")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.stkAssetsBlueprints.sizePolicy().hasHeightForWidth())
        self.stkAssetsBlueprints.setSizePolicy(sizePolicy1)
        self.pageAssets = QWidget()
        self.pageAssets.setObjectName(u"pageAssets")
        sizePolicy1.setHeightForWidth(self.pageAssets.sizePolicy().hasHeightForWidth())
        self.pageAssets.setSizePolicy(sizePolicy1)
        self.pageAssets.setMinimumSize(QSize(0, 60))
        self.pageAssets.setMaximumSize(QSize(16777215, 60))
        self.verticalLayout_2 = QVBoxLayout(self.pageAssets)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.wgHoverAssets = QWidget(self.pageAssets)
        self.wgHoverAssets.setObjectName(u"wgHoverAssets")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(1)
        sizePolicy2.setHeightForWidth(self.wgHoverAssets.sizePolicy().hasHeightForWidth())
        self.wgHoverAssets.setSizePolicy(sizePolicy2)
        self.wgHoverAssets.setMinimumSize(QSize(0, 0))
        self.wgHoverAssets.setMaximumSize(QSize(16777215, 70))
        self.wgHoverAssets.setStyleSheet(u"QWidget:hover {background-color: rgb(31, 49, 0); }")
        self.gridLayout_2 = QGridLayout(self.wgHoverAssets)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.imgScene = QPushButton(self.wgHoverAssets)
        self.imgScene.setObjectName(u"imgScene")
        self.imgScene.setEnabled(False)
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.imgScene.sizePolicy().hasHeightForWidth())
        self.imgScene.setSizePolicy(sizePolicy3)
        self.imgScene.setMaximumSize(QSize(80, 16777215))
        self.imgScene.setBaseSize(QSize(0, 0))
        self.imgScene.setStyleSheet(u"QPushButton:hover {transparent}\n"
"\n"
"QPushButton {padding: 9;}")
        icon = QIcon()
        icon.addFile(u":/images/icons/folder_close.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.imgScene.setIcon(icon)
        self.imgScene.setIconSize(QSize(70, 70))

        self.horizontalLayout_6.addWidget(self.imgScene)

        self.btnOpenScene = QPushButton(self.wgHoverAssets)
        self.btnOpenScene.setObjectName(u"btnOpenScene")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.btnOpenScene.sizePolicy().hasHeightForWidth())
        self.btnOpenScene.setSizePolicy(sizePolicy4)
        self.btnOpenScene.setStyleSheet(u"QWidget {background-color: transparent;}\n"
"QPushButton:hover {transparent}\n"
"QPushButton {border: 0px;\n"
"padding-left: 10px;}")
        self.btnOpenScene.setFlat(False)

        self.horizontalLayout_6.addWidget(self.btnOpenScene)


        self.gridLayout_2.addLayout(self.horizontalLayout_6, 0, 0, 1, 1)


        self.verticalLayout_2.addWidget(self.wgHoverAssets)

        self.stkAssetsBlueprints.addWidget(self.pageAssets)
        self.pageBlueprints = QWidget()
        self.pageBlueprints.setObjectName(u"pageBlueprints")
        sizePolicy1.setHeightForWidth(self.pageBlueprints.sizePolicy().hasHeightForWidth())
        self.pageBlueprints.setSizePolicy(sizePolicy1)
        self.pageBlueprints.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout_5 = QVBoxLayout(self.pageBlueprints)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.widget_2 = QWidget(self.pageBlueprints)
        self.widget_2.setObjectName(u"widget_2")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy5)
        self.widget_2.setMinimumSize(QSize(0, 30))
        self.widget_2.setMaximumSize(QSize(16777215, 35))
        self.widget_2.setStyleSheet(u"QWidget:hover {background-color: rgb(31, 49, 0); }")
        self.horizontalLayout = QHBoxLayout(self.widget_2)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.iconArrowBlueprint = QPushButton(self.widget_2)
        self.iconArrowBlueprint.setObjectName(u"iconArrowBlueprint")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Expanding)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.iconArrowBlueprint.sizePolicy().hasHeightForWidth())
        self.iconArrowBlueprint.setSizePolicy(sizePolicy6)
        self.iconArrowBlueprint.setMinimumSize(QSize(0, 0))
        self.iconArrowBlueprint.setMaximumSize(QSize(30, 16777215))
        self.iconArrowBlueprint.setStyleSheet(u"QWidget {background-color: transparent;}\n"
"QPushButton:hover {transparent}\n"
"QPushButton {border: 0px;\n"
"padding-left: 10px;}")
        icon1 = QIcon()
        icon1.addFile(u":/images/icons/arrow_full_right.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.iconArrowBlueprint.setIcon(icon1)
        self.iconArrowBlueprint.setIconSize(QSize(11, 11))
        self.iconArrowBlueprint.setFlat(False)

        self.horizontalLayout.addWidget(self.iconArrowBlueprint)

        self.btnBlueprintName = QPushButton(self.widget_2)
        self.btnBlueprintName.setObjectName(u"btnBlueprintName")
        sizePolicy3.setHeightForWidth(self.btnBlueprintName.sizePolicy().hasHeightForWidth())
        self.btnBlueprintName.setSizePolicy(sizePolicy3)
        self.btnBlueprintName.setStyleSheet(u"QWidget {background-color: transparent;}\n"
"QPushButton:hover {transparent}\n"
"QPushButton {border: 0px;\n"
"		padding-left: -1px;\n"
"}\n"
"")
        self.btnBlueprintName.setIcon(icon)
        self.btnBlueprintName.setIconSize(QSize(14, 14))
        self.btnBlueprintName.setFlat(False)

        self.horizontalLayout.addWidget(self.btnBlueprintName)


        self.verticalLayout_5.addWidget(self.widget_2)

        self.widget = QWidget(self.pageBlueprints)
        self.widget.setObjectName(u"widget")
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")

        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)


        self.verticalLayout_5.addWidget(self.widget)

        self.verticalSpacer = QSpacerItem(20, 1, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer)

        self.stkAssetsBlueprints.addWidget(self.pageBlueprints)

        self.verticalLayout.addWidget(self.stkAssetsBlueprints)


        self.retranslateUi(arAsset)

        self.stkAssetsBlueprints.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(arAsset)
    # setupUi

    def retranslateUi(self, arAsset):
        arAsset.setWindowTitle(QCoreApplication.translate("arAsset", u"Pixels and Crafts Pipeline", None))
        self.imgScene.setText("")
        self.btnOpenScene.setText(QCoreApplication.translate("arAsset", u"Asset name", None))
        self.iconArrowBlueprint.setText("")
        self.btnBlueprintName.setText(QCoreApplication.translate("arAsset", u"Blueprint name", None))
    # retranslateUi


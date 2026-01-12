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
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)
import app_imgs_rc

class Ui_arAsset(object):
    def setupUi(self, arAsset):
        if not arAsset.objectName():
            arAsset.setObjectName(u"arAsset")
        arAsset.setEnabled(True)
        arAsset.resize(537, 72)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
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
        self.verticalLayout.setContentsMargins(0, 4, 0, 0)
        self.wgtAsset = QWidget(arAsset)
        self.wgtAsset.setObjectName(u"wgtAsset")
        sizePolicy.setHeightForWidth(self.wgtAsset.sizePolicy().hasHeightForWidth())
        self.wgtAsset.setSizePolicy(sizePolicy)
        self.wgtAsset.setMinimumSize(QSize(0, 0))
        self.wgtAsset.setMaximumSize(QSize(16777215, 16777215))
        self.wgtAsset.setStyleSheet(u"")
        self.gridLayout_3 = QGridLayout(self.wgtAsset)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.btnArrowBlueprint = QPushButton(self.wgtAsset)
        self.btnArrowBlueprint.setObjectName(u"btnArrowBlueprint")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btnArrowBlueprint.sizePolicy().hasHeightForWidth())
        self.btnArrowBlueprint.setSizePolicy(sizePolicy1)
        self.btnArrowBlueprint.setMinimumSize(QSize(0, 0))
        self.btnArrowBlueprint.setMaximumSize(QSize(30, 16777215))
        self.btnArrowBlueprint.setStyleSheet(u"QWidget {background-color: transparent;}\n"
"QPushButton:hover {transparent}\n"
"QPushButton {border: 0px;\n"
"padding-left: 10px;}")
        icon = QIcon()
        icon.addFile(u":/images/icons/arrow_full_right.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnArrowBlueprint.setIcon(icon)
        self.btnArrowBlueprint.setIconSize(QSize(11, 11))
        self.btnArrowBlueprint.setFlat(False)

        self.horizontalLayout_7.addWidget(self.btnArrowBlueprint)

        self.imgScene = QPushButton(self.wgtAsset)
        self.imgScene.setObjectName(u"imgScene")
        self.imgScene.setEnabled(False)
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.imgScene.sizePolicy().hasHeightForWidth())
        self.imgScene.setSizePolicy(sizePolicy2)
        self.imgScene.setMaximumSize(QSize(80, 60))
        self.imgScene.setBaseSize(QSize(0, 0))
        self.imgScene.setStyleSheet(u"/*QPushButton:hover {transparent}\n"
"\n"
"QPushButton {padding: -15px;}*/")
        icon1 = QIcon()
        icon1.addFile(u":/images/icons/folder_close.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.imgScene.setIcon(icon1)
        self.imgScene.setIconSize(QSize(110, 110))

        self.horizontalLayout_7.addWidget(self.imgScene)

        self.btnOpenScene = QPushButton(self.wgtAsset)
        self.btnOpenScene.setObjectName(u"btnOpenScene")
        sizePolicy.setHeightForWidth(self.btnOpenScene.sizePolicy().hasHeightForWidth())
        self.btnOpenScene.setSizePolicy(sizePolicy)
        self.btnOpenScene.setStyleSheet(u"QWidget {background-color: transparent;}\n"
"QPushButton:hover {transparent}\n"
"QPushButton {border: 0px;\n"
"padding-left: 10px;}")
        self.btnOpenScene.setCheckable(True)
        self.btnOpenScene.setFlat(False)

        self.horizontalLayout_7.addWidget(self.btnOpenScene)


        self.gridLayout_3.addLayout(self.horizontalLayout_7, 0, 0, 1, 1)


        self.verticalLayout.addWidget(self.wgtAsset)

        self.wgtBpMeshes = QWidget(arAsset)
        self.wgtBpMeshes.setObjectName(u"wgtBpMeshes")
        sizePolicy.setHeightForWidth(self.wgtBpMeshes.sizePolicy().hasHeightForWidth())
        self.wgtBpMeshes.setSizePolicy(sizePolicy)
        self.wgtBpMeshes.setMaximumSize(QSize(16777215, 16777215))
        self.wgtBpMeshes.setStyleSheet(u"/*background-color: rgb(40, 40, 40);")
        self.gridLayout_4 = QGridLayout(self.wgtBpMeshes)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.layBpMeshes = QVBoxLayout()
        self.layBpMeshes.setSpacing(0)
        self.layBpMeshes.setObjectName(u"layBpMeshes")

        self.gridLayout_4.addLayout(self.layBpMeshes, 0, 0, 1, 1)


        self.verticalLayout.addWidget(self.wgtBpMeshes)

        self.verticalSpacer_2 = QSpacerItem(0, 89, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)


        self.retranslateUi(arAsset)

        QMetaObject.connectSlotsByName(arAsset)
    # setupUi

    def retranslateUi(self, arAsset):
        arAsset.setWindowTitle(QCoreApplication.translate("arAsset", u"Pixels and Crafts Pipeline", None))
        self.btnArrowBlueprint.setText("")
        self.imgScene.setText("")
        self.btnOpenScene.setText(QCoreApplication.translate("arAsset", u"Asset name", None))
    # retranslateUi


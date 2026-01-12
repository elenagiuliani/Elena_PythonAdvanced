# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'arScene.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QLabel,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)
import app_imgs_rc

class Ui_arScene(object):
    def setupUi(self, arScene):
        if not arScene.objectName():
            arScene.setObjectName(u"arScene")
        arScene.setEnabled(True)
        arScene.resize(325, 184)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(arScene.sizePolicy().hasHeightForWidth())
        arScene.setSizePolicy(sizePolicy)
        arScene.setMinimumSize(QSize(0, 0))
        arScene.setStyleSheet(u"text-align: center;\n"
"/*padding: 9px;")
        self.verticalLayout = QVBoxLayout(arScene)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.Main = QWidget(arScene)
        self.Main.setObjectName(u"Main")
        self.verticalLayout_2 = QVBoxLayout(self.Main)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_3)

        self.label = QLabel(self.Main)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.label)

        self.gridLayout = QGridLayout()
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalSpacer = QSpacerItem(10, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer, 1, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 2, 4, 1, 1)

        self.cbxChooseDepartment = QComboBox(self.Main)
        self.cbxChooseDepartment.addItem("")
        self.cbxChooseDepartment.addItem("")
        self.cbxChooseDepartment.addItem("")
        self.cbxChooseDepartment.addItem("")
        self.cbxChooseDepartment.addItem("")
        self.cbxChooseDepartment.addItem("")
        self.cbxChooseDepartment.addItem("")
        self.cbxChooseDepartment.addItem("")
        self.cbxChooseDepartment.addItem("")
        self.cbxChooseDepartment.addItem("")
        self.cbxChooseDepartment.setObjectName(u"cbxChooseDepartment")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.cbxChooseDepartment.sizePolicy().hasHeightForWidth())
        self.cbxChooseDepartment.setSizePolicy(sizePolicy1)
        self.cbxChooseDepartment.setMaximumSize(QSize(110, 16777215))
        self.cbxChooseDepartment.setStyleSheet(u"")

        self.gridLayout.addWidget(self.cbxChooseDepartment, 0, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 2, 0, 1, 1)

        self.widget = QWidget(self.Main)
        self.widget.setObjectName(u"widget")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy2)
        self.widget.setMinimumSize(QSize(90, 0))
        self.verticalLayout_3 = QVBoxLayout(self.widget)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(3, 3, 3, 3)
        self.btnCreateScene = QPushButton(self.widget)
        self.btnCreateScene.setObjectName(u"btnCreateScene")
        sizePolicy1.setHeightForWidth(self.btnCreateScene.sizePolicy().hasHeightForWidth())
        self.btnCreateScene.setSizePolicy(sizePolicy1)
        self.btnCreateScene.setStyleSheet(u"text-align: center;")

        self.verticalLayout_3.addWidget(self.btnCreateScene)


        self.gridLayout.addWidget(self.widget, 2, 1, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)


        self.verticalLayout.addWidget(self.Main)


        self.retranslateUi(arScene)

        self.cbxChooseDepartment.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(arScene)
    # setupUi

    def retranslateUi(self, arScene):
        arScene.setWindowTitle(QCoreApplication.translate("arScene", u"Pixels and Crafts Pipeline", None))
        self.label.setText(QCoreApplication.translate("arScene", u"Choose a department", None))
        self.cbxChooseDepartment.setItemText(0, QCoreApplication.translate("arScene", u"3Dscanning", None))
        self.cbxChooseDepartment.setItemText(1, QCoreApplication.translate("arScene", u"Modeling", None))
        self.cbxChooseDepartment.setItemText(2, QCoreApplication.translate("arScene", u"Clothing", None))
        self.cbxChooseDepartment.setItemText(3, QCoreApplication.translate("arScene", u"Sculpting", None))
        self.cbxChooseDepartment.setItemText(4, QCoreApplication.translate("arScene", u"Baking", None))
        self.cbxChooseDepartment.setItemText(5, QCoreApplication.translate("arScene", u"Texturing", None))
        self.cbxChooseDepartment.setItemText(6, QCoreApplication.translate("arScene", u"Grooming", None))
        self.cbxChooseDepartment.setItemText(7, QCoreApplication.translate("arScene", u"Rigging", None))
        self.cbxChooseDepartment.setItemText(8, QCoreApplication.translate("arScene", u"Pose", None))
        self.cbxChooseDepartment.setItemText(9, QCoreApplication.translate("arScene", u"Animation", None))

        self.btnCreateScene.setText(QCoreApplication.translate("arScene", u"Create", None))
    # retranslateUi


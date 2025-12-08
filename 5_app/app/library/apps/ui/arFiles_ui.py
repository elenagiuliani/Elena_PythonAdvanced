# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'arFiles.ui'
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
    QLabel, QLayout, QListWidget, QListWidgetItem,
    QPushButton, QScrollArea, QSizePolicy, QSpacerItem,
    QStackedWidget, QVBoxLayout, QWidget)
import app_imgs_rc

class Ui_arFiles(object):
    def setupUi(self, arFiles):
        if not arFiles.objectName():
            arFiles.setObjectName(u"arFiles")
        arFiles.resize(624, 417)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(arFiles.sizePolicy().hasHeightForWidth())
        arFiles.setSizePolicy(sizePolicy)
        arFiles.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(arFiles)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, -1, -1, 0)
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_3)

        self.widget_3 = QWidget(arFiles)
        self.widget_3.setObjectName(u"widget_3")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy1)
        self.widget_3.setMinimumSize(QSize(60, 0))
        self.widget_3.setStyleSheet(u"QPushButton {background-color: rgb(30, 30, 30);   /*unchecked state*/\n"
"\n"
"			   			color: rgb(200, 200, 200);\n"
"						padding: 3px 18px;}\n"
"\n"
"QPushButton:checked {background-color: rgb(71, 89, 30);\n"
"						color: rgb(240, 240, 240);\n"
"}\n"
"\n"
"\n"
"QPushButton:hover {background-color: rgb(31, 49, 0);\n"
"color: rgb(200, 200, 200);\n"
" }\n"
"\n"
"\n"
"\n"
"")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.btnAssets = QPushButton(self.widget_3)
        self.btnAssets.setObjectName(u"btnAssets")
        self.btnAssets.setMinimumSize(QSize(18, 0))
        self.btnAssets.setStyleSheet(u"QPushButton {\n"
"    border-top-left-radius: 6px;\n"
"    border-bottom-left-radius: 6px;\n"
"    border-top-right-radius: 0px;\n"
"    border-bottom-right-radius: 0px;\n"
"\n"
"}")
        self.btnAssets.setCheckable(True)
        self.btnAssets.setChecked(True)

        self.horizontalLayout_2.addWidget(self.btnAssets)

        self.btnFiles = QPushButton(self.widget_3)
        self.btnFiles.setObjectName(u"btnFiles")
        self.btnFiles.setMinimumSize(QSize(18, 0))
        self.btnFiles.setStyleSheet(u"\n"
"    border-top-left-radius: 0px;\n"
"    border-bottom-left-radius: 0px;\n"
"    border-top-right-radius: 6px;\n"
"    border-bottom-right-radius: 6px;\n"
"")
        self.btnFiles.setCheckable(True)
        self.btnFiles.setChecked(False)
        self.btnFiles.setAutoDefault(False)
        self.btnFiles.setFlat(True)

        self.horizontalLayout_2.addWidget(self.btnFiles)


        self.horizontalLayout_7.addWidget(self.widget_3)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_4)


        self.verticalLayout.addLayout(self.horizontalLayout_7)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.widget = QWidget(arFiles)
        self.widget.setObjectName(u"widget")
        sizePolicy1.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy1)
        self.verticalLayout_4 = QVBoxLayout(self.widget)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(9, 0, 0, 0)
        self.widget_2 = QWidget(self.widget)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout_3 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.btnAddScene = QPushButton(self.widget_2)
        self.btnAddScene.setObjectName(u"btnAddScene")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.btnAddScene.sizePolicy().hasHeightForWidth())
        self.btnAddScene.setSizePolicy(sizePolicy2)
        self.btnAddScene.setMinimumSize(QSize(25, 25))
        self.btnAddScene.setMaximumSize(QSize(25, 25))
        self.btnAddScene.setSizeIncrement(QSize(0, 0))
        icon = QIcon()
        icon.addFile(u":/images/icons/plus_icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnAddScene.setIcon(icon)
        self.btnAddScene.setIconSize(QSize(12, 12))

        self.horizontalLayout_3.addWidget(self.btnAddScene)

        self.btnOpenFilesFolder = QPushButton(self.widget_2)
        self.btnOpenFilesFolder.setObjectName(u"btnOpenFilesFolder")
        self.btnOpenFilesFolder.setEnabled(True)
        sizePolicy2.setHeightForWidth(self.btnOpenFilesFolder.sizePolicy().hasHeightForWidth())
        self.btnOpenFilesFolder.setSizePolicy(sizePolicy2)
        self.btnOpenFilesFolder.setMinimumSize(QSize(25, 25))
        self.btnOpenFilesFolder.setMaximumSize(QSize(25, 25))
        self.btnOpenFilesFolder.setBaseSize(QSize(0, 0))
        self.btnOpenFilesFolder.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        icon1 = QIcon()
        icon1.addFile(u":/images/icons/open_folder.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnOpenFilesFolder.setIcon(icon1)
        self.btnOpenFilesFolder.setIconSize(QSize(16, 16))

        self.horizontalLayout_3.addWidget(self.btnOpenFilesFolder)

        self.btnOpenLastVersionScene = QPushButton(self.widget_2)
        self.btnOpenLastVersionScene.setObjectName(u"btnOpenLastVersionScene")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.btnOpenLastVersionScene.sizePolicy().hasHeightForWidth())
        self.btnOpenLastVersionScene.setSizePolicy(sizePolicy3)
        self.btnOpenLastVersionScene.setMinimumSize(QSize(25, 0))
        self.btnOpenLastVersionScene.setMaximumSize(QSize(25, 25))
        icon2 = QIcon()
        icon2.addFile(u":/images/icons/maya_icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnOpenLastVersionScene.setIcon(icon2)

        self.horizontalLayout_3.addWidget(self.btnOpenLastVersionScene)


        self.verticalLayout_4.addWidget(self.widget_2)

        self.listDepartments = QListWidget(self.widget)
        QListWidgetItem(self.listDepartments)
        QListWidgetItem(self.listDepartments)
        QListWidgetItem(self.listDepartments)
        QListWidgetItem(self.listDepartments)
        QListWidgetItem(self.listDepartments)
        QListWidgetItem(self.listDepartments)
        QListWidgetItem(self.listDepartments)
        QListWidgetItem(self.listDepartments)
        self.listDepartments.setObjectName(u"listDepartments")
        self.listDepartments.setEnabled(True)
        self.listDepartments.setMinimumSize(QSize(100, 0))
        self.listDepartments.setMaximumSize(QSize(100, 16777215))
        self.listDepartments.setStyleSheet(u"")
        self.listDepartments.setSortingEnabled(False)

        self.verticalLayout_4.addWidget(self.listDepartments)


        self.horizontalLayout.addWidget(self.widget)

        self.scrFiles = QScrollArea(arFiles)
        self.scrFiles.setObjectName(u"scrFiles")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.scrFiles.sizePolicy().hasHeightForWidth())
        self.scrFiles.setSizePolicy(sizePolicy4)
        self.scrFiles.setWidgetResizable(True)
        self.scrollAreaWidgetContents_4 = QWidget()
        self.scrollAreaWidgetContents_4.setObjectName(u"scrollAreaWidgetContents_4")
        self.scrollAreaWidgetContents_4.setGeometry(QRect(0, 0, 244, 215))
        self.gridLayout_17 = QGridLayout(self.scrollAreaWidgetContents_4)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.gridLayout_17.setVerticalSpacing(0)
        self.gridLayout_17.setContentsMargins(0, 0, 0, 0)
        self.layFiles2 = QWidget(self.scrollAreaWidgetContents_4)
        self.layFiles2.setObjectName(u"layFiles2")
        sizePolicy4.setHeightForWidth(self.layFiles2.sizePolicy().hasHeightForWidth())
        self.layFiles2.setSizePolicy(sizePolicy4)
        self.layFiles2.setMinimumSize(QSize(100, 0))
        self.layFiles2.setMaximumSize(QSize(16777215, 16777215))
        self.layFiles2.setSizeIncrement(QSize(0, 0))
        self.layFiles2.setBaseSize(QSize(0, 0))
        self.verticalLayout_8 = QVBoxLayout(self.layFiles2)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.stkFiles = QStackedWidget(self.layFiles2)
        self.stkFiles.setObjectName(u"stkFiles")
        sizePolicy4.setHeightForWidth(self.stkFiles.sizePolicy().hasHeightForWidth())
        self.stkFiles.setSizePolicy(sizePolicy4)
        self.stkFiles.setMaximumSize(QSize(16777215, 16777215))
        self.stkFiles.setSizeIncrement(QSize(0, 0))
        font = QFont()
        font.setPointSize(8)
        self.stkFiles.setFont(font)
        self.stkFiles.setStyleSheet(u"")
        self.page_0_modeling = QWidget()
        self.page_0_modeling.setObjectName(u"page_0_modeling")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.page_0_modeling.sizePolicy().hasHeightForWidth())
        self.page_0_modeling.setSizePolicy(sizePolicy5)
        self.verticalLayout_9 = QVBoxLayout(self.page_0_modeling)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(5, 5, 5, 5)
        self.label_15 = QLabel(self.page_0_modeling)
        self.label_15.setObjectName(u"label_15")
        sizePolicy3.setHeightForWidth(self.label_15.sizePolicy().hasHeightForWidth())
        self.label_15.setSizePolicy(sizePolicy3)
        self.label_15.setMaximumSize(QSize(16777215, 15))
        self.label_15.setFont(font)

        self.verticalLayout_9.addWidget(self.label_15)

        self.layFilesModeling = QVBoxLayout()
        self.layFilesModeling.setSpacing(6)
        self.layFilesModeling.setObjectName(u"layFilesModeling")

        self.verticalLayout_9.addLayout(self.layFilesModeling)

        self.verticalSpacer_19 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_9.addItem(self.verticalSpacer_19)

        self.stkFiles.addWidget(self.page_0_modeling)
        self.page_1_sculpting = QWidget()
        self.page_1_sculpting.setObjectName(u"page_1_sculpting")
        self.verticalLayout_3 = QVBoxLayout(self.page_1_sculpting)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(5, 5, 5, 5)
        self.label = QLabel(self.page_1_sculpting)
        self.label.setObjectName(u"label")
        sizePolicy3.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy3)
        self.label.setMaximumSize(QSize(16777215, 15))
        self.label.setFont(font)

        self.verticalLayout_3.addWidget(self.label)

        self.layFilesSculpting = QVBoxLayout()
        self.layFilesSculpting.setObjectName(u"layFilesSculpting")

        self.verticalLayout_3.addLayout(self.layFilesSculpting)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.stkFiles.addWidget(self.page_1_sculpting)
        self.page_2_baking = QWidget()
        self.page_2_baking.setObjectName(u"page_2_baking")
        sizePolicy3.setHeightForWidth(self.page_2_baking.sizePolicy().hasHeightForWidth())
        self.page_2_baking.setSizePolicy(sizePolicy3)
        self.gridLayout_18 = QGridLayout(self.page_2_baking)
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.gridLayout_18.setHorizontalSpacing(5)
        self.gridLayout_18.setContentsMargins(5, 5, 5, 5)
        self.label_16 = QLabel(self.page_2_baking)
        self.label_16.setObjectName(u"label_16")
        sizePolicy3.setHeightForWidth(self.label_16.sizePolicy().hasHeightForWidth())
        self.label_16.setSizePolicy(sizePolicy3)
        self.label_16.setMaximumSize(QSize(16777215, 15))

        self.gridLayout_18.addWidget(self.label_16, 0, 0, 1, 1)

        self.layFilesBaking = QVBoxLayout()
        self.layFilesBaking.setObjectName(u"layFilesBaking")

        self.gridLayout_18.addLayout(self.layFilesBaking, 1, 0, 1, 1)

        self.verticalSpacer_20 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_18.addItem(self.verticalSpacer_20, 2, 0, 1, 1)

        self.stkFiles.addWidget(self.page_2_baking)
        self.page_3_texturing = QWidget()
        self.page_3_texturing.setObjectName(u"page_3_texturing")
        sizePolicy3.setHeightForWidth(self.page_3_texturing.sizePolicy().hasHeightForWidth())
        self.page_3_texturing.setSizePolicy(sizePolicy3)
        self.gridLayout_19 = QGridLayout(self.page_3_texturing)
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.gridLayout_19.setHorizontalSpacing(5)
        self.gridLayout_19.setContentsMargins(5, 5, 5, 5)
        self.label_17 = QLabel(self.page_3_texturing)
        self.label_17.setObjectName(u"label_17")
        sizePolicy3.setHeightForWidth(self.label_17.sizePolicy().hasHeightForWidth())
        self.label_17.setSizePolicy(sizePolicy3)
        self.label_17.setMaximumSize(QSize(16777215, 15))

        self.gridLayout_19.addWidget(self.label_17, 0, 0, 1, 1)

        self.layFilesTexturing = QVBoxLayout()
        self.layFilesTexturing.setObjectName(u"layFilesTexturing")
        self.layFilesTexturing.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)

        self.gridLayout_19.addLayout(self.layFilesTexturing, 1, 0, 1, 1)

        self.verticalSpacer_21 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_19.addItem(self.verticalSpacer_21, 2, 0, 1, 1)

        self.stkFiles.addWidget(self.page_3_texturing)
        self.page_4_groom = QWidget()
        self.page_4_groom.setObjectName(u"page_4_groom")
        sizePolicy3.setHeightForWidth(self.page_4_groom.sizePolicy().hasHeightForWidth())
        self.page_4_groom.setSizePolicy(sizePolicy3)
        self.gridLayout_20 = QGridLayout(self.page_4_groom)
        self.gridLayout_20.setObjectName(u"gridLayout_20")
        self.gridLayout_20.setHorizontalSpacing(5)
        self.gridLayout_20.setContentsMargins(5, 5, 5, 5)
        self.label_18 = QLabel(self.page_4_groom)
        self.label_18.setObjectName(u"label_18")
        sizePolicy3.setHeightForWidth(self.label_18.sizePolicy().hasHeightForWidth())
        self.label_18.setSizePolicy(sizePolicy3)
        self.label_18.setMinimumSize(QSize(0, 0))
        self.label_18.setMaximumSize(QSize(16777215, 15))

        self.gridLayout_20.addWidget(self.label_18, 0, 0, 1, 1)

        self.layFilesGroom = QVBoxLayout()
        self.layFilesGroom.setObjectName(u"layFilesGroom")

        self.gridLayout_20.addLayout(self.layFilesGroom, 1, 0, 1, 1)

        self.verticalSpacer_22 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_20.addItem(self.verticalSpacer_22, 2, 0, 1, 1)

        self.stkFiles.addWidget(self.page_4_groom)
        self.page_5_rigging = QWidget()
        self.page_5_rigging.setObjectName(u"page_5_rigging")
        sizePolicy3.setHeightForWidth(self.page_5_rigging.sizePolicy().hasHeightForWidth())
        self.page_5_rigging.setSizePolicy(sizePolicy3)
        self.gridLayout_21 = QGridLayout(self.page_5_rigging)
        self.gridLayout_21.setObjectName(u"gridLayout_21")
        self.gridLayout_21.setHorizontalSpacing(5)
        self.gridLayout_21.setContentsMargins(5, 5, 5, 5)
        self.label_19 = QLabel(self.page_5_rigging)
        self.label_19.setObjectName(u"label_19")
        sizePolicy3.setHeightForWidth(self.label_19.sizePolicy().hasHeightForWidth())
        self.label_19.setSizePolicy(sizePolicy3)
        self.label_19.setMaximumSize(QSize(16777215, 15))

        self.gridLayout_21.addWidget(self.label_19, 0, 0, 1, 1)

        self.layFilesRigging = QVBoxLayout()
        self.layFilesRigging.setObjectName(u"layFilesRigging")

        self.gridLayout_21.addLayout(self.layFilesRigging, 1, 0, 1, 1)

        self.verticalSpacer_23 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_21.addItem(self.verticalSpacer_23, 2, 0, 1, 1)

        self.stkFiles.addWidget(self.page_5_rigging)
        self.page_6_pose = QWidget()
        self.page_6_pose.setObjectName(u"page_6_pose")
        sizePolicy3.setHeightForWidth(self.page_6_pose.sizePolicy().hasHeightForWidth())
        self.page_6_pose.setSizePolicy(sizePolicy3)
        self.gridLayout_22 = QGridLayout(self.page_6_pose)
        self.gridLayout_22.setObjectName(u"gridLayout_22")
        self.gridLayout_22.setHorizontalSpacing(5)
        self.gridLayout_22.setContentsMargins(5, 5, 5, 5)
        self.layFilesPose = QVBoxLayout()
        self.layFilesPose.setObjectName(u"layFilesPose")

        self.gridLayout_22.addLayout(self.layFilesPose, 1, 0, 1, 1)

        self.label_20 = QLabel(self.page_6_pose)
        self.label_20.setObjectName(u"label_20")
        sizePolicy3.setHeightForWidth(self.label_20.sizePolicy().hasHeightForWidth())
        self.label_20.setSizePolicy(sizePolicy3)
        self.label_20.setMaximumSize(QSize(16777215, 15))
        self.label_20.setFont(font)

        self.gridLayout_22.addWidget(self.label_20, 0, 0, 1, 1)

        self.verticalSpacer_24 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_22.addItem(self.verticalSpacer_24, 2, 0, 1, 1)

        self.stkFiles.addWidget(self.page_6_pose)
        self.page_7_animation = QWidget()
        self.page_7_animation.setObjectName(u"page_7_animation")
        sizePolicy3.setHeightForWidth(self.page_7_animation.sizePolicy().hasHeightForWidth())
        self.page_7_animation.setSizePolicy(sizePolicy3)
        self.gridLayout_23 = QGridLayout(self.page_7_animation)
        self.gridLayout_23.setObjectName(u"gridLayout_23")
        self.gridLayout_23.setHorizontalSpacing(5)
        self.gridLayout_23.setContentsMargins(5, 5, 5, 5)
        self.layFilesAnimation = QVBoxLayout()
        self.layFilesAnimation.setObjectName(u"layFilesAnimation")

        self.gridLayout_23.addLayout(self.layFilesAnimation, 1, 0, 1, 1)

        self.verticalSpacer_25 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_23.addItem(self.verticalSpacer_25, 2, 0, 1, 1)

        self.label_21 = QLabel(self.page_7_animation)
        self.label_21.setObjectName(u"label_21")
        sizePolicy3.setHeightForWidth(self.label_21.sizePolicy().hasHeightForWidth())
        self.label_21.setSizePolicy(sizePolicy3)
        self.label_21.setMaximumSize(QSize(16777215, 15))
        self.label_21.setFont(font)

        self.gridLayout_23.addWidget(self.label_21, 0, 0, 1, 1)

        self.stkFiles.addWidget(self.page_7_animation)

        self.verticalLayout_8.addWidget(self.stkFiles)

        self.verticalSpacer_26 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.MinimumExpanding)

        self.verticalLayout_8.addItem(self.verticalSpacer_26)


        self.gridLayout_17.addWidget(self.layFiles2, 0, 0, 1, 1)

        self.scrFiles.setWidget(self.scrollAreaWidgetContents_4)

        self.horizontalLayout.addWidget(self.scrFiles)

        self.wgtSpacerAssets = QWidget(arFiles)
        self.wgtSpacerAssets.setObjectName(u"wgtSpacerAssets")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.wgtSpacerAssets.sizePolicy().hasHeightForWidth())
        self.wgtSpacerAssets.setSizePolicy(sizePolicy6)

        self.horizontalLayout.addWidget(self.wgtSpacerAssets)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.wgtAssets = QWidget(arFiles)
        self.wgtAssets.setObjectName(u"wgtAssets")
        sizePolicy4.setHeightForWidth(self.wgtAssets.sizePolicy().hasHeightForWidth())
        self.wgtAssets.setSizePolicy(sizePolicy4)
        self.gridLayout_9 = QGridLayout(self.wgtAssets)
        self.gridLayout_9.setSpacing(0)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = QScrollArea(self.wgtAssets)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setFrameShadow(QFrame.Shadow.Sunken)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 613, 163))
        self.verticalLayout_7 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(9, 0, 9, 0)
        self.layBlueprints = QVBoxLayout()
        self.layBlueprints.setSpacing(0)
        self.layBlueprints.setObjectName(u"layBlueprints")

        self.verticalLayout_7.addLayout(self.layBlueprints)

        self.layAsset = QVBoxLayout()
        self.layAsset.setSpacing(0)
        self.layAsset.setObjectName(u"layAsset")

        self.verticalLayout_7.addLayout(self.layAsset)

        self.verticalSpacer_9 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_9)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_9.addWidget(self.scrollArea, 0, 0, 1, 1)


        self.verticalLayout.addWidget(self.wgtAssets)


        self.retranslateUi(arFiles)

        self.listDepartments.setCurrentRow(0)
        self.stkFiles.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(arFiles)
    # setupUi

    def retranslateUi(self, arFiles):
        arFiles.setWindowTitle(QCoreApplication.translate("arFiles", u"Pixels and Crafts Pipeline", None))
        self.btnAssets.setText(QCoreApplication.translate("arFiles", u"Assets", None))
        self.btnFiles.setText(QCoreApplication.translate("arFiles", u"Files", None))
#if QT_CONFIG(tooltip)
        self.btnAddScene.setToolTip(QCoreApplication.translate("arFiles", u"Create new project for selected department", None))
#endif // QT_CONFIG(tooltip)
        self.btnAddScene.setText("")
#if QT_CONFIG(tooltip)
        self.btnOpenFilesFolder.setToolTip(QCoreApplication.translate("arFiles", u"Open scenes folder", None))
#endif // QT_CONFIG(tooltip)
        self.btnOpenFilesFolder.setText("")
#if QT_CONFIG(tooltip)
        self.btnOpenLastVersionScene.setToolTip(QCoreApplication.translate("arFiles", u"Open last version scene", None))
#endif // QT_CONFIG(tooltip)
        self.btnOpenLastVersionScene.setText("")

        __sortingEnabled = self.listDepartments.isSortingEnabled()
        self.listDepartments.setSortingEnabled(False)
        ___qlistwidgetitem = self.listDepartments.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("arFiles", u"Modeling", None));
        ___qlistwidgetitem1 = self.listDepartments.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("arFiles", u"Sculpting", None));
        ___qlistwidgetitem2 = self.listDepartments.item(2)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("arFiles", u"Baking", None));
        ___qlistwidgetitem3 = self.listDepartments.item(3)
        ___qlistwidgetitem3.setText(QCoreApplication.translate("arFiles", u"Texturing", None));
        ___qlistwidgetitem4 = self.listDepartments.item(4)
        ___qlistwidgetitem4.setText(QCoreApplication.translate("arFiles", u"Groom", None));
        ___qlistwidgetitem5 = self.listDepartments.item(5)
        ___qlistwidgetitem5.setText(QCoreApplication.translate("arFiles", u"Rigging", None));
        ___qlistwidgetitem6 = self.listDepartments.item(6)
        ___qlistwidgetitem6.setText(QCoreApplication.translate("arFiles", u"Pose", None));
        ___qlistwidgetitem7 = self.listDepartments.item(7)
        ___qlistwidgetitem7.setText(QCoreApplication.translate("arFiles", u"Animation", None));
        self.listDepartments.setSortingEnabled(__sortingEnabled)

        self.label_15.setText(QCoreApplication.translate("arFiles", u"Modeling files", None))
        self.label.setText(QCoreApplication.translate("arFiles", u"Sculpting files", None))
        self.label_16.setText(QCoreApplication.translate("arFiles", u"Baking files", None))
        self.label_17.setText(QCoreApplication.translate("arFiles", u"Texturing files", None))
        self.label_18.setText(QCoreApplication.translate("arFiles", u"Groom files", None))
        self.label_19.setText(QCoreApplication.translate("arFiles", u"Rigging files", None))
        self.label_20.setText(QCoreApplication.translate("arFiles", u"Pose files", None))
        self.label_21.setText(QCoreApplication.translate("arFiles", u"Animation files", None))
    # retranslateUi


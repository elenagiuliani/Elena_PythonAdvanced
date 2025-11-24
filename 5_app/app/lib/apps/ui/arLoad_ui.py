# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'arLoad.ui'
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

class Ui_arLoad(object):
    def setupUi(self, arLoad):
        if not arLoad.objectName():
            arLoad.setObjectName(u"arLoad")
        arLoad.resize(468, 340)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(arLoad.sizePolicy().hasHeightForWidth())
        arLoad.setSizePolicy(sizePolicy)
        arLoad.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(arLoad)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, -1, -1, -1)
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_3)

        self.btnAssets = QPushButton(arLoad)
        self.btnAssets.setObjectName(u"btnAssets")
        self.btnAssets.setCheckable(True)
        self.btnAssets.setChecked(True)

        self.horizontalLayout_7.addWidget(self.btnAssets)

        self.btnFiles = QPushButton(arLoad)
        self.btnFiles.setObjectName(u"btnFiles")
        self.btnFiles.setCheckable(True)

        self.horizontalLayout_7.addWidget(self.btnFiles)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_4)


        self.verticalLayout.addLayout(self.horizontalLayout_7)

        self.stkAssetsFiles = QStackedWidget(arLoad)
        self.stkAssetsFiles.setObjectName(u"stkAssetsFiles")
        self.pageAssets = QWidget()
        self.pageAssets.setObjectName(u"pageAssets")
        self.pageAssets.setEnabled(True)
        self.verticalLayout_8 = QVBoxLayout(self.pageAssets)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = QScrollArea(self.pageAssets)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setFrameShadow(QFrame.Shadow.Sunken)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 457, 288))
        self.verticalLayout_3 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(9, 0, 9, -1)
        self.layBlueprints = QVBoxLayout()
        self.layBlueprints.setObjectName(u"layBlueprints")

        self.verticalLayout_3.addLayout(self.layBlueprints)

        self.layAsset = QVBoxLayout()
        self.layAsset.setObjectName(u"layAsset")

        self.verticalLayout_3.addLayout(self.layAsset)

        self.verticalSpacer_10 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_10)

        self.lblAssetsFeedback = QLabel(self.scrollAreaWidgetContents)
        self.lblAssetsFeedback.setObjectName(u"lblAssetsFeedback")
        self.lblAssetsFeedback.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.lblAssetsFeedback)

        self.verticalSpacer_9 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_9)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_8.addWidget(self.scrollArea)

        self.stkAssetsFiles.addWidget(self.pageAssets)
        self.pageFiles = QWidget()
        self.pageFiles.setObjectName(u"pageFiles")
        self.horizontalLayout = QHBoxLayout(self.pageFiles)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, -1, 0, -1)
        self.widget = QWidget(self.pageFiles)
        self.widget.setObjectName(u"widget")
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setMaximumSize(QSize(100, 16777215))
        self.gridLayout_2 = QGridLayout(self.widget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.btnAddScene = QPushButton(self.widget)
        self.btnAddScene.setObjectName(u"btnAddScene")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btnAddScene.sizePolicy().hasHeightForWidth())
        self.btnAddScene.setSizePolicy(sizePolicy1)
        self.btnAddScene.setMinimumSize(QSize(25, 25))
        self.btnAddScene.setMaximumSize(QSize(25, 25))
        self.btnAddScene.setSizeIncrement(QSize(0, 0))
        icon = QIcon()
        icon.addFile(u":/images/icons/plus_icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnAddScene.setIcon(icon)
        self.btnAddScene.setIconSize(QSize(12, 12))

        self.gridLayout_2.addWidget(self.btnAddScene, 0, 0, 1, 1)

        self.listDepartments = QListWidget(self.widget)
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

        self.gridLayout_2.addWidget(self.listDepartments, 1, 0, 1, 1)


        self.horizontalLayout.addWidget(self.widget)

        self.scrollArea_2 = QScrollArea(self.pageFiles)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 342, 270))
        self.gridLayout = QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setVerticalSpacing(0)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.layFiles2 = QWidget(self.scrollAreaWidgetContents_2)
        self.layFiles2.setObjectName(u"layFiles2")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.layFiles2.sizePolicy().hasHeightForWidth())
        self.layFiles2.setSizePolicy(sizePolicy2)
        self.layFiles2.setMinimumSize(QSize(100, 0))
        self.layFiles2.setMaximumSize(QSize(16777215, 16777215))
        self.layFiles2.setSizeIncrement(QSize(0, 0))
        self.layFiles2.setBaseSize(QSize(0, 0))
        self.verticalLayout_2 = QVBoxLayout(self.layFiles2)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.stkFiles = QStackedWidget(self.layFiles2)
        self.stkFiles.setObjectName(u"stkFiles")
        sizePolicy2.setHeightForWidth(self.stkFiles.sizePolicy().hasHeightForWidth())
        self.stkFiles.setSizePolicy(sizePolicy2)
        self.stkFiles.setMaximumSize(QSize(16777215, 16777215))
        self.stkFiles.setSizeIncrement(QSize(0, 0))
        font = QFont()
        font.setPointSize(8)
        self.stkFiles.setFont(font)
        self.stkFiles.setStyleSheet(u"")
        self.page_0_modeling = QWidget()
        self.page_0_modeling.setObjectName(u"page_0_modeling")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.page_0_modeling.sizePolicy().hasHeightForWidth())
        self.page_0_modeling.setSizePolicy(sizePolicy3)
        self.verticalLayout_4 = QVBoxLayout(self.page_0_modeling)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(5, 5, 5, 5)
        self.label_5 = QLabel(self.page_0_modeling)
        self.label_5.setObjectName(u"label_5")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy4)
        self.label_5.setMaximumSize(QSize(16777215, 15))
        self.label_5.setFont(font)

        self.verticalLayout_4.addWidget(self.label_5)

        self.layFilesModeling = QVBoxLayout()
        self.layFilesModeling.setSpacing(6)
        self.layFilesModeling.setObjectName(u"layFilesModeling")

        self.verticalLayout_4.addLayout(self.layFilesModeling)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)

        self.stkFiles.addWidget(self.page_0_modeling)
        self.page_1_baking = QWidget()
        self.page_1_baking.setObjectName(u"page_1_baking")
        sizePolicy4.setHeightForWidth(self.page_1_baking.sizePolicy().hasHeightForWidth())
        self.page_1_baking.setSizePolicy(sizePolicy4)
        self.gridLayout_3 = QGridLayout(self.page_1_baking)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setHorizontalSpacing(5)
        self.gridLayout_3.setContentsMargins(5, 5, 5, 5)
        self.label_6 = QLabel(self.page_1_baking)
        self.label_6.setObjectName(u"label_6")
        sizePolicy4.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy4)
        self.label_6.setMaximumSize(QSize(16777215, 15))

        self.gridLayout_3.addWidget(self.label_6, 0, 0, 1, 1)

        self.layFilesBaking = QVBoxLayout()
        self.layFilesBaking.setObjectName(u"layFilesBaking")

        self.gridLayout_3.addLayout(self.layFilesBaking, 1, 0, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_4, 2, 0, 1, 1)

        self.stkFiles.addWidget(self.page_1_baking)
        self.page_2_texturing = QWidget()
        self.page_2_texturing.setObjectName(u"page_2_texturing")
        sizePolicy4.setHeightForWidth(self.page_2_texturing.sizePolicy().hasHeightForWidth())
        self.page_2_texturing.setSizePolicy(sizePolicy4)
        self.gridLayout_4 = QGridLayout(self.page_2_texturing)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setHorizontalSpacing(5)
        self.gridLayout_4.setContentsMargins(5, 5, 5, 5)
        self.label_7 = QLabel(self.page_2_texturing)
        self.label_7.setObjectName(u"label_7")
        sizePolicy4.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy4)
        self.label_7.setMaximumSize(QSize(16777215, 15))

        self.gridLayout_4.addWidget(self.label_7, 0, 0, 1, 1)

        self.layFilesTexturing = QVBoxLayout()
        self.layFilesTexturing.setObjectName(u"layFilesTexturing")
        self.layFilesTexturing.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)

        self.gridLayout_4.addLayout(self.layFilesTexturing, 1, 0, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer_3, 2, 0, 1, 1)

        self.stkFiles.addWidget(self.page_2_texturing)
        self.page_3_groom = QWidget()
        self.page_3_groom.setObjectName(u"page_3_groom")
        sizePolicy4.setHeightForWidth(self.page_3_groom.sizePolicy().hasHeightForWidth())
        self.page_3_groom.setSizePolicy(sizePolicy4)
        self.gridLayout_5 = QGridLayout(self.page_3_groom)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setHorizontalSpacing(5)
        self.gridLayout_5.setContentsMargins(5, 5, 5, 5)
        self.label = QLabel(self.page_3_groom)
        self.label.setObjectName(u"label")
        sizePolicy4.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy4)
        self.label.setMinimumSize(QSize(0, 0))
        self.label.setMaximumSize(QSize(16777215, 15))

        self.gridLayout_5.addWidget(self.label, 0, 0, 1, 1)

        self.layFilesGroom = QVBoxLayout()
        self.layFilesGroom.setObjectName(u"layFilesGroom")

        self.gridLayout_5.addLayout(self.layFilesGroom, 1, 0, 1, 1)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_5.addItem(self.verticalSpacer_5, 2, 0, 1, 1)

        self.stkFiles.addWidget(self.page_3_groom)
        self.page_4_rigging = QWidget()
        self.page_4_rigging.setObjectName(u"page_4_rigging")
        sizePolicy4.setHeightForWidth(self.page_4_rigging.sizePolicy().hasHeightForWidth())
        self.page_4_rigging.setSizePolicy(sizePolicy4)
        self.gridLayout_6 = QGridLayout(self.page_4_rigging)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setHorizontalSpacing(5)
        self.gridLayout_6.setContentsMargins(5, 5, 5, 5)
        self.layFilesRigging = QVBoxLayout()
        self.layFilesRigging.setObjectName(u"layFilesRigging")

        self.gridLayout_6.addLayout(self.layFilesRigging, 1, 0, 1, 1)

        self.label_2 = QLabel(self.page_4_rigging)
        self.label_2.setObjectName(u"label_2")
        sizePolicy4.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy4)
        self.label_2.setMaximumSize(QSize(16777215, 15))

        self.gridLayout_6.addWidget(self.label_2, 0, 0, 1, 1)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_6.addItem(self.verticalSpacer_6, 2, 0, 1, 1)

        self.stkFiles.addWidget(self.page_4_rigging)
        self.page_5_pose = QWidget()
        self.page_5_pose.setObjectName(u"page_5_pose")
        sizePolicy4.setHeightForWidth(self.page_5_pose.sizePolicy().hasHeightForWidth())
        self.page_5_pose.setSizePolicy(sizePolicy4)
        self.gridLayout_7 = QGridLayout(self.page_5_pose)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setHorizontalSpacing(5)
        self.gridLayout_7.setContentsMargins(5, 5, 5, 5)
        self.layFilesPose = QVBoxLayout()
        self.layFilesPose.setObjectName(u"layFilesPose")

        self.gridLayout_7.addLayout(self.layFilesPose, 1, 0, 1, 1)

        self.label_3 = QLabel(self.page_5_pose)
        self.label_3.setObjectName(u"label_3")
        sizePolicy4.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy4)
        self.label_3.setMaximumSize(QSize(16777215, 15))
        self.label_3.setFont(font)

        self.gridLayout_7.addWidget(self.label_3, 0, 0, 1, 1)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_7.addItem(self.verticalSpacer_7, 2, 0, 1, 1)

        self.stkFiles.addWidget(self.page_5_pose)
        self.page_6_animation = QWidget()
        self.page_6_animation.setObjectName(u"page_6_animation")
        sizePolicy4.setHeightForWidth(self.page_6_animation.sizePolicy().hasHeightForWidth())
        self.page_6_animation.setSizePolicy(sizePolicy4)
        self.gridLayout_8 = QGridLayout(self.page_6_animation)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setHorizontalSpacing(5)
        self.gridLayout_8.setContentsMargins(5, 5, 5, 5)
        self.label_4 = QLabel(self.page_6_animation)
        self.label_4.setObjectName(u"label_4")
        sizePolicy4.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy4)
        self.label_4.setMaximumSize(QSize(16777215, 15))
        self.label_4.setFont(font)

        self.gridLayout_8.addWidget(self.label_4, 0, 0, 1, 1)

        self.layFilesAnimation = QVBoxLayout()
        self.layFilesAnimation.setObjectName(u"layFilesAnimation")

        self.gridLayout_8.addLayout(self.layFilesAnimation, 1, 0, 1, 1)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_8.addItem(self.verticalSpacer_8, 2, 0, 1, 1)

        self.stkFiles.addWidget(self.page_6_animation)

        self.verticalLayout_2.addWidget(self.stkFiles)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.MinimumExpanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.gridLayout.addWidget(self.layFiles2, 1, 0, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.btnOpenFilesFolder = QPushButton(self.scrollAreaWidgetContents_2)
        self.btnOpenFilesFolder.setObjectName(u"btnOpenFilesFolder")
        sizePolicy1.setHeightForWidth(self.btnOpenFilesFolder.sizePolicy().hasHeightForWidth())
        self.btnOpenFilesFolder.setSizePolicy(sizePolicy1)
        self.btnOpenFilesFolder.setMinimumSize(QSize(25, 25))
        self.btnOpenFilesFolder.setMaximumSize(QSize(25, 25))
        self.btnOpenFilesFolder.setBaseSize(QSize(0, 0))
        icon1 = QIcon()
        icon1.addFile(u":/images/icons/open_folder.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnOpenFilesFolder.setIcon(icon1)
        self.btnOpenFilesFolder.setIconSize(QSize(16, 16))

        self.horizontalLayout_3.addWidget(self.btnOpenFilesFolder)

        self.btnOpenLastVersionScene = QPushButton(self.scrollAreaWidgetContents_2)
        self.btnOpenLastVersionScene.setObjectName(u"btnOpenLastVersionScene")
        sizePolicy4.setHeightForWidth(self.btnOpenLastVersionScene.sizePolicy().hasHeightForWidth())
        self.btnOpenLastVersionScene.setSizePolicy(sizePolicy4)
        self.btnOpenLastVersionScene.setMinimumSize(QSize(25, 0))
        self.btnOpenLastVersionScene.setMaximumSize(QSize(25, 25))
        icon2 = QIcon()
        icon2.addFile(u":/images/icons/maya_icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnOpenLastVersionScene.setIcon(icon2)

        self.horizontalLayout_3.addWidget(self.btnOpenLastVersionScene)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)


        self.gridLayout.addLayout(self.horizontalLayout_3, 0, 0, 1, 1)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.horizontalLayout.addWidget(self.scrollArea_2)

        self.stkAssetsFiles.addWidget(self.pageFiles)

        self.verticalLayout.addWidget(self.stkAssetsFiles)


        self.retranslateUi(arLoad)

        self.stkAssetsFiles.setCurrentIndex(0)
        self.listDepartments.setCurrentRow(0)
        self.stkFiles.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(arLoad)
    # setupUi

    def retranslateUi(self, arLoad):
        arLoad.setWindowTitle(QCoreApplication.translate("arLoad", u"Pixels and Crafts Pipeline", None))
        self.btnAssets.setText(QCoreApplication.translate("arLoad", u"Assets", None))
        self.btnFiles.setText(QCoreApplication.translate("arLoad", u"Files", None))
        self.lblAssetsFeedback.setText("")
        self.btnAddScene.setText("")

        __sortingEnabled = self.listDepartments.isSortingEnabled()
        self.listDepartments.setSortingEnabled(False)
        ___qlistwidgetitem = self.listDepartments.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("arLoad", u"Modeling", None));
        ___qlistwidgetitem1 = self.listDepartments.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("arLoad", u"Baking set up", None));
        ___qlistwidgetitem2 = self.listDepartments.item(2)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("arLoad", u"Texturing", None));
        ___qlistwidgetitem3 = self.listDepartments.item(3)
        ___qlistwidgetitem3.setText(QCoreApplication.translate("arLoad", u"Groom", None));
        ___qlistwidgetitem4 = self.listDepartments.item(4)
        ___qlistwidgetitem4.setText(QCoreApplication.translate("arLoad", u"Rigging", None));
        ___qlistwidgetitem5 = self.listDepartments.item(5)
        ___qlistwidgetitem5.setText(QCoreApplication.translate("arLoad", u"Pose", None));
        ___qlistwidgetitem6 = self.listDepartments.item(6)
        ___qlistwidgetitem6.setText(QCoreApplication.translate("arLoad", u"Animation", None));
        self.listDepartments.setSortingEnabled(__sortingEnabled)

        self.label_5.setText(QCoreApplication.translate("arLoad", u"Modeling files", None))
        self.label_6.setText(QCoreApplication.translate("arLoad", u"Baking files", None))
        self.label_7.setText(QCoreApplication.translate("arLoad", u"Texturing files", None))
        self.label.setText(QCoreApplication.translate("arLoad", u"Groom files", None))
        self.label_2.setText(QCoreApplication.translate("arLoad", u"Rigging files", None))
        self.label_3.setText(QCoreApplication.translate("arLoad", u"Pose files", None))
        self.label_4.setText(QCoreApplication.translate("arLoad", u"Animation files", None))
        self.btnOpenFilesFolder.setText("")
        self.btnOpenLastVersionScene.setText("")
    # retranslateUi


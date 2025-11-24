# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'arType.ui'
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
    QStackedWidget, QTabWidget, QVBoxLayout, QWidget)
import app_imgs_rc

class Ui_arType(object):
    def setupUi(self, arType):
        if not arType.objectName():
            arType.setObjectName(u"arType")
        arType.resize(595, 386)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(arType.sizePolicy().hasHeightForWidth())
        arType.setSizePolicy(sizePolicy)
        arType.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(arType)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 4, 0)
        self.wgMain_2 = QWidget(arType)
        self.wgMain_2.setObjectName(u"wgMain_2")
        self.verticalLayout_7 = QVBoxLayout(self.wgMain_2)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(-1, 0, -1, -1)
        self.tabWidget = QTabWidget(self.wgMain_2)
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
        self.tabArchitectural.setEnabled(True)
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.tabArchitectural.sizePolicy().hasHeightForWidth())
        self.tabArchitectural.setSizePolicy(sizePolicy2)
        self.tabArchitectural.setMinimumSize(QSize(200, 0))
        self.verticalLayout_2 = QVBoxLayout(self.tabArchitectural)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.stkTabArch = QStackedWidget(self.tabArchitectural)
        self.stkTabArch.setObjectName(u"stkTabArch")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.gridLayout_3 = QGridLayout(self.page)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.layTabArch = QVBoxLayout()
        self.layTabArch.setObjectName(u"layTabArch")

        self.gridLayout_3.addLayout(self.layTabArch, 0, 0, 1, 1)

        self.stkTabArch.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.gridLayout_4 = QGridLayout(self.page_2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.layTabArchProjects = QVBoxLayout()
        self.layTabArchProjects.setObjectName(u"layTabArchProjects")
        self.layTabArchProjects.setContentsMargins(0, 0, -1, -1)
        self.scrollArea = QScrollArea(self.page_2)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 387, 356))
        self.gridLayout_10 = QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.listEnvironmentProjects = QListWidget(self.scrollAreaWidgetContents_2)
        QListWidgetItem(self.listEnvironmentProjects)
        self.listEnvironmentProjects.setObjectName(u"listEnvironmentProjects")

        self.gridLayout_10.addWidget(self.listEnvironmentProjects, 0, 0, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)

        self.layTabArchProjects.addWidget(self.scrollArea)


        self.gridLayout_4.addLayout(self.layTabArchProjects, 0, 0, 1, 1)

        self.stkTabArch.addWidget(self.page_2)

        self.verticalLayout_2.addWidget(self.stkTabArch)

        self.tabWidget.addTab(self.tabArchitectural, "")
        self.tabProps = QWidget()
        self.tabProps.setObjectName(u"tabProps")
        self.verticalLayout_4 = QVBoxLayout(self.tabProps)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.stkTabProps = QStackedWidget(self.tabProps)
        self.stkTabProps.setObjectName(u"stkTabProps")
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.gridLayout_5 = QGridLayout(self.page_3)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.layTabProps = QVBoxLayout()
        self.layTabProps.setObjectName(u"layTabProps")

        self.gridLayout_5.addLayout(self.layTabProps, 0, 0, 1, 1)

        self.stkTabProps.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.gridLayout_7 = QGridLayout(self.page_4)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.layTabPropsProjects = QVBoxLayout()
        self.layTabPropsProjects.setObjectName(u"layTabPropsProjects")
        self.scrollArea_2 = QScrollArea(self.page_4)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_5 = QWidget()
        self.scrollAreaWidgetContents_5.setObjectName(u"scrollAreaWidgetContents_5")
        self.scrollAreaWidgetContents_5.setGeometry(QRect(0, 0, 387, 356))
        self.gridLayout_11 = QGridLayout(self.scrollAreaWidgetContents_5)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.listPropsProjects = QListWidget(self.scrollAreaWidgetContents_5)
        self.listPropsProjects.setObjectName(u"listPropsProjects")

        self.gridLayout_11.addWidget(self.listPropsProjects, 0, 0, 1, 1)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_5)

        self.layTabPropsProjects.addWidget(self.scrollArea_2)


        self.gridLayout_7.addLayout(self.layTabPropsProjects, 0, 0, 1, 1)

        self.stkTabProps.addWidget(self.page_4)

        self.verticalLayout_4.addWidget(self.stkTabProps)

        self.tabWidget.addTab(self.tabProps, "")
        self.tabLamps = QWidget()
        self.tabLamps.setObjectName(u"tabLamps")
        self.verticalLayout_5 = QVBoxLayout(self.tabLamps)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.stkTab3Dscans = QStackedWidget(self.tabLamps)
        self.stkTab3Dscans.setObjectName(u"stkTab3Dscans")
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.gridLayout_8 = QGridLayout(self.page_5)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.layTabLamps = QVBoxLayout()
        self.layTabLamps.setObjectName(u"layTabLamps")

        self.gridLayout_8.addLayout(self.layTabLamps, 0, 0, 1, 1)

        self.stkTab3Dscans.addWidget(self.page_5)
        self.page_6 = QWidget()
        self.page_6.setObjectName(u"page_6")
        self.gridLayout_9 = QGridLayout(self.page_6)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.layTabLampsProjects = QVBoxLayout()
        self.layTabLampsProjects.setObjectName(u"layTabLampsProjects")
        self.scrollArea_3 = QScrollArea(self.page_6)
        self.scrollArea_3.setObjectName(u"scrollArea_3")
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollAreaWidgetContents_6 = QWidget()
        self.scrollAreaWidgetContents_6.setObjectName(u"scrollAreaWidgetContents_6")
        self.scrollAreaWidgetContents_6.setGeometry(QRect(0, 0, 387, 356))
        self.gridLayout_12 = QGridLayout(self.scrollAreaWidgetContents_6)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.list3DscansProjects = QListWidget(self.scrollAreaWidgetContents_6)
        self.list3DscansProjects.setObjectName(u"list3DscansProjects")

        self.gridLayout_12.addWidget(self.list3DscansProjects, 0, 0, 1, 1)

        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_6)

        self.layTabLampsProjects.addWidget(self.scrollArea_3)


        self.gridLayout_9.addLayout(self.layTabLampsProjects, 0, 0, 1, 1)

        self.stkTab3Dscans.addWidget(self.page_6)

        self.verticalLayout_5.addWidget(self.stkTab3Dscans)

        self.tabWidget.addTab(self.tabLamps, "")

        self.horizontalLayout_5.addWidget(self.tabWidget)

        self.stkDetails = QStackedWidget(self.wgMain_2)
        self.stkDetails.setObjectName(u"stkDetails")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(1)
        sizePolicy3.setHeightForWidth(self.stkDetails.sizePolicy().hasHeightForWidth())
        self.stkDetails.setSizePolicy(sizePolicy3)
        self.stkDetails.setMaximumSize(QSize(150, 16777215))
        self.page_manage_projects = QWidget()
        self.page_manage_projects.setObjectName(u"page_manage_projects")
        self.gridLayout = QGridLayout(self.page_manage_projects)
        self.gridLayout.setObjectName(u"gridLayout")
        self.layDetails = QVBoxLayout()
        self.layDetails.setObjectName(u"layDetails")
        self.layDetails.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.layDetails.setContentsMargins(0, -1, 0, -1)
        self.label_2 = QLabel(self.page_manage_projects)
        self.label_2.setObjectName(u"label_2")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(1)
        sizePolicy4.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy4)
        self.label_2.setMaximumSize(QSize(600, 30))

        self.layDetails.addWidget(self.label_2)

        self.line = QFrame(self.page_manage_projects)
        self.line.setObjectName(u"line")
        self.line.setStyleSheet(u"")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.layDetails.addWidget(self.line)

        self.layMeshesInfo = QGridLayout()
        self.layMeshesInfo.setObjectName(u"layMeshesInfo")
        self.lblInteractiveMeshesNumber = QLabel(self.page_manage_projects)
        self.lblInteractiveMeshesNumber.setObjectName(u"lblInteractiveMeshesNumber")
        self.lblInteractiveMeshesNumber.setMargin(5)

        self.layMeshesInfo.addWidget(self.lblInteractiveMeshesNumber, 3, 1, 1, 1)

        self.lblProjectType = QLabel(self.page_manage_projects)
        self.lblProjectType.setObjectName(u"lblProjectType")

        self.layMeshesInfo.addWidget(self.lblProjectType, 1, 0, 1, 1)

        self.lblUniqueMeshesNumber = QLabel(self.page_manage_projects)
        self.lblUniqueMeshesNumber.setObjectName(u"lblUniqueMeshesNumber")
        self.lblUniqueMeshesNumber.setMargin(5)

        self.layMeshesInfo.addWidget(self.lblUniqueMeshesNumber, 2, 1, 1, 1)

        self.lblInteractiveMeshes = QLabel(self.page_manage_projects)
        self.lblInteractiveMeshes.setObjectName(u"lblInteractiveMeshes")

        self.layMeshesInfo.addWidget(self.lblInteractiveMeshes, 3, 0, 1, 1)

        self.lblUniqueMeshes = QLabel(self.page_manage_projects)
        self.lblUniqueMeshes.setObjectName(u"lblUniqueMeshes")

        self.layMeshesInfo.addWidget(self.lblUniqueMeshes, 2, 0, 1, 1)


        self.layDetails.addLayout(self.layMeshesInfo)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.layDetails.addItem(self.verticalSpacer_2)

        self.widget_7 = QWidget(self.page_manage_projects)
        self.widget_7.setObjectName(u"widget_7")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.widget_7.sizePolicy().hasHeightForWidth())
        self.widget_7.setSizePolicy(sizePolicy5)
        self.widget_7.setMinimumSize(QSize(50, 50))
        self.widget_7.setMaximumSize(QSize(300, 300))
        self.widget_7.setSizeIncrement(QSize(0, 0))
        self.widget_7.setBaseSize(QSize(0, 0))
        self.gridLayout_6 = QGridLayout(self.widget_7)
        self.gridLayout_6.setSpacing(0)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer_4, 0, 2, 1, 1)

        self.imgRef = QPushButton(self.widget_7)
        self.imgRef.setObjectName(u"imgRef")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.imgRef.sizePolicy().hasHeightForWidth())
        self.imgRef.setSizePolicy(sizePolicy6)
        self.imgRef.setMinimumSize(QSize(90, 90))
        self.imgRef.setMaximumSize(QSize(300, 300))
        self.imgRef.setSizeIncrement(QSize(0, 0))
        self.imgRef.setBaseSize(QSize(0, 0))
        self.imgRef.setAutoFillBackground(False)

        self.gridLayout_6.addWidget(self.imgRef, 0, 1, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer_5, 0, 0, 1, 1)


        self.layDetails.addWidget(self.widget_7)


        self.gridLayout.addLayout(self.layDetails, 0, 0, 1, 1)

        self.stkDetails.addWidget(self.page_manage_projects)
        self.page_create_project = QWidget()
        self.page_create_project.setObjectName(u"page_create_project")
        self.gridLayout_2 = QGridLayout(self.page_create_project)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(-1, 9, -1, -1)
        self.verticalSpacer = QSpacerItem(20, 150, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.lblManageFeedback = QLabel(self.page_create_project)
        self.lblManageFeedback.setObjectName(u"lblManageFeedback")
        self.lblManageFeedback.setMinimumSize(QSize(0, 120))
        self.lblManageFeedback.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.lblManageFeedback)

        self.widget = QWidget(self.page_create_project)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.btnSetProject = QPushButton(self.widget)
        self.btnSetProject.setObjectName(u"btnSetProject")
        sizePolicy5.setHeightForWidth(self.btnSetProject.sizePolicy().hasHeightForWidth())
        self.btnSetProject.setSizePolicy(sizePolicy5)
        self.btnSetProject.setMinimumSize(QSize(90, 0))
        self.btnSetProject.setMaximumSize(QSize(90, 16777215))

        self.horizontalLayout.addWidget(self.btnSetProject)


        self.verticalLayout_3.addWidget(self.widget)


        self.gridLayout_2.addLayout(self.verticalLayout_3, 0, 0, 1, 1)

        self.stkDetails.addWidget(self.page_create_project)

        self.horizontalLayout_5.addWidget(self.stkDetails)


        self.verticalLayout_7.addLayout(self.horizontalLayout_5)


        self.verticalLayout.addWidget(self.wgMain_2)


        self.retranslateUi(arType)

        self.tabWidget.setCurrentIndex(0)
        self.stkTabArch.setCurrentIndex(0)
        self.stkTabProps.setCurrentIndex(0)
        self.stkTab3Dscans.setCurrentIndex(0)
        self.stkDetails.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(arType)
    # setupUi

    def retranslateUi(self, arType):
        arType.setWindowTitle(QCoreApplication.translate("arType", u"Pixels and Crafts Pipeline", None))

        __sortingEnabled = self.listEnvironmentProjects.isSortingEnabled()
        self.listEnvironmentProjects.setSortingEnabled(False)
        ___qlistwidgetitem = self.listEnvironmentProjects.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("arType", u"To do: display list of projects", None));
        self.listEnvironmentProjects.setSortingEnabled(__sortingEnabled)

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabArchitectural), QCoreApplication.translate("arType", u"Architectural", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabProps), QCoreApplication.translate("arType", u"Props", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabLamps), QCoreApplication.translate("arType", u"Lamps", None))
        self.label_2.setText(QCoreApplication.translate("arType", u"Details", None))
        self.lblInteractiveMeshesNumber.setText(QCoreApplication.translate("arType", u"0", None))
        self.lblProjectType.setText("")
        self.lblUniqueMeshesNumber.setText(QCoreApplication.translate("arType", u"0", None))
        self.lblInteractiveMeshes.setText(QCoreApplication.translate("arType", u"Interactive meshes", None))
        self.lblUniqueMeshes.setText(QCoreApplication.translate("arType", u"Unique meshes", None))
        self.imgRef.setText("")
        self.lblManageFeedback.setText("")
        self.btnSetProject.setText(QCoreApplication.translate("arType", u"Set project", None))
    # retranslateUi


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
    QLabel, QLayout, QLineEdit, QListWidget,
    QListWidgetItem, QPushButton, QRadioButton, QScrollArea,
    QSizePolicy, QSpacerItem, QStackedWidget, QTabWidget,
    QVBoxLayout, QWidget)
import app_imgs_rc

class Ui_arType(object):
    def setupUi(self, arType):
        if not arType.objectName():
            arType.setObjectName(u"arType")
        arType.resize(629, 522)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(arType.sizePolicy().hasHeightForWidth())
        arType.setSizePolicy(sizePolicy)
        arType.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(arType)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 4, 0)
        self.wgMain = QWidget(arType)
        self.wgMain.setObjectName(u"wgMain")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.wgMain.sizePolicy().hasHeightForWidth())
        self.wgMain.setSizePolicy(sizePolicy1)
        self.wgMain.setMinimumSize(QSize(0, 0))
        self.wgMain.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout_8 = QVBoxLayout(self.wgMain)
        self.verticalLayout_8.setSpacing(20)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.wgMain)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_7 = QVBoxLayout(self.widget)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.wgtSettings = QWidget(self.widget)
        self.wgtSettings.setObjectName(u"wgtSettings")
        self.wgtSettings.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout_3 = QVBoxLayout(self.wgtSettings)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(-1, -1, -1, 4)
        self.wgtCreateProject = QWidget(self.wgtSettings)
        self.wgtCreateProject.setObjectName(u"wgtCreateProject")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.wgtCreateProject.sizePolicy().hasHeightForWidth())
        self.wgtCreateProject.setSizePolicy(sizePolicy2)
        self.horizontalLayout_6 = QHBoxLayout(self.wgtCreateProject)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_4 = QLabel(self.wgtCreateProject)
        self.label_4.setObjectName(u"label_4")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy3)
        self.label_4.setMinimumSize(QSize(170, 0))
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_6.addWidget(self.label_4)

        self.radEnvironment = QRadioButton(self.wgtCreateProject)
        self.radEnvironment.setObjectName(u"radEnvironment")
        self.radEnvironment.setChecked(True)

        self.horizontalLayout_6.addWidget(self.radEnvironment)

        self.radProps = QRadioButton(self.wgtCreateProject)
        self.radProps.setObjectName(u"radProps")

        self.horizontalLayout_6.addWidget(self.radProps)

        self.radScans = QRadioButton(self.wgtCreateProject)
        self.radScans.setObjectName(u"radScans")

        self.horizontalLayout_6.addWidget(self.radScans)

        self.radCharacters = QRadioButton(self.wgtCreateProject)
        self.radCharacters.setObjectName(u"radCharacters")

        self.horizontalLayout_6.addWidget(self.radCharacters)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_8)


        self.verticalLayout_3.addWidget(self.wgtCreateProject)

        self.widget_9 = QWidget(self.wgtSettings)
        self.widget_9.setObjectName(u"widget_9")
        sizePolicy2.setHeightForWidth(self.widget_9.sizePolicy().hasHeightForWidth())
        self.widget_9.setSizePolicy(sizePolicy2)
        self.widget_9.setMaximumSize(QSize(16777215, 30))
        self.horizontalLayout_3 = QHBoxLayout(self.widget_9)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(9, 0, 9, 0)
        self.lblRootPath = QLabel(self.widget_9)
        self.lblRootPath.setObjectName(u"lblRootPath")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.lblRootPath.sizePolicy().hasHeightForWidth())
        self.lblRootPath.setSizePolicy(sizePolicy4)
        self.lblRootPath.setMinimumSize(QSize(170, 0))

        self.horizontalLayout_3.addWidget(self.lblRootPath)

        self.linRootPath = QLineEdit(self.widget_9)
        self.linRootPath.setObjectName(u"linRootPath")

        self.horizontalLayout_3.addWidget(self.linRootPath)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_5)

        self.btnChangeRootPath = QPushButton(self.widget_9)
        self.btnChangeRootPath.setObjectName(u"btnChangeRootPath")

        self.horizontalLayout_3.addWidget(self.btnChangeRootPath)


        self.verticalLayout_3.addWidget(self.widget_9)

        self.widget_6 = QWidget(self.wgtSettings)
        self.widget_6.setObjectName(u"widget_6")
        sizePolicy2.setHeightForWidth(self.widget_6.sizePolicy().hasHeightForWidth())
        self.widget_6.setSizePolicy(sizePolicy2)
        self.widget_6.setMaximumSize(QSize(16777215, 30))
        self.horizontalLayout_10 = QHBoxLayout(self.widget_6)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(-1, 0, -1, 0)
        self.lblMarketplaceName = QLabel(self.widget_6)
        self.lblMarketplaceName.setObjectName(u"lblMarketplaceName")
        sizePolicy3.setHeightForWidth(self.lblMarketplaceName.sizePolicy().hasHeightForWidth())
        self.lblMarketplaceName.setSizePolicy(sizePolicy3)
        self.lblMarketplaceName.setMinimumSize(QSize(170, 0))
        self.lblMarketplaceName.setMaximumSize(QSize(170, 16777215))
        self.lblMarketplaceName.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.lblMarketplaceName.setWordWrap(False)

        self.horizontalLayout_10.addWidget(self.lblMarketplaceName)

        self.linMarketplaceName = QLineEdit(self.widget_6)
        self.linMarketplaceName.setObjectName(u"linMarketplaceName")

        self.horizontalLayout_10.addWidget(self.linMarketplaceName)

        self.horizontalSpacer_9 = QSpacerItem(32, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_9)

        self.btnChangeMarketplaceName = QPushButton(self.widget_6)
        self.btnChangeMarketplaceName.setObjectName(u"btnChangeMarketplaceName")

        self.horizontalLayout_10.addWidget(self.btnChangeMarketplaceName)


        self.verticalLayout_3.addWidget(self.widget_6)


        self.verticalLayout_7.addWidget(self.wgtSettings)

        self.widget_4 = QWidget(self.widget)
        self.widget_4.setObjectName(u"widget_4")
        sizePolicy.setHeightForWidth(self.widget_4.sizePolicy().hasHeightForWidth())
        self.widget_4.setSizePolicy(sizePolicy)
        self.widget_4.setMinimumSize(QSize(0, 0))
        self.widget_4.setMaximumSize(QSize(16777215, 16777215))
        self.horizontalLayout = QHBoxLayout(self.widget_4)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.wgtSpacer = QWidget(self.widget_4)
        self.wgtSpacer.setObjectName(u"wgtSpacer")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.wgtSpacer.sizePolicy().hasHeightForWidth())
        self.wgtSpacer.setSizePolicy(sizePolicy5)

        self.horizontalLayout.addWidget(self.wgtSpacer)

        self.tabWidget = QTabWidget(self.widget_4)
        self.tabWidget.setObjectName(u"tabWidget")
        sizePolicy5.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy5)
        self.tabWidget.setMinimumSize(QSize(0, 0))
        self.tabWidget.setMaximumSize(QSize(16777215, 16777215))
        self.tabWidget.setSizeIncrement(QSize(0, 0))
        self.tabWidget.setBaseSize(QSize(0, 0))
        self.tabWidget.setFocusPolicy(Qt.FocusPolicy.TabFocus)
        self.tabWidget.setStyleSheet(u"")
        self.tabWidget.setTabPosition(QTabWidget.TabPosition.North)
        self.tabWidget.setTabShape(QTabWidget.TabShape.Triangular)
        self.tabWidget.setElideMode(Qt.TextElideMode.ElideNone)
        self.tabArchitectural = QWidget()
        self.tabArchitectural.setObjectName(u"tabArchitectural")
        self.tabArchitectural.setEnabled(True)
        sizePolicy.setHeightForWidth(self.tabArchitectural.sizePolicy().hasHeightForWidth())
        self.tabArchitectural.setSizePolicy(sizePolicy)
        self.tabArchitectural.setMinimumSize(QSize(200, 0))
        self.verticalLayout_2 = QVBoxLayout(self.tabArchitectural)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.stkTabArch = QStackedWidget(self.tabArchitectural)
        self.stkTabArch.setObjectName(u"stkTabArch")
        sizePolicy.setHeightForWidth(self.stkTabArch.sizePolicy().hasHeightForWidth())
        self.stkTabArch.setSizePolicy(sizePolicy)
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
        sizePolicy.setHeightForWidth(self.page_2.sizePolicy().hasHeightForWidth())
        self.page_2.setSizePolicy(sizePolicy)
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
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 274, 348))
        self.gridLayout_10 = QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.listEnvironmentProjects = QListWidget(self.scrollAreaWidgetContents_2)
        self.listEnvironmentProjects.setObjectName(u"listEnvironmentProjects")
        self.listEnvironmentProjects.setFrameShape(QFrame.Shape.NoFrame)
        self.listEnvironmentProjects.setFrameShadow(QFrame.Shadow.Plain)

        self.gridLayout_10.addWidget(self.listEnvironmentProjects, 0, 0, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)

        self.layTabArchProjects.addWidget(self.scrollArea)


        self.gridLayout_4.addLayout(self.layTabArchProjects, 0, 1, 1, 1)

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
        self.scrollAreaWidgetContents_5.setGeometry(QRect(0, 0, 274, 348))
        self.gridLayout_11 = QGridLayout(self.scrollAreaWidgetContents_5)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.listPropsProjects = QListWidget(self.scrollAreaWidgetContents_5)
        self.listPropsProjects.setObjectName(u"listPropsProjects")
        self.listPropsProjects.setFrameShape(QFrame.Shape.NoFrame)
        self.listPropsProjects.setFrameShadow(QFrame.Shadow.Plain)

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
        self.scrollAreaWidgetContents_6.setGeometry(QRect(0, 0, 274, 348))
        self.gridLayout_12 = QGridLayout(self.scrollAreaWidgetContents_6)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.list3DscansProjects = QListWidget(self.scrollAreaWidgetContents_6)
        self.list3DscansProjects.setObjectName(u"list3DscansProjects")
        self.list3DscansProjects.setFrameShape(QFrame.Shape.NoFrame)
        self.list3DscansProjects.setFrameShadow(QFrame.Shadow.Plain)

        self.gridLayout_12.addWidget(self.list3DscansProjects, 0, 0, 1, 1)

        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_6)

        self.layTabLampsProjects.addWidget(self.scrollArea_3)


        self.gridLayout_9.addLayout(self.layTabLampsProjects, 0, 0, 1, 1)

        self.stkTab3Dscans.addWidget(self.page_6)

        self.verticalLayout_5.addWidget(self.stkTab3Dscans)

        self.tabWidget.addTab(self.tabLamps, "")
        self.tabCharacters = QWidget()
        self.tabCharacters.setObjectName(u"tabCharacters")
        self.verticalLayout_6 = QVBoxLayout(self.tabCharacters)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.stkTabCharacters = QStackedWidget(self.tabCharacters)
        self.stkTabCharacters.setObjectName(u"stkTabCharacters")
        self.page_7 = QWidget()
        self.page_7.setObjectName(u"page_7")
        self.gridLayout_13 = QGridLayout(self.page_7)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.layTabChar = QVBoxLayout()
        self.layTabChar.setObjectName(u"layTabChar")

        self.gridLayout_13.addLayout(self.layTabChar, 0, 0, 1, 1)

        self.stkTabCharacters.addWidget(self.page_7)
        self.page_8 = QWidget()
        self.page_8.setObjectName(u"page_8")
        self.gridLayout_14 = QGridLayout(self.page_8)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.layTabCharProjects = QVBoxLayout()
        self.layTabCharProjects.setObjectName(u"layTabCharProjects")
        self.scrollArea_4 = QScrollArea(self.page_8)
        self.scrollArea_4.setObjectName(u"scrollArea_4")
        self.scrollArea_4.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 274, 348))
        self.gridLayout_15 = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.gridLayout_15.setContentsMargins(0, 0, 0, 0)
        self.widget_2 = QWidget(self.scrollAreaWidgetContents)
        self.widget_2.setObjectName(u"widget_2")
        self.gridLayout_16 = QGridLayout(self.widget_2)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.listCharactersProjects = QListWidget(self.widget_2)
        self.listCharactersProjects.setObjectName(u"listCharactersProjects")
        self.listCharactersProjects.setFrameShape(QFrame.Shape.NoFrame)
        self.listCharactersProjects.setFrameShadow(QFrame.Shadow.Plain)

        self.gridLayout_16.addWidget(self.listCharactersProjects, 0, 0, 1, 1)


        self.gridLayout_15.addWidget(self.widget_2, 0, 0, 1, 1)

        self.scrollArea_4.setWidget(self.scrollAreaWidgetContents)

        self.layTabCharProjects.addWidget(self.scrollArea_4)


        self.gridLayout_14.addLayout(self.layTabCharProjects, 0, 0, 1, 1)

        self.stkTabCharacters.addWidget(self.page_8)

        self.verticalLayout_6.addWidget(self.stkTabCharacters)

        self.tabWidget.addTab(self.tabCharacters, "")

        self.horizontalLayout.addWidget(self.tabWidget)

        self.widget_3 = QWidget(self.widget_4)
        self.widget_3.setObjectName(u"widget_3")
        sizePolicy4.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy4)
        self.widget_3.setMinimumSize(QSize(150, 0))
        self.widget_3.setMaximumSize(QSize(150, 16777215))
        self.gridLayout_20 = QGridLayout(self.widget_3)
        self.gridLayout_20.setObjectName(u"gridLayout_20")
        self.layDetails_2 = QVBoxLayout()
        self.layDetails_2.setObjectName(u"layDetails_2")
        self.layDetails_2.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.layDetails_2.setContentsMargins(0, -1, 0, -1)
        self.layDetails = QWidget(self.widget_3)
        self.layDetails.setObjectName(u"layDetails")
        self.layDetails.setMinimumSize(QSize(0, 0))
        self.verticalLayout_9 = QVBoxLayout(self.layDetails)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, -1, 0, -1)
        self.label_5 = QLabel(self.layDetails)
        self.label_5.setObjectName(u"label_5")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(1)
        sizePolicy6.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy6)
        self.label_5.setMaximumSize(QSize(600, 30))

        self.verticalLayout_9.addWidget(self.label_5)

        self.line_3 = QFrame(self.layDetails)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setStyleSheet(u"")
        self.line_3.setFrameShape(QFrame.Shape.HLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_9.addWidget(self.line_3)

        self._2 = QGridLayout()
        self._2.setObjectName(u"_2")
        self._2.setVerticalSpacing(0)
        self.lblInteractiveMeshesNumber = QLabel(self.layDetails)
        self.lblInteractiveMeshesNumber.setObjectName(u"lblInteractiveMeshesNumber")
        self.lblInteractiveMeshesNumber.setMargin(5)

        self._2.addWidget(self.lblInteractiveMeshesNumber, 3, 1, 1, 1)

        self.lblProjectType_2 = QLabel(self.layDetails)
        self.lblProjectType_2.setObjectName(u"lblProjectType_2")

        self._2.addWidget(self.lblProjectType_2, 1, 0, 1, 1)

        self.lblUniqueMeshesNumber = QLabel(self.layDetails)
        self.lblUniqueMeshesNumber.setObjectName(u"lblUniqueMeshesNumber")
        self.lblUniqueMeshesNumber.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.lblUniqueMeshesNumber.setMargin(5)

        self._2.addWidget(self.lblUniqueMeshesNumber, 2, 1, 1, 1)

        self.lblInteractiveMeshes = QLabel(self.layDetails)
        self.lblInteractiveMeshes.setObjectName(u"lblInteractiveMeshes")

        self._2.addWidget(self.lblInteractiveMeshes, 3, 0, 1, 1)

        self.lblUniqueMeshes = QLabel(self.layDetails)
        self.lblUniqueMeshes.setObjectName(u"lblUniqueMeshes")

        self._2.addWidget(self.lblUniqueMeshes, 2, 0, 1, 1)


        self.verticalLayout_9.addLayout(self._2)


        self.layDetails_2.addWidget(self.layDetails)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.layDetails_2.addItem(self.verticalSpacer_5)

        self.layTotal = QWidget(self.widget_3)
        self.layTotal.setObjectName(u"layTotal")
        sizePolicy2.setHeightForWidth(self.layTotal.sizePolicy().hasHeightForWidth())
        self.layTotal.setSizePolicy(sizePolicy2)
        self.layTotal.setMinimumSize(QSize(0, 90))
        self.verticalLayout_10 = QVBoxLayout(self.layTotal)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, -1, 0, -1)
        self.label = QLabel(self.layTotal)
        self.label.setObjectName(u"label")

        self.verticalLayout_10.addWidget(self.label)

        self.line = QFrame(self.layTotal)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_10.addWidget(self.line)

        self._3 = QGridLayout()
        self._3.setObjectName(u"_3")
        self._3.setVerticalSpacing(0)
        self.label_3 = QLabel(self.layTotal)
        self.label_3.setObjectName(u"label_3")

        self._3.addWidget(self.label_3, 3, 0, 1, 1)

        self.lblTotalInteractiveMeshesNumber = QLabel(self.layTotal)
        self.lblTotalInteractiveMeshesNumber.setObjectName(u"lblTotalInteractiveMeshesNumber")
        self.lblTotalInteractiveMeshesNumber.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.lblTotalInteractiveMeshesNumber.setMargin(5)

        self._3.addWidget(self.lblTotalInteractiveMeshesNumber, 3, 1, 1, 1)

        self.lblTotalUniqueMeshesNumber = QLabel(self.layTotal)
        self.lblTotalUniqueMeshesNumber.setObjectName(u"lblTotalUniqueMeshesNumber")
        self.lblTotalUniqueMeshesNumber.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.lblTotalUniqueMeshesNumber.setMargin(5)

        self._3.addWidget(self.lblTotalUniqueMeshesNumber, 2, 1, 1, 1)

        self.label_2 = QLabel(self.layTotal)
        self.label_2.setObjectName(u"label_2")

        self._3.addWidget(self.label_2, 2, 0, 1, 1)


        self.verticalLayout_10.addLayout(self._3)


        self.layDetails_2.addWidget(self.layTotal)

        self.widget_10 = QWidget(self.widget_3)
        self.widget_10.setObjectName(u"widget_10")
        sizePolicy3.setHeightForWidth(self.widget_10.sizePolicy().hasHeightForWidth())
        self.widget_10.setSizePolicy(sizePolicy3)
        self.widget_10.setMinimumSize(QSize(0, 0))
        self.widget_10.setMaximumSize(QSize(300, 300))
        self.widget_10.setSizeIncrement(QSize(0, 0))
        self.widget_10.setBaseSize(QSize(0, 0))
        self.gridLayout_21 = QGridLayout(self.widget_10)
        self.gridLayout_21.setSpacing(0)
        self.gridLayout_21.setObjectName(u"gridLayout_21")
        self.gridLayout_21.setContentsMargins(0, 0, 0, 9)
        self.btnProject = QPushButton(self.widget_10)
        self.btnProject.setObjectName(u"btnProject")
        sizePolicy3.setHeightForWidth(self.btnProject.sizePolicy().hasHeightForWidth())
        self.btnProject.setSizePolicy(sizePolicy3)
        self.btnProject.setMinimumSize(QSize(90, 0))
        self.btnProject.setMaximumSize(QSize(90, 16777215))

        self.gridLayout_21.addWidget(self.btnProject, 0, 0, 1, 1)


        self.layDetails_2.addWidget(self.widget_10)


        self.gridLayout_20.addLayout(self.layDetails_2, 0, 0, 1, 1)


        self.horizontalLayout.addWidget(self.widget_3)


        self.verticalLayout_7.addWidget(self.widget_4)


        self.verticalLayout_8.addWidget(self.widget)


        self.verticalLayout.addWidget(self.wgMain)


        self.retranslateUi(arType)

        self.tabWidget.setCurrentIndex(1)
        self.stkTabArch.setCurrentIndex(1)
        self.stkTabProps.setCurrentIndex(1)
        self.stkTab3Dscans.setCurrentIndex(1)
        self.stkTabCharacters.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(arType)
    # setupUi

    def retranslateUi(self, arType):
        arType.setWindowTitle(QCoreApplication.translate("arType", u"Pixels and Crafts Pipeline", None))
        self.label_4.setText(QCoreApplication.translate("arType", u"Type of project:", None))
        self.radEnvironment.setText(QCoreApplication.translate("arType", u"Environment", None))
        self.radProps.setText(QCoreApplication.translate("arType", u"Props", None))
        self.radScans.setText(QCoreApplication.translate("arType", u"3Dscans", None))
        self.radCharacters.setText(QCoreApplication.translate("arType", u"Characters", None))
        self.lblRootPath.setText(QCoreApplication.translate("arType", u"Root path:", None))
        self.btnChangeRootPath.setText(QCoreApplication.translate("arType", u"Change path", None))
        self.lblMarketplaceName.setText(QCoreApplication.translate("arType", u"Marketplace folder name:", None))
        self.btnChangeMarketplaceName.setText(QCoreApplication.translate("arType", u"Change Name", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabArchitectural), QCoreApplication.translate("arType", u"Architectural", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabProps), QCoreApplication.translate("arType", u"Props", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabLamps), QCoreApplication.translate("arType", u"Lamps", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabCharacters), QCoreApplication.translate("arType", u"Characters", None))
        self.label_5.setText(QCoreApplication.translate("arType", u"Details", None))
        self.lblInteractiveMeshesNumber.setText(QCoreApplication.translate("arType", u"0", None))
        self.lblProjectType_2.setText("")
        self.lblUniqueMeshesNumber.setText(QCoreApplication.translate("arType", u"0", None))
        self.lblInteractiveMeshes.setText(QCoreApplication.translate("arType", u"Interactive meshes", None))
        self.lblUniqueMeshes.setText(QCoreApplication.translate("arType", u"Unique meshes", None))
        self.label.setText(QCoreApplication.translate("arType", u"Total", None))
        self.label_3.setText(QCoreApplication.translate("arType", u"Interactive meshes", None))
        self.lblTotalInteractiveMeshesNumber.setText(QCoreApplication.translate("arType", u"0", None))
        self.lblTotalUniqueMeshesNumber.setText(QCoreApplication.translate("arType", u"0", None))
        self.label_2.setText(QCoreApplication.translate("arType", u"Unique meshes", None))
        self.btnProject.setText(QCoreApplication.translate("arType", u"Set project", None))
    # retranslateUi


"""
Content  : 

Date     : 2025-11-13

Author   : Elena Giuliani
email    : elenagiuliani94@outlook.it
"""
import os
import sys

from Qt import QtWidgets, QtGui, QtCompat, QtCore

# PARENT UI
from arType import ArType
from arUtil import IMG_PATH, CURRENT_DIR

from lib.appfunc import project_type

TITLE = os.path.splitext(os.path.basename(__file__))[0]


class ArLoad(ArType):
    def __init__(self):

        super(ArLoad, self).__init__()

        path_ui = CURRENT_DIR + '/ui/' + TITLE + '.ui'

        self.wgLoad =  QtCompat.loadUi(path_ui)
        self.wgHeader.setWindowTitle(TITLE)

        self.wgLoad.listDepartments.setVisible(False)

        # create one UI instance per tab
        self.wgLoadArch = QtCompat.loadUi(path_ui)
        self.wgLoadProps = QtCompat.loadUi(path_ui)
        self.wgLoadLamps = QtCompat.loadUi(path_ui)

        self.instances = [self.wgLoadArch, self.wgLoadProps, self.wgLoadLamps]

        # ICONS
        self.wgLoadArch.btnOpenFilesFolder.setIcon(QtGui.QPixmap(IMG_PATH.format('open_folder')))
        self.wgLoadProps.btnOpenFilesFolder.setIcon(QtGui.QPixmap(IMG_PATH.format('open_folder')))
        self.wgLoadLamps.btnOpenFilesFolder.setIcon(QtGui.QPixmap(IMG_PATH.format('open_folder')))

        self.wgLoadArch.btnAddScene.setIcon(QtGui.QPixmap(IMG_PATH.format('plus_icon')))
        self.wgLoadProps.btnAddScene.setIcon(QtGui.QPixmap(IMG_PATH.format('plus_icon')))
        self.wgLoadLamps.btnAddScene.setIcon(QtGui.QPixmap(IMG_PATH.format('plus_icon')))

        #***************************************************************
        # SIGNALS
        # for architecture tab
        self.wgLoadArch.btnAssets.clicked.connect(lambda: self.press_btnAssetsFiles('assets', self.wgLoadArch))
        self.wgLoadArch.btnFiles.clicked.connect(lambda: self.press_btnAssetsFiles('files', self.wgLoadArch))

        # for props tab
        self.wgLoadProps.btnAssets.clicked.connect(lambda: self.press_btnAssetsFiles('assets', self.wgLoadProps))
        self.wgLoadProps.btnFiles.clicked.connect(lambda: self.press_btnAssetsFiles('files', self.wgLoadProps))

        # for lamps tab
        self.wgLoadLamps.btnAssets.clicked.connect(lambda: self.press_btnAssetsFiles('assets', self.wgLoadLamps))
        self.wgLoadLamps.btnFiles.clicked.connect(lambda: self.press_btnAssetsFiles('files', self.wgLoadLamps))


        #***************************************************************
        # ADD to layout

        self.wgType.stkTabArch.setCurrentIndex(0)
        self.wgType.stkTabProps.setCurrentIndex(0)
        self.wgType.stkTab3Dscans.setCurrentIndex(0)

        self.wgType.layTabArch.addWidget(self.wgLoadArch)
        self.wgType.layTabProps.addWidget(self.wgLoadProps)
        self.wgType.layTabLamps.addWidget(self.wgLoadLamps)
        
        self.set_tabs(project_type)

        
    #***************************************************************
    # FUNCTIONS
    def press_btnAssetsFiles(self, type, wg):
        if type == 'assets':
            wg.btnFiles.setChecked(False) # uncheck opposite button
            wg.stkAssetsFiles.setStyleSheet("selection-background-color: rgb(71, 89, 30);") # set color checked button
            wg.stkAssetsFiles.setCurrentIndex(0) # set matching page of QStackedWidget with checked button

        if type == 'files':
            wg.btnAssets.setChecked(False) # uncheck opposite button
            wg.stkAssetsFiles.setStyleSheet("selection-background-color: rgb(71, 89, 30);") # set color checked button
            wg.stkAssetsFiles.setCurrentIndex(1) # set matching page of QStackedWidget with checked button

    # remove tabs if not needed, based on project type
    def set_tabs(self, project_type):
        if project_type == 'Environment':
            pass
        if project_type == 'Props' or project_type == '3Dscans' or project_type == 'Characters':
            self.wgType.tabWidget.removeTab(0)
            self.wgType.tabWidget.removeTab(1)
            


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ar_load = ArLoad()
    app.exec_()
    

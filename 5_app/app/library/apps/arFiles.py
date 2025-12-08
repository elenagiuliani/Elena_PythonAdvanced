"""
Content  : arFiles - UI for switching between 'Assets' and 'Files' sections

Date     : 2025-11-13

Author   : Elena Giuliani
email    : elenagiuliani94@outlook.it
"""
import os
import sys

from Qt import QtWidgets, QtGui, QtCompat, QtCore

from arType import ArType
from arUtil import IMG_PATH, CURRENT_DIR

TITLE = os.path.splitext(os.path.basename(__file__))[0]

class ArFiles(ArType):
    def __init__(self):
        super(ArFiles, self).__init__()
        path_ui = CURRENT_DIR + '/ui/' + TITLE + '.ui'

        self.wgLoad =  QtCompat.loadUi(path_ui)
        self.wgHeader.setWindowTitle(TITLE)

        # UI
        self.wgLoad.listDepartments.setVisible(False)

        # create one UI instance per tab
        self.wgLoadArch = QtCompat.loadUi(path_ui)
        self.wgLoadProps = QtCompat.loadUi(path_ui)
        self.wgLoadLamps = QtCompat.loadUi(path_ui)

        self.instances = [(self.wgLoadArch, 'architectural'), (self.wgLoadProps, 'props'), (self.wgLoadLamps, 'lamps')]
        # added attribute 'category' for differentiating the three tabs when populating them with scenes and assets
        for instance, category in self.instances:
            # ICONS
            instance.btnOpenFilesFolder.setIcon(QtGui.QPixmap(IMG_PATH.format('open_folder')))
            instance.btnAddScene.setIcon(QtGui.QPixmap(IMG_PATH.format('plus_icon')))

            # SIGNALS
            instance.btnAssets.clicked.connect(lambda checked, inst=instance: self.press_btnAssetsFiles('assets', inst))
            instance.btnFiles.clicked.connect(lambda checked, inst=instance: self.press_btnAssetsFiles('files', inst))
            self.press_btnAssetsFiles('assets', instance)

        #***************************************************************
        # ADD to layout
        self.wgType.stkTabArch.setCurrentIndex(0)
        self.wgType.stkTabProps.setCurrentIndex(0)
        self.wgType.stkTab3Dscans.setCurrentIndex(0)

        self.wgType.layTabArch.addWidget(self.wgLoadArch)
        self.wgType.layTabProps.addWidget(self.wgLoadProps)
        self.wgType.layTabLamps.addWidget(self.wgLoadLamps)

    #***************************************************************
    # FUNCTIONS
    def press_btnAssetsFiles(self, type, instance):
        if type == 'assets':
            instance.scrFiles.hide()
            instance.wgtAssets.show()
            instance.btnAddScene.hide()
            instance.listDepartments.hide()
            instance.wgtSpacerAssets.show()
            instance.btnFiles.setChecked(False)
            instance.btnOpenLastVersionScene.hide()

        if type == 'files':
            instance.scrFiles.show()
            instance.wgtAssets.hide()
            instance.btnAddScene.show()
            instance.listDepartments.show()
            instance.wgtSpacerAssets.hide()
            instance.btnAssets.setChecked(False)
            instance.btnOpenLastVersionScene.show()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ar_files = ArFiles()
    app.exec()

"""
Content  : arFiles.py 
            - UI for switching between 'Assets' and 'Files' sections

Date     : 2025-11-13

license  : MIT
Author   : Elena Giuliani
email    : elenagiuliani94@outlook.it
"""
import os
import sys

from Qt import QtWidgets, QtGui, QtCompat

from arType import ArType
from arUtil import ICON_PATH, APPS_DIR

from Git_PackForge_Pipeline.library.apps.ui.stylesheet import get_stylesheet, PALETTE
from Git_PackForge_Pipeline.library.appfunc import ue_meshes_data

TITLE = os.path.splitext(os.path.basename(__file__))[0]



class ArFiles(ArType):
    def __init__(self):
        super(ArFiles, self).__init__()
        path_ui = APPS_DIR + '/ui/' + TITLE + '.ui'

        self.wgFiles =  QtCompat.loadUi(path_ui)
        self.wgHeader.setWindowTitle(TITLE)

        #***************************************************************
        # UI
        self.wgFiles.listDepartments.setVisible(False)

        # create one UI instance per tab
        self.wgLoadArch = QtCompat.loadUi(path_ui)
        self.wgLoadProps = QtCompat.loadUi(path_ui)
        self.wgLoadLamps = QtCompat.loadUi(path_ui)

        self.instances = [(self.wgLoadArch, 'architectural'), (self.wgLoadProps, 'props'), (self.wgLoadLamps, 'lamps')]
        # attribute 'category' for differentiating the three tabs when populating them with scenes and assets

        for instance, category in self.instances:
            self.set_ui_when_ue_meshes(instance, category)

            # ICONS
            instance.btnOpenFilesFolder.setIcon(QtGui.QPixmap(ICON_PATH.format('open_folder')))
            instance.btnAddScene.setIcon(QtGui.QPixmap(ICON_PATH.format('plus_icon')))

            # SIGNALS
            instance.btnAssets.clicked.connect(lambda checked, inst=instance: self.press_btnAssetsFiles('assets', inst))
            instance.btnFiles.clicked.connect(lambda checked, inst=instance: self.press_btnAssetsFiles('files', inst))


        #***************************************************************
        # ADD to layout
        self.wgType.stkTabArch.setCurrentIndex(0)
        self.wgType.stkTabProps.setCurrentIndex(0)
        self.wgType.stkTab3Dscans.setCurrentIndex(0)

        self.wgType.layTabArch.addWidget(self.wgLoadArch)
        self.wgType.layTabProps.addWidget(self.wgLoadProps)
        self.wgType.layTabLamps.addWidget(self.wgLoadLamps)

        self.wgFiles.wgt_AssetsFiles.setStyleSheet(f"""
                        QPushButton {{background-color: rgb(30, 30, 30);   /*unchecked state*/
                                    color: rgb(200, 200, 200);
                                    }}
                        QPushButton:checked {{background-color: rgb(71, 89, 30);
                                            color: {PALETTE['my_white']};
                                            }}
                        QPushButton:hover {{background-color: {PALETTE['light_green']};
                                            color: rgb(200, 200, 200);
                                            }}
                        """)

    #***************************************************************
    # FUNCTIONS
    def set_ui_when_ue_meshes(self, instance, category):
        ue_meshes, blueprints = ue_meshes_data(category)

        def _blueprints_type():
            if isinstance(blueprints, dict):
                return blueprints.items()
            return blueprints

        if not ue_meshes and not _blueprints_type():
            self.press_btnAssetsFiles('files', instance)
            return
        self.press_btnAssetsFiles('assets', instance)

    def press_btnAssetsFiles(self, type, instance):
        if type == 'assets':
            instance.scrFiles.hide()
            instance.wgtAssets.show()
            instance.btnAddScene.hide()
            instance.listDepartments.hide()
            instance.wgtSpacerAssets.show()
            instance.wgtFilesCommands.hide()
            instance.btnAssets.setChecked(True)
            instance.btnFiles.setChecked(False)
            instance.btnOpenLastVersionScene.hide()

        if type == 'files':
            instance.scrFiles.show()
            instance.wgtAssets.hide()
            instance.btnAddScene.show()
            instance.listDepartments.show()
            instance.wgtSpacerAssets.hide()
            instance.wgtFilesCommands.show()
            instance.btnFiles.setChecked(True)
            instance.btnAssets.setChecked(False)
            instance.btnOpenLastVersionScene.show()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ar_files = ArFiles()
    app.setStyleSheet(get_stylesheet())
    app.exec()

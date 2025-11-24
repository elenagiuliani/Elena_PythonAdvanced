"""
Content  : 

Date     : 2025-11-13

Author   : Elena Giuliani
email    : elenagiuliani94@outlook.it
"""
import os
import sys
import webbrowser
import subprocess
from Qt import QtWidgets, QtGui, QtCompat, QtCore

# PARENT UI
from arLoad import ArLoad
from arUtil import CURRENT_DIR, IMG_PATH

from lib.appfunc import get_directory, get_scenes, files_naming, assets_data, project_type

# bat file
start_maya_scene_bat = os.path.join(CURRENT_DIR, '..', '..', 'exe', 'start_maya_scene.bat')
open_set_scene = os.path.join(CURRENT_DIR, '..', '..', 'exe', 'set_scene.bat')

TITLE = os.path.splitext(os.path.basename(__file__))[0]


class ArAsset(ArLoad):
    def __init__(self):

        super(ArAsset, self).__init__()

        self.path_ui = CURRENT_DIR + '/ui/' + TITLE + '.ui'

        self.wgAssets = QtCompat.load_ui(self.path_ui)
        self.wgHeader.setWindowTitle(TITLE)


        # ICONS
        self.wgLoadArch.listDepartments.currentRowChanged.connect(lambda row: self.set_icon_btnSoftwareFirstOpen(row)) # change icon at list item click
        self.wgLoadProps.listDepartments.currentRowChanged.connect(lambda row: self.set_icon_btnSoftwareFirstOpen(row))
        self.wgLoadLamps.listDepartments.currentRowChanged.connect(lambda row: self.set_icon_btnSoftwareFirstOpen(row))

        self.wgLoadArch.btnOpenLastVersionScene.setIcon(QtGui.QPixmap(IMG_PATH.format('maya_icon'))) # load icon at app start
        self.wgLoadProps.btnOpenLastVersionScene.setIcon(QtGui.QPixmap(IMG_PATH.format('maya_icon')))
        self.wgLoadLamps.btnOpenLastVersionScene.setIcon(QtGui.QPixmap(IMG_PATH.format('maya_icon')))

        # open last version scene
        self.wgLoadArch.btnOpenLastVersionScene.clicked.connect(self.press_btnOpenLastVersionScene, 'arch')
        self.wgLoadProps.btnOpenLastVersionScene.clicked.connect(self.press_btnOpenLastVersionScene, 'props')
        self.wgLoadLamps.btnOpenLastVersionScene.clicked.connect(self.press_btnOpenLastVersionScene, 'lamps')


        #***************************************************************
        self.instances = [self.wgLoadArch, self.wgLoadProps, self.wgLoadLamps]

        for instance in self.instances:
            self.display_scenes(instance.layFilesModeling, "/maya/", "model")
            self.display_scenes(instance.layFilesBaking, "/maya/", "bake")
            self.display_scenes(instance.layFilesGroom, "/maya/", "groom")
            self.display_scenes(instance.layFilesRigging, "/maya/", "rig")
            self.display_scenes(instance.layFilesPose, "/maya/", "pose")
            self.display_scenes(instance.layFilesAnimation, "/maya/", "anim")
            self.display_scenes(instance.layFilesTexturing, "/texturing", "")

            self.display_assets(instance.layAsset)

            self.display_blueprints(instance.layBlueprints)

            instance.btnOpenFilesFolder.clicked.connect(self.press_btnOpenFilesFolder)

            instance.btnAddScene.clicked.connect(self.press_btnAddScene)


        # UI
        # disable items list when there are no scenes
        self.set_state_listDepartments()

        self.wgLoadProps.listDepartments.currentRowChanged.connect(lambda row: self.change_stkFiles_page_at_press_item_listDepartments(row))



    #***************************************************************
    # FUNCTIONS

    def display_scenes(self, layout, department, maya_task):
        scenes_paths, _, _ = get_scenes(department, maya_task)

        print(f'scenes_paths   {scenes_paths}')

        # for each scene found in the folder: create a ui instance and add it to the layout
        for path in scenes_paths:
            wgFile = QtCompat.load_ui(self.path_ui)

            wgFile.stkAssetsBlueprints.setCurrentIndex(0)
            wgFile.setMaximumHeight(60)

            # assign the asset name as version (v002, etc)
            extracted_version = os.path.basename(path).split('.')[0].split('_')[-1]
            wgFile.btnOpenScene.setText(extracted_version)

            wgFile.btnOpenScene.clicked.connect(lambda checked, p=path: press_open_scene(p))
            # checked stores the result of clicked -> False, because there is no checked active for the push button
            # p is the variable the respective path is stored in

            # add one widget for each asset
            layout.addWidget(wgFile)

        #***************************************************************
        #***************************************************************
        # OPEN SCENE
        def press_open_scene(path):
            with open(start_maya_scene_bat, 'r') as stream:
                lines = stream.readlines()

            # assemble open scene path command
            lines[42 -1] = f'start "" "{path}"'

            # update the yaml file
            with open(start_maya_scene_bat, 'w') as outfile:
                outfile.writelines(lines) 

            # start scene
            subprocess.run(start_maya_scene_bat, check=True, shell=True)


    def press_btnOpenLastVersionScene(self, category):

        if category == 'arch':
            current_row = self.wgLoadArch.listDepartments.currentRow()

        if category == 'props':
            current_row = self.wgLoadProps.listDepartments.currentRow()

        if category == 'lamps':
            current_row = self.wgLoadLamps.listDepartments.currentRow()

        if not current_row:
            print('No row found')
            return

        path_keywords = [["/maya/", "model"],
                         ["/maya/", "bake"],
                         ["files/texturing", ""],
                         ["/maya/", "groom"],
                         ["/maya/", "rig"],
                         ["/maya/", "pose"],
                         ["/maya/", "anim"],
                        ]
        
        for index, (key, maya_task) in enumerate(path_keywords):

            if current_row == index:
                _, last_version_scene, _ = get_scenes(key, maya_task)

                if last_version_scene:

                    with open(start_maya_scene_bat, 'r') as stream:
                        lines = stream.readlines()

                    # assemble open scene path command
                    lines[42 -1] = f'start "" "{last_version_scene}"'

                    # update the yaml file
                    with open(start_maya_scene_bat, 'w') as outfile:
                        outfile.writelines(lines) 

                    # start scene
                    subprocess.run(start_maya_scene_bat, check=True, shell=True)

                else:
                    print('no scene found')
                    

    def display_blueprints(self, layout):
        _, _, _, bp_assets_in_directory_path = assets_data()

        print(f'bp_assets_in_directory_path  {bp_assets_in_directory_path}')

        for bp_path in bp_assets_in_directory_path:
            wgBlueprints = QtCompat.loadUi(self.path_ui)

            # icons
            wgBlueprints.btnBlueprintName.setIcon(QtGui.QPixmap(IMG_PATH.format('folder_close')))
            wgBlueprints.iconArrowBlueprint.setIcon(QtGui.QPixmap(IMG_PATH.format('arrow_full_right')))
            
            # widget ui
            wgBlueprints.btnBlueprintName.setText(bp_path.split("/")[-1])
            wgBlueprints.stkAssetsBlueprints.setCurrentIndex(1)
            wgBlueprints.setMaximumHeight(30)

            # add widget to ui
            layout.addWidget(wgBlueprints)


    def display_assets(self, layout):
        _, assets_in_directory_path, _, _ = assets_data()

        #print(f'assets_in_directory_path   {assets_in_directory_path}')

        if assets_in_directory_path:
            # create a ui instance for each fbx
            for asset_path in assets_in_directory_path:

                # create instance
                wgAsset = QtCompat.loadUi(self.path_ui)

                # widget ui
                wgAsset.btnOpenScene.setText(asset_path.split("/")[-1])
                wgAsset.stkAssetsBlueprints.setCurrentIndex(0)
                wgAsset.setMaximumHeight(60)

                wgAsset.wgHoverAssets.setStyleSheet(""" QWidget:hover {background-color: transparent; }""") # make assets not hoverable

                # add widget to ui
                layout.addWidget(wgAsset)

        else:
            self.wgLoadProps.lblAssetsFeedback.setText('No assets found\nGo in Files and start creating')
            self.wgLoadArch.lblAssetsFeedback.setText('No assets found\nGo in Files and start creating')
            self.wgLoadLamps.lblAssetsFeedback.setText('No assets found\nGo in Files and start creating')

            for instance in self.instances:
                instance.btnOpenFilesFolder.setEnabled(False)
                instance.btnOpenLastVersionScene.setEnabled(False)

    #************************************************************************************************************************
    def set_icon_btnSoftwareFirstOpen(self, row):
        if row == 2:
            self.wgLoadProps.btnOpenLastVersionScene.setIcon(QtGui.QPixmap(IMG_PATH.format('sp_icon')))
        else:
            self.wgLoadProps.btnOpenLastVersionScene.setIcon(QtGui.QPixmap(IMG_PATH.format('maya_icon')))


    def press_btnOpenFilesFolder(self):
        current_row = self.wgLoadProps.listDepartments.currentRow()

        get_scene_path = [get_scenes("/maya/", files_naming["modeling"]["extension"])[-1],
                          get_scenes("/maya/", files_naming["baking"]["extension"])[-1],
                          get_directory(["/files/texturing"]),
                          get_scenes("/maya/", files_naming["grooming"]["extension"])[-1],
                          get_scenes("/maya/", files_naming["rigging"]["extension"])[-1],
                          get_scenes("/maya/", files_naming["pose"]["extension"])[-1],
                          get_scenes("/maya/", files_naming["animation"]["extension"])[-1]
                          ]
        for index, path in enumerate(get_scene_path):
            if current_row == index:
                scene_path = path
                if scene_path:
                    webbrowser.open(scene_path)


    def set_state_listDepartments(self):

        def set_state():
            for instance in self.instances:
                layouts = [instance.layFilesModeling,
                        instance.layFilesBaking,
                        instance.layFilesTexturing,
                        instance.layFilesGroom,
                        instance.layFilesRigging,
                        instance.layFilesPose,
                        instance.layFilesAnimation
                        ]
                for index, layout in enumerate(layouts):
                    if not layout.count():
                        item = instance.listDepartments.item(index)
                        item.setFlags(item.flags() & ~QtCore.Qt.ItemIsEnabled)
                        #item.setFlags(item.flags() | QtCore.Qt.ItemIsEnabled)
        set_state()


    def change_stkFiles_page_at_press_item_listDepartments(self, row):
        for index in range(0,7):
            if row == index:
                self.wgLoadProps.stkFiles.setCurrentIndex(index)


    def press_btnAddScene(self):
        subprocess.run(open_set_scene, check=True, shell=True)
        




if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ar_asset = ArAsset()
    app.exec_()
    

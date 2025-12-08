"""
Content  : arAsset - main logic to load the app
            - buttons for opening scenes and directories
            - shows scenes and assets in the project

Date     : 2025-11-13

Author   : Elena Giuliani
email    : elenagiuliani94@outlook.it
"""
import os
import sys
import webbrowser
import subprocess
from Qt import QtWidgets, QtGui, QtCompat, QtCore

from ruamel.yaml import YAML
yaml = YAML()
yaml.preserve_quotes = True

from arFiles import ArFiles
from arUtil import CURRENT_DIR, IMG_PATH, open_arScene_bat

from library.appfunc import yml_project_path, loaded_project_path, project_type, env_categories
from library.appfunc import get_directory, get_scenes, assets_data, files_naming

with open(yml_project_path, 'r', encoding='utf-8') as stream:
    project_data = yaml.load(stream)
selected_tab     = project_data['selected_tab']

TITLE = os.path.splitext(os.path.basename(__file__))[0]

class ArAsset(ArFiles):
    def __init__(self):
        super(ArAsset, self).__init__()
        self.path_ui = CURRENT_DIR + '/ui/' + TITLE + '.ui'

        self.wgAssets = QtCompat.load_ui(self.path_ui)
        self.wgHeader.setWindowTitle(TITLE)
        self.wgHeader.btnReloadApp.clicked.connect(lambda: self.press_btnReloadApp(app))
        self.wgType.btnChangeRootPath.clicked.connect(lambda: self.press_btnChangeRootPath(app))

        for instance, category in self.instances:
            # ICONS
            # change icon at list item click
            instance.listDepartments.currentItemChanged.connect(lambda current_item: self.set_icon_btnSoftwareFirstOpen(current_item)) 

            # load icon at app start
            instance.btnOpenLastVersionScene.setIcon(QtGui.QPixmap(IMG_PATH.format('maya_icon'))) 

            # SIGNALS
            instance.btnOpenLastVersionScene.clicked.connect(self.press_btnOpenLastVersionScene)
            instance.btnOpenFilesFolder.clicked.connect(lambda checked, wg=instance: self.press_btnOpenFilesFolder(wg))
            instance.btnAddScene.clicked.connect(self.press_btnAddScene)

        # UI
        for instance, category in self.instances:
            self.display_scenes(instance.layFilesModeling,  'maya', "modeling", category)
            self.display_scenes(instance.layFilesBaking,    'maya', "baking", category)
            self.display_scenes(instance.layFilesGroom,     'maya', "grooming", category)
            self.display_scenes(instance.layFilesRigging,   'maya', "rigging", category)
            self.display_scenes(instance.layFilesPose,      'maya', "pose", category)
            self.display_scenes(instance.layFilesAnimation, 'maya', "animation", category)
            self.display_scenes(instance.layFilesTexturing,     '', "texturing", category)

            self.display_assets(instance.layAsset, category)
            self.display_blueprints(instance.layBlueprints, category)

        self.set_state_listDepartments()

        for instance, category in self.instances:
            instance.listDepartments.currentRowChanged.connect(lambda row: self.change_stkFiles_page_at_press_item_listDepartments(row))

        # SIGNALS
        self.wgHeader.btnManageProjectsMenu.clicked.connect(lambda: self.set_create_manage_tabs('manage', app))
        self.wgHeader.btnCreateProjectMenu.clicked.connect(lambda: self.set_create_manage_tabs('create', app))

    #***************************************************************
    # FUNCTIONS
    def press_btnOpenLastVersionScene(self):
        with open(yml_project_path, 'r', encoding='utf-8') as stream:
            project_data = yaml.load(stream)
        selected_tab     = project_data['selected_tab']

        if selected_tab == 'Architectural':
            current_item = self.wgLoadArch.listDepartments.currentItem()

        elif selected_tab == 'Props':
            current_item = self.wgLoadProps.listDepartments.currentItem()

        elif selected_tab == 'Lamps':
            current_item = self.wgLoadLamps.listDepartments.currentItem()

        path_keywords = [[ files_naming['modeling']['department'],  files_naming['modeling']['extension']],
                         [files_naming['baking']['department'],    files_naming['baking']['extension']],
                         [files_naming['grooming']['department'],  files_naming['grooming']['extension']],
                         [files_naming['rigging']['department'],   files_naming['rigging']['extension']],
                         [files_naming['pose']['department'],      files_naming['pose']['extension']],
                         [files_naming['animation']['department'], files_naming['animation']['extension']],

                         [files_naming['sculpting']['department'], ""],
                         [files_naming['texturing']['department'], ""],
                        ]
        
        current_item = current_item.text()
        for (department, extension) in path_keywords:

            if department in current_item.lower():

                if department == 'texturing' or department == 'sculpting':
                    _, last_version_scene, scene_directory = get_scenes("", "", department)
                else:
                    _, last_version_scene, scene_directory = get_scenes(selected_tab, department, "scenes")

                last_version_scene_path = scene_directory + '/' + last_version_scene
                
                if last_version_scene_path:
                    self.press_open_scene(department, last_version_scene_path)
                    self.wgHeader.lblFeedback.setText(f'Opened {last_version_scene}')
                else:
                    self.wgHeader.lblFeedback.setText('No scene found')
                    

    def press_btnAddScene(self):
        subprocess.run(open_arScene_bat, check=True, shell=True)

    #***************************************************************
    # UI
    def display_scenes(self, layout, department, maya_task, category):
        category = category.title()

        if maya_task == 'texturing':
            all_files, _, scene_directory = get_scenes(category, '', maya_task)
        else:
            all_files, _, scene_directory = get_scenes(category, maya_task, 'scenes')
            
        if all_files:
            scenes_paths = []
            for scene in sorted(all_files, reverse=True):
                scenes_paths.append(scene_directory + '/' + scene)

            # for each scene found in the folder: create a ui instance and add it to the layout
            screenshot_path = None
            for path in scenes_paths:
                screenshot_path = None

                maya_scene = path.split('/')[-1]

                wgFile = QtCompat.load_ui(self.path_ui)

                wgFile.stkAssetsBlueprints.setCurrentIndex(0)
                wgFile.setMaximumHeight(60)

                # assign the asset name as version (v002, etc)
                extracted_version = os.path.basename(path).split('.')[0].split('_')[-1]
                wgFile.btnOpenScene.setText(extracted_version)

                wgFile.btnOpenScene.clicked.connect(lambda checked, path=path, dep=department: self.press_open_scene(dep, path))
                # checked stores the result of clicked -> False, because there is no checked active for the push button
                # p is the variable the respective path is stored in

                #***************************************************************
                # SCREENSHOT
                screenshot_directory = loaded_project_path + '/screenshots'
                if project_type == 'Environment':
                    for categ in env_categories:
                        candidate_path = screenshot_directory + '/' + category + '/files/' + department + '/' + maya_scene + '.png'
                        candidate_path = os.path.normpath(candidate_path)
                        
                        if os.path.exists(candidate_path):
                            if categ in candidate_path:
                                screenshot_path = candidate_path
                        else:
                            break
                else:
                    screenshot_path = screenshot_directory + '/files/' + department + '/' + maya_scene + '.png'

                if screenshot_path:
                    screenshot_path = os.path.normpath(screenshot_path)

                    wgFile.imgScene.setIcon(QtGui.QPixmap(screenshot_path))

                #***************************************************************
                # add one widget for each asset
                layout.addWidget(wgFile)


    def display_blueprints(self, layout, category):
        _, _, _, bp_assets_in_directory_path = assets_data(category.lower())

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


    def display_assets(self, layout, category):
        _, assets_in_directory_path, _, _ = assets_data(category.lower())

        if assets_in_directory_path:

            # create a ui instance for each fbx
            for asset_path in assets_in_directory_path:
                asset_name = os.path.splitext(os.path.basename(asset_path))[0]

                # create instance
                wgAsset = QtCompat.loadUi(self.path_ui)

                # widget ui
                wgAsset.btnOpenScene.setText(asset_name)

                #***************************************************************
                # LOAD SCREENSHOT
                screenshot_path = ''
                if project_type == 'Environment':
                    screenshot_name, _, screenshot_dir = get_scenes('screenshots', 'assets', asset_name)
                else:
                    screenshot_name, _, screenshot_dir = get_scenes('screenshots', '', asset_name)

                if screenshot_dir:
                    screenshot_path = os.path.normpath(screenshot_dir + '/' + screenshot_name[0])
                    wgAsset.imgScene.setIcon(QtGui.QPixmap(screenshot_path))

                    #***************************************************************
                    wgAsset.stkAssetsBlueprints.setCurrentIndex(0)
                    wgAsset.setMaximumHeight(60)
                    wgAsset.wgHoverAssets.setStyleSheet(""" QWidget:hover {background-color: transparent; }""") # make assets not hoverable

                    # add widget to ui
                    layout.addWidget(wgAsset)
        else:
            self.wgHeader.lblFeedback.setText('')


    def set_icon_btnSoftwareFirstOpen(self, current_item):
        current_item = current_item.text().lower()
        if current_item in 'texturing':
            for instance, category in self.instances:
                instance.btnOpenLastVersionScene.setIcon(QtGui.QPixmap(IMG_PATH.format('sp_icon')))
        else:
            for instance, category in self.instances:
                instance.btnOpenLastVersionScene.setIcon(QtGui.QPixmap(IMG_PATH.format('maya_icon')))


    def press_btnOpenFilesFolder(self, wg):
        with open(yml_project_path, 'r', encoding='utf-8') as stream:
            project_data = yaml.load(stream)
        selected_tab     = project_data['selected_tab']

        if wg.btnAssets.isChecked():
            folder_paths = get_directory("UE", selected_tab, "Meshes")

            for folder in folder_paths:
                if 'marketplace' in folder:
                    folder_paths.remove(folder)

            folder_path = folder_paths[0]

            if folder_path:
                if os.path.exists(folder_path):
                    webbrowser.open(folder_path)
            else:
                self.wgHeader.lblFeedback.setText("Folder not found")

        if wg.btnFiles.isChecked():
            item_widget = wg.listDepartments.currentItem()
            current_item = item_widget.text().lower()

            scenes_directories = [get_scenes(selected_tab, files_naming["modeling"]["extension"], "scenes")[-1],
                            get_scenes(selected_tab,   files_naming["baking"]["extension"],       "scenes")[-1],
                            get_directory("files", "", "texturing")[-1],
                            get_scenes(selected_tab,   files_naming["grooming"]["extension"],     "scenes")[-1],
                            get_scenes(selected_tab,   files_naming["rigging"]["extension"],      "scenes")[-1],
                            get_scenes(selected_tab,   files_naming["pose"]["extension"],         "scenes")[-1],
                            get_scenes(selected_tab,   files_naming["animation"]["extension"],    "scenes")[-1]
                            ]
            
            for scene_directory in scenes_directories:
                if scene_directory:
                    if current_item in scene_directory:
                        webbrowser.open(scene_directory)


    def set_state_listDepartments(self):
        def set_state():
            for instance, category in self.instances:
                layouts = [instance.layFilesModeling,
                           instance.layFilesSculpting,
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
        with open(yml_project_path, 'r', encoding='utf-8') as stream:
            project_data = yaml.load(stream)
        selected_tab     = project_data['selected_tab']

        for index in range(0,8):
            if row == index:
                for instance, category in self.instances:
                    if category == selected_tab.lower():
                        instance.stkFiles.setCurrentIndex(index)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ar_asset = ArAsset()
    app.exec()

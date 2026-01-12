"""
Content  : arAsset.py
            - buttons for opening scenes and directories
            - shows scenes and assets in the project

Date     : 2025-11-29

license  : MIT
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
from arUtil import APPS_DIR, ICONS_PATH

from Git_PackForge_Pipeline.library.apps.ui.stylesheet import get_stylesheet
from Git_PackForge_Pipeline.library.appdata import FILES_DEPARTMENTS, FILES_DEPT_COUNT, ENV_CATEGORIES, open_arScene_bat
from Git_PackForge_Pipeline.library.appfunc import get_directory, get_scenes, ue_meshes_data, normalize_paths, press_open_scene

TITLE = os.path.splitext(os.path.basename(__file__))[0]
not_maya_dept_index = [0, 2, 3, 5]


class ArAsset(ArFiles):
    def __init__(self):
        super(ArAsset, self).__init__()
        self.path_ui = APPS_DIR + '/ui/' + TITLE + '.ui'

        self.wgAssets = QtCompat.load_ui(self.path_ui)
        self.wgHeader.setWindowTitle(TITLE)
        self.wgHeader.btnReloadApp.clicked.connect(lambda: self.press_btnReloadApp(app))
        self.wgType.btnChangeRootPath.clicked.connect(lambda: self.press_btnChangeRootPath(app))

        for instance, category in self.instances:
            # ICONS
            # change icon at list item click
            instance.listDepartments.currentItemChanged.connect(lambda current_item: self.set_icon_btnSoftwareFirstOpen(current_item)) 

            # load icon at app start
            instance.btnOpenLastVersionScene.setIcon(QtGui.QPixmap(ICONS_PATH.format('maya_icon'))) 

            #***************************************************************
            # SIGNALS
            instance.btnOpenLastVersionScene.clicked.connect(self.press_btnOpenLastVersionScene)
            instance.btnOpenFilesFolder.clicked.connect(lambda checked, widget=instance, category=category: self.press_btnOpenFilesFolder(widget, category))
            instance.btnAddScene.clicked.connect(self.press_btnAddScene)

            # UI
            for index, attr in enumerate(FILES_DEPARTMENTS):
                layout = getattr(instance, attr[2])
                if index in not_maya_dept_index:
                    self.display_scenes(layout, attr[0], attr[0], category)
                else:
                    self.display_scenes(layout, 'maya', attr[0], category)

            self.display_assets(instance.layAsset, category)
            self.display_blueprints(instance.layBlueprints, category)

            self.set_ui_when_project_created(instance, category)
            instance.listDepartments.currentRowChanged.connect(lambda row: self.change_stkFiles_page_at_press_item_listDepartments(row))

        self.set_state_listDepartments()

        # SIGNALS
        self.wgHeader.btnManageProjectsMenu.clicked.connect(lambda: self.set_create_manage_tabs('manage', app))
        self.wgHeader.btnCreateProjectMenu.clicked.connect(lambda: self.set_create_manage_tabs('create', app))


    #***************************************************************
    # FUNCTIONS
    def press_btnOpenLastVersionScene(self):
        # find the selected item of listDepartments (ui)
        for env_widget, env_category in self.instances: # env_category is 'architectural', 'props', 'lamps'
            if self.selected_tab.lower() == env_category:
                current_item = env_widget.listDepartments.currentItem()

        # create list of keywords
        path_keywords = []
        for dept in range(0, FILES_DEPT_COUNT):
            if not dept in not_maya_dept_index:
                # MAYA
                path_keywords.append([FILES_DEPARTMENTS[dept][0], FILES_DEPARTMENTS[dept][1]]) # eg: ['modeling', 'model']
            # for 3d scanning, sculpting, texturing
            else:
                path_keywords.append([FILES_DEPARTMENTS[dept][0], ''])

        # find the scene path for the selected item of the ui list
        current_item = current_item.text()
        for (department, _) in path_keywords:
            if department in current_item.lower():
                if self.project_type == "Environment":
                    if department == 'texturing' or department == 'sculpting' or department == '3Dscanning' or department == 'clothing':
                        _, last_version_scene, scene_directory = get_scenes('', self.selected_tab, department)
                    else:
                        _, last_version_scene, scene_directory = get_scenes(self.selected_tab, department, "scenes")
                else:
                    if department == 'texturing' or department == 'sculpting' or department == '3Dscanning' or department == 'clothing':
                        _, last_version_scene, scene_directory = get_scenes("", "", department)
                    else:
                        _, last_version_scene, scene_directory = get_scenes("", department, "scenes")
                last_version_scene_path = scene_directory + '/' + last_version_scene
                
                # open scene
                if last_version_scene_path:
                    press_open_scene(department, last_version_scene_path)
                    self.wgHeader.lblFeedback.setText(f'Opened {last_version_scene}')
                else:
                    self.wgHeader.lblFeedback.setText('No scene found')
                    

    def press_btnOpenFilesFolder(self, widget, category):
        # ASSETS
        if widget.btnAssets.isChecked():
            folder_paths = get_directory("UE", category.title(), "Meshes")
            # open folder
            if folder_paths:
                if os.path.exists(folder_paths):
                    webbrowser.open(folder_paths)
            else:
                self.wgHeader.lblFeedback.setText("Folder not found")

        # FILES
        if widget.btnFiles.isChecked():
            current_item = widget.listDepartments.currentItem()
            list_item_text = current_item.text().lower()

            # get the "scenes" folder's path
            scenes_folder_path = []
            if self.project_type == 'Environment':
                for index in range(0, FILES_DEPT_COUNT):
                    if index in not_maya_dept_index:
                        scenes_folder_path.append(get_directory('files', self.selected_tab, FILES_DEPARTMENTS[index][0]))
                    else:
                        scenes_folder_path.append(get_directory(self.selected_tab, FILES_DEPARTMENTS[index][0], "scenes"))
            else:
                for index in range(0, FILES_DEPT_COUNT):
                    if index in not_maya_dept_index:
                        scenes_folder_path.append(get_directory("", "files", FILES_DEPARTMENTS[index][0]))
                    else:
                        scenes_folder_path.append(get_directory('', FILES_DEPARTMENTS[index][0], "scenes"))
            # open folder
            for scene_directory in scenes_folder_path:
                if scene_directory:
                    if list_item_text in scene_directory:
                        webbrowser.open(scene_directory)


    def press_btnAddScene(self):
        target_tab = (self.selected_tab)
        subprocess.run(open_arScene_bat, check=True, shell=True)
        if self.check_if_scene_files(target_tab):
            self.press_btnReloadApp(app)
            for index, env_cat in enumerate(ENV_CATEGORIES):
                if env_cat == target_tab:
                    self.wgType.tabWidget.setCurrentIndex(index)

        
    #***************************************************************
    # UI
    def display_scenes(self, layout, department, maya_task, category):
        category = category.title()

        if self.project_type == 'Environment':
            if not department == 'maya':
                all_files, _, scene_directory = get_scenes('', category, maya_task)
            else:            
                results = get_scenes(category, maya_task, 'scenes')
                if not results:
                    return
                all_files, _, scene_directory = results
        else:
            if not department == 'maya':
                all_files, _, scene_directory = get_scenes('', '', maya_task)
            else:            
                results = get_scenes('', maya_task, 'scenes')
                if not results:
                    return
                all_files, _, scene_directory = results

        if all_files:
            scenes_paths = []
            for scene in sorted(all_files, reverse=True):
                scenes_paths.append(scene_directory + '/' + scene)

            # for each scene found in the folder: create a ui instance and add it to the layout
            for path in scenes_paths:
                scene_name = path.split('/')[-1]
                wgFile = QtCompat.load_ui(self.path_ui)
                wgFile.setMaximumHeight(60)

                # assign the asset name as version (v002, etc)
                extracted_version = os.path.basename(path).split('.')[0].split('_')[-1]
                wgFile.btnOpenScene.setText(extracted_version)

                wgFile.btnOpenScene.clicked.connect(lambda checked, path=path, dep=department: press_open_scene(dep, path))
                # checked stores the result of clicked -> False, because there is no checked active for the push button
                # p is the variable the respective path is stored in

                # SCREENSHOT ***************************************************************
                self.display_screenshot('files', scene_name, wgFile)

                # add one widget for each asset
                layout.addWidget(wgFile)


    def display_blueprints(self, layout, category):
        _, blueprints_data = ue_meshes_data(category.lower())
        # BLUEPRINT ***************************************************************
        if blueprints_data:
            for blueprint, blueprint_meshes in blueprints_data.items():
                wgBlueprints = QtCompat.loadUi(self.path_ui)

                # icons
                wgBlueprints.imgScene.setIcon(QtGui.QPixmap(ICONS_PATH.format('folder_close')))
                wgBlueprints.btnArrowBlueprint.setIcon(QtGui.QPixmap(ICONS_PATH.format('arrow_full_right')))
                
                # widget ui
                wgBlueprints.btnOpenScene.setText(blueprint.split("/")[-1])
                wgBlueprints.wgtBpMeshes.hide()

                wgBlueprints.wgtAsset.setStyleSheet("""background-color: rgb(40, 40, 40);""")
                wgBlueprints.imgScene.setStyleSheet("""padding: -15px;""")

                def _press_Blueprint(widget, checked):
                    if checked:
                        widget.wgtBpMeshes.show()
                        widget.btnArrowBlueprint.setIcon(QtGui.QPixmap(ICONS_PATH.format('arrow_full_down')))
                    else:
                        widget.wgtBpMeshes.hide()
                        widget.btnArrowBlueprint.setIcon(QtGui.QPixmap(ICONS_PATH.format('arrow_full_right')))
                wgBlueprints.btnOpenScene.toggled.connect(lambda checked, wg = wgBlueprints: _press_Blueprint(wg, checked))

                # SCREENSHOT
                self.display_screenshot('assets', blueprint, wgBlueprints)

                # add widget to ui
                layout.addWidget(wgBlueprints)

                # STATIC MESHES IN BLUEPRINT ***************************************************************
                for blueprint_mesh in blueprint_meshes:
                    wgBlueprintItem = QtCompat.loadUi(self.path_ui)
                    wgBlueprintItem.btnOpenScene.setText(os.path.splitext(os.path.basename(blueprint_mesh))[0])

                    wgBlueprintItem.btnOpenScene.setStyleSheet("""
                                                                QWidget {background-color: transparent;}
                                                                QPushButton {border: 0px;
                                                                            padding-left: 10px;
                                                                            background-color: rgb(40, 40, 40);}
                                                                """)
                    wgBlueprintItem.imgScene.setStyleSheet("""padding: -15px;""")

                    # SCREENSHOT
                    self.display_screenshot('bp_mesh', (blueprint_mesh, blueprint), wgBlueprintItem)
                    wgBlueprints.layBpMeshes.addWidget(wgBlueprintItem)


    def display_assets(self, layout, category):
        ue_meshes_path, _ = ue_meshes_data(category.lower())
        if ue_meshes_path:
            # create a ui instance for each fbx
            for asset_path in ue_meshes_path:
                asset_name = os.path.splitext(os.path.basename(asset_path))[0]

                # create instance
                wgAsset = QtCompat.loadUi(self.path_ui)

                # widget ui
                wgAsset.btnOpenScene.setText(asset_name)
                wgAsset.imgScene.setStyleSheet("""padding: -15px;""")

                # SCREENSHOT ***************************************************************
                self.display_screenshot('assets', asset_name, wgAsset)

                layout.addWidget(wgAsset)


    def display_screenshot(self, screenshot_type, asset_scene_name, widget):
        screenshot_path = []
        # DISPLAY BLUEPRINT STATIC MESHES SCREENSHOT
        if screenshot_type == 'bp_mesh':
            asset_scene_name, bp_name = asset_scene_name
            screenshot_dir = get_directory('screenshots', 'assets', bp_name)
            asset_screenshot = f'{asset_scene_name.split('.')[0]}.png'
            screenshot_path = normalize_paths(screenshot_dir + '/' + asset_screenshot)
            widget.imgScene.setIcon(QtGui.QPixmap(screenshot_path))
            return

        #DISPLAY ASSETS' SCREENSHOT
        if screenshot_type == 'assets':
            screenshot_dir = get_directory('screenshots', 'assets', asset_scene_name)
            screenshot_path.append(normalize_paths(screenshot_dir + '/' + asset_scene_name + '.png'))

        # DISPLAY FILES' SCREENSHOT
        elif screenshot_type == 'files':
            screenshot_dir = get_directory('', 'screenshots', screenshot_type)
            if screenshot_dir:
                matched_files = []
                base_name = asset_scene_name.split('.')[0]
                for root, _, files in os.walk(screenshot_dir, topdown=False):
                    for file in files:
                        if file.startswith(base_name):
                            matched_files.append(file)
                            my_root = root
                if matched_files:
                    last_screenshot_version = sorted(matched_files)[-1]
                    screenshot_path.append(normalize_paths(my_root + '/' + last_screenshot_version))
                else:
                    screenshot_path.append(normalize_paths('/'.join(screenshot_dir.split('/')[:-1]) + '/' + 'screenshot_base.png'))

        if screenshot_path:
            for path in screenshot_path:
                widget.imgScene.setIcon(QtGui.QPixmap(path))


    def set_icon_btnSoftwareFirstOpen(self, current_item):
        current_item = current_item.text().lower()
        if current_item in 'texturing':
            for instance, _ in self.instances:
                instance.btnOpenLastVersionScene.setIcon(QtGui.QPixmap(ICONS_PATH.format('sp_icon')))
        if current_item in 'clothing':
            for instance, _ in self.instances:
                instance.btnOpenLastVersionScene.setIcon(QtGui.QPixmap(ICONS_PATH.format('MD_icon')))
        else:
            for instance, _ in self.instances:
                instance.btnOpenLastVersionScene.setIcon(QtGui.QPixmap(ICONS_PATH.format('maya_icon')))


    def set_state_listDepartments(self):
        for instance, _ in self.instances:
            for index, attr in enumerate(FILES_DEPARTMENTS):
                layout = getattr(instance, attr[2])
                if not layout.count():
                    item = instance.listDepartments.item(index)
                    item.setFlags(item.flags() & ~QtCore.Qt.ItemIsEnabled)
                    #item.setFlags(item.flags() | QtCore.Qt.ItemIsEnabled)


    def set_ui_when_project_created(self, instance, category):
            def _disable_btns_Files():
                instance.btnAddScene.setEnabled(False)
                instance.btnOpenFilesFolder.setEnabled(False)
                instance.btnOpenLastVersionScene.setEnabled(False)
                self.wgHeader.btnOpenProjectFolder.setEnabled(False)
                instance.stkFiles.hide()

            if not os.path.exists(self.project_root):
                self.wgHeader.lblFeedback.setText('Insert a root path in Manage projects')
                self._border_button(self.wgHeader.btnManageProjectsMenu)
                self._border_button(self.wgType.btnChangeRootPath)
                _disable_btns_Files()
                return

            if not self.loaded_project:
                if os.listdir(self.project_root):
                    _disable_btns_Files()
                    self.wgHeader.lblFeedback.setText('Load an existing project or create a new one')
                else:
                    _disable_btns_Files()
                    self._border_button(self.wgHeader.btnCreateProjectMenu)
                    self.wgHeader.lblFeedback.setText('Create a new project')

            elif not self.check_if_scene_files(category):
                instance.btnAddScene.setEnabled(True)
                self._border_button(instance.btnAddScene)
            else:
                instance.btnOpenFilesFolder.setEnabled(True)
                instance.btnOpenLastVersionScene.setEnabled(True)
                instance.stkFiles.show()


    def check_if_scene_files(self, category):
        files_found = []
        directories = self.project_root + '/files'
        if os.path.isdir(directories):
            if self.project_type == "Environment":
                scenes_directory = directories + '/' + category.title()
            else:
                scenes_directory = directories

            for _, _, files in os.walk(scenes_directory, topdown=False):
                for file in files:
                    if not file.endswith('.mel') and not file.endswith('.yml'):
                        files_found.append(file)
            if files_found:
                return True
            return False


    def change_stkFiles_page_at_press_item_listDepartments(self, row):
        for index in range(0, FILES_DEPT_COUNT):
            if row == index:
                for instance, category in self.instances:
                    if category == self.selected_tab.lower():
                        instance.stkFiles.setCurrentIndex(index)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ar_asset = ArAsset()
    app.setStyleSheet(get_stylesheet())
    app.exec()

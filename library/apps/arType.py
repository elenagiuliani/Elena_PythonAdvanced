"""
Content  : arType.py 
            - tabs for different project types (architecture, props, 3D scans and characters)

Date     : 2025-11-13

license  : MIT
Author   : Elena Giuliani
email    : elenagiuliani94@outlook.it
"""
import os
import sys
from datetime import datetime

from Qt import QtWidgets, QtGui, QtCompat, QtCore

from arUtil import ArUtil, APPS_DIR, ICON_PATH

from Git_PackForge_Pipeline.library.apps.ui.stylesheet import get_stylesheet
from Git_PackForge_Pipeline.library.appfunc import ue_meshes_data, marketplace_directories, all_directories, normalize_paths, get_directory
from Git_PackForge_Pipeline.library.appdata import yml_project_path, ENV_CATEGORIES, load_config_data, PROJECTS_DATA

from ruamel.yaml import YAML
yaml = YAML()
yaml.preserve_quotes = True

with open(yml_project_path, 'r', encoding='utf-8') as stream:
    project_data = yaml.load(stream)

TITLE = os.path.splitext(os.path.basename(__file__))[0]



class ArType(ArUtil):
    def __init__(self):
        super(ArType, self).__init__()
        path_ui = APPS_DIR + '/ui/' + TITLE + '.ui'
        self.wgType = QtCompat.loadUi(path_ui)
        self.wgHeader.setWindowTitle(TITLE)

        # ADD to layout
        self.wgHeader.layMain.addWidget(self.wgType)

        with open(yml_project_path, 'r', encoding='utf-8') as stream:
            project_data = yaml.load(stream)
        previous_tab = project_data['for_previous_tab']
        #***************************************************************
        # SIGNALS
        self.wgType.stkTabArch.setCurrentIndex(0)
        self.wgType.stkTabProps.setCurrentIndex(0)
        self.wgType.stkTab3Dscans.setCurrentIndex(0)
        self.wgType.btnChangeMarketplaceName.clicked.connect(self.press_btnChangeMarketplaceName)

        # UI
        self.open_Main()
        self.display_projects()

        self.wgType.wgtSpacer.hide()
        self.wgType.wgtSettings.hide()
        self.wgType.btnProject.hide()

        for index, env_cat in enumerate(ENV_CATEGORIES):
            if env_cat == previous_tab:
                self.wgType.tabWidget.setCurrentIndex(index)
                break
        # update at user interaction
        
        self.on_tab_changed(self.wgType.tabWidget.currentIndex())
        self.wgType.tabWidget.currentChanged.connect(lambda index: self.on_tab_changed(index))
        

    #***************************************************************
    # FUNCTIONS
    """CREATE PROJECT SECTION"""
    def press_create_btnProject(self, app):
        radio_buttons = [self.wgType.radEnvironment, self.wgType.radProps, self.wgType.radScans, self.wgType.radCharacters]

        for radio in radio_buttons:
            if radio.isChecked():
                radio_lower = radio.text().lower()
                for project_type_initial, (project_type, _) in PROJECTS_DATA.items():
                    if radio_lower in project_type.lower():

                        if not os.path.exists(self.projects_root):
                            os.makedirs(self.projects_root)         

                        new_project_type = project_type
                        project_type_path = self.projects_root + '/' + project_type
                        new_project_type_initial = project_type_initial

        new_project_name = self.wgType.linRootPath.text().replace(' ', '_')
        new_files_name = self.wgType.linMarketplaceName.text().title().replace(' ', '')
        current_year = str(datetime.now().year)[2:]

        if not new_project_name or not new_files_name:
            self.wgHeader.lblFeedback.setText('Fill all the fields')
            return

        if not os.path.exists(project_type_path):
            os.makedirs(project_type_path)

        # assemble new project name
        projects = os.listdir(project_type_path)  # find the existing projects in Environment or Props etc
        projects_versions = []
        if projects:
            for project in projects:
                projects_versions.append(project.split('__')[0].split('_')[-1])
                new_version = f'{(int(max(sorted(projects_versions))) + 1):03d}'
            new_project_folder = f'{new_project_type_initial}_{current_year}_{new_version}__{new_project_name}'
        else:
            new_project_folder = f'{new_project_type_initial}_{current_year}_001__{new_project_name}'
        new_project_path = project_type_path + '/' + new_project_folder

        # create new project folders
        matched_directories = all_directories(new_project_path, new_project_type, new_project_name)
        for directory in matched_directories:
            if os.path.exists(directory):
                self.wgHeader.lblFeedback.setText('Folder already exists')
            else:
                os.makedirs(directory)
                project_data['loaded_project'] = new_project_folder
                project_data['marketplace_name'] = new_project_name
                project_data['files_name'] = new_files_name

                with open(yml_project_path, 'w') as outfile:
                    yaml.dump(project_data, outfile)

                self.wgHeader.lblFeedback.setText('Project created!')
        # create yaml for project
        yml_data_path = new_project_path + '/files/data.yml'

        yml_data = {'files_name': new_files_name}
        with open(yml_data_path, 'w') as outfile:
            yaml.dump(yml_data, outfile)


    """MANAGE PROJECTS SECTION"""
    def press_btnChangeRootPath(self, app):

        with open(yml_project_path, 'r', encoding='utf-8') as stream:
            project_data = yaml.load(stream)

        project_data["projects_root"] = normalize_paths(self.wgType.linRootPath.text())

        # reset project variables
        project_data['loaded_project'] = ''
        project_data['files_name'] = ''
        project_data['marketplace_name'] = ''

        if os.path.exists(project_data["projects_root"]):

            with open(yml_project_path, 'w') as outfile:
                yaml.dump(project_data, outfile) 

        else:
            self.wgType.linRootPath.setText(self.projects_root)
        self.press_btnReloadApp()


    def press_btnChangeMarketplaceName(self):

        with open(yml_project_path, 'r', encoding='utf-8') as stream:
            project_data = yaml.load(stream)

        new_marketplace_name = self.wgType.linMarketplaceName.text().replace(' ', '_')
        project_data["marketplace_name"] = new_marketplace_name

        new_marketplace_directories = marketplace_directories(new_marketplace_name, self.loaded_project_path)
        for directory in new_marketplace_directories:
            os.makedirs(directory)

        with open(yml_project_path, 'w') as outfile:
            yaml.dump(project_data, outfile) 


    """SET PROJECT
    Project selected in "Manage projects" section in ui:
    - overwrites the "loaded_project" variable in yml
    - finds the "files_name" looking in the files and overwrites it in yml
    - finds the "marketplace_name" looking in the files and overwrites it in yml
    - reloads the UI """
    def press_btnProject(self, app):        
        # find the project selected in the ui
        for index, values in enumerate(PROJECTS_DATA.items()):
            if index == self.wgType.tabWidget.currentIndex():
                selected_list_project = getattr(self.wgType, list(PROJECTS_DATA.values())[index][1])
                break
        selected_project = selected_list_project.selectedItems()
        if selected_project:
            new_selected_project = selected_project[0].text()
            selected_list_project.clearSelection()
            
            if self.selected_tab == "Architectural":
                self.selected_tab == "Environment"
            if self.selected_tab == "Lamps":
                self.selected_tab == "3DScans"
            project_path = self.projects_root + '/' + self.selected_tab + '/' + new_selected_project 

            # find files name
            yml_data_path = project_path + '/files/data.yml'

            with open(yml_data_path, 'r') as stream:
                data = yaml.load(stream)
            data_files_name = data['files_name']

            # find marketplace name
            marketplace_path = project_path + '/marketplace'
            marketplace_versions = os.listdir(marketplace_path)
            marketplace_name = os.listdir(marketplace_path + '/' + max(sorted(marketplace_versions)))[0]

            # update project.yml
            project_data['loaded_project'] = new_selected_project
            project_data['files_name'] = data_files_name
            project_data['marketplace_name'] = marketplace_name

            with open(yml_project_path, 'w') as outfile:
                yaml.dump(project_data, outfile) 

            # update UI
            self.wgHeader.btnOpenProjectFolder.setText(new_selected_project)
            self.wgHeader.btnOpenProjectFolder.clicked.connect(lambda p=project_path: self.press_btnOpenProjectFolder(p))
            self.wgType.linMarketplaceName.setText(marketplace_name)

        self.press_btnReloadApp()
        return


    #*********************************************************************************************************************************
    # UI
    def on_tab_changed(self, index):
        self.selected_tab = self.wgType.tabWidget.tabText(index)        
        self.update_project_yml_selected_tab(self.selected_tab)
        self.display_assets_number(self.selected_tab)

    def on_Main_Manage_changed(self):
        current_index = self.wgType.tabWidget.currentIndex()
        self.selected_tab = self.wgType.tabWidget.tabText(current_index)
        self.update_project_yml_selected_tab(self.selected_tab)


    def display_projects(self):
        for index, ( _, (project_type, layout)) in enumerate(PROJECTS_DATA.items()):
            project_path_per_type = f'{self.projects_root}/{project_type}'

            if os.path.exists(project_path_per_type):
                projects = os.listdir(project_path_per_type)
            else:
                projects = ['']

            for project in projects:
                layout_widget = getattr(self.wgType, layout)
                layout_widget.addItem(project)

                # select loaded project at app start
                if project == self.loaded_project:
                    item = layout_widget.findItems(self.loaded_project, QtCore.Qt.MatchExactly)
                    layout_widget.setCurrentItem(item[0])


    def open_Main(self):
        self.wgType.btnProject.hide()
        self.wgHeader.btnBack.setEnabled(False)
        self.wgHeader.btnCreateProjectMenu.setEnabled(True)
        self.wgHeader.btnCreateProjectMenu.setChecked(False) 
        self.wgHeader.btnManageProjectsMenu.setEnabled(True)
        self.wgHeader.btnManageProjectsMenu.setChecked(False) 
        self.wgHeader.btnBack.setIcon(QtGui.QPixmap(ICON_PATH.format('btn_back_disabled')))

        # set tabs visibility
        if self.project_type == 'Environment':
            self.wgType.tabWidget.setTabVisible(0, True)
            self.wgType.tabWidget.setTabVisible(1, True)
            self.wgType.tabWidget.setTabVisible(2, True)
            self.wgType.tabWidget.setTabVisible(3, False)

        elif self.project_type == 'Props' or self.project_type == '3Dscans':
            self.wgType.tabWidget.setTabVisible(0, False)
            self.wgType.tabWidget.setTabVisible(1, True)
            self.wgType.tabWidget.setTabVisible(2, False)
            self.wgType.tabWidget.setTabVisible(3, False)

        elif self.project_type == 'Characters':
            self.wgType.tabWidget.setTabVisible(0, False)
            self.wgType.tabWidget.setTabVisible(1, False)
            self.wgType.tabWidget.setTabVisible(2, False)
            self.wgType.tabWidget.setTabVisible(3, True)

        # for first load of the app
        else:
            self.wgType.tabWidget.setTabVisible(0, True)
            self.wgType.tabWidget.setTabVisible(1, True)
            self.wgType.tabWidget.setTabVisible(2, True)
            self.wgType.tabWidget.setTabVisible(3, False)

        # set tabs text
        for index, category in enumerate(ENV_CATEGORIES):
            self.wgType.tabWidget.setTabText(index, category)

        self.wgType.tabWidget.show()
        self.wgType.wgtSettings.hide()

        self.wgType.stkTabArch.setCurrentIndex(0)
        self.wgType.stkTabProps.setCurrentIndex(0)
        self.wgType.stkTab3Dscans.setCurrentIndex(0)

        self.wgType.wgtSpacer.hide()
        self.wgType.layDetails.show()
        self.wgType.layTotal.show()


    def set_create_manage_tabs(self, action, app):
        if action == 'manage':
            # SIGNALS
            self.wgType.btnProject.clicked.connect(lambda checked, app=app: self.press_btnProject(app))
            self.wgHeader.btnBack.clicked.connect(self.open_Main)
            #self.update_project_yml_selected_tab(self.selected_tab)

            # UI
            self.wgType.wgtSettings.show()
            self.wgType.btnProject.show()
            self.wgHeader.btnBack.setEnabled(True)
            self.wgHeader.btnCreateProjectMenu.setEnabled(False)
            self.wgHeader.btnCreateProjectMenu.setChecked(False)
            self.wgHeader.btnBack.setIcon(QtGui.QPixmap(ICON_PATH.format('btn_back')))

            for index, (proj_type, _) in enumerate(PROJECTS_DATA.values()):
                self.wgType.tabWidget.setTabText(index, proj_type)

            self.wgType.tabWidget.setTabVisible(3, True)
            self.wgType.stkTabArch.setCurrentIndex(1)
            self.wgType.stkTabProps.setCurrentIndex(1)
            self.wgType.stkTab3Dscans.setCurrentIndex(1)
            self.wgType.stkTabCharacters.setCurrentIndex(1)

            self.wgType.lblRootPath.setText('Root path:')
            self.wgType.lblMarketplaceName.setText('Marketplace folder name:')
            self.wgType.btnProject.setText('Set project')

            self.wgType.linRootPath.setText(self.projects_root)
            self.wgType.linMarketplaceName.setText(self.marketplace_name)

            self.wgType.wgtSpacer.hide()
            self.wgType.layDetails.hide()
            self.wgType.layTotal.hide()
            self.wgType.btnChangeRootPath.show()
            self.wgType.btnChangeMarketplaceName.show()
            self.wgType.wgtCreateProject.hide()
            for index in range (0, 4):
                self.wgType.tabWidget.setTabVisible(index, True)
        self.on_Main_Manage_changed()

        if action == 'create':
            # SIGNALS
            self.wgType.btnProject.clicked.connect(lambda checked, app=app: self.press_create_btnProject(app))
            self.wgHeader.btnBack.clicked.connect(self.open_Main)

            # UI
            self.wgType.wgtSettings.show()
            self.wgType.btnProject.show()
            self.wgHeader.btnBack.setEnabled(True)
            self.wgHeader.btnManageProjectsMenu.setEnabled(False)
            self.wgHeader.btnManageProjectsMenu.setChecked(False)
            self.wgHeader.btnBack.setIcon(QtGui.QPixmap(ICON_PATH.format('btn_back')))

            self.wgType.lblRootPath.setText('Name of the project:')
            self.wgType.lblMarketplaceName.setText('Files name:')
            self.wgType.btnProject.setText('Create')

            self.wgType.linRootPath.setText('')
            self.wgType.linMarketplaceName.setText('')

            self.wgType.wgtSpacer.show()
            self.wgType.layDetails.hide()
            self.wgType.layTotal.hide()
            self.wgType.wgtCreateProject.show()
            self.wgType.btnChangeRootPath.hide()
            self.wgType.btnChangeMarketplaceName.hide()
            self.wgType.tabWidget.hide()


    #*********************************************************************************************************************************
    def display_assets_number(self, tab_name):
        ue_meshes, blueprints_data = ue_meshes_data(tab_name.lower())

        # NUMBER UNIQUE MESHES
        if ue_meshes:
            self.wgType.lblUniqueMeshesNumber.setText(str(len(ue_meshes)))
        else:
             self.wgType.lblUniqueMeshesNumber.setText(str(0))

        # NUMBER BLUEPRINTS
        if blueprints_data:
            if blueprints_data.keys():
                self.wgType.lblInteractiveMeshesNumber.setText(str(len(blueprints_data.keys())))
            else:
                self.wgType.lblInteractiveMeshesNumber.setText(str(0))

        # TOTAL NUMBER UNIQUE MESHES
        ue_paths = get_directory('', 'UE', 'Meshes')
        static_meshes = []
        if isinstance(ue_paths, list):
            for ue_path in ue_paths:
                for mesh in os.listdir(ue_path):
                    if mesh.startswith('SM'):
                        static_meshes.append(mesh)
        else:
            for mesh in os.listdir(ue_paths):
                if mesh.startswith('SM'):
                    static_meshes.append(mesh)

        if static_meshes:
            self.wgType.lblTotalUniqueMeshesNumber.setText(str(len(static_meshes)))

        # TOTAL NUMBER BLUEPRINTS
        ue_bp_paths = get_directory('', 'UE', 'Blueprints')
        blueprints = []
        if isinstance(ue_bp_paths, list):
            for ue_bp_path in ue_bp_paths:
                for bp in os.listdir(ue_bp_path):
                    if bp.startswith('BP'):
                        blueprints.append(bp)
        else:
            for bp in os.listdir(ue_bp_paths):
                if bp.startswith('BP'):
                    blueprints.append(bp)
        if blueprints:
            self.wgType.lblTotalInteractiveMeshesNumber.setText(str(len(blueprints)))


    #*********************************************************************************************************************************
    # YAML

    def update_project_yml_selected_tab(self, tab_text):
        project_data["for_previous_tab"] = tab_text

        # update the yaml file
        with open(yml_project_path, 'w') as outfile:
            yaml.dump(project_data, outfile)            
            

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ar_type = ArType()
    app.setStyleSheet(get_stylesheet())
    app.exec()

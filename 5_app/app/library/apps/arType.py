"""
Content  : arType - tabs for different project types (architecture, props, 3D scans and characters)

Date     : 2025-11-13

Author   : Elena Giuliani
email    : elenagiuliani94@outlook.it
"""
import os
import sys
from datetime import datetime

from Qt import QtWidgets, QtGui, QtCompat, QtCore

from arUtil import ArUtil, CURRENT_DIR, IMG_PATH
from library.appfunc import project_type_dir, project_type, yml_project_path, env_categories, project_types, loaded_project_path
from library.appfunc import assets_data, find_project_path_and_type, marketplace_directories, all_directories

from ruamel.yaml import YAML
yaml = YAML()
yaml.preserve_quotes = True
with open(yml_project_path, 'r', encoding='utf-8') as stream:
    project_data = yaml.load(stream)

TITLE = os.path.splitext(os.path.basename(__file__))[0]

class ArType(ArUtil):
    def __init__(self):
        super(ArType, self).__init__()
        path_ui = CURRENT_DIR + '/ui/' + TITLE + '.ui'

        self.wgType = QtCompat.loadUi(path_ui)

        self.wgHeader.setWindowTitle(TITLE)

        with open(yml_project_path, 'r', encoding='utf-8') as stream:
            project_data = yaml.load(stream)
        self.project_root = project_data['project_root']
        self.loaded_project = project_data['loaded_project']
        self.marketplace_name = project_data['marketplace_name']

        # ADD to layout
        self.wgHeader.layMain.addWidget(self.wgType)

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
        self.wgType.btnSetProject.hide()

        # show number of unique assets and interactive assets (blueprints)
        self.wgType.lblUniqueMeshesNumber.setText(str(self.display_assets_number('assets')))
        self.wgType.lblInteractiveMeshesNumber.setText(str(self.display_assets_number('blueprints')))

        # update selected tab in yml when changing tab
        current_widget = self.wgType.tabWidget.currentWidget()
        self.update_project_yml_selected_tab(current_widget.objectName())
        self.wgType.tabWidget.currentChanged.connect(lambda index: self.update_project_yml_selected_tab(index))
        self.wgType.tabWidget.currentChanged.connect(lambda widget: self.update_project_yml_selected_tab(self.wgType.tabWidget.widget(widget).objectName()))
        

    #***************************************************************
    # FUNCTIONS

    # CREATE PROJECT SECTION
    def press_create_btnSetProject(self, app):
        radio_buttons = [self.wgType.radEnvironment, self.wgType.radProps, self.wgType.radScans, self.wgType.radCharacters]
        new_project_type_initial = None

        for radio in radio_buttons:
            if radio.isChecked():
                radio_lower = radio.text().lower()

                for keys, values in project_type_dir.items():
                    radio_lower = radio.text().lower()
                    
                    if radio_lower in values.lower():
                        if not os.path.exists(values):
                            os.makedirs(values)         

                        new_project_type_initial = keys
                        project_type_path = values

        if new_project_type_initial == 'E':
            new_project_type = 'Environment'

        if new_project_type_initial == 'P':
            new_project_type = 'Props'

        if new_project_type_initial == 'S':
            new_project_type = '3Dscans'

        if new_project_type_initial == 'C':
            new_project_type = 'Characters'

        new_project_name = self.wgType.linRootPath.text().replace(' ', '_')
        new_files_name = self.wgType.linMarketplaceName.text().title().replace(' ', '')
        current_year = str(datetime.now().year)[2:]

        if not new_project_name or not new_files_name:
            self.wgHeader.lblFeedback.setText('Fill all the fields')
            return

        projects = os.listdir(project_type_path)
        projects_versions = []
        if projects:
            for project in projects:
                projects_versions.append(project.split('__')[0].split('_')[-1])

                new_version = f'{(int(max(sorted(projects_versions))) + 1):03d}'
            new_project_folder = f'{new_project_type_initial}_{current_year}_{new_version}__{new_project_name}'

        else:
            new_project_folder = f'{new_project_type_initial}_{current_year}_001__{new_project_name}'

        new_marketplace_name = new_project_name
        new_project_path = project_type_path + '/' + new_project_folder

        # check if the project folder exists
        matched_directories = all_directories(new_project_path, new_project_type, new_marketplace_name)
        for directory in matched_directories:
            if os.path.exists(directory):
                self.wgHeader.lblFeedback.setText('Folder already exists')

            else:
                os.makedirs(directory)

                project_data['loaded_project'] = new_project_folder
                project_data['marketplace_name'] = new_marketplace_name
                project_data['files_name'] = new_files_name

                with open(yml_project_path, 'w') as outfile:
                    yaml.dump(project_data, outfile)

                self.wgHeader.lblFeedback.setText('Project created!')

        yml_data_path = new_project_path + '/files/data.yml'

        yml_data = {'files_name': new_files_name}
        with open(yml_data_path, 'w') as outfile:
            yaml.dump(yml_data, outfile)

        self.press_btnReloadApp(app)

    #***************************************************************
    # MANAGE PROJECTS SECTION
    def press_btnChangeRootPath(self, app):
        with open(yml_project_path, 'r', encoding='utf-8') as stream:
            project_data = yaml.load(stream)

        project_data["project_root"] = self.wgType.linRootPath.text()

        if os.path.exists(project_data["project_root"]):
            with open(yml_project_path, 'w') as outfile:
                yaml.dump(project_data, outfile) 

        else:
            self.wgType.linRootPath.setText(self.project_root)

        self.press_btnReloadApp(app)


    def press_btnChangeMarketplaceName(self):
        with open(yml_project_path, 'r', encoding='utf-8') as stream:
            project_data = yaml.load(stream)

        new_marketplace_name = self.wgType.linMarketplaceName.text().replace(' ', '_')
        project_data["marketplace_name"] = new_marketplace_name

        new_marketplace_directories = marketplace_directories(new_marketplace_name, loaded_project_path)
        for directory in new_marketplace_directories:
            os.makedirs(directory)

        with open(yml_project_path, 'w') as outfile:
            yaml.dump(project_data, outfile) 


    def display_projects(self):
        self.list_projects = [self.wgType.listEnvironmentProjects, self.wgType.listPropsProjects, self.wgType.list3DscansProjects, self.wgType.listCharactersProjects]

        self.list_projects_dict = dict(zip(self.list_projects, project_type_dir.values()))

        for keys, values in self.list_projects_dict.items():
            if os.path.exists(values):
                projects = os.listdir(values)
            else:
                projects = ['']

            for project in projects:
                keys.addItem(project)

    """
    SET PROJECT
    Project selected in "Manage projects" section in ui:
    - overwrites the "loaded_project" variable in yml
    - finds the "files_name" looking in the files and overwrites it in yml
    - finds the "marketplace_name" looking in the files and overwrites it in yml
    - reloads the UI 
    """
    def press_btnSetProject(self, app):
        for project in self.list_projects:
            selected_items = project.selectedItems()

            if selected_items:
                selected_item = selected_items[0].text()
                
                project.clearSelection()

                project_type_path, _ = find_project_path_and_type(selected_item)
                project_path = project_type_path + '/' + selected_item 

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
                project_data['loaded_project'] = selected_item
                project_data['files_name'] = data_files_name
                project_data['marketplace_name'] = marketplace_name

                with open(yml_project_path, 'w') as outfile:
                    yaml.dump(project_data, outfile) 

                # update UI
                self.wgHeader.btnOpenProjectFolder.setText(selected_item)
                self.wgHeader.btnOpenProjectFolder.clicked.connect(lambda: self.press_btnOpenProjectFolder(project_path))
                self.wgType.linMarketplaceName.setText(marketplace_name)

        self.press_btnReloadApp(app)
        return

    #*********************************************************************************************************************************
    def open_Main(self):
        self.read_yml()
        self.wgType.btnSetProject.hide()
        self.wgHeader.btnBack.setEnabled(False)
        self.wgHeader.btnCreateProjectMenu.setEnabled(True)
        self.wgHeader.btnCreateProjectMenu.setChecked(False) 
        self.wgHeader.btnManageProjectsMenu.setEnabled(True)
        self.wgHeader.btnManageProjectsMenu.setChecked(False) 
        self.wgHeader.btnBack.setIcon(QtGui.QPixmap(IMG_PATH.format('btn_back_disabled')))

        # set tabs visibility
        if project_type == 'Environment':
            self.wgType.tabWidget.setTabVisible(0, True)
            self.wgType.tabWidget.setTabVisible(1, True)
            self.wgType.tabWidget.setTabVisible(2, True)
            self.wgType.tabWidget.setTabVisible(3, False)

        elif project_type == 'Props' or project_type == '3Dscans':
            self.wgType.tabWidget.setTabVisible(0, False)
            self.wgType.tabWidget.setTabVisible(1, True)
            self.wgType.tabWidget.setTabVisible(2, False)
            self.wgType.tabWidget.setTabVisible(3, False)

        elif project_type == 'Characters':
            self.wgType.tabWidget.setTabVisible(0, False)
            self.wgType.tabWidget.setTabVisible(1, False)
            self.wgType.tabWidget.setTabVisible(2, False)
            self.wgType.tabWidget.setTabVisible(3, True)

        # for first Load of the app
        else:
            self.wgType.tabWidget.setTabVisible(0, True)
            self.wgType.tabWidget.setTabVisible(1, True)
            self.wgType.tabWidget.setTabVisible(2, True)
            self.wgType.tabWidget.setTabVisible(3, False)

        # set tabs text
        for index, category in enumerate(env_categories):
            self.wgType.tabWidget.setTabText(index, category)

        self.wgType.tabWidget.show()
        self.wgType.wgtSettings.hide()

        self.wgType.stkTabArch.setCurrentIndex(0)
        self.wgType.stkTabProps.setCurrentIndex(0)
        self.wgType.stkTab3Dscans.setCurrentIndex(0)

        self.wgType.wgtSpacer.hide()
        self.wgType.layDetails.show()

        self.wgHeader.lblFeedback.setText('')


    def set_create_manage_tabs(self, action, app):
        try:
            self.wgType.btnSetProject.clicked.disconnect()
        except:
            pass

        if action == 'manage':
            self.read_yml()

            # SIGNALS
            self.wgType.btnSetProject.clicked.connect(lambda checked, app=app: self.press_btnSetProject(app))
            self.wgHeader.btnBack.clicked.connect(self.open_Main)

            # UI
            self.wgType.wgtSettings.show()
            self.wgType.btnSetProject.show()
            self.wgHeader.btnBack.setEnabled(True)
            self.wgHeader.btnCreateProjectMenu.setEnabled(False)
            self.wgHeader.btnCreateProjectMenu.setChecked(False)
            self.wgHeader.btnBack.setIcon(QtGui.QPixmap(IMG_PATH.format('btn_back')))

            for index, proj_type in enumerate(project_types):
                self.wgType.tabWidget.setTabText(index, proj_type)

            self.wgType.tabWidget.setTabVisible(3, True)

            self.wgType.stkTabArch.setCurrentIndex(1)
            self.wgType.stkTabProps.setCurrentIndex(1)
            self.wgType.stkTab3Dscans.setCurrentIndex(1)
            self.wgType.stkTabCharacters.setCurrentIndex(1)

            self.wgType.lblRootPath.setText('Root path:')
            self.wgType.lblMarketplaceName.setText('Marketplace folder name:')
            self.wgType.btnSetProject.setText('Set project')

            self.wgType.linRootPath.setText(self.project_root)
            self.wgType.linMarketplaceName.setText(self.marketplace_name)

            self.wgType.wgtSpacer.hide()
            self.wgType.layDetails.hide()
            self.wgType.btnChangeRootPath.show()
            self.wgType.btnChangeMarketplaceName.show()
            self.wgType.wgtCreateProject.hide()
            for index in range (0, 4):
                self.wgType.tabWidget.setTabVisible(index, True)


        if action == 'create':
            self.read_yml()

            # SIGNALS
            self.wgType.btnSetProject.clicked.connect(lambda checked, app=app: self.press_create_btnSetProject(app))
            self.wgHeader.btnBack.clicked.connect(self.open_Main)

            # UI
            self.wgType.wgtSettings.show()
            self.wgType.btnSetProject.show()
            self.wgHeader.btnBack.setEnabled(True)
            self.wgHeader.btnManageProjectsMenu.setEnabled(False)
            self.wgHeader.btnManageProjectsMenu.setChecked(False)
            self.wgHeader.btnBack.setIcon(QtGui.QPixmap(IMG_PATH.format('btn_back')))

            self.wgType.lblRootPath.setText('Name of the project:')
            self.wgType.lblMarketplaceName.setText('Files name:')
            self.wgType.btnSetProject.setText('Create')

            self.wgType.linRootPath.setText('')
            self.wgType.linMarketplaceName.setText('')

            self.wgType.wgtSpacer.show()
            self.wgType.layDetails.hide()
            self.wgType.wgtCreateProject.show()
            self.wgType.btnChangeRootPath.hide()
            self.wgType.btnChangeMarketplaceName.hide()
            self.wgType.tabWidget.hide()

    #*********************************************************************************************************************************
    def display_assets_number(self, asset_type):
        assets_in_directory, _, bp_assets_in_directory, _ = assets_data(project_type.lower())
        
        if asset_type == 'assets':
            if assets_in_directory:
                return len(assets_in_directory)
            
            else:
                assets_in_directory = 0
                return assets_in_directory
            
        if asset_type == 'blueprints':
            if bp_assets_in_directory:
                return len(bp_assets_in_directory)
            
            else:
                bp_assets_in_directory = 0
                return bp_assets_in_directory

    #*********************************************************************************************************************************
    # YAML
    def update_project_yml_selected_tab(self, widget):
        if widget == 'tabArchitectural':
            project_data["selected_tab"] = 'Architectural'

        elif widget == 'tabProps':
            project_data["selected_tab"] = 'Props'

        elif widget == 'tabLamps':
            project_data["selected_tab"] = 'Lamps'

        # update the yaml file
        with open(yml_project_path, 'w') as outfile:
            yaml.dump(project_data, outfile)            
            

    def read_yml(self):
        with open(yml_project_path, 'r', encoding='utf-8') as stream:
            project_data = yaml.load(stream)
        self.project_root = project_data['project_root']
        self.loaded_project = project_data['loaded_project']
        self.marketplace_name = project_data['marketplace_name']


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ar_type = ArType()
    app.exec()

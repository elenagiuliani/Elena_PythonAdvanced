"""
Content  : 

Date     : 2025-11-13

Author   : Elena Giuliani
email    : elenagiuliani94@outlook.it
"""


import os
import sys

from Qt import QtWidgets, QtGui, QtCompat, QtCore

from arUtil import ArUtil, CURRENT_DIR, IMG_PATH

from lib.appfunc import create_directory, assets_data

#*******************************************
# for update_project_yml_selected_tab
#import yaml
from ruamel.yaml import YAML
yaml = YAML()
yaml.preserve_quotes = True

# yml
yml_project_path = os.path.join(CURRENT_DIR, '..', '..', 'config', 'project.yml')

with open(yml_project_path, 'r', encoding='utf-8') as stream:
    project_data = yaml.load(stream)
selected_tab = project_data['selected_tab']

#*******************************************
TITLE = os.path.splitext(os.path.basename(__file__))[0]



class ArType(ArUtil):

    def __init__(self):
        super(ArType, self).__init__()
        path_ui = CURRENT_DIR + '/ui/' + TITLE + '.ui'
        self.wgType = QtCompat.loadUi(path_ui)
        self.wgManage = QtCompat.loadUi(path_ui)

        self.wgHeader.setWindowTitle(TITLE)

        with open(yml_project_path, 'r', encoding='utf-8') as stream:
            project_data = yaml.load(stream)
        self.main_dir = project_data['base_dir']
        self.loaded_code_project = project_data['loaded_project']
        self.marketplace_name = project_data['marketplace_name']

        # ADD to layout
        self.wgHeader.layMain.addWidget(self.wgType)
        self.wgHeader.layTypeManage.addWidget(self.wgManage)


        #***************************************************************
        # SIGNALS
        self.wgHeader.btnManageProjects.clicked.connect(self.open_btnManageProjects)
        self.wgHeader.btnCreateProject.clicked.connect(self.open_btnCreateProject)
        self.wgHeader.btnBack.clicked.connect(self.open_Main)

        self.wgHeader.btnChangeMarketplaceName.clicked.connect(self.press_btnChangeMarketplaceName)
        self.wgHeader.btnChangeRootPath.clicked.connect(self.press_btnChangeRootPath)

        # show number of unique assets and interactive assets (blueprints)
        self.wgType.lblUniqueMeshesNumber.setText(str(self.display_assets_number('assets')))
        self.wgType.lblInteractiveMeshesNumber.setText(str(self.display_assets_number('blueprints')))


        # writes on project.yml the current tab -> needed for arScene, create files scenes
        #self.wgType.tabWidget.currentChanged.connect(lambda index: self.update_project_yml_selected_tab(index))
        current_widget = self.wgType.tabWidget.currentWidget()
        print(f'\ncurrent_widget  {current_widget}\n')
        self.update_project_yml_selected_tab(current_widget)
        self.wgType.tabWidget.currentChanged.connect(lambda index: self.update_project_yml_selected_tab(index))


    #***************************************************************
    # FUNCTIONS
    
    # CHANGE BASE DIRECTORY AND THE PROJECT NAME FOR THE MARKETPLACE
    def press_btnChangeMarketplaceName(self):
        with open(yml_project_path, 'r', encoding='utf-8') as stream:
            project_data = yaml.load(stream)

        project_data["marketplace_name"] = self.wgHeader.linMarketplaceName.text()

        with open(yml_project_path, 'w') as outfile:
            yaml.dump(project_data, outfile) 


    def press_btnChangeRootPath(self):
        with open(yml_project_path, 'r', encoding='utf-8') as stream:
            project_data = yaml.load(stream)

        project_data["base_dir"] = self.wgHeader.linRootPath.text()
        if os.path.exists(project_data["base_dir"]):

            with open(yml_project_path, 'w') as outfile:
                yaml.dump(project_data, outfile) 

        else:
            self.wgHeader.linRootPath.setText(self.main_dir)
            #self.wgManage.lblManageFeedback.setText("The path doesn't exists")

    #*******************************************
    def open_btnManageProjects(self):
        self.read_yml()

        self.wgHeader.btnBack.setIcon(QtGui.QPixmap(IMG_PATH.format('btn_back')))

        self.wgHeader.stkTypeManageCreate.setCurrentIndex(1)
        self.wgManage.stkDetails.setCurrentIndex(1)
        self.wgHeader.btnBack.setEnabled(True)

        self.wgHeader.btnCreateProject.setEnabled(False)
        self.wgHeader.btnCreateProject.setChecked(False)

        self.wgManage.tabWidget.setTabText(0, "Environment")
        self.wgManage.tabWidget.setTabText(1, "Props")
        self.wgManage.tabWidget.setTabText(2, "3Dscans")

        self.wgManage.stkTabArch.setCurrentIndex(1)
        self.wgManage.stkTabProps.setCurrentIndex(1)
        self.wgManage.stkTab3Dscans.setCurrentIndex(1)

        self.wgHeader.linMarketplaceName.setText(self.marketplace_name)
        self.wgHeader.linRootPath.setText(self.main_dir)


    def open_btnCreateProject(self):
        self.read_yml()

        self.wgHeader.btnBack.setIcon(QtGui.QPixmap(IMG_PATH.format('btn_back')))

        self.wgHeader.stkTypeManageCreate.setCurrentIndex(2)
        self.wgHeader.btnBack.setEnabled(True)

        self.wgHeader.btnManageProjects.setEnabled(False)
        self.wgHeader.btnManageProjects.setChecked(False)


    def open_Main(self):
        self.read_yml()

        self.wgHeader.btnBack.setIcon(QtGui.QPixmap(IMG_PATH.format('btn_back_disabled')))

        self.wgHeader.stkTypeManageCreate.setCurrentIndex(0)
        self.wgType.stkDetails.setCurrentIndex(0)
        self.wgHeader.btnBack.setEnabled(False)

        self.wgHeader.btnCreateProject.setEnabled(True)
        self.wgHeader.btnManageProjects.setEnabled(True)
        self.wgHeader.btnCreateProject.setChecked(False) 
        self.wgHeader.btnManageProjects.setChecked(False) 


    def display_assets_number(self, type):
        assets_in_directory, _, bp_assets_in_directory, _ = assets_data()
        
        if type == 'assets':
            if assets_in_directory:
             return len(assets_in_directory)
            
            else:
                assets_in_directory = 0
                return assets_in_directory
            
        if type == 'blueprints':
            if bp_assets_in_directory:
                return len(bp_assets_in_directory)
            
            else:
                bp_assets_in_directory = 0
                return bp_assets_in_directory


    def update_project_yml_selected_tab(self, index):
        if index == 'tabArchitectural':
            project_data["selected_tab"] = 'Architectural'

        elif index == 'tabProps':
            project_data["selected_tab"] = 'Props'

        elif index == 'tabLamps':
            project_data["selected_tab"] = 'Lamps'

        # update the yaml file
        with open(yml_project_path, 'w') as outfile:
            yaml.dump(project_data, outfile)            


    def read_yml(self):
        with open(yml_project_path, 'r', encoding='utf-8') as stream:
            project_data = yaml.load(stream)
        self.main_dir = project_data['base_dir']
        self.loaded_code_project = project_data['loaded_project']
        self.marketplace_name = project_data['marketplace_name']



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ar_type = ArType()
    app.exec_()
    

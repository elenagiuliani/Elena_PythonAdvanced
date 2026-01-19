"""
Content  : arScene.py 
            - pop up ui for:  - creating and save a new maya workspace and file scene .ma
                              - creating a new Substance Painter file scene .spp

Date     : 2025-11-13

license  : MIT
Author   : Elena Giuliani
email    : elenagiuliani94@outlook.it
"""
import os
import sys
from Qt import QtWidgets, QtGui, QtCompat, QtCore

from ruamel.yaml import YAML
yaml = YAML()
yaml.preserve_quotes = True

from arUtil import ArUtil, APPS_DIR

from Git_PackForge_Pipeline.library.apps.ui.stylesheet import get_stylesheet
from Git_PackForge_Pipeline.library.appdata import yml_project_path, ENV_CATEGORIES, FILES_DEPARTMENTS, restart_app_bat
from Git_PackForge_Pipeline.library.appfunc import get_directory, press_open_scene

TITLE = os.path.splitext(os.path.basename(__file__))[0]


class ArScene(ArUtil):
    def __init__(self):
        super(ArScene, self).__init__()
        self.path_ui = APPS_DIR + '/ui/' + TITLE + '.ui'
        self.wgScene = QtCompat.load_ui(self.path_ui)
        self.wgHeader.setWindowTitle(TITLE)

        #***************************************************************
        # SIGNALS
        self.wgScene.btnCreateScene.clicked.connect(self.press_btnCreateScene)

        # UI
        self.display_items()
        self.wgHeader.wgUpper.hide()
        self.wgHeader.wgtFooter.hide()
        self.wgHeader.lblFeedback.hide()
        self.wgHeader.setFixedWidth(300)
        self.wgHeader.setFixedHeight(200)

        self.wgHeader.layMain.addWidget(self.wgScene)


    #***************************************************************
    # FUNCTIONS
    def display_items(self):
        with open(yml_project_path, 'r', encoding='utf-8') as stream:
            project_data = yaml.load(stream)
        selected_tab     = project_data['for_previous_tab']

        directory = self.project_root + '/files/' + selected_tab
        directories = []
        for department, _, _ in FILES_DEPARTMENTS:
            directories.append(directory + '/' + department)

        # deactivate the lines of the combo box that have files
        combo_model = self.wgScene.cbxChooseDepartment.model()
        for index, directory in enumerate(directories):
            has_files = any(files for _, _, files in os.walk(directory))
            if has_files:
                item = combo_model.item(index)
                item.setFlags(item.flags() & ~QtCore.Qt.ItemIsEnabled)
                item.setData(QtGui.QColor(150, 150, 150), QtCore.Qt.ForegroundRole)


    def press_btnCreateScene(self):
        current_text = self.wgScene.cbxChooseDepartment.currentText()
        current_text = current_text.lower()

        with open(yml_project_path, 'r', encoding='utf-8') as stream:
            project_data = yaml.load(stream)
        selected_tab     = project_data['for_previous_tab']

        for category in ENV_CATEGORIES:
            if selected_tab == category:
                for department, dept_short, _ in FILES_DEPARTMENTS:
                    if department in current_text:
                        # texturing
                        if FILES_DEPARTMENTS[5][0] in current_text:
                            project_path = get_directory('files', selected_tab, FILES_DEPARTMENTS[5][0])
                            press_open_scene(current_text, r'C:\Program Files\Adobe\Adobe Substance 3D Painter\Adobe Substance 3D Painter.exe')

                        # clothing
                        if FILES_DEPARTMENTS[2][0] in current_text:
                            project_path = get_directory('files', selected_tab, FILES_DEPARTMENTS[2][0])
                            press_open_scene(current_text, r'C:\Program Files\Marvelous Designer Enterprise Network Offline\MarvelousDesigner_Enterprise_Offline.exe')

                        # maya
                        else:
                            workspace_base = get_directory('files', selected_tab, department)
                            if self.project_type == "Environment":
                                project_path = os.path.join(workspace_base, f'{self.files_name}_{category.lower()}_{dept_short}_project')
                            else:
                                project_path = os.path.join(workspace_base, f'{self.files_name}_{dept_short}_project')
                            press_open_scene(current_text, '', project_path)
                            print(f'workspace_base    {workspace_base}')
        app.quit()



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ar_scene = ArScene()
    app.setStyleSheet(get_stylesheet())
    app.exec()

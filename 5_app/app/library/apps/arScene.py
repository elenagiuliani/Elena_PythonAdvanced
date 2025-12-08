"""
Content  : arScene - pop up ui for creating a new maya workspace and file scene .ma

Date     : 2025-11-13

Author   : Elena Giuliani
email    : elenagiuliani94@outlook.it
"""
import os
import sys
from Qt import QtWidgets, QtGui, QtCompat, QtCore

from ruamel.yaml import YAML
yaml = YAML()
yaml.preserve_quotes = True

from arUtil import ArUtil, CURRENT_DIR

from library.appfunc import yml_project_path, project_type, env_categories, project_type
from library.appfunc import get_directory, files_naming, file_extensions, file_departments, files_name

TITLE = os.path.splitext(os.path.basename(__file__))[0]

class ArScene(ArUtil):
    def __init__(self):

        super(ArScene, self).__init__()

        self.path_ui = CURRENT_DIR + '/ui/' + TITLE + '.ui'

        self.wgScene = QtCompat.load_ui(self.path_ui)
        self.wgHeader.setWindowTitle(TITLE)

        # SIGNALS
        self.wgScene.btnCreateScene.clicked.connect(self.press_btnCreateScene)

        # UI
        self.wgHeader.wgUpper.hide()
        self.wgHeader.wgFooter.hide()
        self.wgHeader.setFixedWidth(300)
        self.wgHeader.setFixedHeight(200)

        self.wgHeader.layMain.addWidget(self.wgScene)

    #***************************************************************
    # FUNCTIONS
    def press_btnCreateScene(self):
        current_text = self.wgScene.cbxChooseDepartment.currentText()
        current_text = current_text.lower()

        with open(yml_project_path, 'r', encoding='utf-8') as stream:
            project_data = yaml.load(stream)
        selected_tab     = project_data['selected_tab']

        for category in env_categories:
            if selected_tab == category:

                for department in file_departments:
                    if department in current_text:

                        # texturing
                        if files_naming["texturing"]["department"] in current_text:
                            project_path = get_directory(project_type, selected_tab, 'texturing')

                            self.press_open_scene(current_text, 'C:\Program Files\Adobe\Adobe Substance 3D Painter\Adobe Substance 3D Painter.exe')

                        # maya
                        else:
                            for extension in file_extensions:
                                if extension in department:
                                    file_extension = extension
                            workspace_base = get_directory(project_type, selected_tab, department)
                            print(f'workspace_base    {workspace_base}')

                            project_path = os.path.join(workspace_base[0], f'{files_name}_{file_extension}_project')

                            self.press_open_scene(current_text, '', project_path)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ar_scene = ArScene()
    app.exec()

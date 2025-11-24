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

from arUtil import ArUtil, CURRENT_DIR

from arType import ArType

from lib.appfunc import project_dir, project_type, get_directory, selected_tab, files_naming, env_categories

TITLE = os.path.splitext(os.path.basename(__file__))[0]


class ArScene(ArUtil):
    def __init__(self):

        super(ArScene, self).__init__()

        self.path_ui = CURRENT_DIR + '/ui/' + TITLE + '.ui'

        self.wgScene = QtCompat.load_ui(self.path_ui)
        self.wgHeader.setWindowTitle(TITLE)

        self.wgHeader.wgUpper.hide()
        self.wgHeader.wgFooter.hide()
        self.wgHeader.setFixedWidth(300)
        self.wgHeader.setFixedHeight(200)

        # SIGNALS
        self.wgHeader.layMain.addWidget(self.wgScene)

        self.wgScene.btnCreateScene.clicked.connect(self.press_btnCreateScene)

    #***************************************************************
    # FUNCTIONS

    def press_btnCreateScene(self):

        current_index = self.wgScene.cbxChooseDepartment.currentIndex()
        print(f'selected_tab      {selected_tab}')

        files_departments = [files_naming["modeling"]["department"],
                             files_naming["baking"]["department"],
                             files_naming["texturing"]["department"],
                             files_naming["grooming"]["department"],
                             files_naming["rigging"]["department"],
                             files_naming["pose"]["department"],
                             files_naming["animation"]["department"]
                             ]
        
        for category in env_categories:

            if selected_tab == category:

                for index, path in enumerate(files_departments):
                    if current_index == index:
                        scene_path = path
                        print(f'scene_path   {scene_path}')

                        if index == 2:
                            project_path = get_directory(["/files/" + category + "/" + scene_path])

                        else:
                            project_path = get_directory([category + "/maya/" + scene_path])

                        print(f'project_path         {project_path}')


        print(current_index)

        # TO DO: CRATE MAYA PROJECT AND EMPTY SCENE



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ar_scene = ArScene()
    app.exec_()
    

"""
Content  : arUtil.py 
            - main UI with header and footer

Date     : 2025-11-13

license  : MIT
Author   : Elena Giuliani
email    : elenagiuliani94@outlook.it
"""
import os
import sys
import subprocess
import webbrowser

from Qt import QtWidgets, QtGui, QtCompat, QtCore

ROOT_PATH = '\\'.join(os.path.dirname(__file__).split('\\')[:-3])
sys.path.append(ROOT_PATH)

from Git_PackForge_Pipeline.library.apps.ui.stylesheet import get_stylesheet
from Git_PackForge_Pipeline.library.appdata import APPS_DIR, ICON_PATH, load_config_data, restart_app_bat

(projects_root, project_root, loaded_project, loaded_project_path, loaded_project_name, project_type, 
 files_name, marketplace_name, selected_tab, screenshot_dir_base, project_path) = load_config_data()

TITLE = os.path.splitext(os.path.basename(__file__))[0]



class ArUtil():
    def __init__(self):
        path_ui = APPS_DIR + '/ui/' + TITLE + '.ui'
        self.wgHeader = QtCompat.loadUi(path_ui)
        self.wgCreate = QtCompat.loadUi(path_ui)

        self.project_root     = project_root
        self.projects_root    = projects_root
        self.selected_tab     = selected_tab
        self.project_type     = project_type
        self.files_name       = files_name
        self.project_path     = project_path
        self.loaded_project   = loaded_project
        self.marketplace_name = marketplace_name

        # ICONS
        self.wgHeader.setWindowIcon(QtGui.QPixmap(ICON_PATH.format('logo_store')))
        self.wgHeader.btnCgtraderLink.setIcon(QtGui.QPixmap(ICON_PATH.format('cgtrader_logo')))
        self.wgHeader.btnFabLink.setIcon(QtGui.QPixmap(ICON_PATH.format('fab_logo')))
        self.wgHeader.btnBack.setIcon(QtGui.QPixmap(ICON_PATH.format('btn_back_disabled')))
        self.wgHeader.btnReloadApp.setIcon(QtGui.QPixmap(ICON_PATH.format('btn_reload_app')))

        self.wgHeader.wgtFooter.setStyleSheet(f"""QWidget {{background-color: rgb(34, 35, 38)}};""")

        #***************************************************************
        # SIGNALS
        self.wgHeader.btnCgtraderLink.clicked.connect(lambda: self.press_btnStore('cgtrader'))
        #self.wgHeader.btnFabLink.clicked.connect(lambda: self.press_btnStore('fab'))
        self.wgHeader.btnFabLink.setEnabled(False)

        self.wgHeader.btnHelp.clicked.connect(self.press_btnHelp)
        self.wgHeader.btnOpenProjectFolder.setText(loaded_project)
        self.wgHeader.btnOpenProjectFolder.clicked.connect(lambda: self.press_btnOpenProjectFolder(loaded_project_path))

        self.wgHeader.show()


        self.watcher = QtCore.QFileSystemWatcher()
        self.reload_timer = QtCore.QTimer()
        self.reload_timer.setSingleShot(True)

    #***************************************************************
    # FUNCTIONS
        
    def press_btnStore(self, button):
        if button == 'cgtrader':
            webbrowser.open("https://www.cgtrader.com/designers/pixelsandcrafts")
        if button == 'fab':
            webbrowser.open("")

    def press_btnHelp(self):
        webbrowser.open("https://github.com/elenagiuliani/Elena_PythonAdvanced/wiki")

    def press_btnOpenProjectFolder(self, project_path):
        webbrowser.open(project_path)


    def _border_button(self, button):
        button.setStyleSheet("""QPushButton {
                                    border: 3px solid rgb(71, 89, 30);
                                    border-radius: 6px;
                                }""")


    def press_btnReloadApp(self):
        
        app = QtWidgets.QApplication.instance()
        app.quit()
        subprocess.run(restart_app_bat, check=True)

        """
        app.quit()
        subprocess.run(restart_app_bat, check=True)
        """

    # RELOAD WHEN FBX ADD/CHANGE ***************************************************************
    def reload_at_ue_file_change(self, path):

        def add_ue_paths(path):
            paths = []
            for root, _, _ in os.walk(path):
                paths.append(root)
            self.watcher.addPaths(paths)

        def _on_dir_changed(path):
            # wait Maya stops exporting
            add_ue_paths(path)
            self.reload_timer.start(1000)

        #add_ue_paths(path)
        
        self.reload_timer.timeout.connect(lambda: self.press_btnReloadApp())

        self.watcher.directoryChanged.connect(_on_dir_changed)




if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ar_util = ArUtil()
    app.setStyleSheet(get_stylesheet())
    app.exec()

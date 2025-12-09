"""
Content  : arUtil - main UI with header and footer

Date     : 2025-11-13

Author   : Elena Giuliani
email    : elenagiuliani94@outlook.it
"""
import os
import sys
import subprocess
import webbrowser

from Qt import QtWidgets, QtGui, QtCompat, QtCore

TITLE = os.path.splitext(os.path.basename(__file__))[0]
CURRENT_DIR =  os.path.dirname(__file__)
ROOT_PATH = '/'.join(CURRENT_DIR.split('\\')[:-2])
IMG_PATH =  CURRENT_DIR + '/../img/icons/{}.png'
sys.path.append(ROOT_PATH)

from library.appfunc import loaded_project, loaded_project_path, files_name, files_naming

# bat files
exe_main_path    = os.path.join(CURRENT_DIR, '..', '..', 'exe')
start_DCC_bat    = exe_main_path + '/start_DCC.bat'
open_arScene_bat = exe_main_path + '/create_scene.bat'
restart_app_bat  = exe_main_path + '/../desktop_app.bat'

class ArUtil():
    def __init__(self):
        path_ui = CURRENT_DIR + '/ui/' + TITLE + '.ui'
        self.wgHeader = QtCompat.loadUi(path_ui)
        self.wgCreate = QtCompat.loadUi(path_ui)

        # ICONS
        self.wgHeader.setWindowIcon(QtGui.QPixmap(IMG_PATH.format('logo_store')))
        self.wgHeader.btnCgtraderLink.setIcon(QtGui.QPixmap(IMG_PATH.format('cgtrader_logo')))
        self.wgHeader.btnFabLink.setIcon(QtGui.QPixmap(IMG_PATH.format('fab_logo')))
        self.wgHeader.btnBack.setIcon(QtGui.QPixmap(IMG_PATH.format('btn_back_disabled')))
        self.wgHeader.btnReloadApp.setIcon(QtGui.QPixmap(IMG_PATH.format('btn_reload_app')))

        # SIGNALS
        self.wgHeader.btnCgtraderLink.clicked.connect(lambda: self.press_btnStore('cgtrader'))
        #self.wgHeader.btnFabLink.clicked.connect(lambda: self.press_btnStore('fab'))
        self.wgHeader.btnFabLink.setEnabled(False)

        self.wgHeader.btnHelp.clicked.connect(self.press_btnHelp)
        self.wgHeader.btnOpenProjectFolder.setText(loaded_project)
        self.wgHeader.btnOpenProjectFolder.clicked.connect(lambda: self.press_btnOpenProjectFolder(loaded_project_path))

        self.wgHeader.show()

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

    def press_btnReloadApp(self, app):
        app.quit()
        subprocess.run(restart_app_bat, check=True, shell=True)

    #***************************************************************
    # OPEN SCENE
    # function partially created with the help of Copilot
    def press_open_scene(self, department, scene_path, workspace_path=None):

        # convert workspace_path from list to string if needed 
        if isinstance(workspace_path, list):
            if len(workspace_path) > 0:
                workspace_path = workspace_path[0]
            else:
                None

        with open(start_DCC_bat, 'r') as stream:
            lines = stream.readlines()

        # normalize existing scene_path
        if scene_path:
            scene_path = os.path.normpath(scene_path)

        # open substance painter
        if 'texturing' in department:
            lines[40] = (f'start "" "{scene_path}" ')

        # open new empty maya scene
        elif not scene_path:
            if workspace_path:
                workspace_path = os.path.normpath(workspace_path)

                # create the maya workspace structure
                self._create_maya_workspace(workspace_path)

                for name, info in files_naming.items():
                    if department in info['department']:
                        file_ext = info['extension']

                scenes_dir = workspace_path + '/scenes'
                save_path = scenes_dir + f'/{files_name}_{file_ext}_v001.ma'
                save_path_unix = save_path.replace('\\', '/')



                # command to execute in maya: create and save new maya scene
                python_command = (
                    f"maya.utils.executeDeferred(lambda: __import__('custom_shelf')); "
                    f"import maya.cmds as cmds; "
                    f"cmds.file(new=True, force=True); "
                    f"cmds.file(rename=r'{save_path_unix}'); "
                    f"cmds.file(save=True, type='mayaAscii')"
                )

                lines[40] = (
                    f'start "" "%MAYA_DIR%\\bin\\maya.exe" -proj "{workspace_path}" -command "python(\\\"{python_command}\\\")"\n'
                )
            else:
                lines[40] = (
                    f'start "" "%MAYA_DIR%\\bin\\maya.exe"\n'
                )

        # open existing maya scene
        else:
            if workspace_path:
                workspace_path = os.path.normpath(workspace_path)
                self._create_maya_workspace(workspace_path)

                lines[40] = (
                    f'start "" "%MAYA_DIR%\\bin\\maya.exe" -proj "{workspace_path}" -file "{scene_path}"\n'
                )
            else:
                lines[40] = (
                    f'start "" "%MAYA_DIR%\\bin\\maya.exe" -file "{scene_path}"\n'
                )

        # update the yaml file
        with open(start_DCC_bat, 'w') as outfile:
            outfile.writelines(lines) 

        # start scene
        subprocess.run(start_DCC_bat, check=True, shell=True)

    # create maya workspace structure
    def _create_maya_workspace(self, workspace_path):
        maya_folders = [
            'scenes',
            'images',
            'sourceImages',
            'scripts',
            'plugins',
            'cache',
            'sound'
        ]

        # create main workspace folder if it doesn't exist
        if not os.path.exists(workspace_path):
            os.makedirs(workspace_path)
        
        # create subfolders
        for folder in maya_folders:
            folder_path = workspace_path + '/' + folder
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)
        
        # create workspace.mel
        workspace_mel_path = workspace_path + '/' + 'workspace.mel'
        if not os.path.exists(workspace_mel_path):
            workspace_mel_content = f'''workspace -fr "translatorData" "{workspace_path}/translatorData";
                                        workspace -fr "offlineEditPack" "{workspace_path}/offlineEditPack";
                                        workspace -fr "renderData" "{workspace_path}/renderData";
                                        workspace -fr "depth" "{workspace_path}/renderData/depth";
                                        workspace -fr "mentalRayIpr" "{workspace_path}/renderData/mentalRayIpr";
                                        workspace -fr "mentalRayShadowData" "{workspace_path}/renderData/mentalRayShadowData";
                                        workspace -fr "ALEMBIC" "{workspace_path}/cache/alembic";
                                        workspace -fr "ifxCache" "{workspace_path}/cache";
                                        workspace -fr "particles" "{workspace_path}/cache/particles";
                                        workspace -fr "DIM" "{workspace_path}/cache/DIM";
                                        workspace -fr "Alembic" "{workspace_path}/cache/alembic";
                                        workspace -fr "sound" "{workspace_path}/sound";
                                        workspace -fr "fur" "{workspace_path}/fur";
                                        workspace -fr "furShadowMap" "{workspace_path}/renderData/furShadowMap";
                                        workspace -fr "furFiles" "{workspace_path}/fur";
                                        workspace -fr "clips" "{workspace_path}/clips";
                                        workspace -fr "Shaders" "{workspace_path}/renderData/shaders";
                                        workspace -fr "images" "{workspace_path}/images";
                                        workspace -fr "sourceImages" "{workspace_path}/sourceImages";
                                        workspace -fr "icons" "{workspace_path}/icons";
                                        workspace -fr "scripts" "{workspace_path}/scripts";
                                        workspace -fr "plugins" "{workspace_path}/plugins";
                                        workspace -fr "scenes" "{workspace_path}/scenes";
                                        '''
            with open(workspace_mel_path, 'w') as f:
                f.write(workspace_mel_content)
            
            print(f'Maya workspace created: {workspace_mel_path}')


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ar_util = ArUtil()
    app.exec()

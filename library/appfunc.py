"""
Content  : appfunc.py
                Main app functions and variables

Date     : 2025-11-05

license  : MIT
Author   : Elena Giuliani
email    : elenagiuliani94@outlook.it
"""
import os
import re
import subprocess
import shutil

from Git_PackForge_Pipeline.library.appdata import ENV_CATEGORIES, FILES_DEPARTMENTS, FILES_DEPT_COUNT, IMG_PATH
from Git_PackForge_Pipeline.library.appdata import start_DCC_bat, yml_project_path, load_config_data

(projects_root, project_root, loaded_project, loaded_project_path, loaded_project_name, project_type, 
 files_name, marketplace_name, selected_tab, screenshot_dir_base, project_path) = load_config_data()

from ruamel.yaml import YAML
yaml = YAML()
yaml.preserve_quotes = True


def normalize_paths(custom_path):
    if custom_path:
        normalized_path = os.path.normpath(custom_path).replace('\\', '/')
        return normalized_path


# CREATE DIRECTORIES PATHS ************************************************************************************
def all_directories(path, proj_type, marketplace_name):
            all_directories = []

            files_directories_rel = []
            for index in range(0, FILES_DEPT_COUNT):
                files_directories_rel.append("/" + FILES_DEPARTMENTS[index][0])

            ue_subfolders    = ["/Meshes", "/Meshes/Blueprints", "/Textures/1k", "/Textures/2k", "/Textures/4k",]
            files_base       = path + "/files/"
            ue_base          = path + "/UE/"

            files_directories = []
            ue_directories = []
            if proj_type == "Environment":
                for category in ENV_CATEGORIES:
                    for name in files_directories_rel:
                        files_directories.append(files_base + category + name)
                    for folder in ue_subfolders:
                        ue_path = ue_base + category + folder
                        ue_directories.append(ue_path)
            else:
                for name in files_directories_rel:
                    files_directories.append(files_base + category + name)
                for folder in ue_subfolders:
                    ue_directories.append(ue_base + folder)

            # append to all_directories
            for directory in files_directories:
                all_directories.append(directory)
            for directory in ue_directories:
                all_directories.append(directory)
            for directory in marketplace_directories(marketplace_name, path):
                all_directories.append(directory)
            all_directories.append(path + "/screenshots/files")
            return all_directories


def _version(marketplace_name, path):
    # create base directory v01
    if not os.path.exists(os.path.join(path, 'marketplace', 'v01')):
        return os.path.join(path, 'marketplace', 'v01', marketplace_name) # marketplace/v01/{marketplace_name}
    # version up
    else:
        versions = os.listdir(os.path.join(path, 'marketplace'))
        last_version = max(sorted(versions))[1:]
        new_version = f'v{(int(last_version)+ 1):02d}'
        return os.path.join(path, 'marketplace', new_version, marketplace_name)


def marketplace_directories(marketplace_name, path):
    directories = []
    sub_directories = ['LODs',
                        'Textures/1k',
                        'Textures/2k',
                        'Textures/4k',
                        'UE/Meshes/Blueprints',
                        'UE/Materials',
                        'UE/Textures/1k',
                        'UE/Textures/2k',
                        'UE/Textures/4k',
                        ]
    for sub_directory in sub_directories:
        directories.append(_version(marketplace_name, path) + f'/{marketplace_name}_{sub_directory}')
    return directories


# GET DIRECTORIES ************************************************************************************
def get_directory(filter1=None, filter2=None, filter3=None):
    matched_directories = []
    for root, dirs, files in os.walk(loaded_project_path, topdown=False):
        if os.path.basename(root) == filter3:
            if not filter2:
                matched_directories.append(normalize_paths(root))
                continue

            if re.search(rf"\\{filter2}\\", root):
                if not filter1:
                    matched_directories.append(normalize_paths(root))
                    continue

                if re.search(rf"\\{filter1}\\", root):
                    matched_directories.append(normalize_paths(root))

    if matched_directories:
        if len(matched_directories) == 1:
            return matched_directories[0]
        else:
            return matched_directories
    else:
        return None


# GET MAYA SCENES ************************************************************************************
def get_scenes(filter1, filter2, filter3):
    scenes_directory = get_directory(filter1, filter2, filter3)
    if scenes_directory:        
        if os.path.isdir(scenes_directory):
            all_files = []
            for _, _, files in os.walk(scenes_directory, topdown=False):
                all_files = files

            if all_files:
                last_version = max(sorted(all_files))
                return all_files, last_version, scenes_directory
            return None, None, scenes_directory
    return None, None, None


# ************************************************************************************
def ue_meshes_data(category):
    if project_type == 'Environment':
        ue_meshes_dir = get_directory('UE', category.title(), 'Meshes')
        ue_bp_dir = get_directory('UE', category.title(), 'Blueprints')
    else:
        ue_meshes_dir = get_directory('', 'UE', 'Meshes')
        ue_bp_dir = get_directory('', 'UE', 'Blueprints')

    if not ue_meshes_dir or not os.path.isdir(ue_meshes_dir):
        return [], []
    
    ue_meshes_path = []
    bp_static_meshes = []
    # find assets paths
    meshes_in_directory = os.listdir(ue_meshes_dir)
    for mesh in meshes_in_directory:
        full_path = ue_meshes_dir + '/' + mesh
        if os.path.isfile(full_path):
            ue_meshes_path.append(full_path)

    blueprints_data = {}
    # find blueprint assets in directory
    if ue_bp_dir and os.path.isdir(ue_bp_dir):
        for blueprint_name in os.listdir(ue_bp_dir):
            blueprint_path = ue_bp_dir + '/' + blueprint_name

            bp_static_meshes = []
            for static_mesh in os.listdir(blueprint_path):
                if static_mesh.startswith('SM'):
                    bp_static_meshes.append(static_mesh)
            blueprints_data[blueprint_name] = bp_static_meshes
    return ue_meshes_path, blueprints_data


# ************************************************************************************
# CREATE/OPEN SCENE
def press_open_scene(department, scene_path, workspace_path=None):
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

    # open substance painter or marvelous designer
    if 'texturing' in department or 'clothing' in department:
        lines[35] = (f'start "" "{scene_path}" ')

    # CREATE maya workspace and scene ***************************************************************
    elif not scene_path:
        screenshot_default = IMG_PATH.format('screenshot_base')
        shutil.copy(screenshot_default, screenshot_dir_base)
        if workspace_path:

            with open(yml_project_path, 'r', encoding='utf-8') as stream:
                project_data = yaml.load(stream)
                selected_tab     = project_data['for_previous_tab']

            workspace_path = os.path.normpath(workspace_path)

            # create the maya workspace structure
            _create_maya_workspace(workspace_path)

            for depart, dept_short, _ in FILES_DEPARTMENTS:
                if depart in department:
                    file_ext = dept_short
            scenes_dir = workspace_path + '/scenes'

            if project_type == "Environment":
                save_scene_path = normalize_paths(scenes_dir + f'/{files_name}_{selected_tab.lower()}_{file_ext}_v001.ma')
            else:
                save_scene_path = normalize_paths(scenes_dir + f'/{files_name}_{file_ext}_v001.ma')

            # command to execute in maya: create and save new maya scene
            python_command = (
                f"maya.utils.executeDeferred(lambda: __import__('custom_shelf')); "
                f"import maya.cmds as cmds; "
                f"cmds.file(new=True, force=True); "
                f"cmds.file(rename=r'{save_scene_path}'); "
                f"cmds.file(save=True, type='mayaAscii')"
                )
            lines[35] = (
                f'start "" "%MAYA_DIR%\\bin\\maya.exe" -proj "{workspace_path}" -command "python(\\\"{python_command}\\\")"\n'
                )
        else:
            lines[35] = (
                f'start "" "%MAYA_DIR%\\bin\\maya.exe"\n'
                )

    # OPEN existing maya scene ***************************************************************
    else:
        if workspace_path:
            workspace_path = os.path.normpath(workspace_path)
            _create_maya_workspace(workspace_path)
            lines[35] = (
                f'start "" "%MAYA_DIR%\\bin\\maya.exe" -proj "{workspace_path}" -file "{scene_path}"\n'
                )
        else:
            lines[35] = (
                f'start "" "%MAYA_DIR%\\bin\\maya.exe" -file "{scene_path}"\n'
                 )
    # update the yaml file
    with open(start_DCC_bat, 'w') as outfile:
        outfile.writelines(lines) 

    # start scene
    subprocess.run(start_DCC_bat, check=True, shell=True)


# create maya workspace structure
def _create_maya_workspace(workspace_path):
    maya_folders = ['scenes',
                    'images',
                    'sourceImages',
                    'scripts',
                    'plugins',
                    'cache',
                    ]
    # create main workspace folder if it doesn't exist
    if not os.path.exists(workspace_path):
        os.makedirs(workspace_path)
    
    workspace_mel_path = workspace_path + '/' + 'workspace.mel'
    print(f'<<<<<<<< workspace_path  {workspace_path}')

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
                                    workspace -fr "Alembic" "{workspace_path}/cache/alembic";
                                    workspace -fr "clips" "{workspace_path}/clips";
                                    workspace -fr "Shaders" "{workspace_path}/renderData/shaders";
                                    workspace -fr "images" "{workspace_path}/images";
                                    workspace -fr "sourceImages" "{workspace_path}/sourceImages";
                                    workspace -fr "scenes" "{workspace_path}/scenes";
                                    '''
        
        with open(workspace_mel_path, 'w') as outfile:
            outfile.write(workspace_mel_content)

        print(f'<<<<<<<<< Maya workspace created: {workspace_mel_path}')

"""
Content  : appdata.py
                - define application data and configuration

Date     : 2025-12-12

license  : MIT
Author   : Elena Giuliani
email    : elenagiuliani94@outlook.it
"""
import os
import subprocess

LIBRARY_PATH = os.path.dirname(__file__)
ROOT_PATH    = os.path.dirname(LIBRARY_PATH)
APPS_DIR     = LIBRARY_PATH + '/apps'
ICON_PATH   = LIBRARY_PATH + '/img/icons/{}.png'
IMG_PATH     = LIBRARY_PATH + '/img/{}.png'
MAYA_PYTHON  = r'C:\\Program Files\\Autodesk\\Maya2022\\bin\\mayapy.exe'

# bat files
exe_main_path    = ROOT_PATH     + '/exe'
restart_app_bat  = ROOT_PATH     + '/desktop_app.bat'
open_arScene_bat = exe_main_path + '/create_scene.bat'
start_DCC_bat    = exe_main_path + '/start_DCC.bat'

yml_project_path = os.path.join(LIBRARY_PATH, 'config', 'project.yml')

ENV_CATEGORIES = ['Architectural', 'Props', 'Lamps']

PROJECTS_DATA = {'E' : ('Environment', 'listEnvironmentProjects'),
                 'P' : ('Props',       'listPropsProjects'), 
                 'S' : ('3Dscans',     'list3DscansProjects'), 
                 'C' : ('Characters',  'listCharactersProjects')
                }

FILES_DEPARTMENTS = [('3Dscanning', 'scan',   'layFilesScanning'),  # 0
                     ('modeling',   'model',  'layFilesModeling'),
                     ('clothing',   'cloth',  'layFilesClothing'),  # 2
                     ('sculpting',  'sculpt', 'layFilesSculpting'), # 3
                     ('baking',     'baking', 'layFilesBaking'),
                     ('texturing',  'tex',    'layFilesTexturing'), # 5
                     ('grooming',   'groom',  'layFilesGroom'),
                     ('rigging',    'rig',    'layFilesRigging'),
                     ('pose',       'pose',   'layFilesPose'),
                     ('animation',  'anim',   'layFilesAnimation'),
                    ]
FILES_DEPT_COUNT = len(FILES_DEPARTMENTS)


def load_config_data():
    try:
        from ruamel.yaml import YAML
    except ImportError:
        subprocess.check_call([
                            MAYA_PYTHON,
                            "-m",
                            "pip",
                            "install",
                            "ruamel.yaml"
                            ])
        from ruamel.yaml import YAML
        print('<<<<<<< ruamel.yaml INSTALLED')

    yaml = YAML()
    yaml.preserve_quotes = True

    with open(yml_project_path, 'r', encoding='utf-8') as stream:
        project_data = yaml.load(stream)

    projects_root    = project_data['projects_root']
    loaded_project   = project_data['loaded_project']
    files_name       = project_data['files_name']
    marketplace_name = project_data['marketplace_name']
    selected_tab     = project_data['for_previous_tab']
    
    # FIRST APP START
    if loaded_project == '':
        loaded_project_path = ''
        project_type = ''
        loaded_project_name = ''
        project_path = ''
    # LOAD AN EXISTING PROJECT
    else:
        loaded_project_name = loaded_project.split('__')[-1] # 1970_ceramic_set        
        for key, value in PROJECTS_DATA.items():

            if loaded_project.startswith(key):
                project_path = f'{projects_root}/{value[0]}'
                project_type = value[0]
        loaded_project_path = f'{project_path}/{loaded_project}'

    project_root = f'{projects_root}/{project_type}/{loaded_project}'
    screenshot_dir_base = f'{project_root}/screenshots'

    return projects_root, project_root, loaded_project, loaded_project_path, loaded_project_name, project_type, files_name, marketplace_name, selected_tab, screenshot_dir_base, project_path

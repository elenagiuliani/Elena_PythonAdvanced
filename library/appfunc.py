"""
Content  : main app functions and variables

Date     : 2025-11-05

Author   : Elena Giuliani
email    : elenagiuliani94@outlook.it
"""
import os
import re

from ruamel.yaml import YAML
yaml = YAML()
yaml.preserve_quotes = True

CURRENT_DIR = os.path.dirname(__file__)

yml_project_path = os.path.join(CURRENT_DIR, 'config', 'project.yml')

with open(yml_project_path, 'r', encoding='utf-8') as stream:
    project_data = yaml.load(stream)

project_root     = project_data['project_root']
loaded_project   = project_data['loaded_project']
marketplace_name = project_data['marketplace_name']
project_types    = project_data['project_types']
files_naming     = project_data['files_naming']
env_categories   = project_data['env_categories']
selected_tab     = project_data['selected_tab']
files_name       = project_data['files_name']

file_departments = [files_naming["modeling"]["department"],
                    files_naming["sculpting"]["department"],
                    files_naming["baking"]["department"],
                    files_naming["texturing"]["department"],
                    files_naming["grooming"]["department"],
                    files_naming["rigging"]["department"],
                    files_naming["pose"]["department"],
                    files_naming["animation"]["department"]
                    ]

file_extensions = [files_naming["modeling"]["extension"],
                    files_naming["sculpting"]["extension"],
                    files_naming["baking"]["extension"],
                    files_naming["texturing"]["extension"],
                    files_naming["grooming"]["extension"],
                    files_naming["rigging"]["extension"],
                    files_naming["pose"]["extension"],
                    files_naming["animation"]["extension"]
                    ]

# PROJECT TYPES
project_type_dir = {
    "E" : project_root + '/' + project_types[0],
    "P" : project_root + '/' + project_types[1],
    "S" : project_root + '/' + project_types[2],
    "C" : project_root + '/' + project_types[3]
    }
#***************************************************************
def find_project_path_and_type(project):
    # find the project path from the project name
    for key, value in project_type_dir.items():
        if project.startswith(key):
            project_path = value

    project_type = project_path.split('/')[-1]
    return project_path, project_type

if loaded_project == '':
    loaded_project_path = ''
    project_type = ''
    loaded_project_name = ''
    loaded_project_code = ''         
    project_path = ''

else:
    project_path, project_type = find_project_path_and_type(loaded_project)

    # list of projects in type directory
    projects_in_dir = os.listdir(project_path)            # displayed in ui list

    print(f'loaded_project          {loaded_project}')
    print(f'\nselected project dir: {project_path}\n')    # eg:  F:/3D_Projects/5_PixelsAndCrafts/Props
    print(f"project_type:           {project_type}")      # eg:  project_type:    Props
    print(f'projects_in_dir:        {projects_in_dir}\n') # eg:  projects_in_dir:    ['P_25_001__1970_ceramic_set']

    #***************************************************************
    # INFO OF LOADED PROJECT FROM PROJECT.YML

    # dir of the loaded project
    loaded_project_path = project_path + "/" + loaded_project

    # loaded project name
    loaded_project_name = loaded_project.split('__')[-1] # 1970_ceramic_set

    # loaded project code
    loaded_project_code = loaded_project.split('__')[0] # P_25_001

    print(f"loaded project path: {loaded_project_path}")   # eg: loaded project path: F:/3D_Projects/5_PixelsAndCrafts/Props/P_25_001__1970_ceramic_set
    print(f"loaded project name: {loaded_project_name}")   # eg: loaded project name: 1970_ceramic_set
    print(f"loaded project code: {loaded_project_code}\n") # eg: loaded project code: P_25_001

#******************************************************************************************************************************
def version(path, marketplace_name):
    # create base directory v01
    if not os.path.exists(os.path.join(path, 'marketplace', 'v01')):
        return os.path.join(path, 'marketplace', 'v01', marketplace_name) # marketplace/v01/{marketplace_name}

    # version up
    else:
        versions = os.listdir(os.path.join(path, 'marketplace'))
        last_version = max(sorted(versions))[1:]
        new_version = f'v{(int(last_version)+ 1):02d}'
        return os.path.join(path, 'marketplace', new_version, marketplace_name)


def all_directories(path, proj_type, marketplace_name):
            all_directories = []

            files_naming_list = ["/maya/" + files_naming["modeling"]["department"],
                                 "/maya/" + files_naming["baking"]["department"],
                                 "/maya/" + files_naming["grooming"]["department"],
                                 "/maya/" + files_naming["rigging"]["department"],
                                 "/maya/" + files_naming["pose"]["department"],
                                 "/maya/" + files_naming["animation"]["department"],
                                 "/"      + files_naming["texturing"]["department"],
                                 "/"      + files_naming["sculpting"]["department"],
                                 ]

            files_naming_list_extension = ["/maya/" + files_naming["modeling"]["extension"],
                                 "/maya/" + files_naming["baking"]["extension"],
                                 "/maya/" + files_naming["grooming"]["extension"],
                                 "/maya/" + files_naming["rigging"]["extension"],
                                 "/maya/" + files_naming["pose"]["extension"],
                                 "/maya/" + files_naming["animation"]["extension"],
                                 "/"      + files_naming["texturing"]["extension"],
                                 "/"      + files_naming["sculpting"]["extension"],
                                 ]

            ue_subfolders = ["/Meshes", "/Meshes/Blueprints", "/Textures/1k", "/Textures/2k", "/Textures/4k",]

            files_base = path + "/files/"
            ue_base = path + "/UE/"

            files_directories = []
            ue_directories = []

            if proj_type == "Environment":
                for category in env_categories:
                    for name in files_naming_list:
                        file_path = files_base + category + name
                        files_directories.append(file_path)

                    for folder in ue_subfolders:
                        ue_path = ue_base + category + folder

                        ue_directories.append(ue_path)
            else:
                for name in files_naming_list:
                    files_directories.append(files_base + name)

                for folder in ue_subfolders:
                    ue_directories.append(ue_base + folder)

              
            # append to all_directories
            for directory in files_directories:
                all_directories.append(directory)

            for directory in ue_directories:
                all_directories.append(directory)
                
            for directory in marketplace_directories(marketplace_name, path):
                all_directories.append(directory)
            
            return all_directories


def marketplace_directories(marketplace_name, path):
    marketplace_directories = [
        version(path, marketplace_name) + '/' + f'{marketplace_name}_staticRender/LODs',
        version(path, marketplace_name) + '/' + f'{marketplace_name}_staticRender/maya',
        version(path, marketplace_name) + '/' + f'{marketplace_name}_staticRender/Textures',

        version(path, marketplace_name) + '/' + f'{marketplace_name}_UE/Meshes/Blueprints',
        version(path, marketplace_name) + '/' + f'{marketplace_name}_UE/Materials',
        version(path, marketplace_name) + '/' + f'{marketplace_name}_UE/Textures/1k',
        version(path, marketplace_name) + '/' + f'{marketplace_name}_UE/Textures/2k',
        version(path, marketplace_name) + '/' + f'{marketplace_name}_UE/Textures/4k',

        version(path, marketplace_name) + '/' + f'{marketplace_name}_UnrealEngine_Textures/1k',
        version(path, marketplace_name) + '/' + f'{marketplace_name}_UnrealEngine_Textures/2k',
        version(path, marketplace_name) + '/' + f'{marketplace_name}_UnrealEngine_Textures/4k'
    ]
    return marketplace_directories


def get_directory(env_category, filter1, filter2):
    matches_first = []
    matches_second = []
    matches_third = []
    for root, dirs, files in os.walk(loaded_project_path, topdown=False):
        if re.search(env_category, root):
            matches_first.append(root)

            if re.search(filter1, root):
                matches_second.append(root)

                if os.path.basename(root) == filter2:
                    matches_third.append(root)

    return matches_third

#******************************************************************************************************************************
# GET MAYA SCENES
def get_scenes(filter1, filter2, filter3):
    results = get_directory(filter1, filter2, filter3)

    if not results:
        return None, None, None

    scene_directory = results[0]
    if scene_directory:
        if os.path.isdir(scene_directory):

            all_files = []
            for root, dirs, files in os.walk(scene_directory, topdown=False):
                all_files = files

            if all_files:
                last_version = max(sorted(all_files))

                return all_files, last_version, scene_directory
            
            return None, None, scene_directory
    return None, None, None


# UE folder with assets fbx
def assets_data(category):
    if project_type == 'Environment':
        ue_meshes_candidates = get_directory('UE', category.title(), 'Meshes')
        ue_bp_candidates = get_directory('UE', category.title(), 'Blueprints')
    else:
        ue_meshes_candidates = get_directory('UE', '', 'Meshes')
        ue_bp_candidates = get_directory('UE', '', 'Blueprints')


    def pick_dir(candidates):
        if not candidates:
            return None

        for directory in candidates:
            # find directory without 'marketplace
            if "marketplace" not in directory.lower():
                return directory
            
        return None


    ue_meshes_dir = pick_dir(ue_meshes_candidates)
    ue_bp_dir = pick_dir(ue_bp_candidates)

    if not ue_meshes_dir or not os.path.isdir(ue_meshes_dir):
        return [], [], [], []

    if not ue_bp_dir or not os.path.isdir(ue_bp_dir):
        bp_items_in_directory = []
    else:
        bp_items_in_directory = os.listdir(ue_bp_dir)

    # find items in directory
    items_in_directory = os.listdir(ue_meshes_dir)

    assets_in_directory_path = []
    assets_in_directory = []

    for name in items_in_directory:
        full = ue_meshes_dir + '/' + name
        if os.path.isfile(full):
            assets_in_directory_path.append(full)
            assets_in_directory.append(os.path.basename(full))

    # find blueprint assets in directory
    bp_assets_in_directory = []
    bp_assets_in_directory_path = []

    if ue_bp_dir and os.path.isdir(ue_bp_dir):
        for name in os.listdir(ue_bp_dir):
            full = ue_bp_dir + '/' + name

            if os.path.isdir(full) and (name.startswith('BP') or True):
                bp_assets_in_directory_path.append(full)
                bp_assets_in_directory.append(name)

    return assets_in_directory, assets_in_directory_path, bp_assets_in_directory, bp_assets_in_directory_path
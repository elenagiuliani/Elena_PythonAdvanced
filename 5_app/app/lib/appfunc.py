"""
Content  : app utils

Date     : 2025-11-05

Author   : Elena Giuliani
email    : elenagiuliani94@outlook.it
"""


import os

#import yaml
from ruamel.yaml import YAML
yaml = YAML()
yaml.preserve_quotes = True

CURRENT_DIR = os.path.dirname(__file__)

# yml
yml_project_path = os.path.join(CURRENT_DIR, '..', 'config', 'project.yml')

with open(yml_project_path, 'r', encoding='utf-8') as stream:
    project_data = yaml.load(stream)
main_dir = project_data['base_dir']

loaded_code_project = project_data['loaded_project']
files_name = project_data['files_name']
marketplace_name = project_data['marketplace_name']

project_types = project_data['project_types']

files_naming = project_data['files_naming']

env_categories = project_data['env_categories']

selected_tab = project_data['selected_tab']

#***************************************************************
# PROJECT TYPES
project_type_dir = {
    "E" : main_dir + '/' + project_types[0],
    "P" : main_dir + '/' + project_types[1],
    "S" : main_dir + '/' + project_types[2],
    "C" : main_dir + '/' + project_types[3]
}

for key, value in project_type_dir.items():
    if loaded_code_project.startswith(key):
        project_dir = value

project_type = project_dir.split('/')[-1]

# list of projects in type directory
projects_in_dir = os.listdir(project_dir)            # displayed in ui list

print(f'\nselected project dir:    {project_dir}\n') # eg:  F:/3D_Projects/5_PixelsAndCrafts/Props
print(f"project_type:    {project_type}")            # eg:  project_type:    Props
print(f'projects_in_dir:    {projects_in_dir}\n')    # eg:  projects_in_dir:    ['P_25_001__1970_ceramic_set']


#***************************************************************
# CHANGE PROJECT
# overwrite yml loaded project path with ui selected project path

# new loaded project based on selection in ui
project_data["loaded_project"] = projects_in_dir[0] # link to ui button to choose and load project\   "LOAD PROJECT" BUTTON

# update the yaml file
with open(yml_project_path, 'w') as outfile:
    yaml.dump(project_data, outfile) 


#***************************************************************
# INFO OF LOADED PROJECT FROM PROJECT.YML

# dir of the loaded project
loaded_project_path = project_dir + "/" + loaded_code_project

# loaded project name
loaded_project = loaded_code_project.split('__')[-1] # 1970_ceramic_set

# loaded project code
loaded_project_code = loaded_code_project.split('__')[0] # P_25_001

print(f"loaded project path: {loaded_project_path}")   # eg: loaded project path: F:/3D_Projects/5_PixelsAndCrafts/Props/P_25_001__1970_ceramic_set
print(f"loaded project name: {loaded_project}")        # eg: loaded project name: 1970_ceramic_set
print(f"loaded project code: {loaded_project_code}\n") # eg: loaded project code: P_25_001


#******************************************************************************************************************************
# FUNCTIONS

def version():
    # create base directory v01
    if not os.path.exists(os.path.join(loaded_project_path, 'marketplace', 'v01')):
        return os.path.join(loaded_project_path, 'marketplace', 'v01', marketplace_name) # marketplace/v01/{marketplace_name}

    # version up
    else:
        versions = os.listdir(os.path.join(loaded_project_path, 'marketplace'))

        last_version = max(sorted(versions))[1:]

        new_version = f'v{(int(last_version)+ 1):02d}'
        
        return os.path.join(loaded_project_path, 'marketplace', new_version, marketplace_name)

def all_directories():
            all_directories = []

            files_naming_list = ["/maya/" + files_naming["modeling"]["department"],
                                 "/maya/" + files_naming["baking"]["department"],
                                 "/maya/" + files_naming["grooming"]["department"],
                                 "/maya/" + files_naming["pose"]["department"],
                                 "/maya/" + files_naming["animation"]["department"],
                                 "/"      + files_naming["texturing"]["department"]
                                 ]

            ue_subfolders = ["/Meshes", "/Meshes/Blueprints", "/Textures/1k", "/Textures/2k", "/Textures/4k",]

            files_base = loaded_project_path + "/files/"
            ue_base = loaded_project_path + "/UE/"

            files_directories = []
            ue_directories = []

            if project_type == "Environment":


                for category in env_categories:
                    for name in files_naming_list:
                        file_path = files_base + category + name

                        files_directories.append(file_path)

                    for folder in ue_subfolders:
                        ue_path = ue_base + category + folder

                        ue_directories.append(ue_path)

            else:
                for name in files_naming_list:
                    file_path = files_base + name

                    files_directories.append(file_path)

                for folder in ue_subfolders:
                    ue_path = ue_base + folder

                    ue_directories.append(ue_path)


            marketplace_directories = [
                version() + '/' + f'{marketplace_name}_staticRender/LODs',
                version() + '/' + f'{marketplace_name}_staticRender/maya',
                version() + '/' + f'{marketplace_name}_staticRender/Textures',

                version() + '/' + f'{marketplace_name}_UE/Meshes/Blueprints',
                version() + '/' + f'{marketplace_name}_UE/Materials',
                version() + '/' + f'{marketplace_name}_UE/Textures/1k',
                version() + '/' + f'{marketplace_name}_UE/Textures/2k',
                version() + '/' + f'{marketplace_name}_UE/Textures/4k',

                version() + '/' + f'{marketplace_name}_UnrealEngine_Textures/1k',
                version() + '/' + f'{marketplace_name}_UnrealEngine_Textures/2k',
                version() + '/' + f'{marketplace_name}_UnrealEngine_Textures/4k'
            ]
              

            
            all_directories.append
            for directory in files_directories:
                all_directories.append(directory)

            for directory in ue_directories:
                all_directories.append(directory)
                
            for directory in marketplace_directories:
                all_directories.append(directory)

            return all_directories
          
def get_directory(filters):
    directories = all_directories()
    matched_directories = []
    
    for directory in directories:

        if all(f in directory for f in filters):  # if all the filters are in each directory
            matched_directories.append(directory)

            if matched_directories:
                return matched_directories
            
            else:
                print('No directories found')             
              
def create_directory(filters):
    matched_directories = get_directory(filters)
    for directory in matched_directories:
        if os.path.exists(directory):
            pass
        else:
            os.makedirs(directory)
            print('Directory created')

#******************************************************************************************************************************
# GET MAYA SCENES
def get_scenes(department, maya_task):
    scenes_directory = get_directory([department, maya_task])
    print(f'scenes_directory  {scenes_directory}')

    if scenes_directory:

        if 'maya' in department:
            folder_dir = scenes_directory[0] + '/' + f'{files_name}_{maya_task}_project/scenes'

            if os.path.exists(folder_dir):
                scenes_paths = []

                for obj in os.listdir(folder_dir):
                    scenes_paths.append(folder_dir + '/' + obj)

                # check if obj is a file scene
                all_scenes = []
                for scene in scenes_paths:
                    if os.path.isfile(scene):
                        all_scenes.append(scene)

                    else:
                        pass
                last_version_scene = max(sorted(all_scenes))
                return sorted(all_scenes, reverse=True), last_version_scene, folder_dir

            else:
                all_scenes = []
                last_version_scene = []
                return all_scenes, last_version_scene, folder_dir
                
        else:
            folder_dir = get_directory(["/files/", department])[0]

            print(f'folder_dir   {folder_dir}')

            if os.path.exists(folder_dir):
                scenes_paths = []

                for obj in os.listdir(folder_dir):
                    scenes_paths.append(folder_dir + '/' + obj)

                # check if obj is a file scene
                all_scenes = []
                for scene in scenes_paths:
                    if os.path.isfile(scene):

                        if 'texturing' in scene and not 'autosave' in scene:
                            all_scenes.append(scene)
                        else:
                            all_scenes.append(scene)
                    else:
                        pass

                last_version_scene = max(sorted(all_scenes))
                return all_scenes, last_version_scene, folder_dir
            
            else:
                all_scenes = []
                last_version_scene = []
                return all_scenes, last_version_scene, folder_dir

    else:
        return [], [], []


def assets_data():
        # folder with fbxs
        ue_meshes_dir = get_directory(["/UE/", "Meshes/"])[0]

        if ue_meshes_dir.endswith('Blueprints'):
            ue_meshes_dir = ('/').join(ue_meshes_dir.split('/')[:-1]).replace('//', '/')

        print(f'\nue_meshes_dir  {ue_meshes_dir}\n')

        if ue_meshes_dir:

            items_in_directory = os.listdir(ue_meshes_dir)
            bp_items_in_directory = os.listdir(ue_meshes_dir + '/Blueprints')
            
            # for unique assets
            assets_in_directory_path = []
            assets_in_directory = []


            for item in items_in_directory:
                item = ue_meshes_dir + "/" + item
                
                if os.path.isfile(item):
                    assets_in_directory_path.append(item)
                    assets_in_directory.append(item.split("/")[-1])

            # for blueprints
            # identified as folders starting with "BP"
            bp_assets_in_directory = []
            bp_assets_in_directory_path = []

            for item in bp_items_in_directory:
                item = ue_meshes_dir + '/Blueprints/' + item
                if not os.path.isfile(item):
                    bp_assets_in_directory_path.append(item)
                    bp_assets_in_directory.append(item.split("/")[-1])

            return assets_in_directory, assets_in_directory_path, bp_assets_in_directory, bp_assets_in_directory_path



#print(get_scenes('texturing', ''))
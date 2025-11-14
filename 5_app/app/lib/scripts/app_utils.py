"""
Content  : app utils

Date     : 2025-11-05

Author   : Elena Giuliani
email    : elenagiuliani94@outlook.it
"""


import os

import maya.cmds as cmds

#import yaml
from ruamel.yaml import YAML
yaml = YAML()
yaml.preserve_quotes = True

# current directory
CURRENT_DIR = os.path.dirname(__file__)


"""
WHY THE CONFIGURATION FILE WOULD IMPROVE THIS MODULE

The yaml file manages the project configuration all in one place.

The user can set a directory that will contain the projects.
If the user need to change a DCC (3dsMax instead of maya) or any category can overwrite the existing elements
(problem to update the ui? maybe not with classes)

Two variables of the yaml file will change when triggered by the ui inputs:   
- loaded_project      --> the project the user decides to work on                   
- marketplace_project --> the final name of the project to sell on marketplace
(can change without damaging linked files, like maya references)

"""
# path to projects yml
yml_project_path = os.path.join(CURRENT_DIR, '..', '..', 'config', 'projects', 'project.yml')

# load main paths
with open(yml_project_path, 'r', encoding='utf-8') as stream:
    project_data = yaml.load(stream)
main_path_dir = project_data['base_dir']

loaded_project = project_data['loaded_project']
marketplace_project = project_data['marketplace_project']

project_types = project_data['project_types']

env_categories = project_data['env_categories']
maya_tasks = project_data['maya_tasks']
softwares = project_data['softwares']

folders_ue = project_data['folders_ue']
texture_resolutions = project_data['texture_resolutions']
folders_static_render = project_data['folders_static_render']


# PROJECT TYPES
project_type_dir = {
    "environment_sets" : main_path_dir         + '/' + project_types[0],
    "props"            : main_path_dir         + '/' + project_types[1],
    "scans"            : main_path_dir         + '/' + project_types[2],
    "characters"       : main_path_dir         + '/' + project_types[3]
}

# DETERMINE project type by selecting an option (link a button to each indices of project_types variable)
"""
if loaded_project.startswith('E'):
    selected_project_type = project_type_dir['environment_sets']

if loaded_project.startswith('P'):
    selected_project_type = project_type_dir['props']

if loaded_project.startswith('S'):
    selected_project_type = project_type_dir['scans']

if loaded_project.startswith('C'):
    selected_project_type = project_type_dir['characters']
    """
selected_project_type = project_type_dir['props']
print(f'\nselected project type:    {selected_project_type}\n')     #eg:  F:/3D_Projects/5_PixelsAndCrafts/Props

project_type = selected_project_type.split('/')[-1]
print(f"project_type:    {selected_project_type.split('/')[-1]}")    # eg:  project_type:    Props

# list of projects in type directory
projects_in_dir = os.listdir(selected_project_type)      # displayed in ui list
print(f'projects_in_dir:    {projects_in_dir}\n')        # eg:  projects_in_dir:    ['P_25_001__1970_ceramic_set']

"""
#***************************************************************
# CHANGE PROJECT
# OVERWRITE YML LOADED PROJECT PATH WITH UI SELECTED PROJECT PATH
"""
# new loaded project based on selection in ui
project_data["loaded_project"] = projects_in_dir[0]    # link to ui button to choose and load project\   "LOAD PROJECT" BUTTON

# update the yaml file
with open(yml_project_path, 'w') as outfile:
    yaml.dump(project_data, outfile) 

"""
#***************************************************************
# INFO OF LOADED PROJECT FROM PROJECT.YML
"""
# dir of the loaded project
loaded_project_path = os.path.join(selected_project_type, loaded_project)

# loaded project name
loaded_project = loaded_project.split('__')[-1]

# loaded project code
loaded_project_code = loaded_project.split('__')[0]

print(f"loaded project path: {loaded_project_path}")    # eg:  loaded project path:    F:/3D_Projects/5_PixelsAndCrafts/Props/P_25_001__1970_ceramic_set
print(f"loaded project name: {loaded_project}")    # eg:  loaded project name:    1970_ceramic_set
print(f"loaded project code: {loaded_project_code}\n")  # eg:  loaded project code:    P_25_001



"""
WHY A CLASS WOULD IMPROVE THIS MODULE

- less lines of code
- extensible and flexible
- be sure that the class items are in the generated objects

************************************************
WHY CHILD CLASSES

- there is shared logic between the parent class and its child classes, where the parent class handles the main shared logic
- consistency between the objects and child classes as they share the same logic
- create objects that can manage a variety of items

************************************************
HOW IT WORKS
Three different but related systems for managing directory trees:   
- FilesDirectoryManager            --> contains the files that makes the assets
- UnrealEngineDirectoriesManager   --> contains the assets exported from files (eg: in fbx, png)
- MarketplaceDirectoryManager         --> contains the final assets after "publish" confirmation of the assets in UnrealEngineDirectories
                                       (uassets and fbx, for Unreal Engine or static render ends)
in short:  Files Directory --> Unreal Engine Directory (with manual import in engine)   -->   Marketplace Directory (files to sell on marketplace)

This way it is easy to add possible new directories and manage them

************************************************
WORKFLOW                                                       
Shared class functions:   
- filtered_directories  --> filters the list from assemble_directories keeping only the directories that match the keyword inserted
 in the parameter when creating the object
- create_directory --> used for creating directories when the project is set
- get_directory --> used to get the directories for exporting assets

Unique class functions in the child classes:    
assemble_directories  --> generate a list of all the directories expected
finalize  --> it access and executes the class functions in the parent class (filtered_directories and create_directory)

in short:   when creating an object --> assemble_directories -> finalize (filtered_directories -> create_directory)

#**********************************************
EXAMPLES

Return directory path for:
marketplace = MarketplaceDirectoryManager(folder_filter='meshes',  feedback_label='').get_directory()
output:
['F:/3D_Projects/5_PixelsAndCrafts/Props/P_25_001__1970_ceramic_set\\marketplace\\v04\\Fast and Furious\\Fast and Furious_UE\\Meshes']

Of all the paths in marketplace I get the one for Meshes like expected, because I applied to filter directories with "meshes" when crating the object.
Now I can use the path when exporting the fbx meshes.

#***************************************************************
# PARENT CLASS
# FOR CREATING DIRECTORY AND GETTING DIRECTORY PATH

loaded_project_path / custom_add
eg:   loaded_project_path = F:/3D_Projects/5_PixelsAndCrafts/Environment/E_25_002__The_Haunting_Of_Hill_House
      custom_add  = UE/Meshes
"""
class BaseDirectoryManager:
    def __init__(self, custom_add='', feedback_label=''):
        self.custom_add = [custom_add]
        self.feedback_label = feedback_label

    def assemble_directories(self):
        alldirs = []
        base_dir = loaded_project_path
        
        for d in self.custom_add:
            alldirs.append(os.path.join(base_dir, d))
        return alldirs, base_dir
    
    # filter directories
    def filtered_directories(self, filters):
        alldirs, base_dir = self.assemble_directories()

        matched = []
        for d in alldirs:
            rel = os.path.relpath(d, base_dir)     # os.path.relpath()  -->  rel:   maya\model

            parts = []
            for p in rel.split(os.sep):      # os.sep  -->  is the path separator character (windows: backslash \,  linux, unix, mac:forward /)
                if p:
                    parts.append(p.lower())

            skip = False                    # assumes there is a match
            for f in filters:
                if f and f not in parts:    # but if there is not a match
                    skip = True             # breaks the loop
                    break

            if not skip:                    # if there is a match append the matching directory
                matched.append(d)

        return matched

    #***************************************************************
    # CREATE THE DIRECTORIES
    def create_directory(self):
        filters = []

        if isinstance(self.custom_add, list):   # checks whether an object or variable is an instance of a specified type or class
            filters.extend(self.custom_add)   # adds elements individually
        else:
            filters.append(self.custom_add)   # adds single element
        self.custom_add = self.filtered_directories(filters)

        for d in self.custom_add:

            if not os.path.exists(d):
                os.makedirs(d)
                print(f'Folder {d} successfully created')
                self.feedback_label = f'Folder {d} successfully created'

            else:
                print(f'The {d} folder already exists')
                self.feedback_label = f'The {d} folder already exists'

        return self.custom_add

    #*****************************************************************************
    # RETURN THE DIRECTORY PATH
    def get_directory(self):
        filters = []

        if isinstance(self.custom_add, list):
            filters.extend(self.custom_add)   # adds elements individually
        else:
            filters.append(self.custom_add)   # adds single element
        self.custom_add = self.filtered_directories(filters)

        for d in self.custom_add:
            return self.custom_add
        
        

"""
#***************************************************************
# child class
# FOR "FILES" DIRECTORY
"""
class FilesDirectoryManager(BaseDirectoryManager):
    def __init__(self, env_category='architectural', software_filter='', maya_task_filter='', feedback_label=''):

        super(FilesDirectoryManager, self).__init__(feedback_label=feedback_label)

        self.software = software_filter.lower().strip()             # the strip() method removes any leading, and trailing whitespaces
        self.maya_task = maya_task_filter.lower().strip()
        self.env_category = env_category.lower().strip()

        # filters
        self.custom_add = [self.software, self.maya_task, self.env_category]

    def assemble_directories(self):
        alldirs = []
        base_dir = os.path.join(loaded_project_path, 'files')

        # if the project is an Environment
        if project_type == 'Environment':

            for category in env_categories:
                print('ENVIRONMENT')
                for sw in softwares:

                    if sw.lower() == 'maya':
                        maya_base = os.path.join(base_dir, category, 'maya')

                        for task in maya_tasks:
                            alldirs.append(os.path.join(maya_base, task))

                    else:
                        alldirs.append(os.path.join(base_dir, category, sw))

        # if project is Prop, 3D scan or Character
        else:
            print('NOT ENVIRONMENT')
            for sw in softwares:

                if sw.lower() == 'maya':
                    maya_base = os.path.join(base_dir, 'maya')

                    for task in maya_tasks:
                        alldirs.append(os.path.join(maya_base, task))

                else:
                    alldirs.append(os.path.join(base_dir, sw))

        return alldirs, base_dir


"""
#***************************************************************
# child class
# CREATE UNREAL ENGINE DIRECTORIES
"""
class UnrealEngineDirectoriesManager(BaseDirectoryManager):
    def __init__(self, sub_folder_filter='meshes', env_category='lamps', texture_res='2k', feedback_label=''):

        super(UnrealEngineDirectoriesManager, self).__init__(feedback_label=feedback_label)

        self.sub_folder_filter = sub_folder_filter.lower().strip()
        self.env_category = env_category.lower().strip()
        self.texture_res = texture_res.lower().strip()

        # filters
        self.custom_add = [self.sub_folder_filter, self.env_category, self.texture_res]

    def assemble_directories(self):
        alldirs = []
        base_dir = os.path.join(loaded_project_path, 'UE')

        # if the project is an Environment
        if project_type == 'Environment':
            print('ENVIRONMENT')
            for category in env_categories:

                meshes_ue_dir = os.path.join(base_dir, category, folders_ue[0])                         # UE/Architectural/Meshes
                alldirs.append(meshes_ue_dir)
                
                for res in texture_resolutions:                                               # UE/Architectural/Textures/1k
                    textures_dir = os.path.join(base_dir, category, folders_ue[2], res)
                    alldirs.append(textures_dir)

        # if project is Prop, 3D scan or Character
        else:
            print('NOT ENVIRONMENT')
            meshes_ue_dir = os.path.join(base_dir, folders_ue[0])                         # UE/Meshes
            alldirs.append(meshes_ue_dir)

            for res in texture_resolutions:
                textures_dir = os.path.join(base_dir, folders_ue[2], res)                 # UE/Textures/1k
                alldirs.append(textures_dir)

        return alldirs, base_dir
    

"""
#***************************************************************
# CREATE CGTRADER DIRECTORIES
"""
class MarketplaceDirectoryManager(BaseDirectoryManager):
    def __init__(self, folder_filter='meshes', texture_res='2k',  feedback_label=''):

        super(MarketplaceDirectoryManager, self).__init__(feedback_label=feedback_label)

        self.folder_filter = folder_filter.lower().strip()
        self.texture_res = texture_res.lower().strip()

        # filters
        self.custom_add = [self.folder_filter, self.texture_res]

    #******************************************************************
    def version(self):
        # create base directory v01
        if not os.path.exists(os.path.join(loaded_project_path, 'marketplace', 'v01')):
            return os.path.join(loaded_project_path, 'marketplace', 'v01', marketplace_project)      # marketplace/v01/{marketplace_project}

        # version up
        else:
            versions = max(sorted(os.listdir(os.path.join(loaded_project_path, 'marketplace'))))[1:]
            new_version = f'v{(int(versions)+ 1):02d}'
            return os.path.join(loaded_project_path, 'marketplace', new_version, marketplace_project)

    def assemble_directories(self):
        alldirs = []

        base_dir = self.version()
        marketplace_static = os.path.join(base_dir, f'{marketplace_project}_staticRender')           # marketplace/v01/{marketplace_project}/{marketplace_project}_staticRender
        marketplace_ue = os.path.join(base_dir, f'{marketplace_project}_UE')                         # marketplace/v01/{marketplace_project}/{marketplace_project}_UE

        #***************************************************************
        # {marketplace_project}_staticRender
        # directories for static renders (maya, 3ds max, etc)
        for folder in folders_static_render:
            alldirs.append(os.path.join(marketplace_static, folder))                                   # {marketplace_project}_staticRender/LODs

        for res in texture_resolutions:
            alldirs.append(os.path.join(marketplace_static, folders_ue[2], res))                   # {marketplace_project}_staticRender/Textures/1k
                
        #******************************************************************
        # {marketplace_project}_UE
        # directories for uassets
        for folder in folders_ue[0:2]:
            alldirs.append(os.path.join(marketplace_ue, folder))                                       # {marketplace_project}_UE/Meshes

        for res in texture_resolutions:
            alldirs.append(os.path.join(marketplace_ue, folders_ue[2], res))                       # {marketplace_project}_UE/Textures/1k

        #******************************************************************
        # {marketplace_project}_UnrealEngine_Textures
        # directories for textures png
        for res in texture_resolutions:
            alldirs.append(os.path.join(base_dir, f'{marketplace_project}_UnrealEngine_Textures', res))     # {marketplace_project}_UnrealEngine_Textures/1k
  
        return alldirs, base_dir


def open_software(software_filter, maya_task_filter):
    main_directory = FilesDirectoryManager('', software_filter, maya_task_filter).get_directory()
    if software_filter == 'maya':
        maya_scenes = []
        scene_directory = os.path.join(main_directory[0], str(loaded_project) + '_' + str(maya_task_filter) + '_project', 'scenes')
        
        for scene in os.listdir(scene_directory):
            if '.ma' in scene:
                if scene.split('.')[-2].isdigit():
                    maya_scenes.append(scene)
        scene_path = os.path.join(scene_directory, max(sorted(maya_scenes)))
        cmds.file(path = scene_path, open=True)
        print(f'scene directory:   {scene_path}')
        print('sono maya')
            
#***************************************************************************************************************************************
# TEST

#print(loaded_project)

#--------------------------------------------
#USE PARENT CLASS
# use the parent class to create a single directory with custom name
"""
refs = BaseDirectoryManager(custom_add='refs', feedback_label='').get_directory()
print(f'\nrefs:  {refs}\n')
#--------------------------------------------
# USE CHILD CLASSES
# create/get marketplace directories
marketplace = MarketplaceDirectoryManager(folder_filter='textures', texture_res='2k',  feedback_label='').get_directory()
print(f'\nmarketplace filtered dirs:\n{marketplace}\n')

"""
# create/get files directories
files = FilesDirectoryManager(env_category='', software_filter='maya', maya_task_filter='model').get_directory()
print(f'\nfiles filtered dirs:\n{files}\n')

open_software('maya', 'model')
"""
# create/get ue directories
ue = UnrealEngineDirectoriesManager(sub_folder_filter='textures', env_category='architectural').get_directory()
print(f'\nunreal engine filtered dirs:\n{ue}\n')

"""


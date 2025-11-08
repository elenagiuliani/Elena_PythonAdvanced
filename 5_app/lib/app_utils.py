"""
***************************************************************
***************************************************************
Content  : app utils

Date     : 2025-11-05

Author   : Elena Giuliani
email    : elenagiuliani94@outlook.it
***************************************************************
***************************************************************
"""
import os

#import yaml
from ruamel.yaml import YAML
yaml = YAML()
yaml.preserve_quotes = True

# current directory
CURRENT_DIR = os.path.dirname(__file__)

# path to projects yml
YML_MAIN_PATH = os.path.join(CURRENT_DIR, 'config', 'projects', 'project.yml')

# load main paths
with open(YML_MAIN_PATH, 'r', encoding='utf-8') as stream:
    main_data = yaml.load(stream)
PIXELSANDCRAFTS_DIR = main_data['PixelsAndCrafts']
loaded_project_full_name = main_data['selected_project']
#************************************************


# keep these updated to add/remove software or maya tasks
env_categories = ['Architectural', 'Props', 'Lamps', '']
maya_tasks = ['model', 'baking', 'rig', 'pose', 'anim']
softwares = ['maya', 'SP', 'ZB', 'SD', 'RealityScan']


# CGTRADER
sub_folders_static_render = ['LODs', 'maya']
shader_types = ['Textures/RoughMetal', 'Textures/UnrealEngine']
texture_resolutions = ['1k', '2k', '4k']

sub_folders_ue = ['Meshes', 'Materials']


# PROJECT TYPES
project_types = ['Environment', 'Props', '3Dscans', 'Characters']      # in ui button list











#************************************************
# PROJECT TYPES
project_type_dir = {
    "environment_sets"   : PIXELSANDCRAFTS_DIR         + '/' + project_types[0],
    "props"              : PIXELSANDCRAFTS_DIR         + '/' + project_types[1],
    "scans"              : PIXELSANDCRAFTS_DIR         + '/' + project_types[2],
    "characters"         : main_data["Characters"]     + '/' + project_types[3]
}
#************************************************
# DETERMINE project type by selecting an option (link a button to each indices of project_types variable)
selected_project_type = project_type_dir['environment_sets']          # link to ui button to load project
print(f'\nselected project type:    {selected_project_type}\n')     #eg:  F:/3D_Projects/5_PixelsAndCrafts/Props



project_type = selected_project_type.split('/')[-1]
print(f"project_type:    {selected_project_type.split('/')[-1]}")    # eg:  project_type:    Props



# list of projects in type directory
projects_in_dir = os.listdir(selected_project_type)      # displayed in ui list
print(f'projects_in_dir:    {projects_in_dir}\n')        # eg:  projects_in_dir:    ['P_25_001__1970_ceramic_set']




"""
#***************************************************************
#***************************************************************
# CHANGE PROJECT
# OVERWRITE YML LOADED PROJECT PATH WITH UI SELECTED PROJECT PATH
#***************************************************************
#***************************************************************
"""
# selected project
main_data["selected_project"] = projects_in_dir[1]    # link to ui button to choose and load project\   "LOAD PROJECT" BUTTON
with open(YML_MAIN_PATH, 'w') as outfile:
    yaml.dump(main_data, outfile)



"""
#***************************************************************
#***************************************************************
# INFO OF LOADED PROJECT FROM PROJECT.YML
#***************************************************************
#***************************************************************
"""
# dir of the loaded project
loaded_project_path = f'{selected_project_type}/{loaded_project_full_name}'

# loaded project name
loaded_project_name = loaded_project_full_name.split('__')[-1]

# loaded project code
loaded_project_code = loaded_project_full_name.split('__')[0]

print(f"loaded project path:    {loaded_project_path}")    # eg:  loaded project path:    F:/3D_Projects/5_PixelsAndCrafts/Props/P_25_001__1970_ceramic_set
print(f"loaded project name:    {loaded_project_name}")    # eg:  loaded project name:    1970_ceramic_set
print(f"loaded project code:    {loaded_project_code}\n")  # eg:  loaded project code:    P_25_001












"""
#***************************************************************
#***************************************************************
# FOR FILES DIR
# MAKE DIRECTORIES OR GET DIRECTORY PATH
#***************************************************************
#***************************************************************
"""

class PipelineDirectoryManager:
    def __init__(self, env_category='', software='', maya_task='', feedback_label='', make_dir=False):
        # normalized filters
        self.env_category = env_category.lower().strip()       # the strip() method removes any leading, and trailing whitespaces
        self.software = software.lower().strip()
        self.maya_task = maya_task.lower().strip()

        self.feedback_label = feedback_label
        self.make_dir = make_dir

#***************************************************************
        # command
        self.dirs = self.process_directories()

    def assemble_directories(self):
        base_dir_files = os.path.join(loaded_project_path, 'files')
        alldirs = []

        for category in env_categories:
            if self.env_category != '':
                for sw in softwares:
                    if sw.lower() == 'maya':
                        if category:
                            maya_base = os.path.join(base_dir_files, category, 'maya')
                        else:
                            maya_base = os.path.join(base_dir_files, 'maya')
                        for task in maya_tasks:
                            alldirs.append(os.path.join(maya_base, task))
                    else:
                        if category:
                            dir_path = os.path.join(base_dir_files, category, sw)
                        else:
                            dir_path = os.path.join(base_dir_files, sw)
                        alldirs.append(dir_path)
            else:
                print('\nNOT CATEGORY')
                for sw in softwares:
                    if sw.lower() == 'maya':
                        maya_base = os.path.join(base_dir_files, 'maya')
                        for task in maya_tasks:
                            alldirs.append(os.path.join(maya_base, task))
                    else:
                        dir_path = os.path.join(base_dir_files, sw)
                        alldirs.append(dir_path)

        return alldirs, base_dir_files

    # filter dirs
    def filtered_dirs(self):
        alldirs, base_dir_files = self.assemble_directories()
        print(f'base:   {base_dir_files}')
        
        matched = []
        for d in alldirs:
            # used Copilot! Review this part
            rel = os.path.relpath(d, base_dir_files)
            parts = [p.lower() for p in rel.split(os.sep) if p]
            #print(f'parts:   {parts}\n')

            if self.env_category and self.env_category not in parts:
                continue
            if self.software and self.software not in parts:
                continue
            if self.maya_task and self.maya_task not in parts:
                continue

            matched.append(d)
        return matched

#***************************************************************
#***************************************************************
    # COMMAND MAKE DIRS OR GET DIR PATH
    def process_directories(self):
        final_dirs = self.filtered_dirs()

        #print(f'\nfinal dirs:   {final_dirs}')
#*****************************************************************************
        # MAKE THE DIRECTORIES
        if self.make_dir == True:

            for d in final_dirs:
                if not os.path.exists(d):
                    os.makedirs(d)
                    print(f'Folder {d} successfully created')
                    self.feedback_label = f'Folder {d} successfully created'

                else:
                    print(f'The {d} folder already exists')
                    self.feedback_label = f'The {d} folder already exists'

            return final_dirs

#*****************************************************************************
        # RETURN THE DIRECTORY PATH
        else:
            print(f'\nlength:    {len(final_dirs)}')
            if len(final_dirs) == 1:
                return final_dirs



"""
#***************************************************************
#***************************************************************
# MAKE UE DIRECTORIES
#***************************************************************
#***************************************************************
"""
class MakeUEDirectories:
    def __init__(self, make_dir=False):

        self.make_dir = make_dir

        # command
        self.dirs = self.process_directories()

    def assemble_ue_dirs(self):
        base_dir_ue = os.path.join(loaded_project_path, 'UE')

        alldirs = []

        # if the project is an Environment
        if project_type == 'Environment':

            for category in env_categories:
                if category != '':

                    meshes_ue_dir = os.path.join(base_dir_ue, category, 'Meshes')
                    alldirs.append(meshes_ue_dir)
                    
                    for res in texture_resolutions:
                        new = os.path.join(base_dir_ue, category, 'Textures', res)
                        alldirs.append(new)

        # if project is Prop, 3D scan or Character
        else:

            meshes_ue_dir = os.path.join(base_dir_ue, 'Meshes')
            alldirs.append(meshes_ue_dir)

            for res in texture_resolutions:
                new = os.path.join(base_dir_ue, 'Textures', res)
                alldirs.append(new)

        return alldirs

#*****************************************************************************
#*****************************************************************************
    def process_directories(self):
        final_dirs = self.assemble_ue_dirs()
        #print(f'\nfinal dirs:   {final_dirs}')

        # MAKE THE DIRECTORIES
        if self.make_dir == True:

            for d in final_dirs:
                if not os.path.exists(d):
                    os.makedirs(d)
                    print(f'Folder {d} successfully created')
                    self.feedback_label = f'Folder {d} successfully created'

                else:
                    print(f'The {d} folder already exists')
                    self.feedback_label = f'The {d} folder already exists'

            return final_dirs

#*****************************************************************************
        # RETURN THE DIRECTORY PATH
        else:
            for d in final_dirs:
                if os.path.exists(d):
                    print(f'\nlength:    {len(final_dirs)}')
                    return final_dirs
                else:
                    print('Directories do not exist')




"""
#***************************************************************
#***************************************************************
# MAKE CGTRADER DIRECTORIES
#***************************************************************
#***************************************************************
"""
# obsolete (keep for now)
def make_textures_res_dirs(base):
    alldirs = []
    for shader_type in shader_types:
        for res in texture_resolutions:
            new = os.path.join(base, shader_type, res)
            alldirs.append(new)
    return alldirs


def make_cgtrader_base_dirs():
    # create directories for cgtrader
    if not os.path.exists(os.path.join(loaded_project_path, 'cgtrader', 'v01')):
        cgtrader_base = os.path.join(loaded_project_path, 'cgtrader', 'v01', loaded_project_name)

    # version up
    else:
        versions = max(sorted(os.listdir(os.path.join(loaded_project_path, 'cgtrader'))))[1:]
        new_version = f'v{(int(versions)+ 1):02d}'
        cgtrader_base = os.path.join(loaded_project_path, 'cgtrader', new_version, loaded_project_name)
    return cgtrader_base

#************************************************
#************************************************
# COMMAND FOR CREATING DIRECTORIES
def make_cgtrader_dirs():             # to assign to ui button
    new_dirs = []    
    cgtrader_base = make_cgtrader_base_dirs()

    cgtrader_static = os.path.join(cgtrader_base, f'{loaded_project_name}_staticRender')
    cgtrader_ue = os.path.join(cgtrader_base, f'{loaded_project_name}_UE')

    # directories for cgtrader static renders (DCC)
    for folder in sub_folders_static_render:

        new_dirs.append(os.path.join(cgtrader_static, folder))


    for res in texture_resolutions:
        new_dirs.append(os.path.join(cgtrader_static, 'Textures', 'RoughMetal', res))
            


#******************************************************************
    # directories for cgtrader Unreal Engine
    for folder in sub_folders_ue:
        new_dirs.append(os.path.join(cgtrader_ue, folder))

    for res in texture_resolutions:
        new_dirs.append(os.path.join(cgtrader_ue, 'Textures', res))

    for res in texture_resolutions:
        new_dirs.append(os.path.join(cgtrader_base, f'{loaded_project_name}_UnrealEngine_Textures', res))

    for d in new_dirs:
        print(d)
        os.makedirs(d)





#make_cgtrader_dirs()


# Example usage for ui        --> link buttons to open specific project file 
#arch = PipelineDirectoryManager(env_category='architectural', software='', maya_task='')
#print(f"\narch directories: {arch.dirs}")

props = PipelineDirectoryManager(env_category='props', software='', maya_task='', make_dir=True)
print(f"\nprops directories: {props.dirs}")

#lamps = PipelineDirectoryManager(env_category='lamps', software='', maya_task='')
#print(f"\narch directories: {lamps.dirs}")

#generic = PipelineDirectoryManager(env_category='props', software='', maya_task='')
#print(f"\narch directories: {generic.dirs}")

#PipelineDirectoryManager(env_category='props', software='maya', maya_task='', make_dir=True)  

#PipelineDirectoryManager(env_category='props', software='SP', maya_task='', make_dir=False)





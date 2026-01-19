"""
Content  : Maya functions for the shelf buttons

Date     : 2025-12-03

license  : MIT
Author   : Elena Giuliani
email    : elenagiuliani94@outlook.it
"""
import os
import sys
import subprocess
import maya.mel as mel
import maya.cmds as cmds

CURRENT_DIR = os.path.dirname(__file__)
ROOT_DIR = '\\'.join(CURRENT_DIR.split('\\')[:-4])
sys.path.append(ROOT_DIR)

from Git_PackForge_Pipeline.library.appdata import ENV_CATEGORIES, load_config_data, restart_app_bat

(projects_root, project_root, loaded_project, loaded_project_path, loaded_project_name, project_type, 
 files_name, marketplace_name, selected_tab, screenshot_dir_base, project_path) = load_config_data()


def scene_data():
    current_scene_path = cmds.file(query=True, sceneName=True)
    file_dir = os.path.dirname(current_scene_path)
    file_name = os.path.basename(os.path.splitext(current_scene_path)[0])
    file_extension = os.path.splitext(current_scene_path)[-1]

    # find directory for Unreal meshes
    if 'Environment' in current_scene_path:
        for category in ENV_CATEGORIES:
            if category in current_scene_path:
                asset_dir =  project_root + '/UE/' + category + '/Meshes'
    else:
        asset_dir = project_root + '/UE/Meshes'

    return current_scene_path, file_dir, file_name, asset_dir, file_extension


def take_screenshot(screenshot_path):
    cmds.playblast(completeFilename=screenshot_path,
                    format='image',
                    width=1920,
                    height=1080,
                    showOrnaments=True,
                    framePadding=0,
                    viewer=False,
                    startTime=1,
                    endTime=1)


def press_btnIncrementSave(save_type):
    current_scene_path, file_dir, file_name_full, _, file_extension = scene_data()
    file_name_full_split = file_name_full.split('_')
    file_name = ('_').join(file_name_full_split[:-1])
    file_version = file_name_full_split[-1][1:]

    screenshot_dir = screenshot_dir_base + '/files/'
    if project_type == 'Environment':
        for category in ENV_CATEGORIES:
            if category in current_scene_path:
                screenshot_dir = screenshot_dir + category

    if save_type == 'increment':
        new_file_name_path = f"{file_dir}/{file_name}_v{int(file_version) + 1:03d}{file_extension}"
        new_screenshot_name = os.path.basename(new_file_name_path).split('.')[0]
        screenshot_path = screenshot_dir + '/' + new_screenshot_name + '_000.png'
    else:
        new_file_name_path = current_scene_path
        new_screenshot_name = os.path.basename(new_file_name_path).split('.')[0]
        existing_versions = []
        for root, dirs, files in os.walk(screenshot_dir):
            for file in files:
                if file.startswith(new_screenshot_name):
                    existing_versions.append(int(file.split('.')[0].split('_')[-1]))
        if existing_versions:
            screenshot_path = f"{screenshot_dir}/{new_screenshot_name}_{max(existing_versions) + 1:03d}.png"
        else:
            screenshot_path = f"{screenshot_dir}/{new_screenshot_name}_000.png"

    cmds.file(rename=new_file_name_path)
    cmds.file(save=True, type='mayaAscii')

    if not os.path.exists(screenshot_dir):
        os.makedirs(screenshot_dir)

    # take screenshot of the viewport
    take_screenshot(screenshot_path)


# **************************************************************************************************
def versioning_screenshot(base_name, screenshot_dir):
    base_path = f"{screenshot_dir}/{base_name}.png"
    versioned = []
    for screens in os.listdir(screenshot_dir):
        if screens.startswith(base_name + '_') and screens.endswith('.png'):
            version = screens.split("_")[-1].split(".")[0]
            if version.isdigit() and len(version) == 3:
                versioned.append(int(version))

    # only BP_door.png
    if os.path.exists(base_path) and not versioned:
        new_path = f"{screenshot_dir}/{base_name}_001.png"
        os.rename(base_path, new_path)
        return base_path  # new screenshot: BP_door.png

    # BP_door_001.png
    if versioned:
        new_version = max(versioned) + 1
        return f"{screenshot_dir}/{base_name}_{new_version:03d}.png"

    # no screenshot exists
    return base_path


# take screenshot of selected asset
def press_btnScreenshot():
    selected = cmds.ls(selection=True)
    if len(selected) > 1:
        return
    if not selected:
        return
    if not (selected[0].startswith('SM') or selected[0].startswith('BP')):
        return
    
    def _find_bp_parent(node):
        parent = cmds.listRelatives(node, parent=True)
        print(f'parent:  {parent}')
        if parent:
            if parent[0].startswith('BP'):
                return parent
            else:
                return None

    # create screenshot_dir
    if selected[0].startswith('SM'):
        parent = _find_bp_parent(selected[0])
        if parent:
            screenshot_dir = f'{screenshot_dir_base}/assets/{parent}'
        else:
            screenshot_dir = f'{screenshot_dir_base}/assets/{selected[0]}'
    else:
        screenshot_dir = f'{screenshot_dir_base}/assets/{selected[0]}'

    if not os.path.isdir(screenshot_dir):
        os.makedirs(screenshot_dir)

    # find active viewport
    current_panel = cmds.getPanel(withFocus=True)
    if current_panel == 'outlinerPanel1':
        current_panel = 'modelPanel4'

    def _take_mesh_screenshot(obj_name):
        obj = obj_name
        screenshot_path = versioning_screenshot(obj_name, screenshot_dir)
        cmds.isolateSelect(current_panel, state=1)
        cmds.isolateSelect(current_panel, addSelected=True)
        cmds.refresh(force=True)

        cmds.select(clear=True)
        take_screenshot(screenshot_path)
        cmds.select(obj)

        cmds.isolateSelect(current_panel, state=0)

    if selected[0].startswith('SM'):
        _take_mesh_screenshot(selected[0].split('.')[0])

    elif selected[0].startswith('BP'):
        _take_mesh_screenshot(selected[0])
        bp_static_meshes = cmds.listRelatives(selected[0], children=True)
        if bp_static_meshes:
            for static_mesh in bp_static_meshes:
                if cmds.getAttr(f'{static_mesh}.visibility'):
                    cmds.select(clear=True)
                    cmds.select(static_mesh)
                    _take_mesh_screenshot(static_mesh)
    cmds.select(selected)


# EXPORT'S PRIVATE FUNCTIONS ***********************************************************************
def _configure_file_extension(file_extension):
    if file_extension == 'fbx':
        mel.eval("FBXExportTangents -v true")
        mel.eval("FBXExportTriangulate -v false")
        mel.eval("FBXExportSmoothingGroups -v true")
        export_options = 'v=0;'
        return 'FBX export', export_options
    elif file_extension == 'obj':
        export_obj_options_groups = 'groups=1;'
        export_obj_options_triangulate = 'tri=0;'
        export_obj_options_normals = 'normals=1;'
        export_obj_options_materials = 'materials=0;'
        export_obj_options_smoothing_groups = 'smoothing=1;'
        export_options = f'{export_obj_options_groups}{export_obj_options_materials}{export_obj_options_smoothing_groups}{export_obj_options_normals}{export_obj_options_triangulate}'
        return 'OBJexport', export_options
    else:
        print('<<<<<<<<<<<<<<< file type not supported')
        

# return a list of selected objs or all objs in outliner
def _objects_to_export():
    selected = cmds.ls(selection=True)
    if selected:
        return selected
    else:
        print('<<<<<<<<<<<<<<< No objects selected')


# check if obj is group
def _is_group_with_one_child(obj):
    children = cmds.listRelatives(obj, children=True, type='transform')
    if children:
        for child in children:
            if not cmds.getAttr(f'{child}.visibility'):
                children.remove(child)
        if len(children) == 1:
            return True, True, children
        else:
            return True, False, children
    else:
        return False, False, children


def _combine_group(to_combine):
    to_combine_temp = to_combine + '_temp'
    cmds.rename(to_combine, to_combine_temp)
    to_combine_children = cmds.listRelatives(to_combine_temp, children=True, type='transform')
    visible_meshes = []
    if len(to_combine_children) > 1:
        for obj in to_combine_children:
            if cmds.getAttr(f'{obj}.visibility'):
                visible_meshes.append(obj)
        combined, _ = cmds.polyUnite(visible_meshes, name=to_combine, mergeUVSets=2)
        cmds.delete(combined, constructionHistory=True)
        obj = combined
    return obj


def _is_child_of_world(obj):
    long_path = cmds.ls(obj, long=True)[0]
    if long_path.count('|') == 1:
        return True
    else:
        return False


# EXPORT SM OR SKM *********************************************************************************
def press_btnExportMesh():
    _, _, _, asset_dir, _ = scene_data()
    export_paths = []
    if len(_objects_to_export()) == 1:
        press_btnScreenshot()
    selected = _objects_to_export()

    cmds.undoInfo(openChunk=True)
    try:
        for obj in _objects_to_export():
            cmds.move(0, 0, 0, obj, absolute=True, worldSpace=True)
            is_group, has_one_child, children = _is_group_with_one_child(obj)

            if obj.startswith('SM'):
                if not is_group:
                    if not _is_child_of_world(obj):
                        cmds.parent(obj, world=True)
                    final_obj = obj
                else:
                    if has_one_child:
                        if not children[0].startswith('SM'):
                            new_name_child = 'SM_' + obj
                            cmds.rename(children[0], new_name_child)

                        cmds.move(0, 0, 0, new_name_child, absolute=True, worldSpace=True)
                        cmds.parent(new_name_child, world=True)
                        final_obj = new_name_child
                    else:
                        final_obj = _combine_group(obj)
                export_paths.append(asset_dir + '/' + final_obj)
            elif obj.startswith('BP'):
                bp_dir = asset_dir + '/Blueprints/' + obj
                if not os.path.exists(bp_dir):
                    os.makedirs(bp_dir)
                if is_group:
                    for child in children:
                        if child.startswith('SM'):
                            cmds.select(child)
                            press_btnScreenshot()
                            cmds.select(selected)
                            cmds.move(0, 0, 0, child, absolute=True, worldSpace=True)
                            cmds.parent(child, world=True)
                            final_obj = child
                            export_paths.append(bp_dir + '/' + final_obj)
            elif not obj.startswith('SM', 'BP'):
                print(f'<<<<<<<<<<<<<<< Assign a prefix')

        file_extension, export_options = _configure_file_extension('fbx')
        for path in export_paths:
            node = os.path.basename(path)
            cmds.select(node, replace=True)
            cmds.file(path, options = export_options, type = file_extension, pr=True, es=True)

    finally:
        cmds.undoInfo(closeChunk=True)
    cmds.undo()


def add_remove_prefixes(prefix):
    for obj in _objects_to_export():
        if not prefix in obj:
            if not len(obj.split('_')) == 1:
                old_name = obj
                new_name = prefix + '_' + old_name
                if new_name[-1].isdigit():
                    new_name = '_'.join(new_name.split('_')[:-1])
                cmds.rename(old_name, new_name)
        else:
            obj_split = obj.split('_')
            obj_split.remove(prefix)
            new_name = '_'.join(obj_split)
            cmds.rename(obj, new_name)


def fix_names():
    selected = cmds.ls(selection=True)[0]
    if not selected:
        print('<<<<<<<<<<<<<<< select something')
    if not selected.startswith('SM') and not selected.startswith('BP'):
        print('<<<<<<<<<<<<<<< invalid selection')
        return

    children = cmds.listRelatives(selected, children=True, fullPath=True)
    number = 0
    for child in children:
        if cmds.getAttr(f'{child}.visibility'):
            if 'SM' in selected:
                new_name = f"{'_'.join(selected.split('_')[1:])}_{int(number) + 1}"
            if 'BP' in selected:
                new_name = f"SM_{'_'.join(selected.split('_')[1:])}_{int(number) + 1}"
            cmds.rename(child, new_name)

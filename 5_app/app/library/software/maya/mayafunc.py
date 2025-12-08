"""
Content  : Maya functions for the shelf buttons

Date     : 2025-12-03

Author   : Elena Giuliani
email    : elenagiuliani94@outlook.it
"""
import os
import sys
import maya.mel as mel
import maya.cmds as cmds

# module path
CURRENT_DIR = os.getcwd()
sys.path.append(CURRENT_DIR)

# current maya scene path
scene_path = cmds.file(query=True, sceneName=True)

env_categories = ['Architectural', 'Props', 'Lamps']

def file_data():
    scene_path = cmds.file(query=True, sceneName=True)
    file_dir = os.path.dirname(scene_path)
    file_name = os.path.basename(os.path.splitext(scene_path)[0])
    file_type = os.path.splitext(scene_path)[-1]

    if 'Environment' in scene_path:
        project_type = 'Environment'
        for category in env_categories:
            if category in scene_path:
                asset_dir =  ('/').join(file_dir.split('/')[:-6]) + '/UE/' + str(category) + '/Meshes'

    else:
        project_type = 'other'
        asset_dir = ('/').join(file_dir.split('/')[:-5]) + '/UE/Meshes'

    return scene_path, file_dir, file_name, asset_dir, file_type, project_type


def press_btnIncrementSave():
    scene_path, file_dir, file_name_full, _, file_type, project_type = file_data()

    file_name_full_split = file_name_full.split('_')
    file_name = ('_').join(file_name_full_split[:-1])
    file_version = file_name_full_split[-1][1:]

    if project_type == 'Environment':
        if 'Architectural' in scene_path:
            screenshot_dir = ('/').join(file_dir.split('/')[:-6]) + '/screenshots/Architectural/files/maya/'
        if 'Props' in scene_path:
            screenshot_dir = ('/').join(file_dir.split('/')[:-6]) + '/screenshots/Props/files/maya/'
        if 'Lamps' in scene_path:
            screenshot_dir = ('/').join(file_dir.split('/')[:-6]) + '/screenshots/Lamps/files/maya/'

        new_file_name_path = f"{file_dir}/{file_name}_v{int(file_version) + 1:03d}{file_type}"

    else:
        screenshot_dir = ('/').join(file_dir.split('/')[:-5]) + '/screenshots/files/maya/'
        new_file_name_path = f"{file_dir}/{file_name}_v{int(file_version) + 1:03d}{file_type}"

    cmds.file(rename=new_file_name_path)
    cmds.file(save=True, type='mayaAscii')

    if not os.path.exists(screenshot_dir):
        os.makedirs(screenshot_dir)

    # take screenshot of the viewport
    screenshot_path = screenshot_dir + new_file_name_path.split('/')[-1] + '.png'
    cmds.playblast(completeFilename=screenshot_path,
                    format='image',
                    width=1920,
                    height=1080,
                    showOrnaments=False,
                    framePadding=0,
                    viewer=False,
                    startTime=1,
                    endTime=1)


# take screenshot of selected asset
def press_btnScreenshot():
    _, _, _, _, _, project_type = file_data()
    selected = cmds.ls(selection=True)
    if selected:
        if selected[0].startswith('SM') or selected[0].startswith('BP'):
            _, file_dir, _, _, _, _ = file_data()

            if project_type == 'Environment':
                screenshot_dir = ('/').join(file_dir.split('/')[:-6]) + '/screenshots/assets/' + selected[0]
            else:
                screenshot_dir = ('/').join(file_dir.split('/')[:-5]) + '/screenshots/assets/' + selected[0]

            if not os.path.isdir(screenshot_dir):
                os.makedirs(screenshot_dir)

            # isolate selected
            current_panel = cmds.getPanel(withFocus=True)
            cmds.isolateSelect(current_panel, state=1)
            cmds.isolateSelect(current_panel, addSelected=True)

            # deselect
            cmds.select(clear=True)

            # take screenshot
            screenshot_path = f"{screenshot_dir}/{selected[0].split('.')[0]}.png"
            cmds.playblast(completeFilename=screenshot_path,
                            format='image',
                            width=1920,
                            height=1080,
                            showOrnaments=False,
                            framePadding=0,
                            viewer=False,
                            startTime=1,
                            endTime=1)

            # exit isolate select
            cmds.isolateSelect(current_panel, state=0)
        else:
            print('\nSelect an asset starting with "SM" to take screenshot')
    else:
        print('\nNo object selected')

#***************************************************************
# EXPORT PRIVATE FUNCTIONS
def _configure_file_type(file_type):
    file_type = file_type.upper()

    if file_type == 'FBX':
        mel.eval("FBXExportTangents -v true")
        mel.eval("FBXExportTriangulate -v false")
        mel.eval("FBXExportSmoothingGroups -v true")
        export_options = 'v=0;'

        return 'FBX export', export_options
    
    elif file_type == 'OBJ':
        export_obj_options_groups = 'groups=1;'
        export_obj_options_triangulate = 'tri=0;'
        export_obj_options_normals = 'normals=1;'
        export_obj_options_materials = 'materials=0;'
        export_obj_options_smoothing_groups = 'smoothing=1;'
        export_options = f'{export_obj_options_groups}{export_obj_options_materials}{export_obj_options_smoothing_groups}{export_obj_options_normals}{export_obj_options_triangulate}'

        return 'OBJexport', export_options
    else:
        print('file type not supported')
        

# return a list of selected objs or all objs in outliner
def _objects_to_export():
    selected = cmds.ls(selection=True)
    if selected:
        meshes = selected

        meshes_to_export = []
        for obj in meshes:
            mesh_shape = cmds.listRelatives(obj, shapes=True)

            if cmds.nodeType(mesh_shape) == 'mesh' or mesh_shape is None:
                meshes_to_export.append(obj)

        return meshes_to_export
    else:
        print('No objects selected')


# check if obj has a skin cluster
def _has_skin_cluster(obj):
    history = cmds.listHistory(obj)
    for node in history:
        if cmds.nodeType(node) == 'skinCluster':
            return True
    return False


# check if obj is group
def _is_group(obj):
    if cmds.objectType(obj) != 'transform':
        return True
    shapes = cmds.listRelatives(obj, shapes=True)
    if not shapes:
        return True
    else:
        return False

#***************************************************************
# EXPORT SM OR SKM
def press_btnExportMesh():
    scene_path, _, _, asset_dir, _, project_type = file_data()

    for obj in _objects_to_export():

        # IF SKELETAL MESH
        if _has_skin_cluster(obj):
            if not obj.startswith('SKM_'):
                print(f'SKIP exporting {obj}: not starting with "SKM_"')
                continue

            skin_clusters = cmds.ls(cmds.listHistory(obj), type='skinCluster')
            influences = cmds.skinCluster(skin_clusters[0], query=True, influence=True)
            
            # select joints
            cmds.select(influences, add=True)

        # IF STATIC MESH
        else:
            if not obj.startswith('SM_') and not obj.startswith('BP_'):
                print(f'SKIP exporting {obj}: not starting with "SM" or "BP"')
                continue

        #***************************************************************
        # IF GROUP
        visible_children = []
        prefix_children = []
        if _is_group(obj):
            obj_children = cmds.listRelatives(obj, children=True, fullPath=False, type='transform')

            # find visible children with SM_ or SKM_ prefix
            for child in obj_children:
                if cmds.getAttr(f'{child}.visibility'):
                    visible_children.append(child)

            if not visible_children:
                print(f'SKIP exporting {child}: no visible children found')
                continue    

            # find children with SM_ or SKM_ prefix
            for child in visible_children:
                if child.startswith('SM_') or child.startswith('SKM_'):
                    prefix_children.append(child)

            # create Blueprints folder if not exists
            if obj.startswith('BP_'):
                bp_dir = asset_dir + '/Blueprints/' + obj
                if not os.path.exists(bp_dir):
                    os.makedirs(bp_dir)

                for child in prefix_children:
                    cmds.parent( child, world=True)
                to_export = prefix_children


            elif obj.startswith('SM_'):
                if len(visible_children) > 1:
                    cmds.move(0, 0, 0, obj, absolute=True, worldSpace=True)
                    
                    combined, _ = cmds.polyUnite(visible_children, name=obj)
                    final = cmds.duplicate(combined, name=obj + "_final")[0]
                    cmds.delete(combined)
                    to_export = [final]

                else:
                    to_export = []
                    cmds.parent( visible_children[0], world=True)
                    cmds.move(0, 0, 0, visible_children[0], absolute=True, worldSpace=True)
                    to_export.append(cmds.rename(visible_children[0], obj))

        # IF SINGLE MESH
        else:
            to_export = []
            cmds.makeIdentity(obj, apply=False, t=True, r=True, s=True)

            if cmds.listRelatives(obj, parent=True):
                cmds.parent( obj, world=True)

            to_export.append(obj)

        #***************************************************************
        # EXPORT
        file_type, export_options = _configure_file_type('FBX')
        if obj.startswith('BP_'):
            for child in to_export:
                cmds.select(child, replace=True)

                cmds.move(0, 0, 0, child, absolute=True, worldSpace=True)

                file_name = child
                scene_path = f'{bp_dir}/{file_name}'
                cmds.file(scene_path, options = export_options, type = file_type, pr=True, es=True)

        elif obj.startswith('SM_'):
            for child in to_export:
                cmds.select(child, replace=True)
                file_name = obj

                if project_type == 'Environment':
                    parent_dir = '/'.join(asset_dir.split('/')[:-1])
                    scene_path = f'{parent_dir}/Meshes/{file_name}'
                else:
                    scene_path = f'{asset_dir}/{file_name}'
                cmds.file(scene_path, options = export_options, type = file_type, pr=True, es=True)

        if len(prefix_children) > 1:
            pass

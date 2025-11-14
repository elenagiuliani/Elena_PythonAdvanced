"""
***************************************************************
***************************************************************
Content: export static mesh or skeletal mesh

2025-11-03

Author: Elena Giuliani
email: elenagiuliani94@outlook.it
***************************************************************
***************************************************************
"""
import maya.cmds as cmds

class Exporter:

    def __init__(self, filedir, filetype, feedback_label=print, exportsettings=''):             # feedback_label to show messages in the UI
        # prefixes = [SM, SKM, ANIM]

        self.file_dir = filedir
        self.file_type = filetype.upper()
        self.feedback_label = feedback_label
        self.export_settings = exportsettings

        self.selected = cmds.ls(selection=True)
        self.outliner_objs = cmds.ls(assemblies=True)


    def configure_file_type(self):
        if self.file_type == 'FBX':
            return 'FBX export'
        elif self.file_type == 'OBJ':
            return 'OBJexport'
        else:
            self.feedback_label('File type not supported')    # in ui: exporter = Exporter(filedir, filetype, feedback_label=ui.label_feedback.setText)
            print('file type not supported')

    # return a list of selected objs or all objs in outliner
    def objects_to_export(self):
        if self.selected:
            return self.selected
        else:
            return self.outliner_objs


    # check if obj has a skin cluster
    def has_skin_cluster(self, obj):
        history = cmds.listHistory(obj)
        for node in history:
            if cmds.nodeType(node) == 'skinCluster':
                print('has skin cluster')
                return True
        print('no skin cluster')
        return False

    # check if obj is groups
    def is_group(self, obj):
        if cmds.objectType(obj) != 'transform':
            return True
        shapes = cmds.listRelatives(obj, shapes=True)
        if not shapes:
            return True
        else:
            return False





#***************************************************************
    # EXPORT SM OR SKM
    def export_mesh(self):
  
            for obj in self.objects_to_export():
                cmds.select(obj, replace=True)

                mesh_type = 'static mesh'

                # IF SKELETAL MESH
                if self.has_skin_cluster(obj):
                    if not obj.startswith('SKM_'):
                        print(f'SKIP exporting {obj}: not starting with "SKM_"')
                        break

                    skin_clusters = cmds.ls(cmds.listHistory(obj), type='skinCluster')
                    influences = cmds.skinCluster(skin_clusters[0], query=True, influence=True)
                    
                    # select joints
                    cmds.select(influences, add=True)
                    mesh_type = 'skeletal mesh'

                # IF STATIC MESH
                else:
                    if not obj.startswith('SM_'):
                        print(f'SKIP exporting {obj}: not starting with "SM_"')
                        break

                # if is group combine it
                if is_group(obj):
                    cmds.polyUnite(obj, name=obj)

                file_name = obj
                file_path = f'{self.file_dir}/{file_name}'

                # EXPORT
                cmds.file(file_path, options = self.export_settings, type = self.configure_file_type(), pr=True, es=True)  # pr=True: preserve references, es=True: export selected
                print(f'exported {mesh_type}: {file_path}')

                # undo the combine to have the group back
                cmds.undo()

    




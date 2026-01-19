"""
Content  : custom_shelf.py

Date     : 2025-12-01

license  : MIT
Author   : Elena Giuliani
email    : elenagiuliani94@outlook.it
"""
import os
import sys
import maya.cmds as cmds

from mayafunc import ROOT_DIR

CURRENT_DIR = os.getcwd()
sys.path.append(CURRENT_DIR)

from Git_PackForge_Pipeline.library.appdata import ICON_PATH

"""
icons_dir = ROOT_DIR + '\Git_PackForge_Pipeline\library\img\icons\{}.png'
icons_dir = icons_dir.replace('\\', '/')
"""

def load():
    shelf_name = 'PackForge'

    def _empty_btn():
        cmds.shelfButton(command = '', annotation = '',
                        parent = shelf_name,
                        image = ICON_PATH.format('empty'))

    if not cmds.shelfLayout(shelf_name, exists = True):
        cmds.shelfLayout(shelf_name, parent='ShelfLayout')

        base_command = 'import importlib;\nimport mayafunc;\nimportlib.reload(mayafunc);\n'

        cmds.shelfButton(command = base_command + 'mayafunc.press_btnIncrementSave("")',
                        annotation = 'Save scene',
                        parent = shelf_name,
                        image = ICON_PATH.format('btn_save'))

        cmds.shelfButton(command = base_command + 'mayafunc.press_btnIncrementSave("increment")',
                        annotation = 'Increment save scene',
                        parent = shelf_name,
                        image = ICON_PATH.format('btn_incrementSave'))
                            
        _empty_btn()

        cmds.shelfButton(command = base_command + 'mayafunc.press_btnExportMesh()',
                        annotation = 'Export assets',
                        parent = shelf_name,
                        image = ICON_PATH.format('btn_export_asset'))
                            

        cmds.shelfButton(command = base_command + 'mayafunc.press_btnScreenshot()',
                        annotation = 'Take screenshot',
                        parent = shelf_name,
                        image = ICON_PATH.format('btn_screenshot'))
        
        _empty_btn()

        cmds.shelfButton(command = base_command + 'mayafunc.add_remove_prefixes("SM")',
                        annotation = 'Add/remove SM',
                        parent = shelf_name,
                        image = ICON_PATH.format('btn_SM'))

        cmds.shelfButton(command = base_command + 'mayafunc.add_remove_prefixes("BP")',
                        annotation = 'Add/remove BP',
                        parent = shelf_name,
                        image = ICON_PATH.format('btn_BP'))

        cmds.shelfButton(command = base_command + 'mayafunc.add_remove_prefixes("UCX")',
                        annotation = 'Add/remove UCX',
                        parent = shelf_name,
                        image = ICON_PATH.format('btn_UCX'))

        _empty_btn()

        cmds.shelfButton(command = base_command + 'mayafunc.fix_names()',
                        annotation = 'Rename the children of a group as the parent',
                        parent = shelf_name,
                        image = ICON_PATH.format('btn_fixNames'))

    else:
        print(f'<<<<<<<<<<<< {shelf_name} already created')

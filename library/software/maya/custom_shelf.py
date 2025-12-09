"""
Content  : custom shelf creation script

Date     : 2025-12-01

Author   : Elena Giuliani
email    : elenagiuliani94@outlook.it
"""
import os
import sys
import maya.utils
import maya.cmds as cmds

CURRENT_DIR = os.getcwd()
sys.path.append(CURRENT_DIR)

icons_dir = CURRENT_DIR + '\library\img\icons\{}.png'
icons_dir = icons_dir.replace('\\', '/')

# load this module after maya has loaded the ui
maya.utils.executeDeferred(lambda: __import__("custom_shelf"))

shelf_name = 'PackForge'

if not cmds.shelfLayout(shelf_name, exists = True):
    cmds.shelfLayout(shelf_name, parent='ShelfLayout')

    cmds.shelfButton(command = 'import importlib; import mayafunc; importlib.reload(mayafunc); mayafunc.press_btnIncrementSave()',
                    annotation = 'Increment save scene',
                    parent = shelf_name,
                    image = icons_dir.format('btn_save'))
                        
    cmds.shelfButton(command = 'import importlib; import mayafunc; importlib.reload(mayafunc); mayafunc.press_btnExportMesh()',
                    annotation = 'Export assets',
                    parent = shelf_name,
                    image = icons_dir.format('btn_export_asset'))
                        
    cmds.shelfButton(command = 'import importlib; import mayafunc; importlib.reload(mayafunc); mayafunc.press_btnScreenshot()',
                    annotation = 'Take screenshot',
                    parent = shelf_name,
                    image = icons_dir.format('btn_screenshot'))
else:
    print(f'{shelf_name} already created')

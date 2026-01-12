# *********************************************************
# PACKFORGE SHELF
# copy/paste inside userSetup.py in C:\Users\utente\Documents\maya\[version]\scripts
import os
import maya.cmds as cmds
print('<<<<<<<<<<<<<<<<<<<<< LOAD_CUSTOM_SHELF =', os.getenv('LOAD_CUSTOM_SHELF'))
def load_shelf():
    if os.getenv('LOAD_CUSTOM_SHELF') != "1":
        # NOT BAT FILE
        if cmds.shelfLayout('PackForge', exists=True):
            cmds.deleteUI('PackForge', layout=True)
            print('<<<<<<<<<<<<<<<<<<<<< Removed PackForge shelf (this is not bat mode)')
        return
    # BAT FILE
    if os.getenv('LOAD_CUSTOM_SHELF') == "1":
        cmds.evalDeferred('import custom_shelf; custom_shelf.load()')
        print('<<<<<<<<<<<<<<<<<<<<< PackForge shelf successfully created!')

# load or remove shelf after maya loaded
cmds.evalDeferred(load_shelf)
# *********************************************************


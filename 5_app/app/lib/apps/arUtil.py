"""
Content  : 

Date     : 2025-11-13

Author   : Elena Giuliani
email    : elenagiuliani94@outlook.it
"""


import os
import sys
import webbrowser

from Qt import QtWidgets, QtGui, QtCompat, QtCore

TITLE = os.path.splitext(os.path.basename(__file__))[0]
CURRENT_DIR =  os.path.dirname(__file__)
ROOT_PATH = '/'.join(CURRENT_DIR.split('\\')[:-2])
IMG_PATH = ROOT_PATH + '/img/icons/{}.png'

sys.path.append(ROOT_PATH)

from lib.appfunc import loaded_code_project, loaded_project_path


class ArUtil():

    def __init__(self):
        path_ui = CURRENT_DIR + '/ui/' + TITLE + '.ui'
        self.wgHeader = QtCompat.loadUi(path_ui)

        # ICONS
        self.wgHeader.setWindowIcon(QtGui.QPixmap(IMG_PATH.format('logo_store')))

        self.wgHeader.btnCgtraderLink.setIcon(QtGui.QPixmap(IMG_PATH.format('cgtrader_logo')))
        self.wgHeader.btnFabLink.setIcon(QtGui.QPixmap(IMG_PATH.format('fab_logo')))

        self.wgHeader.btnBack.setIcon(QtGui.QPixmap(IMG_PATH.format('btn_back_disabled')))

        # SIGNALS
        self.wgHeader.btnCgtraderLink.clicked.connect(lambda: self.press_btnStore('cgtrader'))
        #self.wgHeader.btnFabLink.clicked.connect(lambda: self.press_btnStore('fab'))
        self.wgHeader.btnFabLink.setEnabled(False)


        self.wgHeader.btnHelp.clicked.connect(self.press_btnHelp)
        self.wgHeader.btnProject.clicked.connect(self.press_btnProject)
        self.wgHeader.btnProject.setText(loaded_code_project)


        self.wgHeader.show()

    #***************************************************************
    # FUNCTIONS
    def press_btnStore(self, button):
        if button == 'cgtrader':
            webbrowser.open("https://www.cgtrader.com/designers/pixelsandcrafts")

        if button == 'fab':
            webbrowser.open("")


    def press_btnHelp(self):
        webbrowser.open("https://github.com/elenagiuliani/Elena_PythonAdvanced/wiki")


    def press_btnProject(self):
        webbrowser.open(loaded_project_path)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ar_util = ArUtil()
    app.exec_()
    

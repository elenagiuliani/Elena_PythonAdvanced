"""
Content  : 

Date     : 2025-11-13

Author   : Elena Giuliani
email    : elenagiuliani94@outlook.it
"""


import os
import sys
import webbrowser

import Qt
from Qt import QtWidgets, QtGui, QtCompat, QtCore

#import app_utils


TITLE = os.path.splitext(os.path.basename(__file__))[0]
CURRENT_PATH =  os.path.dirname(__file__)
ROOT_PATH = '/'.join(CURRENT_PATH.split('\\')[:-2])
IMG_PATH = ROOT_PATH + '/img/icons/{}.png'

sys.path.append(ROOT_PATH)
print(f'\nsys paths:        {sys.path}\n')
print(TITLE)


class ArUtil:

    def __init__(self):

        path_ui = CURRENT_PATH + '/ui/' + TITLE + '.ui'
        self.wgHeader = QtCompat.loadUi(path_ui)


        # ICONS
        self.wgHeader.btnStoreLink.setIcon(QtGui.QPixmap(IMG_PATH.format('btn_store_link')))
        self.wgHeader.btnBack.setIcon(QtGui.QPixmap(IMG_PATH.format('btn_back')))



        self.wgHeader.show()


    # FUNCTIONS
    def resize_widget(self, widget):
        x = widget.frameGeometry().width()
        y = self.wgHeader.frameGeometry().height() + widget.frameGeometry().height() - 0.1
        self.wgHeader.resize(x, y)
        self.wgHeader.setMinimumSize(x, y)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ar_util = ArUtil()
    app.exec_()
    










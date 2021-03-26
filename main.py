#!/usr/bin/python

import sys
import random
import json
from PySide6 import QtGui
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6 import QtCore, QtWidgets, QtGui

from BeatSheetIems import *


class BeatSheetGridWidget(QWidget):
    _items = []
    def __init__(self):
        super().__init__()
        self.setUI()

    def save(self):
        items = []
        for item in self._items:
            items.append(item['item'].serialize())
        with open("save/save-the-cat.cat", "w") as write_file:
        #jsonString = print(json.dumps(self._items, sort_keys=True, indent=4))
            json.dump(items, write_file, sort_keys=True, indent=4)
        #    json.dump(self._items, write_file)
        print(items)

    def setUI(self):
        grid = QGridLayout()

        self._items = [
                {"item":BeatSheetItemOpenImageWidget(), "position-x": 0, "position-y": 0},
                {"item":BeatSheetItemThemwStatedWidget(), "position-x": 0, "position-y": 1},
                {"item":BeatSheetItemSetupWidget(), "position-x": 0, "position-y": 2},
                {"item":BeatSheetItemCatalystWidget(), "position-x": 0, "position-y": 3},
                {"item":BeatSheetItemDebateWidget(), "position-x": 1, "position-y": 0},
                {"item":BeatSheetItemBreakeInto2Widget(), "position-x": 1, "position-y": 1},
                {"item":BeatSheetItemFunAndGamesWidget(), "position-x": 1, "position-y": 2},
                {"item":BeatSheetItemMidpointWidget(), "position-x": 1, "position-y": 3},
                {"item":BeatSheetItemBadGuysCloseInWidget(), "position-x": 2, "position-y": 0},
                {"item":BeatSheetItemAllIsLostWidget(), "position-x": 2, "position-y": 1},
                {"item":BeatSheetItemDarkNoghtOfTheSoulWidget(), "position-x": 2, "position-y": 2},
                {"item":BeatSheetItemBreakInto3Widget(), "position-x": 2, "position-y": 3},
                {"item":BeatSheetItemGatheringTheTeamWidget(), "position-x": 3, "position-y": 0},
                {"item":BeatSheetItemStormingTheCastleWidget(), "position-x": 3, "position-y": 1},
                {"item":BeatSheetItemHightoweSurpriseWidget(), "position-x": 3, "position-y": 2},
                {"item":BeatSheetItemDigDeepDownWidget(), "position-x": 3, "position-y": 3},
                {"item":BeatSheetItemExecutingThePlanWidget(), "position-x": 4, "position-y": 0},
                {"item":BeatSheetItemFinalImageWidget(), "position-x": 4, "position-y": 1}
                ]
        for item in self._items:
            grid.addWidget(item['item'],item['position-x'], item['position-y'])

        self.setLayout(grid)


class AppMainWindow(QMainWindow):
    
    def __init__(self):
        super(AppMainWindow, self).__init__()
        
        self.initUI()
       
    def initGrid(self):
        textEdit = QTextEdit()
        #self.setCentralWidget(textEdit)
        self._grid = BeatSheetGridWidget()
        self.setCentralWidget(self._grid)


    def initUI(self):               
        exitIcon = "/usr/src/frustrado/scribus/resources/iconsets/1_5_1_dark/exit22.png"
        newIcon = "/opt/git/scribus/share/scribus/icons/1_5_1_dark/document2.png"
        saveIcon = "/usr/share/scribus/icons/1_5_1_dark/22/document-save.png"
        openIcon = "/opt/git/scribus/share/scribus/icons/1_5_1_dark/22/document-open.png"
        exportIcon = "/opt/git/scribus/share/scribus/icons/1_5_1_dark/22/document-print.png"
        appIcon = "/opt/kritadev/install/share/icons/hicolor/64x64/apps/krita.png"

        self.initGrid()

        exitAction = QtGui.QAction(QIcon(exitIcon),'Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(self.close)

        newAction = QtGui.QAction(QIcon(newIcon),'New', self)
        newAction.setShortcut('Ctrl+N')
        newAction.setStatusTip('New Beat Sheet')
        newAction.triggered.connect(self.new)

        saveAction = QtGui.QAction(QIcon(saveIcon),'Save', self)
        saveAction.setShortcut('Ctrl+S')
        saveAction.setStatusTip('Save Beat Sheet')
        saveAction.triggered.connect(self.save)

        openAction = QtGui.QAction(QIcon(openIcon),'Open', self)
        openAction.setShortcut('Ctrl+S')
        openAction.setStatusTip('Open Beat Sheet')
        openAction.triggered.connect(self.open)

        exportAction = QtGui.QAction(QIcon(exportIcon),'Export', self)
        exportAction.setShortcut('Ctrl+E')
        exportAction.setStatusTip('Export Beat Sheet')
        exportAction.triggered.connect(self.export)

        self.statusBar()

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAction)

        toolbar = self.addToolBar('BeatSheet')
        toolbar.addAction(exitAction)
        
        toolbar.addAction(newAction)
        toolbar.addAction(saveAction)
        toolbar.addAction(openAction)
        toolbar.addAction(exportAction)
        
        self.setWindowTitle('Save the Cat Beat Sheet') 

        MainAppIcon = QIcon(appIcon)
        self.setWindowIcon(MainAppIcon)
        self.setGeometry(0,0, 1920,1080)

        self.showMaximized()

        self.show()

    def save(self):
        self._grid.save()
    
    def open(self):
        #self._grid.open()
        print("Open")
    
    def new(self):
        print("New")

    def export(self):
        print("New")


def main():
    app = QApplication([])
    ex = AppMainWindow()
    File = QtCore.QFile("resources/stye.qss")
    File.open(QtCore.QFile.ReadOnly)
    qss = QtCore.QTextStream(File)
	#setup stylesheet
    app.setStyleSheet(qss.readAll())

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()

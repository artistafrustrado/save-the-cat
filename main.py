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

# https://zetcode.com/gui/pysidetutorial/dialogs/
# https://david-estevez.gitbooks.io/tutorial-pyside-pyqt4/content/06_dialog.html
class BeatSheetGridWidget(QWidget):
    _items = []
    def __init__(self):
        super().__init__()
        self.setUI()

    def save(self):
        items = []
        for item in self._items:
            items.append(item['item'].serialize())

        filename, filter = QFileDialog.getSaveFileName(parent=self, caption='Select Save the Cat file', dir='.', filter='Save the Cat Beat Sheet (*.cat)')

        if filename:
            print(filename)
            with open(filename, "w") as write_file:
                json.dump(items, write_file, sort_keys=True, indent=4)

    def export(self):
        items = []
        buffer = ''
        for item in self._items:
            items.append(item['item'].serialize())
            buffer += '\subsection{' + item['item'].title + '}'
            buffer += "\n\n"
            buffer += item['item'].text
            buffer += "\n\n"

        filename, filter = QFileDialog.getSaveFileName(parent=self, caption='LaTex File (.tex)', dir='.', filter='LaTex File (*.tex)')

        content = ''

        print(buffer)

        with open('templates/export-latex.tex', "r") as read_file:
            template = read_file.read()
            content = template.replace('<[CONTENT]>', buffer)
        
        if filename:
            print(filename)
            with open(filename, 'w',encoding = 'utf-8') as write_file:
                write_file.write(content)
                write_file.close()

    def exportHtml(self):
        pass

    def load(self):

        filename, filter = QFileDialog.getOpenFileName(self, 'Open file', '~/')
        with open(filename, 'r') as json_data:
            json_data = json.load(json_data)
            for item in self._items:
                for entry in json_data:
                    if entry['type'] == item['item'].getType():
                        item['item'].setText(entry['text'])
#        fileName = QFileDialog.getOpenFileName()
#        print(fileName)
#        fname, _ = QFileDialog.getOpenFileName(self, 'Open file', '/home')
#        print(fname)
#        f = open(fname, 'r')
#        with f:
#            data = f.read()
#            self.textEdit.setText(data)


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

        grid.addWidget(BeatSheetLoglineWidget(), 4, 2, 4, 3)

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
        exitIcon = "resources/icons/exit22.png"
        newIcon = "resources/icons/document2.png"
        saveIcon = "resources/icons/document-save.png"
        openIcon = "resources/icons/document-open.png"
        exportIcon = "resources/icons/document-print.png"
        exportHtmlIcon = "resources/icons/goto.png"
        appIcon = "resources/icons/krita.png"

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

        exportHtmlAction = QtGui.QAction(QIcon(exportHtmlIcon),'Export HTML', self)
        exportHtmlAction.setShortcut('Ctrl+H')
        exportHtmlAction.setStatusTip('Export Beat Sheet (HTML)')
        exportHtmlAction.triggered.connect(self.exportHtml)

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
        toolbar.addAction(exportHtmlAction)
        
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
        self._grid.load()
    
    def new(self):
        print("New")

    def export(self):
        print("Export")
        self._grid.export()

    def exportHtml(self):
        self._grid.exportHtml()
        

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

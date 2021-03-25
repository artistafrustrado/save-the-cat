#!/usr/bin/python

import sys
import random
from PySide6 import QtGui
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6 import QtCore, QtWidgets, QtGui


class BeatSheetGridWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setUI()

    def setUI(self):
        grid = QGridLayout()

        items = [
                {"item":BeatSheetItemOpenImageWidget(), "position-x": 0, "position-y": 0},
                {"item":BeatSheetItemWidget(), "position-x": 0, "position-y": 1},
                {"item":BeatSheetItemWidget(), "position-x": 0, "position-y": 2},
                {"item":BeatSheetItemWidget(), "position-x": 0, "position-y": 3}
                ]
        for item in items:
            print(item)
            grid.addWidget(item['item'],item['position-x'], item['position-y'])

        self.setLayout(grid)


class BeatSheetItemWidget(QWidget):
    title = "Example Title"
    _type = "opening-image"

    def __init__(self):
        super().__init__()

        self.hello = ["Hello World","Hei maailma","Hola Mundo", "Can't type that"]

        self._title = QLabel("<b>" + self.title + "</b>",alignment=QtCore.Qt.AlignCenter)
        self.button = QPushButton("Click Me!")
        self.text = QLabel("Hello World",alignment=QtCore.Qt.AlignCenter)
        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self._title)
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.button)

        self.setLayout(self.layout)

        self.button.clicked.connect(self.magic)

    @QtCore.Slot()
    def magic(self):
        self.text.setText(random.choice(self.hello))

class BeatSheetItemOpenImageWidget(BeatSheetItemWidget):
    def __init__(self):
        self.title = "Opening Image"
        self.type = "opening-image"
        super().__init__()


class AppMainWindow(QMainWindow):
    
    def __init__(self):
        super(AppMainWindow, self).__init__()
        
        self.initUI()
       
    def initGrid(self):
        textEdit = QTextEdit()
        #self.setCentralWidget(textEdit)
        grid = BeatSheetGridWidget()
        self.setCentralWidget(grid)


    def initUI(self):               
        exitIcon = "/usr/src/frustrado/scribus/resources/iconsets/1_5_1_dark/exit22.png"
        newIcon = "/opt/git/scribus/share/scribus/icons/1_5_1_dark/document2.png"
        saveIcon = "/usr/share/scribus/icons/1_5_1_dark/22/document-save.png"
        exportIcon = "/opt/git/scribus/share/scribus/icons/1_5_1_dark/22/document-print.png"
        appIcon = "/opt/kritadev/install/share/icons/hicolor/64x64/apps/krita.png"

        self.initGrid()

        exitAction = QtGui.QAction(QIcon(exitIcon),'Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(self.close)

        newAction = QtGui.QAction(QIcon(newIcon),'New', self)
        newAction.setShortcut('Ctrl+N')
        newAction.setStatusTip('Exit application')
        newAction.triggered.connect(self.close)

        saveAction = QtGui.QAction(QIcon(saveIcon),'Save', self)
        saveAction.setShortcut('Ctrl+S')
        saveAction.setStatusTip('Exit application')
        saveAction.triggered.connect(self.close)

        exportAction = QtGui.QAction(QIcon(exportIcon),'Export', self)
        exportAction.setShortcut('Ctrl+E')
        exportAction.setStatusTip('Exit application')
        exportAction.triggered.connect(self.close)

        self.statusBar()

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAction)

        toolbar = self.addToolBar('Exit')
        toolbar.addAction(exitAction)
        
        toolbar.addAction(newAction)
        toolbar.addAction(saveAction)
        toolbar.addAction(exportAction)
        
        self.setWindowTitle('Save the Cat Beat Sheet') 

        MainAppIcon = QIcon(appIcon)
        self.setWindowIcon(MainAppIcon)
        self.setGeometry(0,0, 1920,1080)

        self.showMaximized()

        self.show()
        
        
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

#!/usr/bin/python

import os
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

class SynopsisWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setUI()

    def setUI(self):
        self._synopsisText = QTextEdit()
        grid = QGridLayout()
        grid.addWidget(self._synopsisText, 0, 0)
        self.setLayout(grid)

    def setSynopsis(self, text):
        self._synopsisText.setPlainText(text)

    def getSynopsis(self):
        return self._synopsisText.toPlainText()
    
    
class ReferenceWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setUI()

    def setUI(self):
        with open('help/beat-sheet.html', "r") as read_file:
            reference = read_file.read()

        # web_view.load(QUrl('http://www.www.pythoncentral.io'))
        # web_view.setUrl(QUrl('http://www.www.pythoncentral.io'))

        # layout.addStretch()

        scroll = QtWidgets.QScrollArea()
        scroll.setWidgetResizable(1)

        self._referenceText = QLabel(reference)
        scroll.setWidget(self._referenceText)
        grid = QVBoxLayout()
#        grid.addWidget(self._referenceText)
        grid.addWidget(scroll)
#        grid.addStretch()
        self.setLayout(grid)

    
class MovieWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setUI()

    def setUI(self):
        self._movieNameText = QLineEdit()
        self._movieThemeText = QLineEdit()
        self._movieGenreText = QLineEdit()
        grid = QFormLayout()
        grid.addRow('Name',self._movieNameText)
        grid.addRow('Theme',self._movieThemeText)
        grid.addRow('Genre',self._movieGenreText)
        self.setLayout(grid)

    def getName(self):
        return self._movieNameText.text()

    def getTheme(self):
        return self._movieThemeText.text()

    def getGenre(self):
        return self._movieGenreText.text()

    def setName(self, text):
        self._movieNameText = text
        self._text.text(self._movieNameText)
    
    def setTheme(self, text):
        self._movieThemeText = text
        self._text.text(self._movieThemeText)
    
    def setGenre(self, text):
        self._movieGenreText = text
        self._text.text(self._movieGenreText)
    
class AuthorWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setUI()

    def setUI(self):
        self._authorNameText = QLineEdit()
        self._authorEmailText = QLineEdit()
        self._authorInstituteText = QLineEdit()
        grid = QFormLayout()
        grid.addRow('Nome',self._authorNameText)
        grid.addRow('e-mail',self._authorEmailText)
        grid.addRow('Institute',self._authorInstituteText)
        self.setLayout(grid)

    def getName(self):
        return self._authorNameText.text()

    def setName(self, text):
        self._authorNameText = text
        self._text.text(self._authorNameText)
    
    def getEmail(self):
        return self._authorEmailText.text()

    def setEmail(self, text):
        self._authorEmailText = text
        self._text.text(self._authorEmailText)

    def getInstitute(self):
        return self._authorInstituteText.text()

    def setInstitute(self, text):
        self._authorInstituteText = text
        self._text.text(self._authorInstituteText)


class EscaletaWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setUI()

    def setUI(self):
        self._escaletaText = QTextEdit()
        grid = QGridLayout()
        grid.addWidget(self._escaletaText, 0, 0)
        self.setLayout(grid)

    def setEscaleta(self, text):
        self._escaletaText.setPlainText(text)

    def getEscaleta(self):
        return self._escaletaText.toPlainText()
    
    


class ArgumentoWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setUI()

    def setUI(self):
        self._argumentoText = QTextEdit()
        grid = QGridLayout()
        grid.addWidget(self._argumentoText, 0, 0)
        self.setLayout(grid)
    
    def setArgumento(self, text):
        self._argumentoText.setPlainText(text)

    def getArgumento(self):
        return self._argumentoText.toPlainText()
    
    


class PlotWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setUI()

    def setUI(self):
        self._plotText = QTextEdit()
        grid = QGridLayout()
        grid.addWidget(self._plotText, 0, 0)
        self.setLayout(grid)
    
    def setPlot(self, text):
        self._plotText.setPlainText(text)

    def getPlot(self):
        return self._plotText.toPlainText()
    
    

class BeatSheetGridWidget(QWidget):
    _items = []
    def __init__(self):
        super().__init__()
        self.setUI()

    def getItems(self):
        items = []
        for item in self._items:
            items.append(item['item'].serialize())
        return items

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

#        print(buffer)

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

        self._logLineText = BeatSheetLoglineWidget()
        grid.addWidget(self._logLineText, 4, 2, 4, 3)

        self.setLayout(grid)

    def setLogLine(self, text):
        self._logLineText.setPlainText(text)

    def getLogLine(self):
        return self._logLineText.toPlainText()


class AppMainWindow(QMainWindow):
    
    def __init__(self):
        super(AppMainWindow, self).__init__()
        
        self.initUI()
       
    def initGrid(self):
 
        self.tabs = QTabWidget()

        textEdit = QTextEdit()
        #self.setCentralWidget(textEdit)
        self._grid = BeatSheetGridWidget()
        self.setCentralWidget(self.tabs)
        
        self._synopsis = SynopsisWidget()
        self._plot = PlotWidget()
        self._argumento = ArgumentoWidget()
        self._escaleta = EscaletaWidget()
        self._author = AuthorWidget()
        self._movie = MovieWidget()
        self._reference = ReferenceWidget()

        self.tabs.addTab(self._grid,"Beat Sheet")
        self.tabs.addTab(self._movie,"Movie Info")
        self.tabs.addTab(self._synopsis,"Synopsis")
        self.tabs.addTab(self._plot,"Plot")
        self.tabs.addTab(self._argumento,"Argumento")
        self.tabs.addTab(self._escaleta,"Escaleta")
        self.tabs.addTab(self._author,"Author")
        self.tabs.addTab(self._reference,"Reference")

#        self.layout.addWidget(self.tabs)
#        self.setLayout(self.layout)

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

    def _getData(self):
        items = self._grid.getItems()
#        print(items)
        movie_name = self._movie.getName()
        movie_theme = self._movie.getTheme()
        movie_genre = self._movie.getGenre()
        print(self._movie)
        author_name = self._author.getName()
        author_email = self._author.getEmail()
        author_institute = self._author.getInstitute()
        
        plot_text = self._plot.getPlot()
        escaleta_text = self._escaleta.getEscaleta()
        argumento_text = self._argumento.getArgumento()
        synopsis_text = self._synopsis.getSynopsis()

        movie = [
                {'movie': {'name': movie_name, 'genre': movie_genre, 'theme': movie_theme}},
                {'beat-sheet': items},
                {'synopsis': synopsis_text},
                {'plot': plot_text},
                {'argumento': argumento_text},
                {'escaleta': escaleta_text},
                {'author': {'name':author_name, 'email': author_email, 'institute':author_institute }}
                ]
        return movie

    def save(self):
        movie = self.getData()

        filename, filter = QFileDialog.getSaveFileName(parent=self, caption='Select Save the Cat file', dir='.', filter='Save the Cat Beat Sheet (*.cat)')

        if filename:
            filename, file_extension = os.path.splitext(filename)
            if file_extension != 'cat':
                filename = filename + '.cat'
            print(filename)
            with open(filename, "w") as write_file:
                json.dump(movie, write_file, sort_keys=True, indent=4)
    
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

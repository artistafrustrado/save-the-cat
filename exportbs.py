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


class BeatSheetExporter:
    def __init__(self):

        self._data = '' 
        self._parent = ''
        self.caption = 'LaTex File'
        self.filter = 'LaTex File (*.tex)'
        self.extention = 'tex'
        self.savePath = os.path.expanduser("~")

    def setData(self, dataset):
        self._data = dataset

    def setParent(self, parent):
        self._parent = parent

#    def exportFile(self, data):
    def exportFile(self):
        movie = self.generate()

        filename, filter = QFileDialog.getSaveFileName(parent=self._parent, caption=self.caption, dir=self.savePath, filter=self.filter)

        if filename:
            filename, file_extension = os.path.splitext(filename)
            if file_extension != self.extention:
                filename = filename + '.' + self.extention
            print(filename)
            with open(filename, "w") as write_file:
                write_file.write(movie)

    def generate(self):
        buffer = ''

        with open('templates/export-latex.tex', "r") as read_file:
            reference = read_file.read()
            buffer += "\subsection{Name}\n\n"
            buffer += self._data[0]['movie']['name'] + "\n\n"
            buffer += "\subsection{LogLine}\n\n"
            buffer += self._data[0]['movie']['logline']  + "\n\n"
            buffer += "\subsection{Theme}\n\n"
            buffer += self._data[0]['movie']['theme'] + "\n\n"
            buffer += "\subsection{Genre}\n\n"
            buffer += self._data[0]['movie']['genre'] + "\n\n"
            buffer += "\n\n"
            buffer += "\subsection{Author}\n\n"
            buffer += "\\textbf{Name}: " + self._data[6]['author']['name'] + "\n\n"
            buffer += "\\textbf{e-mail}: " + self._data[6]['author']['email'] + "\n\n"
            buffer += "\\textbf{Institute}: " + self._data[6]['author']['institute'] + "\n\n"
            
            buffer += "\subsection{Beat Sheet}\n\n"
            for card in self._data[1]['beat-sheet']:
                buffer += "\subsubsection{" + card["title"] + "}\n\n"
                buffer += card['text'] + "\n\n"

            buffer += "\subsection{Synopsis}\n\n"
            buffer += self._data[2]['synopsis'] + "\n\n"

            buffer += "\subsection{Plot}\n\n"
            buffer += self._data[3]['plot'] + "\n\n"
            
            buffer += "\subsection{Argumento}\n\n"
            buffer += self._data[4]['argumento'] + "\n\n"
            
            buffer += "\subsection{Escaleta}\n\n"
            buffer += self._data[5]['escaleta'] + "\n\n"
            
            buffer += "\n\n"

        template = reference.replace('<[CONTENT]>', buffer)

        return template

    def export(self):
        self.exportFile() 
        print(self._data)

    
class BeatSheetExporterLatex(BeatSheetExporter):
    def __init__(self):
        super().__init__()


class BeatSheetExporterHtml(BeatSheetExporter):
    def __init__(self):
        super().__init__()
        self.caption = '(X)HTML File'
        self.filter = 'XTML File (*.html)'
        self.extention = 'html'
    
    def generate(self):
        buffer = ''

#<div class="card">
#      <div class="card-body">
#        <h5 class="card-title">Special title treatment</h5>
#        <p class="card-text">With supporting text below as a natural lead-in to additional content.</p>
#        <a href="#" class="btn btn-primary">Go somewhere</a>
#      </div>
#</div>

        with open('templates/export.html', "r") as read_file:
            reference = read_file.read()
            buffer += "<h2>Name</h2>\n\n"
            buffer += self._data[0]['movie']['name'] + "\n\n"
            buffer += "<h2>LogLine</h2>\n\n"
            buffer += self._data[0]['movie']['logline']  + "\n\n"
            buffer += "<h2>Theme</h2>\n\n"
            buffer += self._data[0]['movie']['theme'] + "\n\n"
            buffer += "<h2>Genre</h2>\n\n"
            buffer += self._data[0]['movie']['genre'] + "\n\n"
            buffer += "\n\n"
            buffer += "<h2>Author</h2\n\n"
            buffer += "<b>Name}</b>: " + self._data[6]['author']['name'] + "\n<br/>\n\n"
            buffer += "<b>e-mail}</b>: " + self._data[6]['author']['email'] + "\n<br/>\n\n"
            buffer += "<b>Institute</b>: " + self._data[6]['author']['institute'] + "\n<br/>\n\n"
            
            buffer += "<h2>Beat Sheet</h2>\n\n"
            for card in self._data[1]['beat-sheet']:
                buffer += '    <div class="card">'
                buffer += '      <div class="card-body">'
                buffer += '        <h5 class="card-title">' + card['title'] + '</h5>'
                buffer += '        <p class="card-text">' + card['text'] + '</p>'
                buffer += '      </div>'
                buffer += '</div>' + "\n\n"

            buffer += "<h2>Synopsis</h2>\n\n"
            buffer += self._data[2]['synopsis'] + "\n\n"

            buffer += "<h2>Plot</h2>\n\n"
            buffer += self._data[3]['plot'] + "\n\n"
            
            buffer += "<h2>Argumento</h2>\n\n"
            buffer += self._data[4]['argumento'] + "\n\n"
            
            buffer += "<h2>Escaleta</h2>\n\n"
            buffer += self._data[5]['escaleta'] + "\n\n"
            
            buffer += "\n\n"

        template = reference.replace('<[CONTENT]>', buffer)

        return template


class BeatSheetExporterRtf:
    def __init__(self):
        pass


class BeatSheetExporterOdt:
    def __init__(self):
        pass

#from odf.opendocument import OpenDocumentText
#from odf.text import P    
#textdoc = OpenDocumentText()
#p = P(text="Hello World!")
#textdoc.text.addElement(p)
#textdoc.save("helloworld", True)
#
# https://gist.github.com/balasankarc/1832670ec8ddd9a34d33
# https://balasankarc.in/tech/using-python-and-odfpy-to-create-open-document-texts.html

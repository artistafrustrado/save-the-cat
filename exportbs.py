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

# For odt handling
from odf.opendocument import OpenDocumentText
from odf.style import (Style, TextProperties, ParagraphProperties, ListLevelProperties, TabStop, TabStops)
from odf.text import (H, P, List, ListItem, ListStyle, ListLevelStyleNumber, ListLevelStyleBullet)
from odf import teletype


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
            buffer += self._data['movie']['name'] + "\n\n"
            buffer += "\subsection{LogLine}\n\n"
            buffer += self._data['movie']['logline']  + "\n\n"
            buffer += "\subsection{Theme}\n\n"
            buffer += self._data['movie']['theme'] + "\n\n"
            buffer += "\subsection{Genre}\n\n"
            buffer += self._data['movie']['genre'] + "\n\n"
            buffer += "\n\n"
            buffer += "\subsection{Author}\n\n"
            buffer += "\\textbf{Name}: " + self._data['author']['name'] + "\n\n"
            buffer += "\\textbf{e-mail}: " + self._data['author']['email'] + "\n\n"
            buffer += "\\textbf{Institute}: " + self._data['author']['institute'] + "\n\n"
            
            buffer += "\subsection{Beat Sheet}\n\n"
            for card in self._data['beat-sheet']:
                buffer += "\subsubsection{" + card["title"] + "}\n\n"
                buffer += card['text'] + "\n\n"

            buffer += "\subsection{Synopsis}\n\n"
            buffer += self._data['synopsis'] + "\n\n"

            buffer += "\subsection{Plot}\n\n"
            buffer += self._data['plot'] + "\n\n"
            
            buffer += "\subsection{Argumento}\n\n"
            buffer += self._data['argumento'] + "\n\n"
            
            buffer += "\subsection{Escaleta}\n\n"
            buffer += self._data['escaleta'] + "\n\n"
            
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

        with open('templates/export.html', "r") as read_file:
            reference = read_file.read()
            buffer += "<h2>Name</h2>\n\n"
            buffer += self._data['movie']['name'] + "\n\n"
            buffer += "<h2>LogLine</h2>\n\n"
            buffer += self._data['movie']['logline']  + "\n\n"
            buffer += "<h2>Theme</h2>\n\n"
            buffer += self._data['movie']['theme'] + "\n\n"
            buffer += "<h2>Genre</h2>\n\n"
            buffer += self._data['movie']['genre'] + "\n\n"
            buffer += "\n\n"
            buffer += "<h2>Author</h2\n\n"
            buffer += "<b>Name}</b>: " + self._data['author']['name'] + "\n<br/>\n\n"
            buffer += "<b>e-mail}</b>: " + self._data['author']['email'] + "\n<br/>\n\n"
            buffer += "<b>Institute</b>: " + self._data['author']['institute'] + "\n<br/>\n\n"
            
            buffer += "<h2>Beat Sheet</h2>\n\n"
            for card in self._data['beat-sheet']:
                buffer += '    <div class="card">'
                buffer += '      <div class="card-body">'
                buffer += '        <h5 class="card-title">' + card['title'] + '</h5>'
                buffer += '        <p class="card-text">' + card['text'] + '</p>'
                buffer += '      </div>'
                buffer += '</div>' + "\n\n"

            buffer += "<h2>Synopsis</h2>\n\n"
            buffer += self._data['synopsis'] + "\n\n"

            buffer += "<h2>Plot</h2>\n\n"
            buffer += self._data['plot'] + "\n\n"
            
            buffer += "<h2>Argumento</h2>\n\n"
            buffer += self._data['argumento'] + "\n\n"
            
            buffer += "<h2>Escaleta</h2>\n\n"
            buffer += self._data['escaleta'] + "\n\n"
            
            buffer += "\n\n"

        template = reference.replace('<[CONTENT]>', buffer)

        return template


class BeatSheetExporterRtf:
    def __init__(self):
        pass


class BeatSheetExporterOdt(BeatSheetExporter):
    def __init__(self):
        super().__init__()
        self.caption = 'ODT File'
        self.filter = 'ODT File (*.odt)'
        self.extention = 'odt'
    
    def exportFile(self):
        movie = self.generate()

    def _addSubSection(self, title, text):
        # Adding second heading
        mysecondheading_element = H(outlinelevel=1, stylename=self._h2style)
        mysecondheading_text = title 
        teletype.addTextToElement(mysecondheading_element, mysecondheading_text)
        self._textdoc.text.addElement(mysecondheading_element)

        if text != '':
            # Adding a paragraph
            paragraph_element = P(stylename=self._justifystyle)
            paragraph_text = text
            teletype.addTextToElement(paragraph_element, paragraph_text)
            self._textdoc.text.addElement(paragraph_element, paragraph_text)

    def _addSubSubSection(self, title, text):
        # Adding second heading
        mysecondheading_element = H(outlinelevel=2, stylename=self._h3style)
        mysecondheading_text = title 
        teletype.addTextToElement(mysecondheading_element, mysecondheading_text)
        self._textdoc.text.addElement(mysecondheading_element)

        if text != '':
            # Adding a paragraph
            paragraph_element = P(stylename=self._justifystyle)
            paragraph_text = text
            teletype.addTextToElement(paragraph_element, paragraph_text)
            self._textdoc.text.addElement(paragraph_element, paragraph_text)

    def _addParagraph(self, text):
        paragraph_element = P(stylename=self._justifystyle)
        paragraph_text = text
        teletype.addTextToElement(paragraph_element, paragraph_text)
        self._textdoc.text.addElement(paragraph_element, paragraph_text)

    def generate(self):
        self._textdoc = OpenDocumentText()

        # Creating different style used in the document
        s = self._textdoc.styles

        # For Level-1 Headings that are centerd
        h1style = Style(name="BsHeading 1", family="paragraph")
        h1style.addElement(ParagraphProperties(attributes={"textalign": "center"}))
        h1style.addElement(TextProperties(attributes={"fontsize": "18pt", "fontweight": "bold"}))

        # For Level-2 Headings that are centered
        self._h2style = Style(name="BsHeading 2", family="paragraph")
        self._h2style.addElement(ParagraphProperties(attributes={"textalign": "left"}))
        self._h2style.addElement(TextProperties(attributes={"fontsize": "15pt", "fontweight": "bold"}))

        # For Level-3 Headings that are centered
        self._h3style = Style(name="BsHeading 3", family="paragraph")
        self._h3style.addElement(ParagraphProperties(attributes={"textalign": "left"}))
        self._h3style.addElement(TextProperties(attributes={"fontsize": "14pt", "fontweight": "bold"}))

        # For bold text
        boldstyle = Style(name="Bold", family="text")
        boldstyle.addElement(TextProperties(attributes={"fontweight": "bold"}))

        # For numbered list
        numberedliststyle = ListStyle(name="NumberedList")
        level = 1
        numberedlistproperty = ListLevelStyleNumber(
            level=str(level), numsuffix=".", startvalue=1)
        numberedlistproperty.setAttribute('numsuffix', ".")
        numberedlistproperty.addElement(ListLevelProperties(
            minlabelwidth="%fcm" % (level - .2)))
        numberedliststyle.addElement(numberedlistproperty)

        # For Bulleted list
        bulletedliststyle = ListStyle(name="BulletList")
        level = 1
        bulletlistproperty = ListLevelStyleBullet(level=str(level), bulletchar=u"•")
        bulletlistproperty.addElement(ListLevelProperties(minlabelwidth="%fcm" % level))
        bulletedliststyle.addElement(bulletlistproperty)


        # Justified style
        self._justifystyle = Style(name="justified", family="paragraph")
        self._justifystyle.addElement(ParagraphProperties(attributes={"textalign": "justify"}))

        # Creating a tabstop at 10cm
        tabstops_style = TabStops()
        tabstop_style = TabStop(position="10cm")
        tabstops_style.addElement(tabstop_style)
        tabstoppar = ParagraphProperties()
        tabstoppar.addElement(tabstops_style)
        tabparagraphstyle = Style(name="Question", family="paragraph")
        tabparagraphstyle.addElement(tabstoppar)
        s.addElement(tabparagraphstyle)


        # Register created styles to styleset
        s.addElement(h1style)
        s.addElement(self._h2style)
        s.addElement(boldstyle)
        s.addElement(numberedliststyle)
        s.addElement(bulletedliststyle)
        s.addElement(self._justifystyle)
        s.addElement(tabparagraphstyle)

        # Adding main heading
        mymainheading_element = H(outlinelevel=1, stylename=h1style)
        mymainheading_text = "Save the Cat Beat Sheet"
        teletype.addTextToElement(mymainheading_element, mymainheading_text)
        self._textdoc.text.addElement(mymainheading_element)

        self._addSubSection('Name', self._data['movie']['name'])
        self._addSubSection('LogLine', self._data['movie']['logline'])
        self._addSubSection('Theme', self._data['movie']['theme'])
        self._addSubSection('Genre', self._data['movie']['genre'])
        self._addSubSection('Author', '')
        self._addParagraph('Nome: ' + self._data['author']['name'])
        self._addParagraph('e-mail: ' +  self._data['author']['email'])
        self._addParagraph('Institute: ' + self._data['author']['institute'])

        self._addSubSection('Synopsis', self._data['synopsis'])
        self._addSubSection('Beat Sheet', '')
        for card in self._data[1]['beat-sheet']:
            self._addSubSubSection(card['title'], card['text'])


        self._addSubSection('Plot', self._data['plot'])
        self._addSubSection('Argumento', self._data['argumento'])
        self._addSubSection('Escaleta', self._data['escaleta'])

        # Adding bulleted list
#        bulletlist = List(stylename=bulletedliststyle)
#        listitemelement1 = ListItem()
#        listitemelement1_paragraph = P()
#        listitemelement1_content = "My first item"
#        teletype.addTextToElement(listitemelement1_paragraph, listitemelement1_content)
#        listitemelement1.addElement(listitemelement1_paragraph)
#        bulletlist.addElement(listitemelement1)
#        listitemelement2 = ListItem()
#        listitemelement2_paragraph = P()
#        listitemelement2_content = "My second item"
#        teletype.addTextToElement(listitemelement2_paragraph, listitemelement2_content)
#        listitemelement2.addElement(listitemelement2_paragraph)
#        bulletlist.addElement(listitemelement2)
#
#        self._textdoc.text.addElement(bulletlist)
#
#        # Adding numbered list
#        numberlist = List(stylename=numberedliststyle)
#        listitemelement1 = ListItem()
#        listitemelement1_paragraph = P()
#        listitemelement1_content = "My first item"
#        teletype.addTextToElement(listitemelement1_paragraph, listitemelement1_content)
#        listitemelement1.addElement(listitemelement1_paragraph)
#        numberlist.addElement(listitemelement1)
#        listitemelement2 = ListItem()
#        listitemelement2_paragraph = P()
#        listitemelement2_content = "My second item"
#        teletype.addTextToElement(listitemelement2_paragraph, listitemelement2_content)
#        listitemelement2.addElement(listitemelement2_paragraph)
##        numberlist.addElement(listitemelement2)
##
#        self._textdoc.text.addElement(numberlist)

        # Adding a tabbed sentence to check tabstop
#        newtext = "Testing\tTabstops"
#        tabp = P(stylename=tabparagraphstyle)
#        teletype.addTextToElement(tabp, newtext)
#        self._textdoc.text.addElement(tabp)

        self._textdoc.save(u"/tmp/save-the-cat.odt")


#from odf.opendocument import OpenDocumentText
#from odf.text import P    
#self._textdoc = OpenDocumentText()
#p = P(text="Hello World!")
#self._textdoc.text.addElement(p)
#self._textdoc.save("helloworld", True)
#
# https://gist.github.com/balasankarc/1832670ec8ddd9a34d33
# https://balasankarc.in/tech/using-python-and-odfpy-to-create-open-document-texts.html

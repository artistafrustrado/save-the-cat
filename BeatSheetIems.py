#!/usr/bin/pyhon

import sys
import random
from PySide6 import QtGui
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6 import QtCore, QtWidgets, QtGui


class BeatSheetItemWidget(QWidget):
    title = "Example Title"
    _type = "opening-image"
    text = "Example Text"

    def __init__(self):
        super().__init__()

    def setUI(self):
        self.hello = ["Hello World","Hei maailma","Hola Mundo", "Can't type that"]

        self.setStyleSheet("QLabel { color: #FFFFFF; font-size: 11px; background-color: #000000; padding: 5px;}")
        #self.setStyleSheet("QLabel { color: #FFFFFF; font-size: 11px; background-color: #000000; border: 1px solid rgba(188, 188, 188, 250); } QSpinBox { color: rgb(50, 50, 50); font-size: 11px; background-color: rgba(255, 188, 20, 50); }")

        self._title = QLabel("<b>" + self.title + "</b>",alignment=QtCore.Qt.AlignCenter)
        self.button = QPushButton("Click Me!")
        #self.text = QLabel("Hello World",alignment=QtCore.Qt.AlignCenter)
        self._text = QTextEdit()
        self._text.setPlainText(self.text)
        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self._title)
        self.layout.addWidget(self._text)
#        self.layout.addWidget(self.button)

        self.setLayout(self.layout)

        self.button.clicked.connect(self.magic)

    @QtCore.Slot()
    def magic(self):
        self.text.setText(random.choice(self.hello))

    def serialize(self):
        data = {"title": self.title, "type": self._type, "text": self._text.toPlainText()}
        return data

    def setType(self, string_type):
        self._type = string_type

    def getType(self):
        return self._type

    def setText(self, text):
        self.text = text
        self._text.setPlainText(self.text)
    
    def setTitle(self, title):
        self.title = title


class BeatSheetItemOpenImageWidget(BeatSheetItemWidget):
    def __init__(self):
        super().__init__()
        self.title = "Opening Image"
        self._type = "opening-image"
        self.setUI()

class BeatSheetItemThemwStatedWidget(BeatSheetItemWidget):
    def __init__(self):
        super().__init__()
        self.title = "Theme Stated"
        self._type = "theme-stated"
        self.setUI()

class BeatSheetItemSetupWidget(BeatSheetItemWidget):
    def __init__(self):
        super().__init__()
        self.title = "Setup"
        self._type = "setup"
        self.setUI()


class BeatSheetItemCatalystWidget(BeatSheetItemWidget):
    def __init__(self):
        super().__init__()
        self.title = "Catalyst"
        self._type = "catalyst"
        self.setUI()

class BeatSheetItemDebateWidget(BeatSheetItemWidget):
    def __init__(self):
        super().__init__()
        self.title = "Debate"
        self._type = "debate"
        self.setUI()

class BeatSheetItemBreakeInto2Widget(BeatSheetItemWidget):
    def __init__(self):
        super().__init__()
        self.title = "Break into 2"
        self._type = "break-into-2"
        self.setUI()

class BeatSheetItemFunAndGamesWidget(BeatSheetItemWidget):
    def __init__(self):
        super().__init__()
        self.title = "Fun and Games"
        self._type = "fun-and-games"
        self.setUI()

class BeatSheetItemMidpointWidget(BeatSheetItemWidget):
    def __init__(self):
        super().__init__()
        self.title = "Midpoint"
        self._type = "midpoint"
        self.setUI()

class BeatSheetItemBadGuysCloseInWidget(BeatSheetItemWidget):
    def __init__(self):
        super().__init__()
        self.title = "Bad Gyus Close In"
        self._type = "bad-gyus-close-in"
        self.setUI()


class BeatSheetItemAllIsLostWidget(BeatSheetItemWidget):
    def __init__(self):
        super().__init__()
        self.title = "All is Lost"
        self._type = "all-is-lost"
        self.setUI()


class BeatSheetItemDarkNoghtOfTheSoulWidget(BeatSheetItemWidget):
    def __init__(self):
        super().__init__()
        self.title = "Dark Night of the Soul"
        self._type = "dark-night-of-the soul"
        self.setUI()


class BeatSheetItemBreakInto3Widget(BeatSheetItemWidget):
    def __init__(self):
        super().__init__()
        self.title = "Break Into 3"
        self._type = "break-into-3"
        self.setUI()


class BeatSheetItemGatheringTheTeamWidget(BeatSheetItemWidget):
    def __init__(self):
        super().__init__()
        self.title = "Gathering the Team"
        self._type = "gathering-the-team"
        self.setUI()


class BeatSheetItemStormingTheCastleWidget(BeatSheetItemWidget):
    def __init__(self):
        super().__init__()
        self.title = "Storming the Castle"
        self._type = "storming-the-castle"
        self.setUI()


class BeatSheetItemHightoweSurpriseWidget(BeatSheetItemWidget):
    def __init__(self):
        super().__init__()
        self.title = "Hightower Surprise"
        self._type = "hightower-surprise"
        self.setUI()


class BeatSheetItemDigDeepDownWidget(BeatSheetItemWidget):
    def __init__(self):
        super().__init__()
        self.title = "Dig Deep Down"
        self._type = "dig-deep-down"
        self.setUI()



class BeatSheetItemExecutingThePlanWidget(BeatSheetItemWidget):
    def __init__(self):
        super().__init__()
        self.title = "Executing the Plan"
        self._type = "executing-the-plan"
        self.setUI()



class BeatSheetItemFinalImageWidget(BeatSheetItemWidget):
    def __init__(self):
        super().__init__()
        self.title = "Final Image"
        self._type = "final-image"
        self.setUI()


class BeatSheetLogLineWidget(QWidget):
    title = "Logline"
    _type = "logline"
    text = "Logline"

    def __init__(self):
        super().__init__()
        self.setUI()

    def setUI(self):
        self.hello = ["Hello World","Hei maailma","Hola Mundo", "Can't type that"]

        self.setStyleSheet("QLabel { color: #FFFFFF; font-size: 11px; background-color: #000000; padding: 5px;}")

        self._title = QLabel("<b>" + self.title + "</b>",alignment=QtCore.Qt.AlignCenter)
        self.button = QPushButton("Click Me!")
        self._text = QTextEdit()
        self._text.setPlainText(self.text)
        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self._title)
        self.layout.addWidget(self._text)
#        self.layout.addWidget(self.button)

        self.setLayout(self.layout)

        self.button.clicked.connect(self.magic)

    @QtCore.Slot()
    def magic(self):
        self.text.setText(random.choice(self.hello))

    def getLogLine(self): 
        return self._text.toPlainText()

    def setLogLine(self, logline):
        self._text.setPlainText(logline)

#    def serialize(self):
#        data = {"title": self.title, "type": self._type, "text": self._text.toPlainText()}
#        return data
#
#    def setType(self, string_type):
#        self._type = string_type
#
#    def getType(self):
#        return self._type
#
#    def setText(self, text):
#        self.text = text
#        self._text.setPlainText(self.text)
#    
#    def setTitle(self, title):
#        self.title = title


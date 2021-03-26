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

class BeatSheetItemThemwStatedWidget(BeatSheetItemWidget):
    def __init__(self):
        self.title = "Theme Stated"
        self.type = "theme-stated"
        super().__init__()

class BeatSheetItemSetupWidget(BeatSheetItemWidget):
    def __init__(self):
        self.title = "Setup"
        self.type = "setup"
        super().__init__()

class BeatSheetItemCatalystWidget(BeatSheetItemWidget):
    def __init__(self):
        self.title = "Catalyst"
        self.type = "catalyst"
        super().__init__()

class BeatSheetItemDebateWidget(BeatSheetItemWidget):
    def __init__(self):
        self.title = "Debate"
        self.type = "debate"
        super().__init__()

class BeatSheetItemBreakeInto2Widget(BeatSheetItemWidget):
    def __init__(self):
        self.title = "Break into 2"
        self.type = "break-into-2"
        super().__init__()

class BeatSheetItemFunAndGamesWidget(BeatSheetItemWidget):
    def __init__(self):
        self.title = "Fun and Games"
        self.type = "fun-and-games"
        super().__init__()

class BeatSheetItemMidpointWidget(BeatSheetItemWidget):
    def __init__(self):
        self.title = "Midpoint"
        self.type = "midpoint"
        super().__init__()

class BeatSheetItemBadGuysCloseInWidget(BeatSheetItemWidget):
    def __init__(self):
        self.title = "Bad Gyus Close In"
        self.type = "bad-gyus-close-in"
        super().__init__()

class BeatSheetItemAllIsLostWidget(BeatSheetItemWidget):
    def __init__(self):
        self.title = "All is Lost"
        self.type = "all-is-lost"
        super().__init__()

class BeatSheetItemDarkNoghtOfTheSoulWidget(BeatSheetItemWidget):
    def __init__(self):
        self.title = "Dark Night of the Soul"
        self.type = "dark-night-of-the soul"
        super().__init__()

class BeatSheetItemBreakInto3Widget(BeatSheetItemWidget):
    def __init__(self):
        self.title = "Break Into 3"
        self.type = "break-into-3"
        super().__init__()

class BeatSheetItemGatheringTheTeamWidget(BeatSheetItemWidget):
    def __init__(self):
        self.title = "Gathering the Team"
        self.type = "gathering-the-team"
        super().__init__()

class BeatSheetItemStormingTheCastleWidget(BeatSheetItemWidget):
    def __init__(self):
        self.title = "Storming the Castle"
        self.type = "storming-the-castle"
        super().__init__()

class BeatSheetItemHightoweSurpriseWidget(BeatSheetItemWidget):
    def __init__(self):
        self.title = "Hightower Surprise"
        self.type = "hightower-surprise"
        super().__init__()

class BeatSheetItemDigDeepDownWidget(BeatSheetItemWidget):
    def __init__(self):
        self.title = "Dig Deep Down"
        self.type = "dig-deep-down"
        super().__init__()


class BeatSheetItemExecutingThePlanWidget(BeatSheetItemWidget):
    def __init__(self):
        self.title = "Executing the Plan"
        self.type = "executing-the-plan"
        super().__init__()


class BeatSheetItemFinalImageWidget(BeatSheetItemWidget):
    def __init__(self):
        self.title = "Final Image"
        self.type = "final-image"
        super().__init__()


#!/usr/bin/python

import sys
import random
from PySide6 import QtCore, QtWidgets, QtGui

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.hello = ["Hello World","Hei maailma","Hola Mundo", "Can't type that"]

        self.button = QtWidgets.QPushButton("Click Me!")
        self.text = QtWidgets.QLabel("Hello World",alignment=QtCore.Qt.AlignCenter)
        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.button)

        self.button.clicked.connect(self.magic)

    @QtCore.Slot()
    def magic(self):
        self.text.setText(random.choice(self.hello))


if __name__ == '__main__':

    app = QtWidgets.QApplication([])

    File = QtCore.QFile("resources/stye.qss")
#        if nof File.open( QtCore.QFile.ReadOnly | QtCore.QFile.Text):
#            return
#    with File.open(QtCore.QFile.Text):
    File.open(QtCore.QFile.ReadOnly)
    qss = QtCore.QTextStream(File)
	#setup stylesheet
    app.setStyleSheet(qss.readAll())

    widget = MyWidget()
    widget.resize(800,600)
    widget.show()

    sys.exit(app.exec_())


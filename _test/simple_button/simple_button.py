#!/usr/bin/python

import sys
from PySide2.QtWidgets import QApplication, QPushButton
from PySide2.QtCore import Slot


@Slot()
def say_hello():
    print("Button clicked, Hello!")


# Create the Qt Application
app = QApplication(sys.argv)
# Create a button, connect it and show it
button = QPushButton("Click me")
button.clicked.connect(say_hello)
button.show()
# Run the main Qt loop
app.exec_()

# so qml is basically css for qt applications

# a function that is attached to a button's "clicked" signal must be decorated with "@Slot()"

# -*- coding: utf-8 -*-
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from video import VideoReader
from interface import Ui_ventanaPrincipal

#cine2 = VideoSaver('D:/aire2.cine', 'D:/imagenes2/', stream=True, verbose=False)
#uic.loadUi('C:/Users/malopez/Desktop/mainwindow.ui')
"""
pyuic5 mainwindow.ui --output mainW.py
"""

class GuiEvents():
    """ In this class we load the interface stored at interface.py and define
        the events and connections linked to the actions performed to the 
        different widgets (ex: click a button, etc) """
    def __init__(self, dialog):
        """ This method is executed when creating an instance of the class """
        # We create an instance of the QT GUI Interface and store it as an
        # attribute of the main class (so that is easy to access from the
        # other methods of this class)
        self.gui = Ui_ventanaPrincipal()
        # We pass the dialog object to the setupUi method of the GUI, it fills
        # the dialog with the widgets and other elements of the interface
        self.gui.setupUi(dialog)
 
        # Connects "add" saveAsImages_button with a custom function (printMsg)
        self.gui.saveAsImages_button.clicked.connect(self.saveImg)
        self.gui.close_button.clicked.connect(self.closeWindow)
 
    def saveImg(self):
        videoPelotas = VideoReader('D:/aire2.cine')
        videoPelotas.cropVideo(0,790,300,1190)
        videoPelotas.saveAsImages('D:/imagenes2/', stream=True, verbose=False)
        self.gui.status_label.setText("Prueba")
    
    def closeWindow(self):
        pass

# This script needs to be executed form command line (errors if from IDE)
# A PyQt5 application is created
app = QtWidgets.QApplication(sys.argv)
# We create a QDialog object to show our GUI interface
dialog = QtWidgets.QDialog()
# We pass this dialog object as an argument to the main class
program = GuiEvents(dialog)
# Showing the main window until an exec condition is met
dialog.show()
sys.exit(app.exec_())
# -*- coding: utf-8 -*-
import sys
import threading
import PyQt5
from PyQt5 import QtCore, QtGui, QtWidgets
from video import VideoReader
from interface import Ui_ventanaPrincipal

# This line makes the app look good on hiDPI screens
PyQt5.QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)

class GuiEvents(Ui_ventanaPrincipal):
    """ In this class we load the interface stored at interface.py (it
        inherits from the interface class) and define the events and 
        connections linked to the actions performed to the different widgets 
        (ex: click a button, etc) """
    
    def __init__(self, dialog):
        """ This method is executed when creating an instance of the class """
        # We create an instance of the QT GUI Interface (so that is easy 
        # to access from the other methods of this class)
        Ui_ventanaPrincipal.__init__(self)
        # We pass the dialog object to the setupUi method of the GUI, it fills
        # the dialog with the widgets and other elements of the interface
        self.setupUi(dialog)
 
        # Connects "add" saveAsImages_button with a custom function (printMsg)
        self.saveAsImages_button.clicked.connect(self.saveAsImg)
        self.play_button.clicked.connect(self.play)
        self.close_button.clicked.connect(self.closeWindow) 
    

    def saveAsImg(self):
        """ Here we define what happens when pressing the save button """
        # TODO: error when stream==False the interface hangs, saveAsImages()
        # TODO: function should be called in a separate thread
        stream = self.stream_button.isChecked()
        verbose=False
        img_folder = 'D:/imagenes2/'

#
QtCore.QThread.run()     
  
        videoPelotas = VideoReader('D:/aire2.cine')
        videoPelotas.cropVideo(0,790,300,1190)
        self.status_label.setText("Prueba")
        self.saveAsImages_progressBar.setValue(5)
        
        """
        # Launching the function in a new thread so that it doesn't hangs te gui
        new_thread = threading.Thread(target=videoPelotas.saveAsImages(img_folder, verbose), args=())
        new_thread.daemon = True # Daemonize thread
        new_thread.start() # Start the execution
        """
        videoPelotas.saveAsImages(img_folder, verbose)
        
    def play(self):
        videoPelotas = VideoReader('D:/aire2.cine')
        videoPelotas.cropVideo(0,790,300,1190)
        videoPelotas.playVideo()
    
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
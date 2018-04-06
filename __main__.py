# -*- coding: utf-8 -*-
import sys
import threading
import PyQt5
from PyQt5 import QtCore, QtGui, QtWidgets
from video import VideoReader
from interface import Ui_ventanaPrincipal

from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog
from PyQt5.QtGui import QIcon

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
        self.selectFile_button.clicked.connect(self.selectFile)
        
    
    def saveAsImg(self):
        worker = SaveAsImgThread(self)
        worker.run()
        

#    def saveAsImg(self):
        """ Here we define what happens when pressing the save button """
        # TODO: error when stream==False the interface hangs, saveAsImages()
        # TODO: function should be called in a separate thread
#        stream = self.stream_button.isChecked()
#        verbose=False
#        img_folder = 'D:/imagenes2/'   
  
#        videoPelotas = VideoReader('D:/aire2.cine')
#        videoPelotas.cropVideo(0,790,300,1190)
#        self.status_label.setText("Prueba")
#        self.saveAsImages_progressBar.setValue(5)
        
        """
        # Launching the function in a new thread so that it doesn't hangs te gui
        new_thread = threading.Thread(target=videoPelotas.saveAsImages(img_folder, verbose), args=())
        new_thread.daemon = True # Daemonize thread
        new_thread.start() # Start the execution
        """
#        videoPelotas.saveAsImages(img_folder, verbose)
       
    def play(self):
        if self.filePath_edit.text == None:
            pass
        else:
            videoPelotas = VideoReader('D:/aire2.cine')#'D:/aire2.cine'
            videoPelotas.cropVideo(0,790,300,1190)
            videoPelotas.playVideo()
    
    def selectFile(self):
        fileDialog = SelectFileDialog()
        filePath = fileDialog.initUI()
        self.filePath_edit.setText(filePath)       
    
    def closeWindow(self):
        pass






class SaveAsImgThread(QtCore.QThread): #QtCore.QObject
    def __init__(self, GuiEvents):
        #super().__init__() # inits the parent class
        self.gui = GuiEvents
    def run(self):
        """ Here we define what happens when pressing the save button """
        # TODO: error the interface hangs, saveAsImages()
        # TODO: function should be called in a separate thread

        verbose=False
        img_folder = 'D:/imagenes2/'    
  
        videoPelotas = VideoReader('D:/aire2.cine')
        videoPelotas.cropVideo(0,790,300,1190)
        self.gui.status_label.setText("Prueba")
        self.gui.saveAsImages_progressBar.setValue(int(100*videoPelotas.currentFrame_save/videoPelotas.frameCount))

        videoPelotas.saveAsImages(img_folder, verbose)        





 
class SelectFileDialog(QWidget):
 
    def __init__(self):
        super().__init__()
        self.title = 'Seleccionar archivo de Video'
        self.left = 10
        self.top = 10
        self.width = 800
        self.height = 600

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
 
        result = self.openFileNameDialog()
        #self.openFileNamesDialog()
        #self.saveFileDialog()
 
        self.show()
        return result
 
    def openFileNameDialog(self):    
        options = QFileDialog.Options()
        #options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self,"Selecciona un archivo de video", "","All Files (*);;Python Files (*.py)", options=options)
        if fileName:
            return fileName
 
    def openFileNamesDialog(self):    
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        files, _ = QFileDialog.getOpenFileNames(self,"QFileDialog.getOpenFileNames()", "","All Files (*);;Python Files (*.py)", options=options)
        if files:
            print(files)
 
    def saveFileDialog(self):    
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getSaveFileName(self,"QFileDialog.getSaveFileName()","","All Files (*);;Text Files (*.txt)", options=options)
        if fileName:
            print(fileName)






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
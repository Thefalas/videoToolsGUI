# -*- coding: utf-8 -*-
import multiprocessing as mp
import sys
import os
import threading
import cv2
import pims
import PyQt5
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QFileDialog
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
        self.selectFile_button.clicked.connect(self.selectFile)
        self.refreshData_button.clicked.connect(self.refreshInfo)
        self.playFps_slider.valueChanged.connect(self.updatePlayLength)
        self.selectFolder_button.clicked.connect(self.selectFolder)
        
        self.folderPath_edit.textChanged.connect(self.enableButtons)
        self.filePath_edit.textChanged.connect(self.enableButtons)
        
        # Initializing a value for communicating with saveAsImages process
        # and store te percentage of video currently saved to images
        self.percentSaved = mp.Value('i', 0)
        
        # We create a timer that will tick every 1000 ms to update the progress
        # bar (and possibly other tasks)
        self.timer = QtCore.QTimer()
        self.timer.setInterval(1000)
        self.timer.start()
        self.timer.timeout.connect(self.updateProgressBar)
        
        
    def enableButtons(self):
        if os.path.isfile(self.filePath_edit.text()):
            self.play_button.setDisabled(False)
        else:
            self.play_button.setDisabled(True)
        if os.path.isdir(self.folderPath_edit.text()) and os.path.isfile(self.filePath_edit.text()):
            self.saveAsImages_button.setDisabled(False)
        else:
            self.saveAsImages_button.setDisabled(True)
  
    
    def saveAsImg(self):
        """ Here we define what happens when pressing the save button """
        if os.path.isdir(self.folderPath_edit.text()) and os.path.isfile(self.filePath_edit.text()): # If directory  and file exists:
            img_folder = self.folderPath_edit.text() + '/' # 'D:/imagenes2/'
            verbose = False
            
            videoPath = self.filePath_edit.text()
            
            crop = (self.minHeight_slider.value(),
                    self.maxHeight_slider.value(),
                    self.minWidth_slider.value(),
                    self.maxWidth_slider.value())
       
            # A new process is created to save the video to images, this process
            # is run as a daemon and prevents the GUI from hanging meanwhile
            p = mp.Process(target=saveAsImg_Process, args=(videoPath, img_folder, crop, verbose, self.percentSaved,))
            p.daemon = True
            p.start()
            #p.join()
            #p.terminate()
            print('New process started, saving images to:')
            print('Process alive: ' + str(p.is_alive()))
        else:
            print('Incorrect or inexistent folder selected')
            print(self.folderPath_edit.text()+'/')            
        
            
    def updateProgressBar(self):
        self.saveAsImages_progressBar.setValue(self.percentSaved.value)
        
    
    def refreshInfo(self):
        try:
            video = VideoReader(self.filePath_edit.text())
            self.recSpeed_label.setText('Recording Speed: '+str(video.recordingSpeed)+' fps')
            self.width_label.setText('Width: '+str(video.width)+' px')
            self.height_label.setText('Height: '+str(video.height)+' px')
            self.frameCount_label.setText('Frame Count: '+str(video.frameCount))
            self.realTime_label.setText('Recorded Time: '+'{:.2f}'.format(video.realRecordedTime)+' s')
            self.recDate_label.setText('Recording Date: '+video.recordingDate.strftime("%d %b %Y %H:%M"))
            
            self.updatePlayLength()
            
            self.maxHeight_slider.setMaximum(video.height)
            self.maxWidth_slider.setMaximum(video.width)
            
            #self.playFps_slider.setMaximum(video.recordingSpeed)
        except:
            print('Incorrect or empty file selected')
            print(self.filePath_edit.text())
            # Return values to default
            self.recSpeed_label.setText('Recording Speed: ')
            self.width_label.setText('Width: ')
            self.height_label.setText('Height: ')
            self.frameCount_label.setText('Frame Count: ')
            self.realTime_label.setText('Recorded Time: ')
            self.recDate_label.setText('Recording Date: ')
            self.playLength_label.setText('Video Length: ')

         
            
    def updatePlayLength(self):
        """ This function updates te labels indicating video length when played """
        try:
            video = VideoReader(self.filePath_edit.text())
            t = video.frameCount/self.playFps_slider.value()
            multiplier = '{:.1f}'.format(video.recordingSpeed/self.playFps_slider.value())
            self.playLength_label.setText('Video Length: '+ '{:.2f}'.format(t)+' s ('+multiplier+'X)')
        except:
            print('Incorrect or empty file selected')
            print(self.filePath_edit.text()) 
       
        
    def play(self):
        try:
            fps = self.playFps_slider.value()
            videoPelotas = VideoReader(self.filePath_edit.text())#'D:/aire2.cine'
            videoPelotas.cropVideo(self.minHeight_slider.value(),
                                   self.maxHeight_slider.value(),
                                   self.minWidth_slider.value(),
                                   self.maxWidth_slider.value()) #0,790,300,1190
            videoPelotas.playVideo(fps)
        except:
            print('Incorrect or empty file selected')
            print(self.filePath_edit.text())
    
    
    def selectFile(self):
        fileDialog = SelectFileDialog()
        filePath = fileDialog.initUI()
        self.filePath_edit.setText(filePath)
        
        
    def selectFolder(self):
        folderDialog = SelectFolderDialog()
        folderPath = folderDialog.initUI()
        self.folderPath_edit.setText(folderPath)
    
    
    def closeWindow(self):
        pass




def saveAsImg_Process(videoPath, img_folder, crop, verbose, percentSaved):
    """ Here we define what happens when pressing the save button. 
        This method executes u¡in a new process """

    #verbose=False
    #img_folder = 'D:/imagenes2/'    

    video = VideoReader(videoPath)
    frameCount = video.frameCount

    video = cv2.VideoCapture(videoPath)        
        
    i = 0
    while(video.isOpened()):
        # Leemos el frame actual y lo asignamos a la variable frame
        ret, frame = video.read()
        # Recorto el frame a la zona que me interesa (es simplemente operar 
        # con arrays de numpy)
        frame_crop = frame[crop[0]:crop[1], crop[2]:crop[3]]
        # Guardo el frame recortado a una imagen
        path = img_folder + 'img' + "{:06d}".format(i) + '.png'
        cv2.imwrite(path, frame_crop)
            
        i+=1
        # Guardamos el porcentaje que llevamos completado en una variable
        # compartida entre este proceso y el principal
        percentSaved.value = int(100*i/frameCount)          
        if verbose == True:
            percent = " - " + "{:.2f}".format(100*i/frameCount) + " %"
            print("Frame nº: " + str(i)+" / "+str(frameCount) + percent)

    # Cerramos el stream de video
    video.release()





class SelectFolderDialog(QWidget):
 
    def __init__(self):
        super().__init__()
        self.title = 'Seleccionar Carpeta'
        self.left = 10
        self.top = 10
        self.width = 800
        self.height = 600

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
 
        result = self.openFolderDialog() 
        self.show()
        
        return result
 
    def openFolderDialog(self):    
        options = QFileDialog.Options()
        #options |= QFileDialog.DontUseNativeDialog
        folder = QFileDialog.getExistingDirectory(self, "Seleccionar Carpeta", "", options=options)
        if folder:
            return folder


 
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
        fileName, _ = QFileDialog.getOpenFileName(self,"Selecciona un archivo de video", "","Cine Files (*.cine);;All Files (*)", options=options)
        #folder, _ = QFileDialog.getExistingDirectory(self, " kkk", "",options=options)
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





if __name__ == '__main__':
    # This script needs to be executed form command line (errors if from IDE)
    # A PyQt5 application is created
    app = QtWidgets.QApplication(sys.argv)
    # app.setStyleSheet(open('C:/Users/malopez/Desktop/videoToolsGUI/theme.stylesheet').read())
    # We create a QDialog object to show our GUI interface
    dialog = QtWidgets.QDialog()
    # We pass this dialog object as an argument to the main class
    program = GuiEvents(dialog)
    # Showing the main window until an exec condition is met
    dialog.show()
    sys.exit(app.exec_())
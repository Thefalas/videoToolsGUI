# -*- coding: utf-8 -*-
import os
import cv2 # OpenCV
import pims
import numpy as np


class VideoReader():

    def __init__(self, filePath):
        
        self.filePath = filePath
        
        video = pims.open(self.filePath)
        
        self.currentFrame_save = 0 # When saving, keeps track of progress
        self.currentFrame_play = 0 # When playing, keeps track of progress
        self.height = video.frame_shape[1]
        self.width = video.frame_shape[0]
        
        self.minHeight = 0
        self.maxHeight = self.height
        self.minWidth = 0
        self.maxWidth = self.width
        
        self.recordingSpeed = video.frame_rate
        try:
            self.frameCount = video.len()
            self.realRecordedTime = video.get_time(video.len()-1)
            self.recordingDate = video.frame_time_stamps[0][0]
        except:
            # Support for more video formats is needed
            self.frameCount = 0
            self.realRecordedTime = 0
            self.recordingDate = 0
            
    def cropVideo(self, minHeight='none', maxHeight='none', 
                  minWidth='none', maxWidth='none'):
        
        if minHeight == 'none':
            self.minHeight = 0
        else:
            self.minHeight = minHeight            
        if maxHeight == 'none':
            self.maxHeight = self.height
        else:
            self.maxHeight = maxHeight
         
        if minWidth == 'none':
            self.minWidth = 0
        else:
            self.minWidth = minWidth
        if maxWidth == 'none':
            self.maxWidth = self.width
        else:
            self.maxWidth = maxWidth        

    def saveAsImages(self, img_folder, verbose=False):
        
        video = cv2.VideoCapture(self.filePath)
        
        self.currentFrame_save = 0
        while(video.isOpened()):
            # Leemos el frame actual y lo asignamos a la variable frame
            ret, frame = video.read()
            # Recorto el frame a la zona que me interesa (es simplemente operar 
            # con arrays de numpy)
            frame_crop = frame[self.minHeight:self.maxHeight, self.minWidth:self.maxWidth]
            # Guardo el frame recortado a una imagen
            path = img_folder + 'img' + "{:06d}".format(self.currentFrame_save) + '.png'
            cv2.imwrite(path, frame_crop)
            
            self.currentFrame_save+=1            
            if verbose == True:
                percent = " - " + "{:.2f}".format(100*self.currentFrame_save/self.frameCount) + " %"
                print("Frame nº: " + str(self.currentFrame_save)+" / "+str(self.frameCount) + percent)

        # Cerramos el stream de video
        video.release()


    def playVideo(self, fps=1):
        
        waitTime = int(1000/fps)
        
        video = cv2.VideoCapture(self.filePath)

        self.currentFrame_play = 0
        while(video.isOpened()):
            # Leemos el frame actual y lo asignamos a la variable frame
            ret, frame = video.read()
            # Recorto el frame a la zona que me interesa (es simplemente operar 
            # con arrays de numpy)
            frame_crop = frame[self.minHeight:self.maxHeight, self.minWidth:self.maxWidth]
            
            self.currentFrame_play+=1
            # Mostramos en pantalla el video (esperando 3ms entre frame y frame) 
            # hasta que llega al final o se pulsa la tecla q
            cv2.imshow('Video', frame_crop)
            if cv2.waitKey(waitTime) & 0xFF == ord('q'):
                break
#           video.release()
#           cv2.destroyAllWindows()
                
        # Cerramos el stream de video y las ventanas abiertas
        video.release()
        cv2.destroyAllWindows()
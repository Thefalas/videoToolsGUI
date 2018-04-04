# -*- coding: utf-8 -*-
import os
import cv2 # OpenCV
import pims
import numpy as np

class VideoReader():

    def __init__(self, videoFile):
        
        self.videoFile = videoFile
        
        video = pims.open(self.videoFile)
        # Calculamos el numero de frames del video (seguramente haya una manera mejor
        # de hacerlo usando OpenCV en lugar de pims)
        self.frameCount = len(video)
        
        self.minHeight = 0
        self.maxHeight = np.shape(video[0])[0]
        self.minWidth = 0
        self.maxWidth = np.shape(video[0])[1]
            
    def cropVideo(self, minHeight='none', maxHeight='none', 
                  minWidth='none', maxWidth='none'):
        
        video = pims.open(self.videoFile)
        
        if minHeight == 'none':
            self.minHeight = 0
        else:
            self.minHeight = minHeight            
        if maxHeight == 'none':
            self.maxHeight = np.shape(video[0])[0]
        else:
            self.maxHeight = maxHeight
         
        if minWidth == 'none':
            self.minWidth = 0
        else:
            self.minWidth = minWidth
        if maxWidth == 'none':
            self.maxWidth = np.shape(video[0])[1]
        else:
            self.maxWidth = maxWidth        
        
    def saveAsImages(self, img_folder, stream=False, verbose=False):
        
        video = cv2.VideoCapture(self.videoFile)
        
        i = 0
        while(video.isOpened()):
            # Leemos el frame actual y lo asignamos a la variable frame
            ret, frame = video.read()
            # Recorto el frame a la zona que me interesa (es simplemente operar 
            # con arrays de numpy)
            frame_crop = frame[self.minHeight:self.maxHeight, self.minWidth:self.maxWidth]
            # Guardo el frame recortado a una imagen
            path = img_folder + 'img' + "{:06d}".format(i) + '.png'
            cv2.imwrite(path, frame_crop)
            i+=1
            
            if verbose == True:
                percent = " - " + "{:.2f}".format(100*i/self.frameCount) + " %"
                print("Frame nº: "+str(i)+" / "+str(self.frameCount) + percent)
            
            if stream == True:
                # Mostramos en pantalla el video (esperando 3ms entre frame y frame) 
                # hasta que llega al final o se pulsa la tecla q
                cv2.imshow('Video', frame_crop)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
        # Cerramos el stream de video y la ventana abierta
        video.release()
        cv2.destroyAllWindows()
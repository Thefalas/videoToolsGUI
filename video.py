# -*- coding: utf-8 -*-
import os
import cv2 # OpenCV
import pims
import numpy as np
import pandas as pd
import trackpy as tp


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
        
        
    def detectCircles(self, initialFrame, lastFrame):
        # We initialize an empty (actually just a row with zeros) pandas DataFrame
        # with the correct shape and types to store circles detected by OpenCV and 
        # later pass those to trackpy's linking function.
        # TODO: I'm sure there's a simpler way of doing this.
        A = np.zeros((1, 8), dtype=np.float64)
        B = np.zeros((1, 1), dtype=np.int64)
        names = ('x', 'y', 'mass', 'size', 'ecc', 'signal', 'raw_mass', 'ep')
        A = pd.DataFrame(A, index=('-1',), columns=names)
        B = pd.DataFrame(B, index=('-1',), columns=('frame',))
        circles_tp = pd.concat((A, B), axis=1)
        
        video = cv2.VideoCapture(self.filePath)
        
        c = 0 # Accumulator, increases each time a circle is detected
        n = 1 # Simple acumulador, para llevar la cuenta de por cual frame voy
        while(video.isOpened()):
            # Leemos el frame actual y lo asignamos a la variable frame
            frameExists, frame = video.read()
            
            if n<initialFrame+1:
                n+=1
                pass
            elif n>lastFrame+1:
                break
            else:
                # Recorto el frame a la zona que me interesa (es simplemente operar 
                # con arrays de numpy)
                frame_crop = frame[self.minHeight:self.maxHeight, self.minWidth:self.maxWidth]
                b_frame = cv2.medianBlur(frame_crop, 11)
                b_frame_gray = cv2.cvtColor(b_frame, cv2.COLOR_BGR2GRAY)
                # Detectamos los circulos dentro de una clausula try para evitar que el
                # programa se cierre cuando en algun frame no se localiza ningún 
                # círculo (en ese caso OpenCV lanza una excepcion)
                try:
                    circles = cv2.HoughCircles(b_frame_gray,cv2.HOUGH_GRADIENT,1,20,param1=50,
                                           param2=30,minRadius=55,maxRadius=72)
                    # Lo siguiente es necesario para que se dibujen los circulos
                    circles = np.uint16(np.around(circles))
        
                    # For each circle detected we add a new row to the circles_tp DataFrame
                    # After that, we draw a circle over the current frame image.
                    for i in circles[0]:
                        # We firstly extract (x, y) positions of the circle i
                        A = np.zeros((1, 8), dtype=np.float64)
                        A[0,0] = i[0] # x center
                        A[0,1] = i[1] # y center
                        A[0,3] = i[2] # diameter
                        # B (last column) equals the current frame number
                        B = n-1
                        names = ('x', 'y', 'mass', 'size', 'ecc', 'signal', 'raw_mass', 'ep')
                        A = pd.DataFrame(A, index=(str(c),), columns=names)
                        B = pd.DataFrame(B, index=(str(c),), columns=('frame',))
                        new_circle = pd.concat((A, B), axis=1)
                        circles_tp = pd.concat((circles_tp, new_circle), axis=0)
                        c+=1

                        # Draw the outer circle [(x,y), radius, rgb]
                        #cv2.circle(frame_crop,(i[0],i[1]),i[2],(200, 153, 102),2)
                        # Draw the center of the circle
                        #cv2.circle(frame_crop,(i[0],i[1]),2,(255, 255, 255),3)    
              
                except:
                    print('No circles detected in frame nº:')
    
            #cv2.imshow('detected circles',frame_crop)
        
                if cv2.waitKey(10) & 0xFF == ord('q'):
                    break
                n+=1 # Al acabar de procesar este frame aumentamos en 1 el acumulador

        # Cerramos el stream de video
        video.release()
        # We delete the first row of circles_tp, since it was only used for 
        # initialization and is no longer needed.
        circles_tp = circles_tp.drop('-1')
        return circles_tp
    
    
def linkTrajectories(circles_tp, removeDrift=False):
        
    trajectories = tp.link_df(circles_tp, 5, memory=10)
    if removeDrift == True:
        drift = tp.compute_drift(trajectories)
        trajectories = tp.subtract_drift(trajectories.copy(), drift)
            
    return trajectories
    
    
    
    
    
    
    
    """
    frames = pims.open('D:/imagenes2/img000000.png')
    frame = frames[0][:,:,0] #Para hacerlo greyscale
    f = tp.locate(frame, 55, minmass=20)
    tp.annotate(f, frame)
    """
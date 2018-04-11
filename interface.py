# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ventanaPrincipal(object):
    def setupUi(self, ventanaPrincipal):
        ventanaPrincipal.setObjectName("ventanaPrincipal")
        ventanaPrincipal.resize(592, 550)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ventanaPrincipal.sizePolicy().hasHeightForWidth())
        ventanaPrincipal.setSizePolicy(sizePolicy)
        self.saveAsImages_button = QtWidgets.QPushButton(ventanaPrincipal)
        self.saveAsImages_button.setEnabled(False)
        self.saveAsImages_button.setGeometry(QtCore.QRect(20, 130, 131, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.saveAsImages_button.sizePolicy().hasHeightForWidth())
        self.saveAsImages_button.setSizePolicy(sizePolicy)
        self.saveAsImages_button.setObjectName("saveAsImages_button")
        self.close_button = QtWidgets.QPushButton(ventanaPrincipal)
        self.close_button.setGeometry(QtCore.QRect(20, 420, 131, 51))
        self.close_button.setObjectName("close_button")
        self.status_label = QtWidgets.QLabel(ventanaPrincipal)
        self.status_label.setGeometry(QtCore.QRect(500, 10, 61, 20))
        self.status_label.setObjectName("status_label")
        self.play_button = QtWidgets.QPushButton(ventanaPrincipal)
        self.play_button.setEnabled(False)
        self.play_button.setGeometry(QtCore.QRect(20, 200, 131, 51))
        self.play_button.setCheckable(False)
        self.play_button.setObjectName("play_button")
        self.saveAsImages_progressBar = QtWidgets.QProgressBar(ventanaPrincipal)
        self.saveAsImages_progressBar.setGeometry(QtCore.QRect(170, 130, 341, 51))
        self.saveAsImages_progressBar.setProperty("value", 0)
        self.saveAsImages_progressBar.setObjectName("saveAsImages_progressBar")
        self.filePath_edit = QtWidgets.QLineEdit(ventanaPrincipal)
        self.filePath_edit.setGeometry(QtCore.QRect(20, 40, 401, 20))
        self.filePath_edit.setObjectName("filePath_edit")
        self.selectFile_button = QtWidgets.QPushButton(ventanaPrincipal)
        self.selectFile_button.setGeometry(QtCore.QRect(430, 40, 80, 21))
        self.selectFile_button.setObjectName("selectFile_button")
        self.videoFolder_label = QtWidgets.QLabel(ventanaPrincipal)
        self.videoFolder_label.setGeometry(QtCore.QRect(20, 20, 101, 16))
        self.videoFolder_label.setObjectName("videoFolder_label")
        self.graphicsView = QtWidgets.QGraphicsView(ventanaPrincipal)
        self.graphicsView.setGeometry(QtCore.QRect(170, 270, 341, 201))
        self.graphicsView.setObjectName("graphicsView")
        self.verticalLayoutWidget = QtWidgets.QWidget(ventanaPrincipal)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 270, 131, 131))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.infoLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.infoLayout.setContentsMargins(0, 0, 0, 0)
        self.infoLayout.setObjectName("infoLayout")
        self.refreshData_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.refreshData_button.setObjectName("refreshData_button")
        self.infoLayout.addWidget(self.refreshData_button)
        self.recDate_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.recDate_label.setObjectName("recDate_label")
        self.infoLayout.addWidget(self.recDate_label)
        self.frameCount_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.frameCount_label.setObjectName("frameCount_label")
        self.infoLayout.addWidget(self.frameCount_label)
        self.recSpeed_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.recSpeed_label.setObjectName("recSpeed_label")
        self.infoLayout.addWidget(self.recSpeed_label)
        self.realTime_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.realTime_label.setObjectName("realTime_label")
        self.infoLayout.addWidget(self.realTime_label)
        self.width_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.width_label.setObjectName("width_label")
        self.infoLayout.addWidget(self.width_label)
        self.height_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.height_label.setObjectName("height_label")
        self.infoLayout.addWidget(self.height_label)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(ventanaPrincipal)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(170, 200, 341, 51))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.fpsLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.fpsLayout.setContentsMargins(0, 0, 0, 0)
        self.fpsLayout.setObjectName("fpsLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.selectFps_label = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.selectFps_label.setObjectName("selectFps_label")
        self.horizontalLayout.addWidget(self.selectFps_label)
        self.playFps_label = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.playFps_label.setObjectName("playFps_label")
        self.horizontalLayout.addWidget(self.playFps_label)
        self.playLength_label = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.playLength_label.setObjectName("playLength_label")
        self.horizontalLayout.addWidget(self.playLength_label)
        self.fpsLayout.addLayout(self.horizontalLayout)
        self.playFps_slider = QtWidgets.QSlider(self.verticalLayoutWidget_2)
        self.playFps_slider.setMinimum(1)
        self.playFps_slider.setMaximum(120)
        self.playFps_slider.setProperty("value", 30)
        self.playFps_slider.setOrientation(QtCore.Qt.Horizontal)
        self.playFps_slider.setObjectName("playFps_slider")
        self.fpsLayout.addWidget(self.playFps_slider)
        self.folderPath_edit = QtWidgets.QLineEdit(ventanaPrincipal)
        self.folderPath_edit.setGeometry(QtCore.QRect(20, 90, 401, 20))
        self.folderPath_edit.setText("")
        self.folderPath_edit.setObjectName("folderPath_edit")
        self.selectFolder_button = QtWidgets.QPushButton(ventanaPrincipal)
        self.selectFolder_button.setGeometry(QtCore.QRect(430, 90, 80, 21))
        self.selectFolder_button.setObjectName("selectFolder_button")
        self.imagesFolder_label = QtWidgets.QLabel(ventanaPrincipal)
        self.imagesFolder_label.setGeometry(QtCore.QRect(20, 70, 121, 16))
        self.imagesFolder_label.setObjectName("imagesFolder_label")
        self.widget = QtWidgets.QWidget(ventanaPrincipal)
        self.widget.setGeometry(QtCore.QRect(510, 270, 51, 201))
        self.widget.setObjectName("widget")
        self.cropLayoutHS = QtWidgets.QHBoxLayout(self.widget)
        self.cropLayoutHS.setContentsMargins(0, 0, 0, 0)
        self.cropLayoutHS.setObjectName("cropLayoutHS")
        self.minHeight_slider = QtWidgets.QSlider(self.widget)
        self.minHeight_slider.setMaximum(800)
        self.minHeight_slider.setOrientation(QtCore.Qt.Vertical)
        self.minHeight_slider.setObjectName("minHeight_slider")
        self.cropLayoutHS.addWidget(self.minHeight_slider)
        self.maxHeight_slider = QtWidgets.QSlider(self.widget)
        self.maxHeight_slider.setMaximum(800)
        self.maxHeight_slider.setProperty("value", 800)
        self.maxHeight_slider.setOrientation(QtCore.Qt.Vertical)
        self.maxHeight_slider.setObjectName("maxHeight_slider")
        self.cropLayoutHS.addWidget(self.maxHeight_slider)
        self.widget1 = QtWidgets.QWidget(ventanaPrincipal)
        self.widget1.setGeometry(QtCore.QRect(170, 470, 341, 51))
        self.widget1.setObjectName("widget1")
        self.cropLayoutWS = QtWidgets.QVBoxLayout(self.widget1)
        self.cropLayoutWS.setContentsMargins(0, 0, 0, 0)
        self.cropLayoutWS.setObjectName("cropLayoutWS")
        self.minWidth_slider = QtWidgets.QSlider(self.widget1)
        self.minWidth_slider.setMaximum(1280)
        self.minWidth_slider.setOrientation(QtCore.Qt.Horizontal)
        self.minWidth_slider.setObjectName("minWidth_slider")
        self.cropLayoutWS.addWidget(self.minWidth_slider)
        self.maxWidth_slider = QtWidgets.QSlider(self.widget1)
        self.maxWidth_slider.setMaximum(1280)
        self.maxWidth_slider.setProperty("value", 1280)
        self.maxWidth_slider.setOrientation(QtCore.Qt.Horizontal)
        self.maxWidth_slider.setObjectName("maxWidth_slider")
        self.cropLayoutWS.addWidget(self.maxWidth_slider)
        self.widget2 = QtWidgets.QWidget(ventanaPrincipal)
        self.widget2.setGeometry(QtCore.QRect(150, 470, 21, 51))
        self.widget2.setObjectName("widget2")
        self.cropLayoutW = QtWidgets.QVBoxLayout(self.widget2)
        self.cropLayoutW.setContentsMargins(0, 0, 0, 0)
        self.cropLayoutW.setObjectName("cropLayoutW")
        self.label_4 = QtWidgets.QLabel(self.widget2)
        self.label_4.setObjectName("label_4")
        self.cropLayoutW.addWidget(self.label_4)
        self.label_3 = QtWidgets.QLabel(self.widget2)
        self.label_3.setObjectName("label_3")
        self.cropLayoutW.addWidget(self.label_3)
        self.widget3 = QtWidgets.QWidget(ventanaPrincipal)
        self.widget3.setGeometry(QtCore.QRect(510, 250, 51, 20))
        self.widget3.setObjectName("widget3")
        self.cropLayoutH = QtWidgets.QHBoxLayout(self.widget3)
        self.cropLayoutH.setContentsMargins(0, 0, 0, 0)
        self.cropLayoutH.setObjectName("cropLayoutH")
        self.label = QtWidgets.QLabel(self.widget3)
        self.label.setObjectName("label")
        self.cropLayoutH.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.widget3)
        self.label_2.setObjectName("label_2")
        self.cropLayoutH.addWidget(self.label_2)

        self.retranslateUi(ventanaPrincipal)
        self.filePath_edit.textChanged['QString'].connect(self.refreshData_button.click)
        self.playFps_slider.valueChanged['int'].connect(self.playFps_label.setNum)
        self.minHeight_slider.valueChanged['int'].connect(self.label.setNum)
        self.maxHeight_slider.valueChanged['int'].connect(self.label_2.setNum)
        self.minWidth_slider.valueChanged['int'].connect(self.label_4.setNum)
        self.maxWidth_slider.valueChanged['int'].connect(self.label_3.setNum)
        QtCore.QMetaObject.connectSlotsByName(ventanaPrincipal)

    def retranslateUi(self, ventanaPrincipal):
        _translate = QtCore.QCoreApplication.translate
        ventanaPrincipal.setWindowTitle(_translate("ventanaPrincipal", "Video Tools Alpha"))
        self.saveAsImages_button.setText(_translate("ventanaPrincipal", "Save Video as Images"))
        self.close_button.setText(_translate("ventanaPrincipal", "Close"))
        self.status_label.setText(_translate("ventanaPrincipal", "Status"))
        self.play_button.setText(_translate("ventanaPrincipal", "Play Video"))
        self.selectFile_button.setText(_translate("ventanaPrincipal", "Seleccionar"))
        self.videoFolder_label.setText(_translate("ventanaPrincipal", "Ruta al archivo de video:"))
        self.refreshData_button.setText(_translate("ventanaPrincipal", "Refresh Video Info"))
        self.recDate_label.setText(_translate("ventanaPrincipal", "Recording Date:"))
        self.frameCount_label.setText(_translate("ventanaPrincipal", "Frame Count: "))
        self.recSpeed_label.setText(_translate("ventanaPrincipal", "Recording Speed: "))
        self.realTime_label.setText(_translate("ventanaPrincipal", "Recorded Time:"))
        self.width_label.setText(_translate("ventanaPrincipal", "Width:"))
        self.height_label.setText(_translate("ventanaPrincipal", "Height:"))
        self.selectFps_label.setText(_translate("ventanaPrincipal", "Select Play framerate:"))
        self.playFps_label.setText(_translate("ventanaPrincipal", "30"))
        self.playLength_label.setText(_translate("ventanaPrincipal", "Video Length: "))
        self.selectFolder_button.setText(_translate("ventanaPrincipal", "Explorar"))
        self.imagesFolder_label.setText(_translate("ventanaPrincipal", "Ruta a la carpeta de imagenes:"))
        self.label_4.setText(_translate("ventanaPrincipal", "0"))
        self.label_3.setText(_translate("ventanaPrincipal", "1280"))
        self.label.setText(_translate("ventanaPrincipal", "0"))
        self.label_2.setText(_translate("ventanaPrincipal", "800"))


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
        ventanaPrincipal.resize(457, 403)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ventanaPrincipal.sizePolicy().hasHeightForWidth())
        ventanaPrincipal.setSizePolicy(sizePolicy)
        self.saveAsImages_button = QtWidgets.QPushButton(ventanaPrincipal)
        self.saveAsImages_button.setGeometry(QtCore.QRect(20, 60, 131, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.saveAsImages_button.sizePolicy().hasHeightForWidth())
        self.saveAsImages_button.setSizePolicy(sizePolicy)
        self.saveAsImages_button.setObjectName("saveAsImages_button")
        self.close_button = QtWidgets.QPushButton(ventanaPrincipal)
        self.close_button.setGeometry(QtCore.QRect(20, 200, 131, 51))
        self.close_button.setObjectName("close_button")
        self.status_label = QtWidgets.QLabel(ventanaPrincipal)
        self.status_label.setGeometry(QtCore.QRect(250, 360, 201, 41))
        self.status_label.setObjectName("status_label")
        self.stream_button = QtWidgets.QRadioButton(ventanaPrincipal)
        self.stream_button.setGeometry(QtCore.QRect(20, 30, 101, 16))
        self.stream_button.setObjectName("stream_button")
        self.play_button = QtWidgets.QPushButton(ventanaPrincipal)
        self.play_button.setGeometry(QtCore.QRect(20, 130, 131, 51))
        self.play_button.setObjectName("play_button")
        self.saveAsImages_progressBar = QtWidgets.QProgressBar(ventanaPrincipal)
        self.saveAsImages_progressBar.setGeometry(QtCore.QRect(170, 60, 261, 51))
        self.saveAsImages_progressBar.setProperty("value", 0)
        self.saveAsImages_progressBar.setObjectName("saveAsImages_progressBar")

        self.retranslateUi(ventanaPrincipal)
        QtCore.QMetaObject.connectSlotsByName(ventanaPrincipal)

    def retranslateUi(self, ventanaPrincipal):
        _translate = QtCore.QCoreApplication.translate
        ventanaPrincipal.setWindowTitle(_translate("ventanaPrincipal", "Dialog"))
        self.saveAsImages_button.setText(_translate("ventanaPrincipal", "Save Video as Images"))
        self.close_button.setText(_translate("ventanaPrincipal", "Close"))
        self.status_label.setText(_translate("ventanaPrincipal", "Status"))
        self.stream_button.setText(_translate("ventanaPrincipal", "Play video while saving"))
        self.play_button.setText(_translate("ventanaPrincipal", "Play Video"))


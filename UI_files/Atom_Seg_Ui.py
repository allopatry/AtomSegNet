# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AtomSeg_V1.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import PyQt5

if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
    PyQt5.QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)

if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
    PyQt5.QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)

class Ui_MainWindow(QtWidgets.QMainWindow):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1003, 1077)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.imagePath = QtWidgets.QTextEdit(self.centralwidget)
        self.imagePath.setEnabled(True)
        self.imagePath.setGeometry(QtCore.QRect(20, 30, 821, 31))
        self.imagePath.setObjectName("imagePath")
        self.open = QtWidgets.QPushButton(self.centralwidget)
        self.open.setGeometry(QtCore.QRect(880, 30, 91, 31))
        self.open.setObjectName("open")
        self.ori = QtWidgets.QLabel(self.centralwidget)
        self.ori.setGeometry(QtCore.QRect(20, 160, 410, 410))
        self.ori.setFrameShape(QtWidgets.QFrame.Box)
        self.ori.setText("")
        self.ori.setScaledContents(True)
        self.ori.setObjectName("ori")
        self.model_output = QtWidgets.QLabel(self.centralwidget)
        self.model_output.setGeometry(QtCore.QRect(440, 160, 410, 410))
        self.model_output.setFrameShape(QtWidgets.QFrame.Box)
        self.model_output.setText("")
        self.model_output.setScaledContents(True)
        self.model_output.setObjectName("model_output")
        self.preprocess = QtWidgets.QLabel(self.centralwidget)
        self.preprocess.setGeometry(QtCore.QRect(20, 580, 410, 410))
        self.preprocess.setFrameShape(QtWidgets.QFrame.Box)
        self.preprocess.setText("")
        self.preprocess.setScaledContents(True)
        self.preprocess.setObjectName("preprocess")
        self.detect_result = QtWidgets.QLabel(self.centralwidget)
        self.detect_result.setGeometry(QtCore.QRect(440, 580, 410, 410))
        self.detect_result.setFrameShape(QtWidgets.QFrame.Box)
        self.detect_result.setText("")
        self.detect_result.setScaledContents(True)
        self.detect_result.setObjectName("detect_result")
        self.modelPath = QtWidgets.QComboBox(self.centralwidget)
        self.modelPath.setGeometry(QtCore.QRect(20, 70, 821, 31))
        self.modelPath.setObjectName("modelPath")
        self.modelPath.addItem("")
        self.modelPath.addItem("")
        self.modelPath.addItem("")
        self.modelPath.addItem("")
        self.modelPath.addItem("")
        self.modelPath.addItem("")
        self.modelPath.addItem("")
        self.modelPath.addItem("")
        self.modelPath.addItem("")
        self.modelPath.addItem("")
        self.use_cuda = QtWidgets.QCheckBox(self.centralwidget)
        self.use_cuda.setGeometry(QtCore.QRect(860, 110, 131, 21))
        self.use_cuda.setChecked(True)
        self.use_cuda.setObjectName("use_cuda")
        self.se_num = QtWidgets.QSlider(self.centralwidget)
        self.se_num.setGeometry(QtCore.QRect(870, 340, 111, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.se_num.setFont(font)
        self.se_num.setMaximum(20)
        self.se_num.setOrientation(QtCore.Qt.Horizontal)
        self.se_num.setObjectName("se_num")
        self.save = QtWidgets.QPushButton(self.centralwidget)
        self.save.setGeometry(QtCore.QRect(880, 880, 91, 31))
        self.save.setObjectName("save")
        self.auto_save = QtWidgets.QCheckBox(self.centralwidget)
        self.auto_save.setGeometry(QtCore.QRect(880, 920, 101, 21))
        self.auto_save.setObjectName("auto_save")
        self.save_option = QtWidgets.QComboBox(self.centralwidget)
        self.save_option.setGeometry(QtCore.QRect(870, 830, 111, 31))
        self.save_option.setObjectName("save_option")
        self.save_option.addItem("")
        self.save_option.addItem("")
        self.save_option.addItem("")
        self.save_option.addItem("")
        self.save_option.addItem("")
        self.load = QtWidgets.QPushButton(self.centralwidget)
        self.load.setGeometry(QtCore.QRect(880, 70, 91, 31))
        self.load.setObjectName("load")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(870, 310, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(False)
        self.label.setFont(font)
        self.label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.circle_detect = QtWidgets.QPushButton(self.centralwidget)
        self.circle_detect.setGeometry(QtCore.QRect(880, 510, 91, 31))
        self.circle_detect.setObjectName("circle_detect")
        self.revert = QtWidgets.QPushButton(self.centralwidget)
        self.revert.setGeometry(QtCore.QRect(880, 570, 91, 31))
        self.revert.setObjectName("revert")
        self.split = QtWidgets.QCheckBox(self.centralwidget)
        self.split.setGeometry(QtCore.QRect(860, 130, 141, 21))
        self.split.setChecked(True)
        self.split.setObjectName("split")
        self.denoise_method = QtWidgets.QComboBox(self.centralwidget)
        self.denoise_method.setGeometry(QtCore.QRect(880, 280, 91, 23))
        self.denoise_method.setObjectName("denoise_method")
        self.denoise_method.addItem("")
        self.denoise_method.addItem("")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(860, 240, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(False)
        self.label_4.setFont(font)
        self.label_4.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.change_size = QtWidgets.QComboBox(self.centralwidget)
        self.change_size.setGeometry(QtCore.QRect(860, 180, 131, 23))
        self.change_size.setObjectName("change_size")
        self.change_size.addItem("")
        self.change_size.addItem("")
        self.change_size.addItem("")
        self.change_size.addItem("")
        self.change_size.addItem("")
        self.change_size.addItem("")
        self.change_size.addItem("")
        self.set_thre = QtWidgets.QCheckBox(self.centralwidget)
        self.set_thre.setGeometry(QtCore.QRect(880, 400, 111, 21))
        self.set_thre.setChecked(False)
        self.set_thre.setObjectName("set_thre")
        self.thre = QtWidgets.QLineEdit(self.centralwidget)
        self.thre.setGeometry(QtCore.QRect(890, 370, 61, 23))
        self.thre.setObjectName("thre")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(950, 370, 21, 23))
        self.lineEdit_2.setInputMask("")
        self.lineEdit_2.setFrame(False)
        self.lineEdit_2.setReadOnly(True)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.imagePath.raise_()
        self.open.raise_()
        self.ori.raise_()
        self.model_output.raise_()
        self.preprocess.raise_()
        self.detect_result.raise_()
        self.save.raise_()
        self.modelPath.raise_()
        self.se_num.raise_()
        self.auto_save.raise_()
        self.label.raise_()
        self.revert.raise_()
        self.load.raise_()
        self.circle_detect.raise_()
        self.use_cuda.raise_()
        self.save_option.raise_()
        self.split.raise_()
        self.denoise_method.raise_()
        self.label_4.raise_()
        self.change_size.raise_()
        self.set_thre.raise_()
        self.thre.raise_()
        self.lineEdit_2.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1003, 20))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Atom Segmentation"))
        self.open.setText(_translate("MainWindow", "OPEN"))
        self.modelPath.setWhatsThis(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.modelPath.setItemText(0, _translate("MainWindow", "circularMask_mse_beta"))
        self.modelPath.setItemText(1, _translate("MainWindow", "denoise&airysuperrez_beta"))
        self.modelPath.setItemText(2, _translate("MainWindow", "circularMask_chi10_beta"))
        self.modelPath.setItemText(3, _translate("MainWindow", "circularMask_chi100_beta"))
        self.modelPath.setItemText(4, _translate("MainWindow", "gaussianMask+"))
        self.modelPath.setItemText(5, _translate("MainWindow", "circularMask"))
        self.modelPath.setItemText(6, _translate("MainWindow", "guassianMask"))
        self.modelPath.setItemText(7, _translate("MainWindow", "denoise"))
        self.modelPath.setItemText(8, _translate("MainWindow", "denoise&bgremoval"))
        self.modelPath.setItemText(9, _translate("MainWindow", "denoise&bgremoval&superres"))
        self.use_cuda.setText(_translate("MainWindow", "Use CUDA"))
        self.save.setText(_translate("MainWindow", "SAVE"))
        self.auto_save.setText(_translate("MainWindow", "Auto Save"))
        self.save_option.setItemText(0, _translate("MainWindow", "Save ALL"))
        self.save_option.setItemText(1, _translate("MainWindow", "Model output"))
        self.save_option.setItemText(2, _translate("MainWindow", "Original image with markers"))
        self.save_option.setItemText(3, _translate("MainWindow", "Four-panel image"))
        self.save_option.setItemText(4, _translate("MainWindow", "Atom positions"))
        self.load.setText(_translate("MainWindow", "LOAD"))
        self.label.setText(_translate("MainWindow", "Disconnect Level"))
        self.circle_detect.setText(_translate("MainWindow", "DETECT"))
        self.revert.setText(_translate("MainWindow", "REVERT"))
        self.split.setText(_translate("MainWindow", "Split Automatically"))
        self.denoise_method.setItemText(0, _translate("MainWindow", "Opening"))
        self.denoise_method.setItemText(1, _translate("MainWindow", "Erosion"))
        self.label_4.setText(_translate("MainWindow", "Disconnect Method"))
        self.change_size.setItemText(0, _translate("MainWindow", "Do Nothing"))
        self.change_size.setItemText(1, _translate("MainWindow", "Down sample  by 2"))
        self.change_size.setItemText(2, _translate("MainWindow", "Up sample by 2"))
        self.change_size.setItemText(3, _translate("MainWindow", "Down sample by 3"))
        self.change_size.setItemText(4, _translate("MainWindow", "Up sample by 3"))
        self.change_size.setItemText(5, _translate("MainWindow", "Down sample by 4"))
        self.change_size.setItemText(6, _translate("MainWindow", "Up sample by 4"))
        self.set_thre.setText(_translate("MainWindow", "Set Threshold"))
        self.lineEdit_2.setText(_translate("MainWindow", "%"))

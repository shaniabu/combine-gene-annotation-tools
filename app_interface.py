# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'app_interface.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1024, 636)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 50, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.file_path = QtWidgets.QLineEdit(self.centralwidget)
        self.file_path.setGeometry(QtCore.QRect(150, 50, 651, 31))
        self.file_path.setObjectName("file_path")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 140, 651, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(150, 190, 58, 15))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(180, 180, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(290, 190, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(360, 190, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(450, 190, 51, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(510, 180, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(560, 180, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(150, 90, 251, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.Download = QtWidgets.QPushButton(self.centralwidget)
        self.Download.setGeometry(QtCore.QRect(590, 470, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.Download.setFont(font)
        self.Download.setObjectName("Download")
        self.MSC = QtWidgets.QPushButton(self.centralwidget)
        self.MSC.setGeometry(QtCore.QRect(90, 270, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.MSC.setFont(font)
        self.MSC.setObjectName("MSC")
        self.FATHMN = QtWidgets.QPushButton(self.centralwidget)
        self.FATHMN.setGeometry(QtCore.QRect(90, 340, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.FATHMN.setFont(font)
        self.FATHMN.setObjectName("FATHMM")
        self.PROVEAN = QtWidgets.QPushButton(self.centralwidget)
        self.PROVEAN.setGeometry(QtCore.QRect(90, 410, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.PROVEAN.setFont(font)
        self.PROVEAN.setObjectName("PROVEAN")
        self.Mutation = QtWidgets.QPushButton(self.centralwidget)
        self.Mutation.setGeometry(QtCore.QRect(90, 480, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.Mutation.setFont(font)
        self.Mutation.setObjectName("Mutation")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(250, 350, 541, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(290, 490, 211, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(250, 415, 501, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(250, 280, 461, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(470, 520, 321, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1024, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Upload file : "))
        self.label_2.setText(_translate("MainWindow", "資料格式為:  第一欄  第二欄  第三欄  第四欄  第五欄  第六欄  第七欄"))
        self.label_3.setText(_translate("MainWindow", "ID"))
        self.label_4.setText(_translate("MainWindow", "Chromosome"))
        self.label_5.setText(_translate("MainWindow", "Region"))
        self.label_6.setText(_translate("MainWindow", "Reference"))
        self.label_7.setText(_translate("MainWindow", "Allele"))
        self.label_8.setText(_translate("MainWindow", "Type"))
        self.label_9.setText(_translate("MainWindow", "Homo_sapiens_refseq"))
        self.label_10.setText(_translate("MainWindow", "輸入資料路徑，檔案需為excel"))
        self.Download.setText(_translate("MainWindow", "Export"))
        self.MSC.setText(_translate("MainWindow", "MSC"))
        self.FATHMN.setText(_translate("MainWindow", "FATHMM"))
        self.PROVEAN.setText(_translate("MainWindow", "PROVEAN"))
        self.Mutation.setText(_translate("MainWindow", "Mutation Assessor"))
        self.label_11.setText(_translate("MainWindow", "需要手動按下送出以及複製結果網頁成文字檔，檔名為Fathmn_result"))
        self.label_12.setText(_translate("MainWindow", "需要手動按下送出"))
        self.label_13.setText(_translate("MainWindow", "需要手動點選所需結果檔，並將之存成Provean_result的csv檔"))
        self.label_14.setText(_translate("MainWindow", "需自行新增MSC_result的csv檔"))
        self.label_15.setText(_translate("MainWindow", "將需要匯出之檔案放到相同目錄資料夾"))


# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Main.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

from MainController import AnaKontrolcu


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(384, 276)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/filter.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pbKutuk = QtWidgets.QPushButton(self.centralwidget)
        self.pbKutuk.setGeometry(QtCore.QRect(10, 20, 101, 71))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pbKutuk.setFont(font)
        self.pbKutuk.setObjectName("pbKutuk")
        self.pbCevap = QtWidgets.QPushButton(self.centralwidget)
        self.pbCevap.setGeometry(QtCore.QRect(120, 20, 111, 71))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pbCevap.setFont(font)
        self.pbCevap.setObjectName("pbCevap")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(250, 20, 121, 151))
        self.groupBox.setObjectName("groupBox")
        self.widget = QtWidgets.QWidget(self.groupBox)
        self.widget.setGeometry(QtCore.QRect(10, 20, 101, 121))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.cbTurkce = QtWidgets.QCheckBox(self.widget)
        self.cbTurkce.setObjectName("cbTurkce")
        self.verticalLayout.addWidget(self.cbTurkce)
        self.cbMat = QtWidgets.QCheckBox(self.widget)
        self.cbMat.setObjectName("cbMat")
        self.verticalLayout.addWidget(self.cbMat)
        self.cbFen = QtWidgets.QCheckBox(self.widget)
        self.cbFen.setObjectName("cbFen")
        self.verticalLayout.addWidget(self.cbFen)
        self.pbSablon = QtWidgets.QPushButton(self.centralwidget)
        self.pbSablon.setGeometry(QtCore.QRect(10, 100, 221, 71))
        self.pbSablon.setObjectName("pbSablon")
        self.pbHazirla = QtWidgets.QPushButton(self.centralwidget)
        self.pbHazirla.setGeometry(QtCore.QRect(10, 180, 361, 81))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.pbHazirla.setFont(font)
        self.pbHazirla.setStyleSheet("QPushButton { \n"
"    background-color: orange;\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: black;\n"
"    font: bold 14px;\n"
"    min-width: 10em;\n"
"    padding: 6px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(255, 140, 0);\n"
"    border-style: inset;\n"
"}")
        self.pbHazirla.setObjectName("pbHazirla")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ÖDM Dönüştürücü v1.0"))
        self.pbKutuk.setText(_translate("MainWindow", "Kütük Seç"))
        self.pbCevap.setText(_translate("MainWindow", "Cevap\n"
"TXTveya DAT\n"
" Seç"))
        self.groupBox.setTitle(_translate("MainWindow", "Dersler"))
        self.cbTurkce.setText(_translate("MainWindow", "Türkçe"))
        self.cbMat.setText(_translate("MainWindow", "Matematik"))
        self.cbFen.setText(_translate("MainWindow", "Fen Bilimler"))
        self.pbSablon.setText(_translate("MainWindow", "Cevap Şablonunu Ayarla"))
        self.pbHazirla.setText(_translate("MainWindow", "E-Okula Yüklenecek Dosyaları Hazırla"))


        self.pbKutuk.clicked.connect(AnaKontrolcu.getInstance().kutuk_ac)
        self.pbCevap.clicked.connect(AnaKontrolcu.getInstance().cevap_dosyasi_sec)
        self.pbSablon.clicked.connect(AnaKontrolcu.getInstance().sablon_formu_ac)
        self.pbHazirla.clicked.connect(AnaKontrolcu.getInstance().hazirla)
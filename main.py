# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Main.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

from MainController import AnaKontrolcu
from utils import resource_path


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 460)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(400, 460))
        MainWindow.setMaximumSize(QtCore.QSize(400, 460))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(resource_path("filter.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pbKutuk = QtWidgets.QPushButton(self.centralwidget)
        self.pbKutuk.setGeometry(QtCore.QRect(10, 20, 101, 71))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.pbKutuk.setFont(font)
        self.pbKutuk.setObjectName("pbKutuk")
        self.pbCevap = QtWidgets.QPushButton(self.centralwidget)
        self.pbCevap.setGeometry(QtCore.QRect(120, 20, 111, 71))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.pbCevap.setFont(font)
        self.pbCevap.setObjectName("pbCevap")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(250, 10, 141, 161))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.layoutWidget = QtWidgets.QWidget(self.groupBox)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 20, 119, 131))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.cbTurkce = QtWidgets.QCheckBox(self.layoutWidget)
        self.cbTurkce.setChecked(True)
        self.cbTurkce.setObjectName("cbTurkce")
        self.verticalLayout.addWidget(self.cbTurkce)
        self.cbMat = QtWidgets.QCheckBox(self.layoutWidget)
        self.cbMat.setChecked(True)
        self.cbMat.setObjectName("cbMat")
        self.verticalLayout.addWidget(self.cbMat)
        self.cbFen = QtWidgets.QCheckBox(self.layoutWidget)
        self.cbFen.setChecked(True)
        self.cbFen.setObjectName("cbFen")
        self.verticalLayout.addWidget(self.cbFen)
        self.pbSablon = QtWidgets.QPushButton(self.centralwidget)
        self.pbSablon.setGeometry(QtCore.QRect(10, 100, 221, 71))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.pbSablon.setFont(font)
        self.pbSablon.setObjectName("pbSablon")
        self.pbHazirla = QtWidgets.QPushButton(self.centralwidget)
        self.pbHazirla.setGeometry(QtCore.QRect(10, 180, 381, 81))
        font = QtGui.QFont()
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
"    font: bold 16px;\n"
"    min-width: 10em;\n"
"    padding: 6px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(255, 140, 0);\n"
"    border-style: inset;\n"
"}")
        self.pbHazirla.setObjectName("pbHazirla")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 270, 111, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setKerning(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.teHataliKayitlar = QtWidgets.QTextEdit(self.centralwidget)
        self.teHataliKayitlar.setGeometry(QtCore.QRect(10, 290, 381, 161))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.teHataliKayitlar.setFont(font)
        self.teHataliKayitlar.setFrameShape(QtWidgets.QFrame.Box)
        self.teHataliKayitlar.setFrameShadow(QtWidgets.QFrame.Plain)
        self.teHataliKayitlar.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.teHataliKayitlar.setAutoFormatting(QtWidgets.QTextEdit.AutoBulletList)
        self.teHataliKayitlar.setReadOnly(True)
        self.teHataliKayitlar.setObjectName("teHataliKayitlar")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.pbKutuk, self.pbCevap)
        MainWindow.setTabOrder(self.pbCevap, self.pbSablon)
        MainWindow.setTabOrder(self.pbSablon, self.cbTurkce)
        MainWindow.setTabOrder(self.cbTurkce, self.cbMat)
        MainWindow.setTabOrder(self.cbMat, self.cbFen)
        MainWindow.setTabOrder(self.cbFen, self.pbHazirla)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ÖDM Dönüştürücü v1.0"))
        self.pbKutuk.setText(_translate("MainWindow", "Kütük Seç"))
        self.pbCevap.setText(_translate("MainWindow", "Cevaplar\n"
"Dosyasını\n"
"Seç"))
        self.groupBox.setTitle(_translate("MainWindow", "Dersler"))
        self.cbTurkce.setText(_translate("MainWindow", "Türkçe"))
        self.cbMat.setText(_translate("MainWindow", "Matematik"))
        self.cbFen.setText(_translate("MainWindow", "Fen Bilimler"))
        self.pbSablon.setText(_translate("MainWindow", "Cevap Şablonunu Ayarla"))
        self.pbHazirla.setText(_translate("MainWindow", "E-Okula Yüklenecek Dosyaları Hazırla"))
        self.label.setText(_translate("MainWindow", "Hatalı Kayıtlar"))


        self.pbKutuk.clicked.connect(AnaKontrolcu.getInstance().kutuk_ac)
        self.pbCevap.clicked.connect(AnaKontrolcu.getInstance().cevap_dosyasi_sec)
        self.pbSablon.clicked.connect(AnaKontrolcu.getInstance().sablon_formu_ac)
        self.pbHazirla.clicked.connect(AnaKontrolcu.getInstance().hazirla)

        # self.cbFen.stateChanged.connect(lambda: AnaKontrolcu.getInstance().fenSeciliMi(deger=self.cbFen.isChecked()))
        # self.cbTurkce.stateChanged.connect(lambda: AnaKontrolcu.getInstance().fenSeciliMi(deger=self.cbTurkce.isChecked()))
        # self.cbMat.stateChanged.connect(lambda: AnaKontrolcu.getInstance().fenSeciliMi(deger=self.cbMat.isChecked()))


from PyQt5 import QtCore
from PyQt5.QtWidgets import QFileDialog, QDialog

from SettingController import AyarKontrolcu
from ayar import Ui_Settings


class AnaKontrolcu(object):
    __instance = None

    # Singleton tasarım deseni için gerekli metod
    @staticmethod
    def getInstance():
        if AnaKontrolcu.__instance == None:
            AnaKontrolcu()
        return AnaKontrolcu.__instance

    # Singleton tasarım deseni yapıcı metod
    def __init__(self):
        if AnaKontrolcu.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            AnaKontrolcu.__instance = self

    kutuk_yolu = ""
    cevap_dosyasi_yolu = ""
    dersler = []
    sinif_seviyesi = ""



    """Kütük açma işlemini yapan metod. Sadece xls ve excel uzantılı dosyalar açılabilir."""

    def kutuk_ac(self):
        self.kutuk_yolu, _ = QFileDialog.getOpenFileName(None, "Kütük Seç", "", "Excel Dosyaları (*.xls *.xlsx)")
        return self.kutuk_yolu



    """Sekonic ile okunan txt ya da dat dosyasını seçme işlemini yapan metod. Sadece dat ve txt dosyaşarını açabilir."""

    def cevap_dosyasi_sec(self):
        self.cevap_dosyasi_yolu, _ = QFileDialog.getOpenFileName(None, "Cevap Dosyası Seç", "",
                                                                 "Yazı Tabanlı Dosyalar (*.dat *.txt)")
        return self.cevap_dosyasi_yolu



    """Şablon ile Seconicten okunan txt ya da dat dosyalarının satır sütün bilgiileri girilecek
    Yani Cevaplar nerde başlayıp kaç karakter devam ediyor gibi..."""

    def sablon_formu_ac(self):
        dialog = QDialog()
        AyarKontrolcu.dialog = dialog
        dialog.ui = Ui_Settings()
        dialog.ui.setupUi(dialog)
        dialog.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        dialog.exec_()

    """E-Okula yüklenecek dosyaları hazırlar"""

    def hazirla(self):
        pass

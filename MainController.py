import xlrd
from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QFileDialog, QDialog, QMessageBox

from SettingController import AyarKontrolcu
from Models import Ayar, Cevap
from ayar import Ui_Settings


class AnaKontrolcu(object):
    ui = None
    kutuk_yolu = None
    cevap_dosyasi_yolu = None
    dersler = []
    sinif_seviyesi = None
    excel_dosyasi = None
    cevap_dosyasi = None
    wbKutuk = None
    wsKutuk = None
    turkceSeciliMi = matematikSeciliMi = fenSeciliMi =True

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

    """Kütük açma işlemini yapan metod. Sadece xls ve xlsx uzantılı dosyalar açılabilir."""

    def kutuk_ac(self):
        self.ekraniKilitleAc(False)
        self.kutuk_yolu, _ = QFileDialog.getOpenFileName(None, "Kütük Seç", "", "Excel Dosyaları (*.xls *.xlsx)")
        """Kütük kontrolü yapılıyor"""
        if self.kutuk_yolu != "":
            self.wbKutuk = xlrd.open_workbook(self.kutuk_yolu, on_demand=True)
            self.wsKutuk = self.wbKutuk.sheet_by_index(0)
            kontrolDegiskeni = self.wsKutuk.cell(0, 0)
            if kontrolDegiskeni.value != "OPAQ":
                self.mesajKutusuGoster("Dikkat!", "Kütük seçimi hatalı!\nLütfen bakanlık kütüğünü\n"
                                                  "değiştirmeden yazılıma yükleyiniz!")
                self.wbKutuk.release_resources()  # Burası çok önemli ;-) Kaynakları geri veriyorum RAM a
                self.kutuk_ac()
        self.ekraniKilitleAc(True)


    """Sekonic ile okunan txt ya da dat dosyasını seçme işlemini yapan metod. Sadece dat ve txt dosyaşarını açabilir."""

    def cevap_dosyasi_sec(self):
        self.cevap_dosyasi_yolu, _ = QFileDialog.getOpenFileName(None, "Cevap Dosyası Seç", "",
                                                                 "Yazı Tabanlı Dosyalar (*.dat *.txt)")

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
        cevaplar = []
        sorunluKayitlar = []
        kurumKoduVeyaOpak = None
        opak = None
        self.ui.teHataliKayitlar.clear()
        if not self.kutuk_yolu:
            self.mesajKutusuGoster("Dikkat!", "Kütük dosyası seçimi yapılmamış!\nLütfen kütük doyasını seçiniz.")
            return
        elif not self.cevap_dosyasi_yolu:
            self.mesajKutusuGoster("Dikkat!", "Cevap dosyası seçimi yapılmamış!\nLütfen cevap doyasını seçiniz.")
            return
        elif not Ayar.ayarlandiMi():
            self.mesajKutusuGoster("Dikkat!",
                                   "Ayarlar yapılmamış!\nTüm seçeneklerin sıfırdan büyük olduğuna emin olunuz.")
            return
        else:
            #Ekran kilitleniyor
            self.ekraniKilitleAc(False)
            #Sınf bilgisi kütükten alınıyor
            sinif = self.sinifBilgisiBul(wsKutuk=self.wsKutuk)

            """Dosya acma ve okuma işlemleri Ayar sınıfınıniçeriğine göre buradan itibaren yapılıyor"""
            with open(self.cevap_dosyasi_yolu) as cd:
                for satir in cd:
                    kurumKoduVeyaOpak = satir[
                                        Ayar.kkopak_baslangic_degeri - 1: Ayar.kkopak_karakter_sayisi + Ayar.kkopak_baslangic_degeri - 1]

                    ogrenci_no = satir[
                                 Ayar.ogrenci_no_baslangic_degeri - 1: Ayar.ogrenci_no_baslangic_degeri + Ayar.ogrenci_no_karakter_sayisi - 1]
                    turkce_cevaplari = satir[
                                       Ayar.tur_baslangic_degeri - 1: Ayar.tur_baslangic_degeri + Ayar.tur_soru_sayisi - 1]
                    mat_cevaplari = satir[
                                    Ayar.mat_baslangic_degeri - 1: Ayar.mat_baslangic_degeri + Ayar.mat_soru_sayisi - 1]
                    fen_cevaplari = satir[
                                    Ayar.fen_baslangic_degeri - 1: Ayar.fen_baslangic_degeri + Ayar.fen_soru_sayisi - 1]
                    katilimDurumu = satir[Ayar.katilma_durumu_baslangic - 1:Ayar.katilma_durumu_baslangic]
                    kitapcik = satir[Ayar.kitapcik_turu_baslangic - 1:Ayar.kitapcik_turu_baslangic]

                    """Cevap kağıtlarında kurum kodu ve öğrenci no kullanıldı ise işler azıcık karışık çok minicik"""
                    if Ayar.kurum_kodu_kullanimi:
                        if not kurumKoduVeyaOpak.isspace() and not ogrenci_no.isspace():
                            sonuc = self.kutuktenKurumKoduVeOgrenciNoIleBul(self.wsKutuk, int(ogrenci_no), int(kurumKoduVeyaOpak))
                            c = Cevap(opak=sonuc[0],
                                      katilimDurumu=katilimDurumu,
                                      kitapcikTuru=kitapcik,
                                      sinavKodu=sonuc[1],
                                      turkceCevaplar=turkce_cevaplari,
                                      fenCevaplar=fen_cevaplari,
                                      matematikCevaplar=mat_cevaplari)
                            # Opak bulunamadı ise hatalı kayıotlara ekleniyor
                            if sonuc[0] is None:
                                sorunluKayitlar.append(c)
                            # Öğrenci sınava girmiş ancak kitapçık numarası işaretlememiş ise
                            elif kitapcik.isspace() and c.katilimDurumu != 0:
                                #TODO Burada refaktör yapılacak
                                hataliKayitDetay = self.hataliKayitKutuktenBul(self.wsKutuk,int(ogrenci_no),int(kurumKoduVeyaOpak))
                                c.adSoyad = hataliKayitDetay[2]
                                c.okulAdi = hataliKayitDetay[3]
                                c.ilceAdi = hataliKayitDetay[4]
                                sorunluKayitlar.append(c)
                            else:
                                cevaplar.append(c)
                    """Cevap kağıtlarında opak kullanıldı ise işler bu kadar basit"""
                    if Ayar.opak_kullanimi:
                        c = Cevap(opak=kurumKoduVeyaOpak,
                                  katilimDurumu=katilimDurumu,
                                  kitapcikTuru=kitapcik,
                                  sinavKodu=self.kutuktenSinavKoduBul(self.wsKutuk),
                                  turkceCevaplar=turkce_cevaplari,
                                  fenCevaplar=fen_cevaplari,
                                  matematikCevaplar=mat_cevaplari)
                        #Opak bulunamadı ise hatalı kayıotlara ekleniyor
                        if c.opak == 0:
                            sorunluKayitlar.append(c)

                        #Öğrenci sınava girmiş ancak kitapçık numarası işaretlememiş ise
                        elif kitapcik.isspace() and c.katilimDurumu != 0:
                            hataliKayitDetay = self.hataliKayitKutuktenBul(self.wsKutuk, opaq=c.opak)
                            c.adSoyad = hataliKayitDetay[2]
                            c.okulAdi = hataliKayitDetay[3]
                            c.ilceAdi = hataliKayitDetay[4]
                            sorunluKayitlar.append(c)
                        else:
                            cevaplar.append(c)

            """Okuma için açık dosyaları işin bitince mutlaka kapat"""
            cd.close()
            #Oluşuturulan cevapları dosyaya yazdırma işlemi burada yapılıyor
            hedefKlasor = QFileDialog.getExistingDirectory(caption="Kayıt yeri seçiniz")

            # MVC tasarım prensibine göre kontrolcü içinden doğrudan ui a erişmek
            # çok uygun değil ama yine de pratik çözmek için alttaki yaklaşım kullnıldı
            #Profesyonel tasarımlarda kesinlikle önerilmeyen bir durumdur
            if self.ui.cbTurkce.isChecked():
                f = open(hedefKlasor+"/TÜRKÇE-"+ sinif + ".dat", "w+")
                for cvp in cevaplar:
                    cvp.setDersId(1)
                    f.write(cvp.toMEBFormat()+"\n")
                f.close()
            if self.ui.cbMat.isChecked():
                f = open(hedefKlasor + "/MATEMATİK-" + sinif + ".dat", "w+")
                for cvp in cevaplar:
                    cvp.setDersId(2)
                    f.write(cvp.toMEBFormat()+"\n")
                f.close()
            if self.ui.cbFen.isChecked():
                f = open(hedefKlasor + "/FEN-" + sinif + ".dat", "w+")
                for cvp in cevaplar:
                    cvp.setDersId(4)
                    f.write(cvp.toMEBFormat()+"\n")
                f.close()


        for sk in sorunluKayitlar:
            self.ui.teHataliKayitlar.append(sk.toSorunluKayit()+"\n")
        self.ui.teHataliKayitlar.append("Oluşturma işlemleri tamamlandı.")
        self.ekraniKilitleAc(True)

    def fenSeciliMi(self, deger):
        self.fenSeciliMi = deger

    def turkceSeciliMi(self, deger):
        self.turkceSeciliMi = deger

    def matematikSeciliMi(self, deger):
        self.matematikSeciliMi = deger

    def mesajKutusuGoster(self, baslik, icerik):
        mbox = QMessageBox()
        mbox.setIcon(QMessageBox.Warning)
        mbox.setWindowIcon(QtGui.QIcon('images/warning.png'))
        mbox.setWindowTitle(baslik)
        mbox.setText(icerik)
        mbox.setStandardButtons(QMessageBox.Ok)
        mbox.exec_()

    def kutuktenKurumKoduVeOgrenciNoIleBul(self, wsKutuk, ogrenciNo, kurumKodu):
        (opak, sinavKodu) = None, None
        for row_num in range(1, wsKutuk.nrows):
            row_value = wsKutuk.row_values(row_num)
            if int(row_value[4]) == kurumKodu and int(row_value[9]) == ogrenciNo:
                (opak, sinavKodu) = int(row_value[0]), int(row_value[16])
                break
        return (opak, sinavKodu)

    def kutuktenSinavKoduBul(self, wsKutuk):
        return wsKutuk.cell(rowx=1, colx=16).value
        # for row_num in range(1, wsKutuk.nrows):
        #     row_value = wsKutuk.row_values(row_num)
        #     if int(row_value[0]) == opak:
        #         sinavKodu = int(row_value[16])
        #         break
        # return sinavKodu,

    def sinifBilgisiBul(self, wsKutuk):
        return str(int(wsKutuk.cell(rowx=1, colx=15).value))

    def hataliKayitKutuktenBul(self, wsKutuk, ogrenciNo = None, kurumKodu=None, opaq=None):
        (opak, sinavKodu, adSoyad, okulAdi, ilceAdi) = None, None, None, None, None
        if opak != None:
            for row_num in range(1, wsKutuk.nrows):
                row_value = wsKutuk.row_values(row_num)
                if int(row_value[0]) == opaq:
                    (opak, sinavKodu, adSoyad, okulAdi, ilceAdi) = int(row_value[0]), int(row_value[16]), (row_value[10] + " " + row_value[12]), row_value[6], row_value[3]
                    break
        else:
            for row_num in range(1, wsKutuk.nrows):
                row_value = wsKutuk.row_values(row_num)
                if int(row_value[4]) == kurumKodu and int(row_value[9]) == ogrenciNo:
                    (opak, sinavKodu, adSoyad, okulAdi, ilceAdi) = int(row_value[0]), int(row_value[16]), (row_value[10] + " " + row_value[12]), row_value[6], row_value[3]
                    break
        return opak, sinavKodu, adSoyad, okulAdi, ilceAdi

    def ekraniKilitleAc(self, ac):
        if ac:
            self.ui.pbHazirla.setEnabled(True)
            self.ui.pbKutuk.setEnabled(True)
            self.ui.pbCevap.setEnabled(True)
            self.ui.pbSablon.setEnabled(True)
            self.ui.groupBox.setEnabled(True)
        else:
            self.ui.pbHazirla.setDisabled(True)
            self.ui.pbKutuk.setDisabled(True)
            self.ui.pbCevap.setDisabled(True)
            self.ui.pbSablon.setDisabled(True)
            self.ui.groupBox.setDisabled(True)

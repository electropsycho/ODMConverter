from Models import Ayar


class AyarKontrolcu(object):

    dialog = None

    __instance = None

    #Singleton tasarım deseni için gerekli metod
    @staticmethod
    def getInstance():
        if AyarKontrolcu.__instance == None:
            AyarKontrolcu()
        return AyarKontrolcu.__instance

    # Singleton tasarım deseni yapıcı metod
    def __init__(self):
        if AyarKontrolcu.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            AyarKontrolcu.__instance = self


    def ayar_penceresi_ac(self):
        pass

    def ayarla(self, ui):
        Ayar.mat_baslangic_degeri = int(ui.leMatBaslangic.text())
        Ayar.fen_baslangic_degeri = int(ui.leFenBaslangic.text())
        Ayar.tur_baslangic_degeri = int(ui.leTurBaslangic.text())
        Ayar.ogrenci_no_baslangic_degeri = int(ui.leOgrenciNoBaslangic.text())
        Ayar.kkopak_baslangic_degeri = int(ui.leKKOpakBaslangic.text())
        Ayar.katilma_durumu_baslangic = int(ui.leKatilimDurumuBaslangic.text())
        Ayar.kitapcik_turu_baslangic = int(ui.leKitapTurBaslangic.text())

        Ayar.mat_soru_sayisi = int(ui.leMatKarSayisi.text())
        Ayar.fen_soru_sayisi = int(ui.leFenKarSayisi.text())
        Ayar.tur_soru_sayisi = int(ui.leTurKarSayisi.text())
        Ayar.kkopak_karakter_sayisi = int(ui.leKKOpakKarSayisi.text())
        Ayar.ogrenci_no_karakter_sayisi = int(ui.leOgrenciNoKarSayisi.text())

        Ayar.kurum_kodu_kullanimi = ui.rbKKodu.isChecked()
        Ayar.opak_kullanimi = ui.rbOpak.isChecked()
        self.dialog.close()

    @classmethod
    def ayarlari_yukle(self, ui):
        ui.leMatBaslangic.setText(str(Ayar.mat_baslangic_degeri))
        ui.leFenBaslangic.setText(str(Ayar.fen_baslangic_degeri))
        ui.leTurBaslangic.setText(str(Ayar.tur_baslangic_degeri))
        ui.leOgrenciNoBaslangic.setText(str(Ayar.ogrenci_no_baslangic_degeri))
        ui.leKKOpakBaslangic.setText(str(Ayar.kkopak_baslangic_degeri))
        ui.leKatilimDurumuBaslangic.setText(str(Ayar.katilma_durumu_baslangic))
        ui.leKitapTurBaslangic.setText(str(Ayar.kitapcik_turu_baslangic))

        ui.leMatKarSayisi.setText(str(Ayar.mat_soru_sayisi))
        ui.leFenKarSayisi.setText(str(Ayar.fen_soru_sayisi))
        ui.leTurKarSayisi.setText(str(Ayar.tur_soru_sayisi))
        ui.leOgrenciNoKarSayisi.setText(str(Ayar.ogrenci_no_karakter_sayisi))
        ui.leKKOpakKarSayisi.setText(str(Ayar.kkopak_karakter_sayisi))



        ui.rbKKodu.setChecked(Ayar.kurum_kodu_kullanimi)
        ui.rbOpak.setChecked(Ayar.opak_kullanimi)




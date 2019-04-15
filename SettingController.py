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
        Ayar.mat_baslangic_degeri = ui.leMatBaslangic.text()
        Ayar.fen_baslangic_degeri = ui.leFenBaslangic.text()
        Ayar.tur_baslangic_degeri = ui.leTurBaslangic.text()

        Ayar.mat_soru_sayisi = ui.leMatKarSayisi.text()
        Ayar.fen_soru_sayisi = ui.leFenKarSayisi.text()
        Ayar.tur_soru_sayisi = ui.leTurKarSayisi.text()

        Ayar.katilma_durumu_baslangic = ui.leKatilimDurumuBaslangic.text()
        Ayar.kitapcik_turu_baslangic = ui.leKitapTurBaslangic.text()

        Ayar.kurum_kodu_kullanimi = ui.rbKKodu.isChecked()
        Ayar.opak_kullanimi = ui.rbOpak.isChecked()
        self.dialog.close()


class Ayar(object):

    mat_baslangic_degeri = 0
    fen_baslangic_degeri = 0
    tur_baslangic_degeri = 0

    mat_soru_sayisi = 0
    fen_soru_sayisi = 0
    tur_soru_sayisi = 0

    kurum_kodu_kullanimi = True
    opak_kullanimi = False

    katilma_durumu_baslangic = 0
    kitapcik_turu_baslangic = 0

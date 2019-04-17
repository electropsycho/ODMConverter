class Ayar(object):
    mat_baslangic_degeri = 0
    fen_baslangic_degeri = 0
    tur_baslangic_degeri = 0
    ogrenci_no_baslangic_degeri = 11
    kkopak_baslangic_degeri = 3

    mat_soru_sayisi = 0
    fen_soru_sayisi = 0
    tur_soru_sayisi = 0
    kkopak_karakter_sayisi = 8
    ogrenci_no_karakter_sayisi = 5

    kurum_kodu_kullanimi = True
    opak_kullanimi = False

    katilma_durumu_baslangic = 19
    kitapcik_turu_baslangic = 18

    @classmethod
    def ayarlandiMi(self):
        return self.mat_baslangic_degeri > 0 \
               and self.fen_baslangic_degeri > 0 \
               and self.tur_baslangic_degeri > 0 \
               and self.ogrenci_no_baslangic_degeri > 0 \
               and self.kkopak_baslangic_degeri > 0 \
               and self.mat_soru_sayisi > 0 \
               and self.fen_soru_sayisi > 0 \
               and self.tur_soru_sayisi > 0 \
               and self.kkopak_karakter_sayisi > 0 \
               and self.ogrenci_no_karakter_sayisi > 0 \
               and (self.kurum_kodu_kullanimi or self.opak_kullanimi) \
               and self.katilma_durumu_baslangic > 0 \
               and self.kitapcik_turu_baslangic > 0


class Cevap(object):
    opak = None
    kitapcikTuru = None
    turkceCevaplar = None
    matematikCevaplar = None
    fenCevaplar = None,
    sinavKodu = None
    cevapTipi = 0
    katilimDurumu = None
    dersId = None
    ogrenciNo = None
    kurumKodu = None
    adSoyad = None
    okulAdi = None
    ilceAdi = None

    def __init__(self, opak=None,
                 katilimDurumu=None,
                 kitapcikTuru=None,
                 turkceCevaplar=None,
                 matematikCevaplar=None,
                 fenCevaplar=None,
                 sinavKodu=None):
        self.opak = 0 if opak is None else int(opak)
        self.turkceCevaplar = turkceCevaplar
        self.matematikCevaplar = matematikCevaplar
        self.fenCevaplar = fenCevaplar
        self.sinavKodu = sinavKodu
        self.kitapcikTuru = kitapcikTuru
        self.katilimDurumu = 1 if not katilimDurumu else 0

    def setDersId(self, dersId):
        self.dersId = dersId

    def getOpak(self):
        return self.opak

    def getMatematkCevaplari(self):
        return self.matematikCevaplar

    def getTurkceCevaplari(self):
        return self.turkceCevaplar

    def getFenCevaplari(self):
        return self.fenCevaplar

    def toMEBFormat(self):
        formatliCevap = str(self.sinavKodu) + "#" \
               + str(self.opak) + "#" \
               + str(self.dersId) + "#" \
               + self.kitapcikTuru + "#" \
               + str(self.cevapTipi) + "#" \
               + str(self.katilimDurumu) + "#"
        if (self.dersId == 1):
            formatliCevap = formatliCevap + self.turkceCevaplar
        if (self.dersId == 2):
            formatliCevap = formatliCevap + self.matematikCevaplar
        if (self.dersId == 4):
            formatliCevap = formatliCevap + self.fenCevaplar
        return formatliCevap

    def toSorunluKayit(self):
        if self.kitapcikTuru is None or self.kitapcikTuru.isspace():
            return "Kitapçık türü işratelememe hatası, İlçe: " \
                   + self.ilceAdi + " Okul: " + self.okulAdi \
                   + " Öğrenci Adı: " + self.adSoyad
        elif self.kurumKodu is None or self.ogrenciNo is None:
            return "Cevaplar arasında Kurum kodu ve Öğrenci No kodlanmamış kayıt var!"
        return "Hatalı Kayıt, Öğrenci Nakil Olmuş Olabilir." \
               " Kurum Kodu:" + str(self.kurumKodu) \
               + " Öğrenci No:" + str(self.ogrenciNo)

    def __str__(self):
        return "Opak:" + str(self.opak) \
               + " Snav Kodu:" + str(self.sinavKodu) \
               + " Türkçe:" + self.turkceCevaplar \
               + " Matematik:" + self.matematikCevaplar \
               + "Katılım Durumu:" + str(self.katilimDurumu)

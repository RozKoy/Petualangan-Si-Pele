from . import Pemain_2 as PEMAIN
from . import Timer as TMR
from . import Item as ITEM
from . import Bos as BOS
from . import Fon as FON

from .. import Data as DATA
from .. import Suara as SUARA

from ..Menu import Tombol as TMBL

from ..Fungsi import (
    RUBAH_SKALA,
    PERBAHARUI,
    USEREVENT,
    TERTEKAN,
    SURFACE,
    KELUAR,
    TAMPIL,
    ESCAPE,
    TIMER,
    WAKTU,
    ACARA,
    GROUP,
    TEKAN,
    SPASI,
    ENTER,
    KANAN,
    KIRI
)
from ..Konstan import UKURAN_LAYAR, FPS

from ..Gambar.Latar import LATAR_BELAKANG_BOS
from ..Gambar.Cerita import CERITA_2
from ..Gambar.Karakter import GERAK_2
from ..Gambar.Info import LATAR_KALAH, TOMBOL_MENU_UTAMA, LATAR_JEDA, TOMBOL_JEDA

import random


class Lawan_bos:
    def __init__(self, Layar, darah):
        TMBL.Tombol.aktif = 0
        self.latar_belakang = RUBAH_SKALA(LATAR_BELAKANG_BOS, UKURAN_LAYAR)
        self.pemain = PEMAIN.Pemain(GERAK_2[DATA.KARAKTER], darah)
        self.bos = BOS.Bos()
        self.item = GROUP()
        self.waktu = WAKTU()
        self.cerita = [RUBAH_SKALA(i, self.ukuran(i)) for i in CERITA_2]
        self.latar_jeda = RUBAH_SKALA(LATAR_JEDA['file'], LATAR_JEDA['ukuran'])
        self.tombol_jeda = TMBL.Tombol(TOMBOL_JEDA)
        self.latar_kalah = RUBAH_SKALA(
            LATAR_KALAH['file'], LATAR_KALAH['ukuran'])
        self.tombol_kalah = TMBL.Tombol(TOMBOL_MENU_UTAMA)
        self.teks_info = FON.Fon(15, (480, 535), (255, 255, 255))
        self.hitung_mundur = TMR.Timer(
            3, False, [self.pemain, self.pemain.info, self.bos], self.latar_belakang)
        self.item_jatuh = USEREVENT + 2
        self.musik_lawan_bos = SUARA.Suara(
            'Aset\\Suara\\Musik\\lawan_bos.mp3', 'musik')
        self.ke = 0
        self.berjalan, self.jeda, self.menang, self.kalah = True, False, False, False
        self.tampil(Layar)

    def ukuran(self, gambar):
        def ukuran_lebar(gambar, ukuran):
            return gambar.get_height() * ukuran / gambar.get_width()
        return 550, ukuran_lebar(gambar, 550)

    def tampil(self, Layar):
        self.musik_lawan_bos.mulai()
        TIMER(self.item_jatuh, random.randint(1, 3) * 10000, 1)
        while self.berjalan:
            self.tampilkan_isi(Layar)
            self.cek_acara(Layar)
            if self.ke < 2 or self.jeda or self.kalah:
                PERBAHARUI()
                continue
            if not self.menang:
                self.gerak(Layar)
            else:
                self.berakhir()
            PERBAHARUI()
            self.waktu.tick(FPS)
        self.pemain.info.atur_kembali()
        self.musik_lawan_bos.berhenti()

    def tampilkan_isi(self, Layar):
        TAMPIL(Layar, self.latar_belakang, (0, 0))
        if not self.menang:
            self.bos.tampil(Layar)
        self.pemain.tampil(Layar)
        self.pemain.info.tampil(Layar)
        for item in self.item:
            item.tampil(Layar)
        self.teks_info.tampil(Layar, '(ESC) - Jeda')
        if self.ke < 2:
            latar_belakang = SURFACE((UKURAN_LAYAR))
            latar_belakang.set_alpha(150)
            TAMPIL(Layar, latar_belakang, (0, 0))
            cerita = self.cerita[self.ke]
            TAMPIL(Layar, cerita, cerita.get_rect(center=(480, 270)))
        elif self.ke == 2:
            self.hitung_mundur.tampil(Layar)
            self.ke = 3
        elif self.jeda:
            self.tampilan_jeda(Layar)
        elif self.kalah:
            self.tampilan_kalah(Layar)

    def gerak(self, Layar):
        self.pemain.gerak(TERTEKAN())
        if self.pemain.serang(self.bos.posisi_bos()):
            self.bos.darah_berkurang()
        self.bos.aksi(self.pemain.posisi_karakter())
        if self.bos.kena_target(self.pemain.posisi):
            self.pemain.efek_kena_serang.mulai()
            self.pemain.darah_berkurang()
        if self.pemain.cek_kalah(self.bos.posisi_bos()):
            self.kalah = True
        if self.bos.cek_kalah():
            self.menang = True
        for item in self.item:
            item.jatuh()
            if self.pemain.dapat_item(item.dapatkan()):
                item.hilang()

    def cek_acara(self, Layar):
        for acara in ACARA():
            if acara.type == KELUAR:
                exit()
            elif acara.type == TEKAN:
                self.cek_aksi(acara.key, Layar)
            if acara.type == self.item_jatuh:
                self.item.add(ITEM.Item())
                TIMER(self.item_jatuh, random.randint(1, 3) * 10000, 1)

    def cek_aksi(self, key, Layar):
        if key in (ENTER, SPASI) and self.ke < 2:
            self.ke += 1
        if key == ESCAPE and not (self.jeda or self.kalah):
            self.jeda = True
        if self.jeda or self.kalah:
            if key in (KANAN, KIRI):
                if self.jeda:
                    self.tombol_jeda.aksi(key, KIRI)
                else:
                    TMBL.Tombol.aktif = 0
                    self.tombol_kalah.aksi(key, KIRI)
            elif key in (SPASI, ENTER):
                if TMBL.Tombol.aktif == 0:
                    self.berjalan = False
                elif TMBL.Tombol.aktif == 1:
                    if self.jeda:
                        self.jeda = False
                        self.hitung_mundur.tampil(Layar)

    def berakhir(self):
        self.pemain.jalan_kanan()
        if self.pemain.posisi.left >= UKURAN_LAYAR[0]:
            self.berjalan = False

    def tampilan_kalah(self, Layar):
        self.tampil_gelap(Layar)
        TAMPIL(Layar, self.latar_kalah,
               self.latar_kalah.get_rect(center=(480, 270)))
        self.tombol_kalah.tampil(Layar)

    def tampilan_jeda(self, Layar):
        self.tampil_gelap(Layar)
        TAMPIL(Layar, self.latar_jeda,
               self.latar_jeda.get_rect(center=(480, 270)))
        self.tombol_jeda.tampil(Layar)

    def tampil_gelap(self, Layar):
        latar_gelap = SURFACE(UKURAN_LAYAR)
        latar_gelap.set_alpha(150)
        TAMPIL(Layar, latar_gelap, (0, 0))

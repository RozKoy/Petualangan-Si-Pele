from . import Pemain_1 as PEMAIN
from . import Latar as LATAR

from .. import Data as DATA

from ..Fungsi import (
	AMBIL_GAMBAR, 
	RUBAH_SKALA, 
	PERBAHARUI, 
	SURFACE, 
	TAMPIL,
	KELUAR, 
	ACARA, 
	WAKTU, 
	TEKAN, 
	ENTER, 
	SPASI
)
from ..Konstan import UKURAN_LAYAR, FPS

from ..Gambar.Latar import LATAR_BELAKANG_ALUR_CERITA
from ..Gambar.Karakter import GERAK_1
from ..Gambar.Cerita import CERITA_1

class Alur_cerita:
	def __init__(self, Layar):
		self.latar = LATAR.Latar(gambar = LATAR_BELAKANG_ALUR_CERITA.convert(), kecepatan = 8)
		self.pemain = PEMAIN.Pemain(self.gambar())
		self.latar_belakang = SURFACE((UKURAN_LAYAR))
		self.latar_belakang.set_alpha(150)
		self.cerita = [RUBAH_SKALA(i, self.ukuran(i)) for i in CERITA_1]
		self.ke = 0
		self.berjalan = True
		self.waktu = WAKTU()
		self.tampil(Layar)
	def gambar(self):
		lokasi = GERAK_1[DATA.KARAKTER]['lokasi']
		nama = GERAK_1[DATA.KARAKTER]['nama']
		return AMBIL_GAMBAR(lokasi = lokasi, nama = nama)
	def ukuran(self, gambar):
		def ukuran_lebar(gambar, ukuran):
			return gambar.get_height() * ukuran / gambar.get_width()
		return 550, ukuran_lebar(gambar, 550)
	def tampil(self, Layar):
		while self.berjalan:
			self.tampilkan_isi(Layar)
			for acara in ACARA():
				if acara.type == KELUAR:
					exit()
				elif acara.type == TEKAN:
					self.cek_aksi(acara.key, Layar)
			if self.ke == 4:
				self.latar.perbaharui(self.latar)
				self.pemain.lari()
				self.cek_batas_latar()
			PERBAHARUI()
			self.waktu.tick(FPS)
	def cek_batas_latar(self):
		if UKURAN_LAYAR[0] < self.latar.posisi.right < UKURAN_LAYAR[0] + 8:
			self.pemain.posisi.x += 8
			if self.pemain.posisi.left > UKURAN_LAYAR[0]:
				self.berjalan = False
	def tampilkan_isi(self, Layar):
		self.latar.tampil(Layar)
		self.pemain.tampil(Layar)
		if self.ke != 4:
			TAMPIL(Layar, self.latar_belakang, (0, 0))
			cerita = self.cerita[self.ke]
			TAMPIL(Layar, cerita, cerita.get_rect(center = (480, 270)))
	def cek_aksi(self, key, Layar):
		if key in (ENTER, SPASI):
			self.ke = 0 if self.ke > 3 else self.ke + 1
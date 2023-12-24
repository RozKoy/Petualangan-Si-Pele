from . import Pemain_1 as PEMAIN
from . import Latar as LATAR

from .. import Data as DATA
from .. import Suara as SUARA

from ..Fungsi import (
	AMBIL_GAMBAR, 
	RUBAH_SKALA, 
	PERBAHARUI, 
	SURFACE, 
	KELUAR, 
	TAMPIL,
	ACARA, 
	WAKTU, 
	TEKAN, 
	ENTER, 
	SPASI
)
from ..Konstan import UKURAN_LAYAR, FPS

from ..Gambar.Latar import LATAR_BELAKANG_MENANG
from ..Gambar.Karakter import GERAK_1
from ..Gambar.Cerita import CERITA_3

class Menang:
	def __init__(self, Layar):
		self.waktu = WAKTU()
		self.latar = LATAR.Latar(gambar = LATAR_BELAKANG_MENANG.convert(), kecepatan = 8)
		self.pemain = PEMAIN.Pemain(self.gambar())
		self.latar_belakang = SURFACE((UKURAN_LAYAR))
		self.latar_belakang.set_alpha(150)
		self.cerita = RUBAH_SKALA(CERITA_3, self.ukuran(CERITA_3))
		self.musik_menang = SUARA.Suara('Aset\\Suara\\Musik\\selesai.mp3', 'musik')
		self.berjalan, self.selesai = True, False
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
		self.musik_menang.mulai()
		while self.berjalan:
			self.tampilkan_isi(Layar)
			for acara in ACARA():
				if acara.type == KELUAR:
					exit()
				elif acara.type == TEKAN:
					self.cek_aksi(acara.key, Layar)
			if not self.selesai:
				self.latar.perbaharui(self.latar)
				self.pemain.lari()
				self.cek_batas_latar()
			else:
				TAMPIL(Layar, self.latar_belakang, (0, 0))
				TAMPIL(Layar, self.cerita, self.cerita.get_rect(center = (480, 270)))
			PERBAHARUI()
			self.waktu.tick(FPS)
		self.musik_menang.berhenti()
	def cek_batas_latar(self):
		if UKURAN_LAYAR[0] < self.latar.posisi.right < UKURAN_LAYAR[0] + 8:
			self.pemain.posisi.x += 8
			if self.pemain.posisi.left > 600:
				self.selesai = True
	def tampilkan_isi(self, Layar):
		self.latar.tampil(Layar)
		self.pemain.tampil(Layar)
	def cek_aksi(self, key, Layar):
		if key in (ENTER, SPASI) and self.selesai:
			self.berjalan = False
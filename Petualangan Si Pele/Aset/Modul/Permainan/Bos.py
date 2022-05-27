from . import Peluru as PELURU

from ..Fungsi import RUBAH_SKALA, GROUP
from ..Gambar.Bos import GERAK
from ..Gambar.Darah import DARAH_BOS
from ..Gambar.Peluru import PELURU_BOS

import random

class Bos:
	def __init__(self):
		self.darah = 100
		self.file_jalan_kanan = [RUBAH_SKALA(i, self.ukuran(i)) for i in GERAK['jalan']['kanan']]
		self.file_jalan_kiri = [RUBAH_SKALA(i, self.ukuran(i)) for i in GERAK['jalan']['kiri']]
		self.file_lempar = [RUBAH_SKALA(i, self.ukuran(i)) for i in GERAK['lempar']]
		self.file_diam = self.file_lempar[0]
		self.gambar = self.file_diam
		self.posisi = self.gambar.get_rect()
		self.posisi.bottom = 500
		self.posisi.left = 700
		self.bola_api = GROUP()
		self.target = (0, 0)
		self.papan = RUBAH_SKALA(DARAH_BOS['papan'], (280, 80))
		self.hijau = RUBAH_SKALA(DARAH_BOS['hijau'], (245, 30))
		self.merah = RUBAH_SKALA(DARAH_BOS['merah'], (245, 30))
		self.arah = 'kiri'
		self.indeks = 0
		self.berjalan, self.menyerang, self.diam = False, False, False
		self.pilihan = None
	def gaya(self):
		return random.randint(0, len(self.file) - 1)
	def ukuran(self, gambar):
		return 280, gambar.get_height() * 280 / gambar.get_width()
	def aksi(self, target):
		if not (self.berjalan or self.menyerang or self.diam):
			self.pilihan = random.choice(['berjalan', 'menyerang', 'diam'])
		if self.pilihan == 'berjalan':
			self.berjalan = True
		elif self.pilihan == 'menyerang':
			self.menyerang = True
		elif self.pilihan == 'diam':
			self.diam = True
		if self.berjalan:
			self.bergerak()
		elif self.menyerang:
			self.serang(target)
		if self.diam:
			self.berdiam()
	def bergerak(self):
		if self.arah == 'kanan':
			self.posisi.move_ip(2, 0)
			self.gambar = self.file_jalan_kanan[self.indeks // 10]
		elif self.arah == 'kiri':
			self.posisi.move_ip(-2, 0)
			self.gambar = self.file_jalan_kiri[self.indeks // 10]
		self.indeks += -self.indeks if self.indeks >= 29 else 1
		if self.posisi.left >= 700 or self.posisi.left <= 500:
			self.arah = 'kanan' if self.arah == 'kiri' else 'kiri'
			self.berjalan, self.menyerang = False, True
			self.pilihan = 'menyerang'
			self.indeks = 0
	def serang(self, target):
		self.gambar = self.file_lempar[self.indeks // 10]
		self.indeks += 1
		if self.indeks >= 29:
			self.target = target
			self.bola_api.add(PELURU.Peluru(RUBAH_SKALA(PELURU_BOS, (38, 38)), 7))
			self.menyerang, self.diam = False, True
			self.pilihan = 'diam'
			self.indeks = 0
	def kena_target(self, target):
		for bola_api in self.bola_api:
			bola_api.tembak((self.posisi.left + 40, 290), self.target)
			if bola_api.bakar(target):
				bola_api.hilang()
				return True
		return False
	def berdiam(self):
		self.gambar = self.file_diam
		self.indeks += 1
		if self.indeks == 35:
			self.diam = False
			self.indeks = 0
	def posisi_bos(self):
		return self.posisi.left + 70
	def darah_berkurang(self):
		self.darah -= random.choice([1,2,3])
		if self.darah < 0:
			self.darah = 0
		self.rubah_darah()
	def rubah_darah(self):
		self.hijau = RUBAH_SKALA(DARAH_BOS['hijau'], (245 * self.darah / 100, 30))
	def cek_kalah(self):
		if self.darah <= 0:
			return True
		return False
	def tampil(self, Layar):
		Layar.blit(self.gambar, self.posisi)
		Layar.blit(self.papan, (665, 25))
		Layar.blit(self.merah, (680, 65))
		posisi = self.hijau.get_rect()
		posisi.right = 925
		posisi.top = 65
		Layar.blit(self.hijau, posisi)
		for bola_api in self.bola_api:
			bola_api.tampil(Layar)
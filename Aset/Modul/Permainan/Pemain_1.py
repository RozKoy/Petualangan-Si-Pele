from . import Info as INFO

from .. import Data as DATA
from .. import Suara as S

from ..Efek_suara.Karakter import LOKASI, SUARA, SUARA_UNIK

from ..Fungsi import TAMPIL, RUBAH_SKALA, SPASI

import random

class Pemain:
	def __init__(self, gambar):
		self.__darah = 100
		self.__langkah = 0
		self.__batas_lompat = 5
		self.__file = [RUBAH_SKALA(i, (145, 180)) for i in gambar]
		self.ganti_gaya(self.__langkah)
		self.posisi = self.gambar.get_rect()
		self.posisi.x = 70
		self.posisi.y = 330
		self.efek_lari = S.Suara(LOKASI[DATA.KARAKTER] + SUARA['lari'])
		self.efek_lompat = S.Suara(LOKASI[DATA.KARAKTER] + SUARA['lompat'])
		self.efek_kena_rintangan = S.Suara(LOKASI[DATA.KARAKTER] + SUARA['kena_rintangan'])
		self.efek_unik = [S.Suara(LOKASI[DATA.KARAKTER] + unik) for unik in SUARA_UNIK[DATA.KARAKTER]]
		self.indeks = 0
		self.info = INFO.Info()
		self.melompat = False
	def gerak(self, aksi):
		if self.melompat:
			self.lompat()
		else:
			self.posisi.x = 70
			self.lari()
		if not self.melompat and aksi[SPASI]:
			self.efek_lari.berhenti()
			self.efek_lompat.mulai()
			self.melompat = True
	def lari(self):
		self.ganti_gaya(self.__langkah // 4)
		self.__langkah = self.__langkah + 1 if self.__langkah < 15 else 0
		if self.indeks == 0:
			self.efek_lari.mulai()
		self.indeks += 1 if self.indeks < 100 else -self.indeks
	def lompat(self):
		self.ganti_gaya(0)
		if self.melompat :
			self.posisi.y -= self.__batas_lompat * 3
			self.__batas_lompat -= 0.3
			if self.__batas_lompat <= 0:
				self.ganti_gaya(1 if self.__batas_lompat > -3 else 2)
		if self.posisi.y >= 330:
			self.posisi.y = 330
			self.__batas_lompat = 5
			self.melompat = False
			self.indeks = 0
	def ganti_gaya(self, indeks):
		self.gambar = self.__file[indeks]
	def unik(self):
		unik = random.choice(self.efek_unik)
		unik.mulai()
	def kena_rintangan(self, rintangan):
		if self.posisi.colliderect(rintangan):
			self.efek_lari.berhenti()
			self.efek_lompat.berhenti()
			self.efek_kena_rintangan.mulai()
			self.darah_berkurang()
			return True
		return False
	def darah_berkurang(self):
		self.__darah -= random.randint(1, 4) * 5
		if self.__darah < 0:
			self.__darah = 0
		self.info.rubah_darah(self.__darah)
	def cek_darah(self):
		return self.__darah
	def atur_kembali(self):
		INFO.Info.atur_kembali(INFO.Info)
	def tampil(self, Layar):
		TAMPIL(Layar, self.gambar, self.posisi)
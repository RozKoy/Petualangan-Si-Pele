from ..Fungsi import TAMPIL, SPRITE, RUBAH_SKALA
from ..Konstan import UKURAN_LAYAR

from ..Gambar.Rintangan import RINTANGAN

import random

class Rintangan(SPRITE):
	_kecepatan = 8
	def __init__(self):
		super(Rintangan, self).__init__()
		self.__tambah = True
		self.gambar = self.pilih_gambar()
		self.posisi = self.gambar.get_rect()
		self.posisi.left = UKURAN_LAYAR[0] + (random.randint(0, 4) * 50)
		self.posisi.bottom = 528
	def bergerak(self, grup, berhenti):
		self.posisi.move_ip(-self._kecepatan, 0)
		if self.posisi.left < 480 and self.__tambah and not berhenti:
			grup.add(Rintangan())
			self.__tambah = False
		elif self.posisi.right < 0:
			self.hilang()
	def pilih_gambar(self):
		return RUBAH_SKALA(random.choice(RINTANGAN), (60, 60))
	def kecepatan_berubah(self):
		Rintangan._kecepatan += 2
	def atur_kembali(self):
		Rintangan._kecepatan = 8
		self._kecepatan = 8
	def hilang(self):
		self.kill()
	def tampil(self, Layar):
		TAMPIL(Layar, self.gambar, self.posisi)
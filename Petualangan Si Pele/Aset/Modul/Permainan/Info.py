from ..Fungsi import TAMPIL, RUBAH_SKALA

from ..Gambar.Darah import DARAH
from ..Gambar.Level import LEVEL

class Info:
	__lvl = 1
	def __init__(self):
		self.__level = RUBAH_SKALA(LEVEL[Info.__lvl], (70, 25))
		self.__papan = RUBAH_SKALA(DARAH['papan'], (280, 80))
		self.__merah = RUBAH_SKALA(DARAH['merah'], (245, 30))
		self.__hijau = RUBAH_SKALA(DARAH['hijau'], (245, 30))
	def naik_level(self, latar, rintangan):
		rintangan.kecepatan_berubah()
		for i in latar:
			i.kecepatan_berubah()
		if Info.__lvl != 'bos':
			Info.__lvl = 'bos' if Info.__lvl == 3 else Info.__lvl + 1
		self.__level = RUBAH_SKALA(LEVEL[Info.__lvl], (70, 25))
	def rubah_darah(self, darah):
		self.__hijau = RUBAH_SKALA(DARAH['hijau'], (245 * darah / 100, 30))
	def tampil(self, Layar):
		TAMPIL(Layar, self.__papan, (25, 25))
		TAMPIL(Layar, self.__merah, (40, 65))
		TAMPIL(Layar, self.__hijau, (40, 65))
		TAMPIL(Layar, self.__level, (220, 35))
	def atur_kembali(self):
		Info.__lvl = 1
	def tampil_level(self, Layar):
		level = RUBAH_SKALA(LEVEL[Info.__lvl], (140, 50))
		TAMPIL(Layar, level, level.get_rect(center = (480, 250)))
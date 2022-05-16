from ..Gambar.Karakter import DARAH
from ..Gambar.Level import LEVEL
from ..Konstan import pygame

class Info:
	def __init__(self):
		self.__lvl = 1
		self.__level = self.rubah_skala(LEVEL[self.__lvl], (70, 25))
		self.__papan = self.rubah_skala(DARAH['papan'], (280, 80))
		self.__merah = self.rubah_skala(DARAH['merah'], (245, 30))
		self.__hijau = self.rubah_skala(DARAH['hijau'], (245, 30))
	def rubah_skala(self, gambar, ukuran):
		return pygame.transform.smoothscale(gambar, ukuran)
	def naik_level(self, latar, rintangan):
		for i in latar:
			i.kecepatan_berubah()
		rintangan.kecepatan_berubah()
		if self.__lvl != 'bos':
			self.__lvl = 'bos' if self.__lvl == 3 else self.__lvl + 1
		self.__level = self.rubah_skala(LEVEL[self.__lvl], (70, 25))
	def rubah_darah(self, darah):
		self.__hijau = self.rubah_skala(DARAH['hijau'], (245 * darah / 100, 30))
	def tampil(self, Layar):
		Layar.blit(self.__papan, (25, 25))
		Layar.blit(self.__merah, (40, 65))
		Layar.blit(self.__hijau, (40, 65))
		Layar.blit(self.__level, (220, 35))
	def tampil_level(self, Layar):
		level = self.rubah_skala(LEVEL[self.__lvl], (140, 50))
		Layar.blit(level, level.get_rect(center = (480, 250)))
from ..Konstan import pygame
from . import Info as INFO

class Pemain:
	def __init__(self, gambar):
		self.__darah = 100
		self.__langkah = 0
		self.__batas_lompat = 5
		self.info = INFO.Info()
		self.__file = [self.rubah_skala(i) for i in gambar]
		self.ganti_gaya(self.__langkah)
		self.rect = self.gambar.get_rect()
		self.rect.x = 70
		self.rect.y = 330
		self.melompat = False
	def gerak(self, aksi):
		if self.melompat:
			self.lompat()
		else:
			self.rect.x = 70
			self.lari()
		if not self.melompat and aksi[pygame.K_SPACE]:
			self.melompat = True
	def lari(self):
		self.ganti_gaya(self.__langkah // 4)
		self.__langkah = self.__langkah + 1 if self.__langkah < 15 else 0
	def lompat(self):
		self.ganti_gaya(0)
		if self.melompat :
			self.rect.y -= self.__batas_lompat * 3
			self.__batas_lompat -= 0.3
			if self.__batas_lompat <= 0:
				self.ganti_gaya(1 if self.__batas_lompat > -3 else 2)
		if self.rect.y >= 330:
			self.rect.y = 330
			self.__batas_lompat = 5
			self.melompat = False
	def rubah_skala(self, gambar):
		return pygame.transform.smoothscale(gambar, (145, 180))
	def ganti_gaya(self, indeks):
		self.gambar = self.__file[indeks]
	def darah_berkurang(self):
		self.__darah -= 20
		self.info.rubah_darah(self.__darah)
	def cek_darah(self):
		if self.__darah == 0:
			return True
		return False
	def tampil(self, Layar):
		Layar.blit(self.gambar, self.rect)
	def tampil_info(self, Layar):
		self.info.tampil(Layar)
from ..Konstan import pygame, UKURAN_LAYAR
from ..Gambar.Rintangan import RINTANGAN
import random

class Rintangan(pygame.sprite.Sprite):
	_kecepatan = 8
	def __init__(self):
		super(Rintangan, self).__init__()
		self.__tambah = True
		self.gambar = self.pilih_gambar()
		self.rect = self.gambar.get_rect()
		self.rect.bottom = 528
		self.rect.left = UKURAN_LAYAR[0] + (random.randint(0, 2) * 100)
	def update(self, grup):
		self.rect.move_ip(-self._kecepatan, 0)
		if self.rect.left < 480 and self.__tambah:
			grup.add(Rintangan())
			self.__tambah = False
		elif self.rect.right < 0:
			self.kill()
	def pilih_gambar(self):
		return pygame.transform.smoothscale(random.choice(RINTANGAN), (60, 60))
	def kecepatan_berubah(self):
		Rintangan._kecepatan += 2
	def atur_kembali(self):
		self._kecepatan = 8
	def tampil(self, Layar):
		Layar.blit(self.gambar, self.rect)
from ..Fungsi import TAMPIL, RUBAH_SKALA, SPRITE
from ..Gambar.Item import ITEM

import random

class Item(SPRITE):
	def __init__(self):
		super(Item, self).__init__()
		self.file = ITEM
		self.gambar = RUBAH_SKALA(self.file, (40, 40))
		self.posisi = self.gambar.get_rect(center = (random.randint(70, 600), -50))
		self.indeks = 0
		self.sisi = 30
	def jatuh(self):
		self.posisi.move_ip(0, 3)
		self.indeks += 1
		if self.indeks == 25:
			self.indeks = 0
			self.gambar = RUBAH_SKALA(self.file, (self.sisi, self.sisi))
			self.posisi = self.gambar.get_rect(center = self.posisi.center)
			self.sisi = 40 if self.sisi == 30 else 30
		if self.posisi.top > 540:
			self.hilang()
	def dapatkan(self):
		return self.posisi
	def tampil(self, Layar):
		TAMPIL(Layar, self.gambar, self.posisi)
	def hilang(self):
		self.kill()
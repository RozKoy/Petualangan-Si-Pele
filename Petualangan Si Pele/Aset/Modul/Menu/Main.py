from ..Gambar.Latar_menu import LATAR_BELAKANG
from ..Konstan import pygame, UKURAN_LAYAR
from ..Gambar.Tombol import DATA_TOMBOL

from . import Tombol as TMBL

class Menu:
	aktif = 0
	def __init__(self):
		gambar = LATAR_BELAKANG[Menu.aktif].convert()
		ukuran = UKURAN_LAYAR
		self.latar_belakang = self.rubah_skala(gambar, ukuran)
		self.tombol = TMBL.Tombol(DATA_TOMBOL[Menu.aktif])
		self.berjalan = True
		TMBL.Tombol.aktif = 0
	def tampil(self, Layar):
		while self.berjalan:
			self.tampilkan_isi(Layar)
			self.cek_acara(Layar)
			pygame.display.flip()
	def tampilkan_isi(self, Layar):
		Layar.blit(self.latar_belakang, (0, 0))
		self.tombol.tampil(Layar)
	def cek_acara(self, Layar):
		for acara in pygame.event.get():
			if acara.type == pygame.QUIT: 
				exit()
			elif acara.type == pygame.KEYUP:
				self.tombol.cek_aksi(acara.key)
				self.cek_aksi(acara.key, Layar)
	def rubah_skala(self, gambar, ukuran):
		return pygame.transform.smoothscale(gambar, ukuran)
	def keluar(self):
		self.berjalan = False
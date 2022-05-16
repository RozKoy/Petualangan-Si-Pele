from ..Konstan import pygame, UKURAN_LAYAR, ENTER
from ..Gambar.Latar_menu import LATAR_BELAKANG

from . import Main as MASTER

class Menu_info(MASTER.Menu):
	def __init__(self, utama):
		super().__init__()
		self.utama = utama
		gambar = LATAR_BELAKANG[MASTER.Menu.aktif]
		self.latar_belakang = self.rubah_skala(gambar, (600, 400))
		self.Latar_belakang_gelap = pygame.Surface(UKURAN_LAYAR)
		self.Latar_belakang_gelap.fill((0, 0, 0))
		self.Latar_belakang_gelap.set_alpha(150)
	def tampilkan_isi(self, Layar):
		Layar.blit(self.utama.latar_belakang, (0, 0))
		self.utama.tombol.tampil(Layar)
		Layar.blit(self.Latar_belakang_gelap, (0, 0))
		posisi = self.latar_belakang.get_rect(center = (480, 270))
		Layar.blit(self.latar_belakang, posisi)
		self.tombol.tampil(Layar)
	def cek_aksi(self, key, Layar):
		if key == ENTER:
			self.keluar()
from ..Konstan import pygame, KANAN, KIRI, ENTER
from ..Gambar.Karakter import AVATAR

from . import Main as MASTER
from . import Tombol as TMBL
from .. import Data as DATA

class Menu_karakter(MASTER.Menu):
	def __init__(self):
		super().__init__()
		self.rubah_karakter()
	def tampilkan_isi(self, Layar):
		super().tampilkan_isi(Layar)
		Layar.blit(self.sebelum, self.sebelum.get_rect(center = (230, 270)))
		Layar.blit(self.karakter, self.karakter.get_rect(center = (480, 270)))
		Layar.blit(self.sesudah, self.sesudah.get_rect(center = (730, 270)))
	def cek_aksi(self, key:int, Layar):
		if key in (KIRI, KANAN) and TMBL.Tombol.aktif == 0:
			DATA.KARAKTER += 1 if key == KANAN else 6
			DATA.KARAKTER %= 7
			self.rubah_karakter()
		elif key == ENTER and TMBL.Tombol.aktif == 1:
			MASTER.Menu.aktif = TMBL.Tombol.aktif
			self.keluar()
	def rubah_karakter(self):
		sebelum = 6 if (DATA.KARAKTER - 1) < 0 else DATA.KARAKTER - 1
		self.sebelum = self.buram_gambar(AVATAR[sebelum], (200, 255))
		self.karakter = self.rubah_skala(AVATAR[DATA.KARAKTER], (250, 315))
		sesudah = 0 if (DATA.KARAKTER + 1) > 6 else DATA.KARAKTER + 1
		self.sesudah = self.buram_gambar(AVATAR[sesudah], (200, 255))
	def buram_gambar(self, gambar, ukuran:tuple):
		ukuran_skala = (int(ukuran[0] * 0.6), int(ukuran[1] * 0.6))
		objek = pygame.transform.smoothscale(gambar, ukuran_skala)
		return pygame.transform.smoothscale(objek, ukuran)
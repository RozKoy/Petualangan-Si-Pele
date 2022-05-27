from . import Tombol as TMBL
from ..import Suara as SUARA

from ..Fungsi import (
	RUBAH_SKALA, 
	PERBAHARUI, 
	KELUAR, 
	TAMPIL,
	ACARA, 
	TEKAN
)
from ..Konstan import UKURAN_LAYAR

from ..Gambar.Latar import LATAR_BELAKANG_MENU
from ..Gambar.Tombol import DATA_TOMBOL

class Menu:
	aktif = 0
	musik_menu = SUARA.Suara('Aset\\Suara\\Musik\\menu.mp3', 'musik')
	def __init__(self):
		self.latar()
		self.tombol = TMBL.Tombol(DATA_TOMBOL[Menu.aktif])
		TMBL.Tombol.aktif = 0
		self.berjalan = True
	def latar(self):
		gambar = LATAR_BELAKANG_MENU[Menu.aktif].convert()
		ukuran = UKURAN_LAYAR
		self.latar_belakang = self.rubah_skala(gambar, ukuran)
	def tampil(self, Layar):
		while self.berjalan:
			self.tampilkan_isi(Layar)
			for acara in ACARA():
				if acara.type == KELUAR: 
					exit()
				elif acara.type == TEKAN:
					self.tombol.cek_aksi(acara.key)
					self.cek_aksi(acara.key, Layar)
			PERBAHARUI()
	def tampilkan_isi(self, Layar):
		TAMPIL(Layar, self.latar_belakang, (0, 0))
		self.tombol.tampil(Layar)
	def rubah_skala(self, gambar, ukuran):
		return RUBAH_SKALA(gambar, ukuran)
	def keluar(self):
		self.berjalan = False
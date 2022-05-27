from . import Main as MASTER
from . import Tombol as TMBL

from .. import Data as DATA

from ..Fungsi import TAMPIL, KANAN, KIRI, ENTER

from ..Gambar.Avatar import AVATAR

class Menu_karakter(MASTER.Menu):
	def __init__(self):
		super().__init__()
		self.rubah_karakter()
	def tampilkan_isi(self, Layar):
		super().tampilkan_isi(Layar)
		TAMPIL(Layar, self.sebelum, self.sebelum.get_rect(center = (230, 270)))
		TAMPIL(Layar, self.karakter, self.karakter.get_rect(center = (480, 270)))
		TAMPIL(Layar, self.sesudah, self.sesudah.get_rect(center = (730, 270)))
	def cek_aksi(self, key, Layar):
		if key in (KIRI, KANAN) and TMBL.Tombol.aktif == 0:
			self.tombol.efek_geser.mulai()
			DATA.KARAKTER += 1 if key == KANAN else 6
			DATA.KARAKTER %= 7
			self.rubah_karakter()
		elif key == ENTER and TMBL.Tombol.aktif == 1:
			self.tombol.efek_tekan.mulai()
			MASTER.Menu.aktif = TMBL.Tombol.aktif
			self.keluar()
	def rubah_karakter(self):
		self.karakter = self.rubah_skala(AVATAR[DATA.KARAKTER], (250, 315))
		sebelum = 6 if (DATA.KARAKTER - 1) < 0 else DATA.KARAKTER - 1
		self.sebelum = self.buram_gambar(AVATAR[sebelum], (200, 255))
		sesudah = 0 if (DATA.KARAKTER + 1) > 6 else DATA.KARAKTER + 1
		self.sesudah = self.buram_gambar(AVATAR[sesudah], (200, 255))
	def buram_gambar(self, gambar, ukuran):
		ukuran_skala = (int(ukuran[0] * 0.6), int(ukuran[1] * 0.6))
		objek = self.rubah_skala(gambar, ukuran_skala)
		return self.rubah_skala(objek, ukuran)
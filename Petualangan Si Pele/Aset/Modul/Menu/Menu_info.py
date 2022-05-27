from . import Main as MASTER

from ..Fungsi import TAMPIL, SURFACE, ENTER
from ..Konstan import UKURAN_LAYAR

from ..Gambar.Latar import LATAR_BELAKANG_MENU

class Menu_info(MASTER.Menu):
	def __init__(self, utama):
		super().__init__()
		self.utama = utama
		self.Latar_belakang_gelap = SURFACE(UKURAN_LAYAR)
		self.Latar_belakang_gelap.set_alpha(150)
	def latar(self):
		gambar = LATAR_BELAKANG_MENU[MASTER.Menu.aktif]
		self.latar_belakang = self.rubah_skala(gambar, (600, 400))
	def tampilkan_isi(self, Layar):
		TAMPIL(Layar, self.utama.latar_belakang, (0, 0))
		self.utama.tombol.tampil(Layar)
		TAMPIL(Layar, self.Latar_belakang_gelap, (0, 0))
		self.latar_tampil(Layar)
		self.tombol.tampil(Layar)
	def latar_tampil(self, Layar):
		posisi = self.latar_belakang.get_rect(center = (480, 270))
		TAMPIL(Layar, self.latar_belakang, posisi)
	def cek_aksi(self, key, Layar):
		if key == ENTER:
			self.tombol.efek_tekan.mulai()
			self.keluar()

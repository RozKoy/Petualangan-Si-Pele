from ..Fungsi import TAMPIL, SPRITE, RUBAH_SKALA
from ..Konstan import UKURAN_LAYAR

class Latar(SPRITE):
	def __init__(self, *, gambar, kecepatan, tambah = 1, ukuran_lebar = UKURAN_LAYAR[1], ulang = False, posisi_kiri = 0):
		super(Latar, self).__init__()
		self.__kecepatan = kecepatan
		self.__file = gambar
		self.__ukuran = self.ukuran(self.__file, ukuran_lebar)
		self.gambar = RUBAH_SKALA(self.__file, self.__ukuran)
		self.posisi = self.gambar.get_rect()
		self.posisi.bottom = UKURAN_LAYAR[1]
		self.posisi.left = posisi_kiri
		self.bergerak = True
		self.ulang = ulang
		self.tambah_kecepatan = tambah
	def ukuran(self, gambar, ukuran_lebar):
		def ukuran_panjang(gambar, ukuran):
			return gambar.get_width() * ukuran / gambar.get_height()
		return ukuran_panjang(gambar, ukuran_lebar), ukuran_lebar
	def perbaharui(self, grup):
		if self.bergerak:
			self.gerak()
		if self.posisi.right >= UKURAN_LAYAR[0]:
			self.cek_batas(grup)
		elif self.posisi.right < 0:
			self.kill()
	def cek_batas(self, grup):
		selisih = self.posisi.right - UKURAN_LAYAR[0]
		if selisih <= self.__kecepatan:
			selisih %= self.__kecepatan
			if self.posisi.right == UKURAN_LAYAR[0] + selisih:
				self.cek_ulang(grup, UKURAN_LAYAR[0] + selisih)
	def cek_ulang(self, grup, posisi_kiri):
		if self.ulang:
			grup.add(Latar(gambar = self.__file, kecepatan = self.__kecepatan, tambah = self.tambah_kecepatan, ukuran_lebar = self.__ukuran[1], ulang = self.ulang, posisi_kiri = posisi_kiri))
		else:
			self.bergerak = False
	def gerak(self):
		self.posisi.move_ip(-self.__kecepatan, 0)
	def kecepatan_berubah(self):
		self.__kecepatan += self.tambah_kecepatan
	def tampil(self, Layar):
		TAMPIL(Layar, self.gambar, self.posisi)
from . import Pemain as PEMAIN
from . import Latar as LATAR
from .. import Data as DATA

from ..Gambar.Fungsi import gambar as ambil_gambar

from ..Konstan import pygame, UKURAN_LAYAR, FPS, ENTER, SPASI
from ..Gambar.Latar_cerita import LATAR_BELAKANG
from ..Gambar.Karakter import GERAK
from ..Gambar.Cerita import CERITA

class Alur_cerita:
	def __init__(self):
		self.waktu = pygame.time.Clock()
		self.latar = LATAR.Latar(gambar = LATAR_BELAKANG.convert(), kecepatan = 8)
		self.pemain = PEMAIN.Pemain(self.gambar())
		self.latar_belakang = pygame.Surface((UKURAN_LAYAR))
		self.latar_belakang.set_alpha(150)
		self.cerita = [self.rubah_skala(i, self.ukuran(i)) for i in CERITA]
		self.berjalan = True
		self.ke = 0
	def gambar(self):
		lokasi = GERAK[DATA.KARAKTER]['lokasi']
		nama = GERAK[DATA.KARAKTER]['nama']
		return ambil_gambar(lokasi = lokasi, nama = nama)
	def ukuran(self, gambar):
		def ukuran_lebar(gambar, ukuran):
			return gambar.get_height() * ukuran / gambar.get_width()
		return 550, ukuran_lebar(gambar, 550)
	def tampil(self, Layar):
		while self.berjalan:
			self.tampilkan_isi(Layar)
			self.cek_acara(Layar)
			if self.ke == 4:
				self.latar.update(self.latar)
				self.pemain.lari()
				self.cek_batas_latar()
			pygame.display.flip()
			self.waktu.tick(FPS)
	def cek_batas_latar(self):
		if UKURAN_LAYAR[0] < self.latar.posisi.right < UKURAN_LAYAR[0] + 8:
			self.pemain.rect.x += 8
			if self.pemain.rect.left > UKURAN_LAYAR[0]:
				self.berjalan = False
	def tampilkan_isi(self, Layar):
		self.latar.tampil(Layar)
		self.pemain.tampil(Layar)
		if self.ke != 4:
			Layar.blit(self.latar_belakang, (0, 0))
			cerita = self.cerita[self.ke]
			Layar.blit(cerita, cerita.get_rect(center = (480, 270)))
	def cek_acara(self, Layar):
		for acara in pygame.event.get():
			if acara.type == pygame.QUIT:
				exit()
			elif acara.type == pygame.KEYUP:
				self.cek_aksi(acara.key, Layar)
	def cek_aksi(self, key, Layar):
		if key in (ENTER, SPASI):
			self.ke = 0 if self.ke > 3 else self.ke + 1
	def rubah_skala(self, gambar, ukuran):
		return pygame.transform.smoothscale(gambar, ukuran)
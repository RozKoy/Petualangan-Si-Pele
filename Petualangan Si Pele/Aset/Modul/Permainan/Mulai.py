from . import Rintangan as RINTANGAN
from ..Menu import Tombol as TMBL
from . import Pemain as PEMAIN
from . import Latar as LATAR
from . import Timer as TIMER
from .. import Data as DATA
from . import Fon as FON

from ..Gambar.Fungsi import gambar as ambil_gambar

from ..Konstan import pygame, UKURAN_LAYAR, FPS, ENTER, SPASI, ESCAPE, KANAN, KIRI
from ..Gambar.Latar_mulai import LATAR_BELAKANG, LINTASAN
from ..Gambar.Kalah import LATAR_KALAH, TOMBOL_KALAH
from ..Gambar.Jeda import LATAR_JEDA, TOMBOL_JEDA
from ..Gambar.Karakter import GERAK

class Mulai:
	def __init__(self):
		latar_belakang = LATAR.Latar(gambar = LATAR_BELAKANG.convert(), kecepatan = 1, ulang = True)
		lintasan = LATAR.Latar(gambar = LINTASAN, tambah = 2, ukuran_lebar = 100, kecepatan = 8, ulang = True)
		self.latar = pygame.sprite.Group()
		self.latar.add(latar_belakang, lintasan)
		self.rintangan = pygame.sprite.Group()
		self.rintangan.add(RINTANGAN.Rintangan())
		self.pemain = PEMAIN.Pemain(self.gambar())
		self.latar_jeda = self.rubah_skala(LATAR_JEDA['file'], LATAR_JEDA['ukuran'])
		self.tombol_jeda = TMBL.Tombol(TOMBOL_JEDA)
		self.latar_kalah = self.rubah_skala(LATAR_KALAH['file'], LATAR_KALAH['ukuran'])
		self.tombol_kalah = TMBL.Tombol(TOMBOL_KALAH)
		self.teks_waktu = FON.Fon(40, (860, 60), (255, 255, 255))
		self.teks_info = FON.Fon(15, (480, 535), (255, 255, 255))
		self.berjalan = True
		self.jeda = False
		self.kalah = False
		self.menit = 0
		self.hitung_waktu = pygame.USEREVENT + 1
		self.hitung_mundur = TIMER.Timer(3, self.latar, self.rintangan, self.pemain)
		self.waktu = pygame.time.Clock()
	def rubah_skala(self, gambar, ukuran):
		return pygame.transform.smoothscale(gambar, ukuran)
	def gambar(self):
		lokasi = GERAK[DATA.KARAKTER]['lokasi']
		nama = GERAK[DATA.KARAKTER]['nama']
		return ambil_gambar(lokasi = lokasi, nama = nama)
	def tampil(self, Layar):
		self.hitung_mundur.tampil(Layar)
		pygame.time.set_timer(self.hitung_waktu, 625)
		while self.berjalan:
			self.tampilkan_isi(Layar)
			self.cek_acara(Layar)
			self.teks_waktu.tampil(Layar, f'{self.menit} M')
			self.teks_info.tampil(Layar, '(ESC) - Jeda')
			if self.menit % 60 in (0,1,2,4,6):
				self.pemain.info.tampil_level(Layar)
			if self.cek_berhenti(Layar):
				continue
			self.gerak()
			self.cek_pemain_rintangan()
			pygame.display.flip()
			self.waktu.tick(FPS)
	def cek_berhenti(self, Layar):
		self.kalah = self.pemain.cek_darah()
		if self.kalah:
			self.tampilan_kalah(Layar)
			return True
		if self.jeda:
			self.tampilan_jeda(Layar)
			return True
		return False
	def tampilan_kalah(self, Layar):
		self.tampil_gelap(Layar)
		Layar.blit(self.latar_kalah, self.latar_kalah.get_rect(center = (480, 270)))
		self.tombol_kalah.tampil(Layar)
		pygame.display.flip()
	def tampilan_jeda(self, Layar):
		self.tampil_gelap(Layar)
		Layar.blit(self.latar_jeda, self.latar_jeda.get_rect(center = (480, 270)))
		self.tombol_jeda.tampil(Layar)
		pygame.display.flip()
	def tampil_gelap(self, Layar):
		latar_gelap = pygame.Surface(UKURAN_LAYAR)
		latar_gelap.set_alpha(150)
		Layar.blit(latar_gelap, (0, 0))
	def cek_pemain_rintangan(self):
		Terkena_rintangan = pygame.sprite.spritecollideany(self.pemain, self.rintangan)
		if Terkena_rintangan:
			self.rintangan.remove(Terkena_rintangan)
			self.pemain.darah_berkurang()
	def gerak(self):
		self.latar.update(self.latar)
		self.rintangan.update(self.rintangan)
		self.pemain.gerak(pygame.key.get_pressed())
	def tampilkan_isi(self, Layar):
		for l in self.latar:
			l.tampil(Layar)
		for r in self.rintangan:
			r.tampil(Layar)
		self.pemain.tampil(Layar)
		self.pemain.tampil_info(Layar)
	def cek_acara(self, Layar):
		for acara in pygame.event.get():
			if acara.type == pygame.QUIT:
				exit()
			elif acara.type == pygame.KEYUP:
				self.cek_aksi(acara.key, Layar)
			if acara.type == self.hitung_waktu and not (self.jeda or self.kalah):
				self.menit += 1
				self.cek_aksi_waktu()
	def cek_aksi(self, key, Layar):
		if key == ESCAPE and not (self.jeda or self.kalah):
			self.jeda = True
		if self.jeda or self.kalah:
			if key in (KANAN, KIRI):
				TMBL.Tombol.aktif += self.tombol_jeda.banyak_tombol - 1 if key == KIRI else 1
				TMBL.Tombol.aktif %= self.tombol_jeda.banyak_tombol
			if key in (SPASI, ENTER):
				if TMBL.Tombol.aktif == 0:
					self.berjalan = False
					RINTANGAN.Rintangan.atur_kembali(RINTANGAN.Rintangan)
				elif self.jeda:
					self.jeda = False
					self.hitung_mundur.tampil(Layar)
					pygame.time.set_timer(self.hitung_waktu, 625)
				elif self.kalah:
					self.berjalan = False
					RINTANGAN.Rintangan.atur_kembali(RINTANGAN.Rintangan)
					mulai_lagi = Mulai()
					mulai_lagi.tampil(Layar)
	def cek_aksi_waktu(self):
		if self.menit % 60 == 0:
			self.pemain.info.naik_level(self.latar, RINTANGAN.Rintangan())
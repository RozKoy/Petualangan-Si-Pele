from . import Rintangan as RINTANGAN
from . import Pemain_1 as PEMAIN
from . import Latar as LATAR
from . import Timer as T
from . import Fon as FON

from ..Menu import Tombol as TMBL
from .. import Data as DATA

from ..Fungsi import (
	AMBIL_GAMBAR, 
	RUBAH_SKALA, 
	PERBAHARUI, 
	USEREVENT, 
	TERTEKAN, 
	SURFACE, 
	KELUAR, 
	ESCAPE, 
	TAMPIL,
	TIMER, 
	GROUP, 
	WAKTU, 
	ACARA, 
	TEKAN, 
	ENTER, 
	SPASI, 
	KANAN, 
	KIRI
)
from ..Konstan import UKURAN_LAYAR, FPS

from ..Gambar.Info import LATAR_KALAH, TOMBOL_KALAH, LATAR_JEDA, TOMBOL_JEDA
from ..Gambar.Latar import LATAR_BELAKANG, LINTASAN
from ..Gambar.Karakter import GERAK_1

class Mulai:
	_Menang = 180
	def __init__(self, Layar):
		latar_belakang = LATAR.Latar(gambar = LATAR_BELAKANG.convert(), kecepatan = 1, ulang = True)
		lintasan = LATAR.Latar(gambar = LINTASAN, tambah = 2, ukuran_lebar = 100, kecepatan = 8, ulang = True)
		self.latar = GROUP()
		self.latar.add(latar_belakang, lintasan)
		self.rintangan = GROUP()
		self.rintangan.add(RINTANGAN.Rintangan())
		self.pemain = PEMAIN.Pemain(self.gambar())
		self.latar_jeda = RUBAH_SKALA(LATAR_JEDA['file'], LATAR_JEDA['ukuran'])
		self.tombol_jeda = TMBL.Tombol(TOMBOL_JEDA)
		self.latar_kalah = RUBAH_SKALA(LATAR_KALAH['file'], LATAR_KALAH['ukuran'])
		self.tombol_kalah = TMBL.Tombol(TOMBOL_KALAH)
		self.teks_waktu = FON.Fon(40, (860, 60), (255, 255, 255))
		self.teks_info = FON.Fon(15, (480, 535), (255, 255, 255))
		self.berjalan = True
		self.jeda = False
		self.kalah = False
		self.menang = False
		self.menit = 0
		self.hitung_waktu = USEREVENT + 1
		self.hitung_mundur = T.Timer(3, [self.latar, self.rintangan], [self.pemain, self.pemain.info], False)
		self.waktu = WAKTU()
		self.tampil(Layar)
	def gambar(self):
		lokasi = GERAK_1[DATA.KARAKTER]['lokasi']
		nama = GERAK_1[DATA.KARAKTER]['nama']
		return AMBIL_GAMBAR(lokasi = lokasi, nama = nama)
	def tampil(self, Layar):
		self.hitung_mundur.tampil(Layar)
		TIMER(self.hitung_waktu, 625, 1)
		while self.berjalan:
			self.tampilkan_isi(Layar)
			self.cek_acara(Layar)
			if self.menit % 60 in (0,1,2,4,6):
				self.pemain.info.tampil_level(Layar)
			if self.cek_kalah(Layar):
				continue
			self.gerak()
			if self.pemain.posisi.left > UKURAN_LAYAR[0]:
				self.berjalan = False
				self.menang = True
			self.cek_pemain_rintangan()
			PERBAHARUI()
			self.waktu.tick(FPS)
		RINTANGAN.Rintangan.atur_kembali(RINTANGAN.Rintangan)
		if not self.menang:
			self.pemain.info.atur_kembali()
	def cek_kalah(self, Layar):
		if not self.pemain.cek_darah():
			self.tampilan_kalah(Layar)
			self.kalah = True
			return True
		if self.jeda:
			self.tampilan_jeda(Layar)
			return True
		return False
	def tampilan_kalah(self, Layar):
		self.tampil_gelap(Layar)
		TAMPIL(Layar, self.latar_kalah, self.latar_kalah.get_rect(center = (480, 270)))
		self.tombol_kalah.tampil(Layar)
		PERBAHARUI()
	def tampilan_jeda(self, Layar):
		self.tampil_gelap(Layar)
		TAMPIL(Layar, self.latar_jeda, self.latar_jeda.get_rect(center = (480, 270)))
		self.tombol_jeda.tampil(Layar)
		PERBAHARUI()
	def tampil_gelap(self, Layar):
		latar_gelap = SURFACE(UKURAN_LAYAR)
		latar_gelap.set_alpha(150)
		TAMPIL(Layar, latar_gelap, (0, 0))
	def cek_pemain_rintangan(self):
		for rintangan in self.rintangan:
			if self.pemain.kena_rintangan(rintangan.posisi):
				rintangan.hilang()
	def gerak(self):
		berhenti = False
		for latar in self.latar:
			latar.perbaharui(self.latar)
		if self.menit < Mulai._Menang or self.pemain.posisi.y != 330:
			self.pemain.gerak(TERTEKAN())
		else:
			self.pemain.lari()
			self.pemain.posisi.x += 5
		if self.menit > Mulai._Menang - 5:
			berhenti = True
		for rintangan in self.rintangan:
			rintangan.bergerak(self.rintangan, berhenti)
	def tampilkan_isi(self, Layar):
		for latar in self.latar:
			latar.tampil(Layar)
		for rintangan in self.rintangan:
			rintangan.tampil(Layar)
		self.pemain.tampil(Layar)
		self.pemain.info.tampil(Layar)
		self.teks_waktu.tampil(Layar, f'{self.menit} M')
		self.teks_info.tampil(Layar, '(ESC) - Jeda')
	def cek_acara(self, Layar):
		for acara in ACARA():
			if acara.type == KELUAR:
				exit()
			elif acara.type == TEKAN:
				self.cek_aksi(acara.key, Layar)
			if acara.type == self.hitung_waktu and not (self.jeda or self.kalah):
				self.menit += 1
				TIMER(self.hitung_waktu, 625, 1)
				self.cek_aksi_waktu()
	def cek_aksi(self, key, Layar):
		if key == ESCAPE and not (self.jeda or self.kalah):
			self.jeda = True
		elif key in (KANAN, KIRI) and self.jeda:
			self.tombol_jeda.aksi(key, KIRI)
		elif key in (KANAN, KIRI) and self.kalah:
			self.tombol_kalah.aksi(key, KIRI)
		elif key in (SPASI, ENTER) and (self.jeda or self.kalah):
			if TMBL.Tombol.aktif == 0:
				self.berjalan = False
			elif TMBL.Tombol.aktif == 1:
				if self.jeda:
					self.jeda = False
					self.hitung_mundur.tampil(Layar)
					TIMER(self.hitung_waktu, 625)
				elif self.kalah:
					RINTANGAN.Rintangan.atur_kembali(RINTANGAN.Rintangan)
					self.pemain.info.atur_kembali()
					mulai_lagi = Mulai(Layar)
					self.berjalan = False
	def cek_aksi_waktu(self):
		if self.menit % 60 == 0:
			self.pemain.info.naik_level(self.latar, RINTANGAN.Rintangan())
		if self.menit % 25 == 0:
			self.pemain.unik()

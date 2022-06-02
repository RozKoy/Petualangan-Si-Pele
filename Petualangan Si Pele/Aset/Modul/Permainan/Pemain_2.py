from . import Info as INFO
from . import Peluru as PELURU

from .. import Data as DATA
from .. import Suara as S

from ..Fungsi import AMBIL_GAMBAR, RUBAH_SKALA, GROUP, HURUF_W, HURUF_A, HURUF_D, SPASI, ENTER
from ..Konstan import UKURAN_LAYAR

from ..Efek_suara.Karakter import LOKASI, SUARA
from ..Gambar.Peluru import PELURU_PEMAIN

import random

class Pemain:
	def __init__(self, file, darah):
		self.darah = darah
		self.batu = GROUP()
		self.file_jalan_kanan = self.gambar(file['jalan']['kanan'])
		self.file_jalan_kiri = self.gambar(file['jalan']['kiri'])
		self.file_lompat_kanan = self.gambar(file['lompat']['kanan'])
		self.file_lompat_kiri = self.gambar(file['lompat']['kiri'])
		self.file_lempar = self.gambar(file['lempar'])
		self.file_diam = self.file_lempar[0]
		self.gambar = self.file_diam
		self.posisi = self.gambar.get_rect()
		self.posisi.x = 70
		self.posisi.y = 340
		self.info = INFO.Info()
		self.info.rubah_darah(self.darah)
		self.efek_tembak = S.Suara(LOKASI[DATA.KARAKTER] + SUARA['tembak'])
		self.efek_kena_serang = S.Suara(LOKASI[DATA.KARAKTER] + SUARA['kena_rintangan'])
		self.efek_dapat_item = S.Suara('Aset\\Suara\\Efek_suara\\Permainan\\item.mp3')
		self.arah = 'kanan'
		self.kecepatan = 6
		self.melompat = False
		self.melempar = False
		self.batas_lompat = 5
		self.langkah = 0
		self.berjalan = True
	def gambar(self, file):
		gambar = AMBIL_GAMBAR(lokasi = file['lokasi'], nama = file['nama'])
		return [RUBAH_SKALA(i, self.ukuran(i)) for i in gambar]
	def ukuran(self, gambar):
		return 100, gambar.get_height() * 100 / gambar.get_width()
	def gerak(self, aksi):
		if not self.melempar:
			if aksi[HURUF_D]:
				self.jalan_kanan()
				self.arah = 'kanan'
			elif aksi[HURUF_A]:
				self.jalan_kiri()
				self.arah = 'kiri'
			elif aksi[ENTER] or aksi[SPASI]:
				self.melempar = True
			else:
				self.gambar = self.file_diam
				self.arah = 'kanan'
				self.langkah = 0
			if not self.melompat and aksi[HURUF_W]:
				self.melompat = True
				self.langkah = 0

		if self.melompat:
			self.lompat()
		elif self.melempar:
			self.lempar()

		if self.posisi.left <= 0:
			self.posisi.left = 0
		elif self.posisi.right >= UKURAN_LAYAR[0]:
			self.posisi.right = UKURAN_LAYAR[0]
	def jalan_kanan(self):
		self.posisi.move_ip(self.kecepatan, 0)
		self.gambar = self.file_jalan_kanan[self.langkah // 5]
		self.langkah = self.langkah + 1 if self.langkah < 13 else 0
	def jalan_kiri(self):
		self.posisi.move_ip(-self.kecepatan, 0)
		self.gambar = self.file_jalan_kiri[self.langkah // 5]
		self.langkah = self.langkah + 1 if self.langkah < 13 else 0
	def lompat(self):
		file = self.file_lompat_kanan if self.arah == 'kanan' else self.file_lompat_kiri
		self.gambar = file[0]
		if self.melompat:
			self.posisi.y -= self.batas_lompat * 3
			self.batas_lompat -= 0.4
			if self.batas_lompat <= 0:
				self.gambar = file[1]
		if self.posisi.y >= 340:
			self.posisi.y = 340
			self.batas_lompat = 5
			self.melompat = False
	def lempar(self):
		self.gambar = self.file_lempar[self.langkah // 10]
		self.langkah += 1
		if self.langkah == 20:
			self.efek_tembak.mulai()
			self.batu.add(PELURU.Peluru(RUBAH_SKALA(PELURU_PEMAIN, (25, 25)), 15))
		if self.langkah >= 30:
			self.langkah = 0
			self.melempar = False
	def serang(self, bos):
		for batu in self.batu:
			x = self.posisi.left + self.gambar.get_width() / 2
			batu.tembak((x, self.posisi.top), mode = 'parabola')
			if batu.kena(bos):
				batu.hilang()
				return True
		return False
	def dapat_item(self, item):
		if self.posisi.colliderect(item):
			self.efek_dapat_item.mulai()
			self.darah += random.randint(1, 5) * 10
			if self.darah > 100:
				self.darah = 100
			self.info.rubah_darah(self.darah)
			return True
		return False
	def posisi_karakter(self):
		return self.posisi.right, random.randint(self.posisi.top + self.posisi.height / 2, self.posisi.bottom)
	def darah_berkurang(self):
		self.darah -= random.randint(1, 4) * 5
		self.cek_kalah()
		self.info.rubah_darah(self.darah)
	def cek_kalah(self, bos = 960):
		if self.darah <= 0 or self.posisi.x >= bos:
			self.darah = 0
			self.info.rubah_darah(self.darah)
			return True
		return False
	def tampil(self, Layar):
		Layar.blit(self.gambar, self.posisi)
		for batu in self.batu:
			batu.tampil(Layar)

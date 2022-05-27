from .Fon import Fon

from .. import Suara as SUARA

from ..Fungsi import (
	PERBAHARUI, 
	USEREVENT, 
	SURFACE,
	TAMPIL, 
	KELUAR,
	WAKTU, 
	TIMER, 
	ACARA
)
from ..Konstan import UKURAN_LAYAR, FPS

class Timer:
	def __init__(self, waktu, grup, lainnya, tambahan):
		self.teks = Fon(80, (480, 270), (255, 255, 255))
		self.latar_belakang = SURFACE(UKURAN_LAYAR)
		self.latar_belakang.set_alpha(150)
		self.__waktu = waktu
		self.waktu = waktu
		self.grup = grup
		self.lainnya = lainnya
		self.tambahan = tambahan
		self.efek_suara = SUARA.Suara('Aset\\Suara\\Efek_suara\\Permainan\\hitung_mundur.mp3')
		self.jam = WAKTU()
	def tampil(self, Layar):
		hitung_mundur = USEREVENT + 1
		TIMER(hitung_mundur, 1000, self.__waktu)
		self.efek_suara.mulai()
		while True:
			self.tampilkan_isi(Layar)
			for acara in ACARA():
				if acara.type == KELUAR:
					exit()
				if acara.type == hitung_mundur:
					self.efek_suara.mulai()
					self.waktu -= 1
			if self.waktu == 0:
				break
			PERBAHARUI()
			self.jam.tick(FPS)
		self.waktu = self.__waktu
	def tampilkan_isi(self, Layar):
		if self.tambahan:
			TAMPIL(Layar, self.tambahan, (0, 0))
		if self.grup:
			for bagian in self.grup:
				for tampil in bagian:
					tampil.tampil(Layar)
		for bagian in self.lainnya:
			bagian.tampil(Layar)
		TAMPIL(Layar, self.latar_belakang, (0, 0))
		self.teks.tampil(Layar, self.waktu)
from ..Konstan import pygame, UKURAN_LAYAR, FPS
from .Fon import Fon

class Timer:
	def __init__(self, waktu, latar, rintangan, pemain):
		self.jam = pygame.time.Clock()
		self.__waktu = waktu
		self.waktu = waktu
		self.latar = latar
		self.rintangan = rintangan
		self.pemain = pemain
		self.teks = Fon(80, (480, 270), (255, 255, 255))
		self.latar_belakang = pygame.Surface((UKURAN_LAYAR))
		self.latar_belakang.set_alpha(150)
	def tampil(self, Layar):
		hitung_mundur = pygame.USEREVENT + 1
		pygame.time.set_timer(hitung_mundur, 1000, self.__waktu)
		while True:
			self.tampilkan_isi(Layar)
			for acara in pygame.event.get():
				if acara.type == pygame.QUIT:
					exit()
				if acara.type == hitung_mundur:
					self.waktu -= 1
			if self.waktu == 0:
				break
			pygame.display.flip()
			self.jam.tick(FPS)
		self.waktu = self.__waktu
	def tampilkan_isi(self, Layar):
		for l in self.latar:
			l.tampil(Layar)
		for r in self.rintangan:
			r.tampil(Layar)
		self.pemain.tampil(Layar)
		self.pemain.tampil_info(Layar)
		Layar.blit(self.latar_belakang, (0, 0))
		self.teks.tampil(Layar, self.waktu)
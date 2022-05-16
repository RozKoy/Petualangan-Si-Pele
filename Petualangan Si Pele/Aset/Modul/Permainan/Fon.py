from ..Konstan import pygame, FON

pygame.init()

class Fon:
	def __init__(self, ukuran, posisi, warna):
		path = 'Aset\\Fon\\' + FON
		self.fon = pygame.font.Font(path, ukuran)
		self.posisi = posisi
		self.warna = warna
	def tampil(self, Layar, teks):
		tampilan = self.fon.render(str(teks), True, self.warna)
		posisi = tampilan.get_rect(center = (self.posisi))
		Layar.blit(tampilan, posisi)
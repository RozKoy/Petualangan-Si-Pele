from ..Fungsi import TAMPIL, SPRITE
from ..Konstan import UKURAN_LAYAR

from math import sqrt

class Peluru(SPRITE):
	def __init__(self, gambar, kecepatan):
		super(Peluru, self).__init__()
		self.file = gambar
		self.gambar = gambar
		self.posisi = self.gambar.get_rect()
		self.x, self.y = 0, 0
		self.kecepatan = kecepatan
		self.arah = ''
		self.batas = 5
		self.menembak = False
	def tembak(self, posisi, target = (940, 0), mode = 'linear'):
		if not self.menembak:
			self.posisi = self.gambar.get_rect(center = posisi)
			samping = target[0] - posisi[0]
			self.arah = 'kanan' if samping >= 0 else 'kiri'
			if mode == 'linear':
				depan = target[1] - posisi[1]
				miring = sqrt(samping ** 2 + depan ** 2)
				self.x = self.kecepatan * samping / miring
				self.y = self.kecepatan * depan / miring
			else:
				self.x = self.kecepatan
			self.menembak = True
		if mode == 'parabola':
			self.y = self.batas * -2.5
			self.batas -= 0.35
		self.posisi.x += self.x
		self.posisi.y += self.y
		if self.posisi.x <= 0 or self.posisi.x >= UKURAN_LAYAR[0] or self.posisi.y <= 0 or self.posisi.y >= 450:
			self.hilang()
	def tampil(self, Layar):
		TAMPIL(Layar, self.gambar, self.posisi)
	def kena(self, target):
		if (self.arah == 'kanan' and self.posisi.x >= target) or (self.arah == 'kiri' and self.posisi.x <= target):
			return True
		return False
	def bakar(self, target):
		return self.posisi.colliderect(target)
	def hilang(self):
		self.kill()
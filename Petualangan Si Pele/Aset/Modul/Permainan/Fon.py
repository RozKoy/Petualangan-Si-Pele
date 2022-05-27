from ..Fungsi import TAMPIL, JENIS_FON
from ..Konstan import FON

class Fon:
	def __init__(self, ukuran, posisi, warna):
		path = 'Aset\\Fon\\' + FON
		self.fon = JENIS_FON(path, ukuran)
		self.posisi = posisi
		self.warna = warna
	def tampil(self, Layar, teks):
		tampilan = self.fon.render(str(teks), True, self.warna)
		posisi = tampilan.get_rect(center = (self.posisi))
		TAMPIL(Layar, tampilan, posisi)
from . import Data as DATA

from .Fungsi import SOUND

class Suara(SOUND):
	def __init__(self, nama, jenis = 'efek_suara'):
		super().__init__(nama)
		self.jenis = jenis
	def mulai(self):
		if self.jenis == 'musik' and DATA.MUSIK:
			self.play(-1)
		elif self.jenis == 'efek_suara' and DATA.EFEK_SUARA:
			self.play()
	def berhenti(self):
		self.stop()
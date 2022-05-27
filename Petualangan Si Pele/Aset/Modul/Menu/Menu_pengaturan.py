from . import Main as MASTER
from . import Tombol as TMBL

from .. import Data as DATA

from ..Fungsi import (
	AMBIL_GAMBAR, 
	TAMPIL, 
	KIRI, 
	KANAN, 
	ENTER
)

from ..Gambar.Suara import INFO_SUARA

class Menu_pengaturan(MASTER.Menu):
	def __init__(self):
		super().__init__()
		self.posisi_efek_suara = INFO_SUARA['INFO'][1]['posisi']
		self.posisi_musik = INFO_SUARA['INFO'][0]['posisi']
		self.cek_hidup_mati()
	def latar(self):
		super().latar()
		nama_gambar = INFO_SUARA['FILE']
		lokasi_gambar = INFO_SUARA['PATH']
		self.file = AMBIL_GAMBAR(lokasi = lokasi_gambar, nama = nama_gambar)
	def tampilkan_isi(self, Layar):
		super().tampilkan_isi(Layar)
		posisi = self.musik.get_rect(center = self.posisi_musik)
		TAMPIL(Layar, self.musik, posisi)
		posisi = self.efek_suara.get_rect(center = self.posisi_efek_suara)
		TAMPIL(Layar, self.efek_suara, posisi)
	def cek_aksi(self, key, Layar):
		if key in (KIRI, KANAN):
			self.tombol.aksi(key, KIRI)
		elif key == ENTER:
			self.tombol.efek_tekan.mulai()
			MASTER.Menu.aktif = TMBL.Tombol.aktif
			if TMBL.Tombol.aktif == 0: 
				DATA.MUSIK = not DATA.MUSIK
				MASTER.Menu.musik_menu.berhenti()
				MASTER.Menu.musik_menu.mulai()
			elif TMBL.Tombol.aktif == 1: 
				DATA.EFEK_SUARA = not DATA.EFEK_SUARA
			elif TMBL.Tombol.aktif == 2: 
				self.keluar()
			self.cek_hidup_mati()
	def cek_hidup_mati(self):
		gambar = self.file[DATA.MUSIK]
		ukuran = INFO_SUARA['INFO'][0]['ukuran']
		self.musik = self.rubah_skala(gambar, ukuran)
		gambar = self.file[DATA.EFEK_SUARA]
		ukuran = INFO_SUARA['INFO'][1]['ukuran']
		self.efek_suara = self.rubah_skala(gambar, ukuran)
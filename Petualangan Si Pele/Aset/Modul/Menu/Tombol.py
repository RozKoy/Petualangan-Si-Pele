from ..Gambar.Fungsi import gambar as ambil_gambar
from ..Konstan import pygame, ATAS, BAWAH

class Tombol:
	aktif = 0
	def __init__(self, file:dict):
		self.gambar = []
		self.ukuran = []
		self.posisi = []
		self.tambah_data(file)
		self.banyak_tombol = len(file['FILE'])
	def tambah_data(self, file:dict):
		for nama_file, data in zip(file['FILE'], file['INFO']):
			self.gambar.append(ambil_gambar(lokasi = file['PATH'], nama = nama_file))
			self.cek_list(data)
	def cek_list(self, data):
		if type(data) is not list: 
			self.tambah_ukuran_posisi(data['ukuran'], data['posisi'])
		else: 
			self.tambah_ukuran_posisi_grup(data)
	def tambah_ukuran_posisi(self, ukuran:tuple, posisi:tuple):
		self.ukuran.append(ukuran)
		self.posisi.append(posisi)
	def tambah_ukuran_posisi_grup(self, data:list):
		self.ukuran.append([d['ukuran'] for d in data])
		self.posisi.append([d['posisi'] for d in data])
	def tampil(self, Layar):
		for indeks in range(self.banyak_tombol):
			tambah = 0
			if indeks == Tombol.aktif: 
				tambah = 15
			if type(self.gambar[indeks]) is not list:
				self.tampil_data(Layar, indeks, tambah)
			else:
				self.tampil_data_grup(Layar, indeks, tambah)
	def cek_aksi(self, key:int):
		if key in (ATAS, BAWAH):
			Tombol.aktif += self.banyak_tombol - 1 if key == ATAS else 1
			Tombol.aktif %= self.banyak_tombol
	def gambar_berskala(self, gambar, ukuran:tuple):
		return pygame.transform.smoothscale(gambar, ukuran)
	def tampil_data(self, Layar, indeks:int, tambah:int):
		PANJANG, LEBAR = 0, 1
		ukuran = (self.ukuran[indeks][PANJANG] + tambah, self.ukuran[indeks][LEBAR] + tambah)
		gambar = self.gambar_berskala(self.gambar[indeks], ukuran)
		posisi = gambar.get_rect(center = self.posisi[indeks])
		Layar.blit(gambar, posisi)
	def tampil_data_grup(self, Layar, indeks:int, tambah:int):
		PANJANG, LEBAR = 0, 1
		for g, u, p in zip(self.gambar[indeks], self.ukuran[indeks], self.posisi[indeks]):
			ukuran = (u[PANJANG] + tambah, u[LEBAR] + tambah)
			gambar = self.gambar_berskala(g, ukuran)
			Layar.blit(gambar, gambar.get_rect(center = p))
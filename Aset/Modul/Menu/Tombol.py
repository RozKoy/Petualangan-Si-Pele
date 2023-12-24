from .. import Suara as SUARA

from ..Fungsi import (
	AMBIL_GAMBAR, 
	RUBAH_SKALA,
	TAMPIL,
	BAWAH,
	ATAS
)

class Tombol:
	aktif = 0
	efek_geser = SUARA.Suara('Aset\\Suara\\Efek_suara\\Permainan\\tombol_geser.wav')
	efek_tekan = SUARA.Suara('Aset\\Suara\\Efek_suara\\Permainan\\tombol_tekan.mp3')
	def __init__(self, file):
		self.gambar = []
		self.ukuran = []
		self.posisi = []
		self.tambah_data(file)
		self.banyak_tombol = len(file['FILE'])
	def tambah_data(self, file):
		for nama_file, data in zip(file['FILE'], file['INFO']):
			self.gambar.append(AMBIL_GAMBAR(lokasi = file['PATH'], nama = nama_file))
			self.cek_list(data)
	def cek_list(self, data):
		if type(data) is not list: 
			self.tambah_ukuran_posisi(data['ukuran'], data['posisi'])
		else: 
			self.tambah_ukuran_posisi_grup(data)
	def tambah_ukuran_posisi(self, ukuran, posisi):
		self.ukuran.append(ukuran)
		self.posisi.append(posisi)
	def tambah_ukuran_posisi_grup(self, data):
		self.ukuran.append([d['ukuran'] for d in data])
		self.posisi.append([d['posisi'] for d in data])
	def tampil(self, Layar):
		for indeks in range(self.banyak_tombol):
			tambah = 15 if indeks == Tombol.aktif else 0
			if type(self.gambar[indeks]) is not list:
				self.tampil_data(Layar, indeks, tambah)
			else:
				self.tampil_data_grup(Layar, indeks, tambah)
	def tampil_data(self, Layar, indeks, tambah):
		PANJANG, LEBAR = 0, 1
		ukuran = (self.ukuran[indeks][PANJANG] + tambah, self.ukuran[indeks][LEBAR] + tambah)
		gambar = RUBAH_SKALA(self.gambar[indeks], ukuran)
		posisi = gambar.get_rect(center = self.posisi[indeks])
		self.tampilkan(Layar, gambar, posisi)
	def tampil_data_grup(self, Layar, indeks, tambah):
		PANJANG, LEBAR = 0, 1
		for g, u, p in zip(self.gambar[indeks], self.ukuran[indeks], self.posisi[indeks]):
			ukuran = (u[PANJANG] + tambah, u[LEBAR] + tambah)
			gambar = RUBAH_SKALA(g, ukuran)
			self.tampilkan(Layar, gambar, gambar.get_rect(center = p))
	def cek_aksi(self, key):
		if key in (ATAS, BAWAH):
			self.aksi(key, ATAS)
	def aksi(self, key, nilai):
		self.efek_geser.mulai()
		Tombol.aktif += self.banyak_tombol - 1 if key == nilai else 1
		Tombol.aktif %= self.banyak_tombol
	def tampilkan(self, Layar, gambar, posisi):
		TAMPIL(Layar, gambar, posisi)
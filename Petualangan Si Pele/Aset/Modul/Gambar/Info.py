from ..Fungsi import AMBIL_GAMBAR

# Lokasi Info Permainan
PATH = 'Aset\\Gambar\\Permainan\\Level_1_3\\Info'

# Nama File Gambar Info Permainan
FILE_JEDA = [
	'menu_utama.png',
	'lanjut.png'
]
FILE_KALAH = [
	'menu_utama.png',
	'ulang.png'
]
FILE_MENU_UTAMA = [
	'menu_utama.png'
]

# Ukuran dan Posisi Tombol
INFO_JEDA = [
	{'ukuran' : (150, 40), 'posisi' : (330, 350)},
	{'ukuran' : (150, 40), 'posisi' : (630, 350)}
]
INFO_KALAH = [
	{'ukuran' : (150, 40), 'posisi' : (330, 350)},
	{'ukuran' : (150, 40), 'posisi' : (630, 350)}
]
INFO_MENU_UTAMA = [
	{'ukuran' : (150, 40), 'posisi' : (480, 350)}	
]

# Seluruh Informasi Pembangun Tombol Informasi pada Permainan
TOMBOL_JEDA = {'PATH' : PATH, 'FILE' : FILE_JEDA, 'INFO' : INFO_JEDA}
TOMBOL_KALAH = {'PATH' : PATH, 'FILE' : FILE_KALAH, 'INFO' : INFO_KALAH}
TOMBOL_MENU_UTAMA = {'PATH' : PATH, 'FILE' : FILE_MENU_UTAMA, 'INFO' : INFO_MENU_UTAMA}

# Latar Belakang Informasi Permainan
LATAR_JEDA = {
	'file' : AMBIL_GAMBAR(lokasi = PATH, nama = 'latar_jeda.png'),
	'ukuran' : (500, 265)
}
LATAR_KALAH = {
	'file' : AMBIL_GAMBAR(lokasi = PATH, nama = 'latar_kalah.png'),
	'ukuran' : (500, 245)
}
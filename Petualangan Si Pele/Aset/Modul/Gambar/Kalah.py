from .Fungsi import gambar

PATH = 'Aset\\Gambar\\Permainan\\Kalah'

LATAR_KALAH = {
	'file' : gambar(lokasi = PATH, nama = 'kalah.png'),
	'ukuran' : (500, 245)
}

FILE = [
	'menu_utama.png',
	'ulang.png'
]

INFO = [
	{'ukuran' : (150, 40), 'posisi' : (330, 350)},
	{'ukuran' : (150, 40), 'posisi' : (630, 350)}
]

TOMBOL_KALAH = {'PATH' : PATH, 'FILE' : FILE, 'INFO' : INFO}
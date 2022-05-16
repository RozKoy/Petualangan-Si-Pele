from .Fungsi import gambar

PATH = 'Aset\\Gambar\\Permainan\\Jeda'

LATAR_JEDA = {
	'file' : gambar(lokasi = PATH, nama = 'latar_belakang.png'),
	'ukuran' : (500, 265)
}

FILE = [
	'menu_utama.png',
	'lanjut.png'
]

INFO = [
	{'ukuran' : (150, 40), 'posisi' : (330, 350)},
	{'ukuran' : (150, 40), 'posisi' : (630, 350)}
]

TOMBOL_JEDA = {'PATH' : PATH, 'FILE' : FILE, 'INFO' : INFO}
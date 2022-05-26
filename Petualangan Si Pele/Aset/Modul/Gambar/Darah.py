from ..Fungsi import AMBIL_GAMBAR

# Darah Pemain
PATH = 'Aset\\Gambar\\Permainan\\Darah'
DARAH = {
	'papan' : AMBIL_GAMBAR(lokasi = PATH, nama = 'papan_darah.png'),
	'hijau' : AMBIL_GAMBAR(lokasi = PATH, nama = 'darah_hijau.png'),
	'merah' : AMBIL_GAMBAR(lokasi = PATH, nama = 'darah_merah.png')
}

# Darah Bos
PATH = 'Aset\\Gambar\\Permainan\\Darah'
DARAH_BOS = {
	'papan' : AMBIL_GAMBAR(lokasi = PATH, nama = 'papan_darah_bos.png'),
	'hijau' : AMBIL_GAMBAR(lokasi = PATH, nama = 'darah_hijau.png'),
	'merah' : AMBIL_GAMBAR(lokasi = PATH, nama = 'darah_merah.png')
}
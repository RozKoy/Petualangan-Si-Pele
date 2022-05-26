from ..Fungsi import AMBIL_GAMBAR

# Gambar Informasi Level / Tingkatan
PATH = 'Aset\\Gambar\\Permainan\\Pemain\\Level'
LEVEL = {
	1 : AMBIL_GAMBAR(lokasi = PATH, nama = 'level_1.png'),
	2 : AMBIL_GAMBAR(lokasi = PATH, nama = 'level_2.png'),
	3 : AMBIL_GAMBAR(lokasi = PATH, nama = 'level_3.png'),
	'bos' : AMBIL_GAMBAR(lokasi = PATH, nama = 'level_bos.png')
}
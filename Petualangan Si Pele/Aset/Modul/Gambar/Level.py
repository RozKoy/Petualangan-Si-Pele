from .Fungsi import gambar

PATH = 'Aset\\Gambar\\Permainan\\Level'

LEVEL = {
	1 : gambar(lokasi = PATH, nama = 'level_1.png'),
	2 : gambar(lokasi = PATH, nama = 'level_2.png'),
	3 : gambar(lokasi = PATH, nama = 'level_3.png'),
	'bos' : gambar(lokasi = PATH, nama = 'level_bos.png')
}
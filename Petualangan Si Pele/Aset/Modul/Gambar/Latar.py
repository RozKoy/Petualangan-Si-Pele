from ..Fungsi import AMBIL_GAMBAR

# Gambar Latar Belakang untuk Tiap Menu
PATH = 'Aset\\Gambar\\Menu\\Latar_belakang'
LATAR_BELAKANG_MENU = [
	AMBIL_GAMBAR(lokasi = PATH, nama = '1.jpg'),
	AMBIL_GAMBAR(lokasi = PATH, nama = '2.jpg'),
	AMBIL_GAMBAR(lokasi = PATH, nama = '3.jpg'),
	0,
	AMBIL_GAMBAR(lokasi = PATH, nama = '4.png')
]

# Gambar Latar Belakang untuk Tampilan Cerita dan Panduan pada Awal Permainan
PATH = 'Aset\\Gambar\\Permainan\\Alur_cerita'
LATAR_BELAKANG_ALUR_CERITA = AMBIL_GAMBAR(lokasi = PATH, nama = 'latar.jpg')

# Gambar Latar Belakang dan Lintasan untuk Level 1, Level 2 dan Level 3
PATH = 'Aset\\Gambar\\Permainan\\Level_1_3\\Latar'
LATAR_BELAKANG = AMBIL_GAMBAR(lokasi = PATH, nama = 'latar_belakang.png')
LINTASAN = AMBIL_GAMBAR(lokasi = PATH, nama = 'lintasan.png')

# Gambar Latar Belakang untuk Level Bos
PATH = 'Aset\\Gambar\\Permainan\\Bos'
LATAR_BELAKANG_BOS = AMBIL_GAMBAR(lokasi = PATH, nama = 'latar.jpg')

# Gambar Latar Belakang untuk Tampilan Menang
PATH = 'Aset\\Gambar\\Permainan\\Menang'
LATAR_BELAKANG_MENANG = AMBIL_GAMBAR(lokasi = PATH, nama = 'latar.jpg')
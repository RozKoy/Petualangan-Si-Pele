from ..Fungsi import AMBIL_GAMBAR

# Cerita dan Panduan Awal Permainan
PATH = 'Aset\\Gambar\\Permainan\\Alur_cerita\\Cerita'
CERITA_1 = AMBIL_GAMBAR(lokasi = PATH, nama = ['cerita_1.png', 'cerita_2.png', 'cerita_3.png', 'cerita_4.png'])

# Cerita dan Panduan Melawan Bos
PATH = 'Aset\\Gambar\\Permainan\\Bos\\Cerita'
CERITA_2 = AMBIL_GAMBAR(lokasi = PATH, nama = ['cerita_1.png', 'cerita_2.png'])

# Cerita Kemenangan
PATH = 'Aset\\Gambar\\Permainan\\Menang'
CERITA_3 = AMBIL_GAMBAR(lokasi = PATH, nama = 'menang.png')
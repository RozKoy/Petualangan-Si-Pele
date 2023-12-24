# Gambar yang digunakan untuk membangun sebuah Tombol
PATH_1 = 'Aset\\Gambar\\Menu\\Tombol\\Menu_utama'
PATH_2 = 'Aset\\Gambar\\Menu\\Tombol\\Menu_karakter'
PATH_3 = 'Aset\\Gambar\\Menu\\Tombol\\Menu_pengaturan'

# Gambar Tombol pada Menu Utama
FILE_1 = [
	'mulai.png',
	'karakter.png',
	'pengaturan.png',
	'keluar.png',
	'info.png'
]
# Gambar Tombol pada Menu Karakter
FILE_2 = [
	['panah_kiri.png', 'panah_kanan.png'],
	'pilih.png'
]
# Gambar Tombol pada Menu Pengaturan
FILE_3 = [
	'musik.png',
	'efek_suara.png',
	'kembali.png',
]

# Ukuran dan Posisi Tombol pada Menu Utama
INFO_1 = [
	{'ukuran' : (280, 105), 'posisi' : (240, 100)},
	{'ukuran' : (280, 105), 'posisi' : (240, 200)},
	{'ukuran' : (280, 105), 'posisi' : (240, 300)},
	{'ukuran' : (280, 105), 'posisi' : (240, 400)},
	{'ukuran' : (60, 60), 'posisi' : (910, 490)}
]
# Ukuran dan Posisi Tombol pada Menu Karakter
INFO_2 = [
	[{'ukuran' : (30, 35), 'posisi' : (310, 490)}, {'ukuran' : (30, 35), 'posisi' : (650, 490)}],
	{'ukuran' : (180, 55), 'posisi' : (480, 490)}
]
# Ukuran dan Posisi Tombol pada Menu Pengaturan
INFO_3 = [
	{'ukuran' : (340, 90), 'posisi' : (480, 210)},
	{'ukuran' : (340, 90), 'posisi' : (480, 300)},
	{'ukuran' : (70, 70), 'posisi' : (70, 490)}
]
# Ukurang dan Posisi Tombol pada Menu Informasi
INFO_4 = [
	{'ukuran' : (25, 25), 'posisi' : (255, 425)}
]

# Kumpulan data Tombol pada Menu
DATA_TOMBOL = {
	0 : {'PATH' : PATH_1, 'FILE' : FILE_1, 'INFO' : INFO_1},
	1 : {'PATH' : PATH_2, 'FILE' : FILE_2, 'INFO' : INFO_2},
	2 : {'PATH' : PATH_3, 'FILE' : FILE_3, 'INFO' : INFO_3},
	3 : 0,
	4 : {'PATH' : PATH_3, 'FILE' : [FILE_3[2]], 'INFO' : INFO_4}
}
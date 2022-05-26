from ..Fungsi import AMBIL_GAMBAR

# Gerakan Bos
PATH = 'Aset\\Gambar\\Permainan\\Bos\\Gerak\\'
GERAK = {
	'jalan' : {
		'kanan' : AMBIL_GAMBAR(lokasi = PATH + 'Berjalan\\Kanan', nama = ['bos1.png', 'bos2.png', 'bos3.png']),
		'kiri' : AMBIL_GAMBAR(lokasi = PATH + 'Berjalan\\Kiri', nama = ['bos1.png', 'bos2.png', 'bos3.png'])
	},
	'lempar' : AMBIL_GAMBAR(lokasi = PATH + 'Melempar', nama = ['bos1.png', 'bos2.png', 'bos3.png'])
}
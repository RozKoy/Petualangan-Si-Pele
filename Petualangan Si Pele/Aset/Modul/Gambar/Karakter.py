from .Fungsi import gambar

PATH = 'Aset\\Gambar\\Permainan\\Karakter'

AVATAR = gambar(lokasi = PATH, nama = ['SiPele.png', 'Affan.png', 'Carin.png', 'Ilham.png', 'Hariando.png', 'Robi.png', 'Rozin.png'])

GERAK = [
	{'lokasi' : PATH + '\\Aset_SiPele', 'nama' : ['Pele1.png', 'Pele2.png', 'Pele3.png', 'Pele4.png']},
	{'lokasi' : PATH + '\\Aset_Affan', 'nama' : ['Affan1.png', 'Affan2.png', 'Affan3.png', 'Affan4.png']},
	{'lokasi' : PATH + '\\Aset_Carin', 'nama' : ['Carin1.png', 'Carin2.png', 'Carin3.png', 'Carin4.png']},
	{'lokasi' : PATH + '\\Aset_Ilham', 'nama' : ['Ilham1.png', 'Ilham2.png', 'Ilham3.png', 'Ilham4.png']},
	{'lokasi' : PATH + '\\Aset_Hariando', 'nama' : ['Ando1.png', 'Ando2.png', 'Ando3.png', 'Ando4.png']},
	{'lokasi' : PATH + '\\Aset_Robi', 'nama' : ['Robi1.png', 'Robi2.png', 'Robi3.png', 'Robi4.png']},
	{'lokasi' : PATH + '\\Aset_Rozin', 'nama' : ['Rozin1.png', 'Rozin2.png', 'Rozin3.png', 'Rozin4.png']}
]

PATH = 'Aset\\Gambar\\Permainan\\Darah'

DARAH = {
	'papan' : gambar(lokasi = PATH, nama = 'papan_darah.png'),
	'hijau' : gambar(lokasi = PATH, nama = 'darah_hijau.png'),
	'merah' : gambar(lokasi = PATH, nama = 'darah_merah.png')
}
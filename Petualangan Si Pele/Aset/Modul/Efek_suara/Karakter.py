PATH = 'Aset\\Suara\\Efek_suara\\Karakter\\'

NAMA = ('Affan', 'Affan', 'Carin', 'Ilham', 'Hariando', 'Robi', 'Rozin')

LOKASI = [f'{PATH}{nama_folder}\\{nama_folder}' for nama_folder in NAMA]

SUARA = {
	'kena_rintangan' : '_KenaObstekel.mp3',
	'tembak' : '_Menembak.mp3',
	'lompat' : '_Lompat.mp3',
	'lari' : '_Lari.mp3'
}

SUARA_UNIK = [
	['_Unik1.mp3', '_Unik2.mp3'],
	['_Unik1.mp3', '_Unik2.mp3'],
	['_Unik1.mp3', '_Unik2.mp3'],
	['_Unik1.mp3', '_Unik2.mp3', '_Unik3.mp3'],
	['_Unik1.mp3', '_Unik2.mp3', '_Unik3.mp3', '_Unik4.mp3', '_Unik5.mp3'],
	['_Unik1.mp3', '_Unik2.mp3', '_Unik3.mp3'],
	['_Unik1.mp3', '_Unik2.mp3', '_Unik3.mp3'],
]
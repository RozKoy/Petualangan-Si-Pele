from ..Konstan import KIRI, KANAN, ENTER

from ..Permainan import Alur_cerita as AC
from ..Permainan import Mulai as M

from . import Menu_pengaturan as MP
from . import Menu_karakter as MK
from . import Menu_info as MI

from . import Main as MASTER
from . import Tombol as TMBL

class Menu_utama(MASTER.Menu):
	def cek_aksi(self, key:int, Layar):
		if key in (KIRI, KANAN):
			TMBL.Tombol.aktif += self.tombol.banyak_tombol - 1 if key == KIRI else 1
			TMBL.Tombol.aktif %= self.tombol.banyak_tombol
		elif key == ENTER:
			MASTER.Menu.aktif = TMBL.Tombol.aktif
			menu = False
			if TMBL.Tombol.aktif == 0:
				menu = AC.Alur_cerita()
				menu.tampil(Layar)
				menu = M.Mulai()
			elif TMBL.Tombol.aktif == 1:
				menu = MK.Menu_karakter()
			elif TMBL.Tombol.aktif == 2:
				menu = MP.Menu_pengaturan()
			elif TMBL.Tombol.aktif == 3: 
				self.keluar()
			elif TMBL.Tombol.aktif == 4: 
				menu = MI.Menu_info(self)
			if menu:
				menu.tampil(Layar)
			TMBL.Tombol.aktif = MASTER.Menu.aktif
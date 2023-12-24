from . import Main as MASTER
from . import Tombol as TMBL

from . import Menu_pengaturan as MP
from . import Menu_karakter as MK
from . import Menu_info as MI

from .. import Suara as SUARA

from ..Permainan import Alur_cerita as AC
from ..Permainan import Menang as MENANG
from ..Permainan import Lawan_bos as B
from ..Permainan import Mulai as M

from ..Fungsi import TAMPIL, KIRI, KANAN, ENTER

class Menu_utama(MASTER.Menu):
	def __init__(self, Layar):
		super().__init__()
		self.tampil(Layar)
	def tampil(self, Layar):
		self.musik_menu.mulai()
		super().tampil(Layar)
	def cek_aksi(self, key, Layar):
		if key in (KIRI, KANAN):
			self.tombol.aksi(key, KIRI)
		elif key == ENTER:
			self.tombol.efek_tekan.mulai()
			menu = False
			MASTER.Menu.aktif = TMBL.Tombol.aktif
			if TMBL.Tombol.aktif == 0:
				MASTER.Menu.musik_menu.berhenti()
				musik_mulai = SUARA.Suara('Aset\\Suara\\Musik\\mulai.mp3', 'musik')
				musik_mulai.mulai()
				menu = AC.Alur_cerita(Layar)
				menu = M.Mulai(Layar)
				musik_mulai.berhenti()
				if menu.pemain.cek_darah() and menu.menang:
					menu = B.Lawan_bos(Layar, menu.pemain.cek_darah())
					menu = MENANG.Menang(Layar) if menu.menang else False
				menu = False
				MASTER.Menu.musik_menu.mulai()
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
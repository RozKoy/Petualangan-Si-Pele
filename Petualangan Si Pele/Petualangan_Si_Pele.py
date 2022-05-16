from Aset.Modul.Cek import *

if __name__ == '__main__':
	Layar = pygame.display.set_mode(UKURAN_LAYAR)
	pygame.display.set_icon(ICON.convert())
	pygame.display.set_caption(NAMA)
	Menu = Menu_utama()
	Menu.tampil(Layar)
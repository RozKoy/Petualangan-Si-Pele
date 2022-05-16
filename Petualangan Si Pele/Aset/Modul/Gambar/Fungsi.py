from ..Konstan import pygame

def gambar(*, lokasi:str = '', nama):
	if type(nama) is str:
		return pygame.image.load(lokasi + '\\' + nama)
	return [pygame.image.load(lokasi + '\\' + i) for i in nama]
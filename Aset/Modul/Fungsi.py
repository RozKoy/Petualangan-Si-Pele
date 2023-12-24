import pygame 
import pygame.locals

pygame.init()

TAMPILAN = lambda A: pygame.display.set_mode(A)
JUDUL = lambda A: pygame.display.set_caption(A)
LAMBANG = lambda A: pygame.display.set_icon(A)

SURFACE = lambda A: pygame.Surface(A)

RUBAH_SKALA = lambda A,B: pygame.transform.smoothscale(A, B)
JENIS_FON = lambda A,B: pygame.font.Font(A, B)
TAMPIL = lambda A,B,C: A.blit(B, C)

TIMER = lambda A,B,C = 0: pygame.time.set_timer(A, B, C)

TERTEKAN = lambda: pygame.key.get_pressed()
PERBAHARUI = lambda: pygame.display.flip()
GROUP = lambda: pygame.sprite.Group()
WAKTU = lambda: pygame.time.Clock()
ACARA = lambda: pygame.event.get()

SPRITE = pygame.sprite.Sprite
SOUND = pygame.mixer.Sound

USEREVENT = pygame.USEREVENT

KELUAR = pygame.QUIT
TEKAN = pygame.KEYUP

HURUF_A = pygame.K_a
HURUF_D = pygame.K_d
HURUF_W = pygame.K_w

ESCAPE = pygame.locals.K_ESCAPE
ENTER = pygame.locals.K_RETURN
SPASI = pygame.locals.K_SPACE

KANAN = pygame.locals.K_RIGHT
BAWAH = pygame.locals.K_DOWN
KIRI = pygame.locals.K_LEFT
ATAS = pygame.locals.K_UP

def AMBIL_GAMBAR(*, lokasi = '', nama):
	if type(nama) is str:
		return pygame.image.load(lokasi + '\\' + nama)
	return [pygame.image.load(lokasi + '\\' + i) for i in nama]
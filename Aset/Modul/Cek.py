from .Konstan import (
    UKURAN_LAYAR,
    NAMA,
    LINK
)


def tampil(teks: str, posisi: str = 'tengah'):
    if posisi == 'kiri':
        print('| ' + '{:<40}'.format(teks) + ' |')
    else:
        print('| ' + '{:^40}'.format(teks) + ' |')


def garis():
    tampil('-'*40, 'tengah')


try:
    from .Fungsi import TAMPILAN, LAMBANG, JUDUL
    from .Menu import Menu_utama as MENU
    from .Gambar.Icon import ICON
except ModuleNotFoundError:
    print()
    garis()
    tampil('#- Sepele Squad - 04 -#')
    garis()
    tampil('Pesan :', 'kiri')
    tampil('=> Modul Pygame Tidak Ada <=')
    garis()
    tampil('Butuh Bantuan ?', 'kiri')
    garis()
    masukan = input('=> Pilih (y/n): ')
    if masukan in ('Y', 'y'):
        import os
        os.system('start https://www.pygame.org/wiki/GettingStarted')
    exit()
finally:
    tampil('Salam Hangat Kami - Sepele Squad (04)')
    garis()
    print('LINK :', LINK)

# -*- coding: utf-8 -*-
"""web_jpg.py — Copias ligeras (< 500 KB) de los blueprints para presentaciones,
correo y mensajería."""
import os
from PIL import Image

BLUEPRINTS = ['BLU-00_blueprint_completo_A0', 'BLU-01_blueprint',
              'BLU-02_blueprint_cortes_fachadas']


def main(entregadir, ancho_max=2200, calidad=84):
    for base in BLUEPRINTS:
        src = os.path.join(entregadir, base + '.jpg')
        if not os.path.exists(src):
            print('  (falta)', src)
            continue
        im = Image.open(src).convert('RGB')
        if im.width > ancho_max:
            alto = int(round(im.height * ancho_max / im.width))
            im = im.resize((ancho_max, alto), Image.LANCZOS)
        dst = os.path.join(entregadir, base + '_web.jpg')
        im.save(dst, 'JPEG', quality=calidad, optimize=True, progressive=True)
        print('%-46s %5.0f KB  %d × %d' % (base + '_web.jpg',
              os.path.getsize(dst) / 1024.0, im.width, im.height))


if __name__ == '__main__':
    base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    main(os.path.join(base, 'entrega'))

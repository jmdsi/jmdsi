# -*- coding: utf-8 -*-
"""indice.py — Índice visual de láminas (contact sheet) para revisión rápida."""
import os
from PIL import Image, ImageDraw, ImageFont

FONT_R = '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'
FONT_B = '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'

LAMINAS = [
    ('BLU-00_blueprint_completo_A0.png',
     'BLU-00  BLUEPRINT DE CONJUNTO (A0) — PLANTAS, CORTES, ALZADOS Y SITUACIÓN'),
    ('A-01_planta_baja.png', 'A-01  PLANTA BAJA  ·  E 1:50'),
    ('A-02_planta_alta.png', 'A-02  PLANTA ALTA  ·  E 1:50'),
    ('A-03_cortes_detalles.png', 'A-03  CORTES A-A / B-B + DETAILS  ·  E 1:50'),
    ('A-04_fachadas.png', 'A-04  FACHADAS  ·  E 1:50'),
    ('A-05_azotea_situacion.png', 'A-05  AZOTEA Y SITUACIÓN  ·  E 1:75 / 1:280'),
    ('A-06_cortes_fachadas_situacion.png',
     'A-06  CORTES Y FACHADAS (BAJA Y ALTA) + SITUACIÓN  ·  E 1:100'),
    ('S-01_situacion_bloque.png', 'S-01  SITUACIÓN DEL BLOQUE  ·  E 1:200'),
    ('BLU-01_blueprint.png', 'BLU-01  BLUEPRINT — PLANTAS, CORTE Y FACHADA'),
    ('BLU-02_blueprint_cortes_fachadas.png',
     'BLU-02  BLUEPRINT — CORTES Y FACHADAS + SITUACIÓN'),
]


def main(entregadir, salida, cols=3, ancho=760):
    filas = (len(LAMINAS) + cols - 1) // cols
    muestra = Image.open(os.path.join(entregadir, LAMINAS[0][0]))
    ratio = muestra.height / muestra.width
    alto = int(ancho * ratio)
    cab = 74
    pie = 30
    W = cols * (ancho + 14) + 14
    H = cab + filas * (alto + pie + 14) + 14
    img = Image.new('RGB', (W, H), '#f4f6f8')
    d = ImageDraw.Draw(img)
    ft = ImageFont.truetype(FONT_B, 30)
    fs = ImageFont.truetype(FONT_R, 17)
    fb = ImageFont.truetype(FONT_B, 18)
    d.rectangle([0, 0, W, cab - 10], fill='#14456e')
    d.text((24, 14), 'ÍNDICE DE LÁMINAS  ·  BLOQUE DORMITORIOS', font=ft, fill='white')
    d.text((W - 430, 22), 'JMDSI · Ingeniería y Arquitectura  ·  2026-10-04',
           font=fs, fill='#c8dcee')
    for i, (arch, titulo) in enumerate(LAMINAS):
        cx = 14 + (i % cols) * (ancho + 14)
        cy = cab + (i // cols) * (alto + pie + 14)
        im = Image.open(os.path.join(entregadir, arch)).convert('RGB')
        im = im.resize((ancho, alto), Image.LANCZOS)
        img.paste(im, (cx, cy))
        d.rectangle([cx, cy, cx + ancho, cy + alto], outline='#9bb3c8')
        d.text((cx + 4, cy + alto + 6), titulo, font=fb, fill='#14456e')
    img.save(salida)
    print('Índice generado:', salida, os.path.getsize(salida) // 1024, 'KB')


if __name__ == '__main__':
    base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    main(os.path.join(base, 'entrega'), os.path.join(base, 'entrega', 'INDICE_laminas.png'))

# -*- coding: utf-8 -*-
"""
build.py — Genera todas las láminas del BLOQUE DORMITORIOS.

Uso:  python3 build.py [--dpi 150] [--out DIR] [--solo A-06]

Láminas (formato A1, 841 × 594 mm):
  A-01  Planta baja                                        E 1:50
  A-02  Planta alta                                        E 1:50
  A-03  Cortes A-A y B-B (planta baja y alta) + detalles   E 1:50 / 1:20 / 1:25
  A-04  Fachadas sur, norte, este y oeste                  E 1:50
  A-05  Planta de azotea y planta de situación             E 1:75 / 1:330
  A-06  Cortes y fachadas (baja y alta) + situación        E 1:100 / 1:600
  BLU-01 Blueprint: plantas baja y alta + corte y fachada  E 1:75 / 1:100
"""
import argparse
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from core import *          # noqa
from bloque import *        # noqa
from vistas import *        # noqa

FECHA = '2026-10-04'
PROYECTO = 'BLOQUE DORMITORIOS — 2 NIVELES (PLANTA BAJA Y ALTA)'
PLANTILLA = dict(proyecto=PROYECTO, fecha=FECHA, autor='JMDSI · Área de Proyectos',
                 emplazamiento='Campus JMDSI — predio 100,00 × 100,00 m',
                 rev='Emisión inicial')

# Marco de dibujo y cajetín
MX0, MY0, MX1, MY1 = 25.0, 12.0, 829.0, 582.0
CAJ = (639.0, 520.0, 829.0, 582.0)


# ---------------------------------------------------------------------------
def cajetin_lamina(s, datos):
    d = dict(PLANTILLA)
    d.update(datos)
    return cajetin(s, d)


def titulo_vista(sheet, xo, yo, titulo, escala, sub=None, w=None, h=3.6):
    ancho = w if w else max(58.0, len(titulo) * h * 0.62)
    sheet.text((xo, yo), titulo, h=h, bold=True)
    sheet.line((xo, yo + 2.6), (xo + ancho, yo + 2.6), 'marco-medio')
    sheet.text((xo + ancho, yo), escala, h=2.2, anchor='end', layer='texto-suave')
    if sub:
        sheet.text((xo, yo + 5.6), sub, h=2.0, layer='texto-suave')
    return ancho


def notas(sheet, x, y, titulo, lineas, w_col=None, size=2.0, dy=3.4):
    sheet.text((x, y), titulo, h=2.4, bold=True)
    sheet.line((x, y + 2.2), (x + (w_col or 90), y + 2.2), 'marco-medio')
    yy = y + 6.0
    for ln in lineas:
        sheet.text((x, yy), '• ' + ln, h=size, layer='texto')
        yy += dy
    return yy


def cuadro_vanos(sheet, x, y, nivel):
    filas = [['Nº', 'Tipo', 'Ubicación', 'Ancho', 'Alto', 'Alféizar', 'Cant.']]
    agrup = {}
    for w in ventanas(nivel):
        clave = (w['cod'], w['tipo'], w['muro'], w['w'], w['h'], w['sill'])
        agrup[clave] = agrup.get(clave, 0) + 1
    tipo_txt = dict(dorm='Ventana 2 hojas', ssh='Ventana alta', esc='Ventana',
                    serv='Ventana', lav='Ventana', estar='Ventanal')
    muro_txt = dict(N='Fachada norte', S='Fachada sur', E='Fachada este',
                    O='Fachada oeste')
    for k in sorted(agrup):
        cod, tipo, muro, w, h, sill = k
        muro_s = 'Fachada este' if (muro == 'E' and nivel == 1) else muro_txt.get(muro, muro)
        filas.append([cod, tipo_txt.get(tipo, 'Ventana'), muro_s, fmt(w, 2), fmt(h, 2),
                      nivel_txt(sill), str(agrup[k])])
    return cuadro(sheet, x, y, filas, [14, 32, 34, 16, 16, 18, 12], h_fila=4.5,
                  h_cab=5.2, size=1.8)


def cuadro_niveles(sheet, x, y, w_cols=None, h_fila=4.4, size=1.85):
    filas = [['Nivel', 'Cota', 'Alt. libre', 'Destino', 'Estructura']]
    filas.append(['Terreno natural', nivel_txt(NIVEL_TERRENO), '—', 'Exterior', '—'])
    filas.append(['Fondo de cimiento', nivel_txt(-1.05), '—',
                  'Cimiento corrido 0,70 × 0,25', 'Concreto 1:8 + 25 % P.M.'])
    filas.append(['N.P.T. planta baja', '±0,00', fmt(H_LIBRE_PB, 2) + ' m',
                  'Dormitorios · SS.HH. · escalera', 'Losa aligerada h=0,30 m'])
    filas.append(['N.P.T. planta alta', nivel_txt(NPT_PA), fmt(H_LIBRE_PA, 2) + ' m',
                  'Dormitorios · estudio', 'Losa aligerada h=0,30 m'])
    filas.append(['N.P.T. azotea', nivel_txt(NPT_CUB), '—', 'Cubierta inaccesible',
                  'Pendiente 2 %'])
    filas.append(['Remate de parapeto', nivel_txt(7.15), fmt(H_PARAPETO, 2) + ' m',
                  'Parapeto perimetral', 'Albardilla de concreto'])
    return cuadro(sheet, x, y, filas, w_cols or [40, 24, 22, 70, 56], h_fila=h_fila,
                  h_cab=5.2, size=size)


def cuadro_carpinteria(sheet, x, y):
    """Cuadro resumen de carpintería (puertas y ventanas) del bloque."""
    filas = [['Nº', 'Tipo de carpintería', 'Medidas', 'Ubicación', 'Cant.']]
    filas.append(['P-1', 'Puerta de 1 hoja', '0,90 × 2,10', 'Dormitorios, depósito, lavandería', '20'])
    filas.append(['P-2', 'Puerta de 1 hoja', '0,80 × 2,10', 'SS.HH. (por nivel)', '4'])
    filas.append(['P-3', 'Puerta de 2 hojas', '1,80 × 2,40', 'Ingreso principal (vestíbulo)', '1'])
    filas.append(['P-4', 'Puerta de 1 hoja', '1,20 × 2,10', 'Sala de estudio (planta alta)', '1'])
    filas.append(['V-1', 'Ventana corredera 2 hojas', '1,50 × 1,50', 'Dormitorios (ambos niveles)', '16'])
    filas.append(['V-2', 'Ventana alta', '0,50 × 0,80', 'SS.HH. (por nivel)', '4'])
    filas.append(['V-3', 'Ventanal', '2,00 × 1,70', 'Sala de estudio (planta alta)', '1'])
    filas.append(['V-4', 'Ventanas varias', '0,90 a 1,50', 'Servicios, lavandería y escalera', '10'])
    return cuadro(sheet, x, y, filas, [12, 52, 26, 60, 14], h_fila=4.3, h_cab=5.0,
                  size=1.75)


def linea_corte_planta(v, tipo, pos, etiqueta='A', x0=0.0, x1=L_BLOQUE, y0=0.0,
                       y1=D_BLOQUE, largo=0.65):
    if tipo == 'h':
        v.line((x0 - largo, pos), (x1 + largo, pos), layer='marco-medio')
        for (xx, s) in [(x0 - largo, -1), (x1 + largo, 1)]:
            v.line((xx, pos), (xx + s * largo, pos), layer='marco-medio')
            v.fill([(xx + s * largo, pos), (xx, pos - 0.30), (xx, pos + 0.30)],
                   layer='marco-medio')
            v.text((xx + s * largo * 1.30, pos), etiqueta, h=2.6, anchor='middle',
                   bold=True)
    else:
        v.line((pos, y0 - largo), (pos, y1 + largo), layer='marco-medio')
        for (yy, s) in [(y0 - largo, -1), (y1 + largo, 1)]:
            v.line((pos, yy), (pos, yy + s * largo), layer='marco-medio')
            v.fill([(pos, yy + s * largo), (pos - 0.30, yy), (pos + 0.30, yy)],
                   layer='marco-medio')
            v.text((pos, yy + s * largo * 1.45), etiqueta, h=2.6, anchor='middle',
                   bold=True)


def situacion_panel(s, x, y, denom, titulo, escala_txt, w_linea=110.0):
    v = View(s, x, y, denom=denom, nombre='SIT')
    situacion_mini(v)
    s.text((x - 13, y - 175.0 / denom * 100), titulo, h=2.8, bold=True)
    s.line((x - 13, y - 175.0 / denom * 100 + 2.6),
           (x - 13 + w_linea, y - 175.0 / denom * 100 + 2.6), 'marco-medio')
    s.text((x - 13, y + 108 * 1000.0 / denom + 6.0), escala_txt, h=2.0,
           layer='texto-suave')
    return v


# ===========================================================================
# A-01 / A-02 — PLANTAS
# ===========================================================================
def lamina_planta(nivel):
    cod = 'A-01' if nivel == 0 else 'A-02'
    nom = 'PLANTA BAJA' if nivel == 0 else 'PLANTA ALTA'
    cota = 'N.P.T. ±0,00' if nivel == 0 else 'N.P.T. +3,25'
    s = Sheet(841, 594, codigo=cod, titulo=nom, escala='E 1:50')
    marco_lamina(s)
    # ---- planta ----
    v = View(s, 100, 246, denom=50, nombre='P%d' % nivel)
    planta(v, nivel)
    linea_corte_planta(v, 'h', 1.95, 'A', largo=0.65)
    linea_corte_planta(v, 'v', 12.0, 'B', largo=0.65)
    titulo_vista(s, 64, 296, nom + '  ·  ' + cota, 'E 1:50',
                 sub='Escala 1:50  ·  cotas en metros  ·  mobiliario tipo')
    # ---- situación ----
    vs = View(s, 650, 310, denom=650, nombre='SIT')
    situacion_mini(vs)
    s.text((638, 128), 'SITUACIÓN  ·  BLOQUE DORMITORIOS (D)', h=2.8, bold=True)
    s.line((638, 130.6), (800, 130.6), 'marco-medio')
    s.text((638, 330), 'Escala 1:650  ·  predio de 100,00 × 100,00 m', h=2.0,
           layer='texto-suave')
    # ---- cuadros ----
    cuadro_areas(s, 30, 340, nivel=nivel, w_cols=[15, 15, 46, 16], h_fila=4.4,
                 size=1.85)
    cuadro_ejes(s, 250, 340)
    cuadro_vanos(s, 250, 392, nivel)
    cuadro_niveles(s, 420, 340, w_cols=[36, 20, 22, 60, 50], h_fila=4.3, size=1.75)
    notas(s, 420, 385, 'AMOBLAMIENTO TIPO — DORMITORIO DOBLE (11,36 m²)', [
        '2 camas de 1,00 × 2,00 m, 2 escritorios de 1,20 × 0,60 m y 1 ropero.',
        'SS.HH. por nivel: 3 inodoros, 3 lavabos, 2 duchas y 1 urinario.',
        'Aforo: 16 camas por nivel · 32 camas en total.',
    ], w_col=176, size=1.85, dy=3.3)
    notas(s, 420, 425, 'NOTAS', [
        'Pasillo central de 1,70 m libre (ancho mínimo de circulación).',
        'Puertas de dormitorio 0,90 m y de SS.HH. 0,80 m.',
        'Dormitorios con ventilación cruzada (fachadas opuestas).',
    ], w_col=200, size=1.85, dy=3.3)
    # ---- norte y escalas ----
    norte(s, 792, 462, r=13)
    escala_grafica(s, 640, 480, 50, n=5, seg_m=1.0)
    cajetin_lamina(s, dict(codigo=cod, contenido=nom + '  ·  planta de arquitectura '
                           'amoblada, ejes y cotas', escala='E 1:50', num=cod,
                           hoja='1 de 1'))
    return s


# ===========================================================================
# A-03 — CORTES + DETALLES
# ===========================================================================
def lamina_cortes():
    s = Sheet(841, 594, codigo='A-03', titulo='CORTES A-A Y B-B', escala='E 1:50')
    marco_lamina(s)
    # ---- Corte A-A ----
    v1 = View(s, 110, 200, denom=50, nombre='AA')
    corte_transversal(v1, 12.0)
    titulo_vista(s, 86, 30, 'CORTE A-A  ·  TRANSVERSAL', 'E 1:50',
                 sub='Crujía de 9,60 m — niveles ±0,00 · +3,25 · +6,20', w=180)
    # ---- Corte B-B ----
    v2 = View(s, 300, 430, denom=50, nombre='BB')
    corte_longitudinal(v2, 2.0)
    titulo_vista(s, 276, 262, 'CORTE B-B  ·  LONGITUDINAL', 'E 1:50',
                 sub='Longitud de 24,00 m — planta baja y planta alta', w=200)
    # ---- Detalle 1: cimiento ----
    v3 = View(s, 96, 330, denom=20, nombre='D1')
    detalle_cimiento(v3)
    titulo_vista(s, 60, 278, 'DETALLE 1  ·  CIMIENTO CORRIDO', 'E 1:20',
                 sub='Cimiento, sobrecimiento y solera', w=120, h=2.6)
    # ---- Detalle 2: alero y parapeto ----
    v5 = View(s, 700, 330, denom=20, oy=7.70, nombre='D2')
    detalle_parapeto(v5)
    titulo_vista(s, 640, 296, 'DETALLE 2  ·  ALERO Y PARAPETO', 'E 1:20',
                 sub='Encuentro de losa de azotea con parapeto', w=118, h=2.6)
    # ---- Detalle 3: escalera ----
    v4 = View(s, 140, 400, denom=25, nombre='D3')
    detalle_escalera(v4)
    titulo_vista(s, 138, 440, 'DETALLE 3  ·  ESCALERA', 'E 1:25',
                 sub='2 tramos · 18 C/H de 0,181 m · huella 0,28 m', w=120, h=2.6)
    # ---- cuadros y notas ----
    cuadro_niveles(s, 620, 30, w_cols=[34, 20, 22, 50, 50], h_fila=4.4, size=1.8)
    notas(s, 620, 80, 'NOTAS DE CORTE', [
        'Losa aligerada h = 0,30 m en ambos niveles.',
        'Vigas peraltadas de borde en las fachadas norte y sur.',
        'Albañilería confinada con columnas de amarre en los ejes.',
        'Concreto estructural f\'c = 210 kg/cm²; acero fy = 4 200 kg/cm².',
    ], w_col=180, size=1.85, dy=3.3)
    escala_grafica(s, 640, 190, 50, n=5, seg_m=1.0)
    escala_grafica(s, 640, 212, 20, n=5, seg_m=0.1)
    cajetin_lamina(s, dict(codigo='A-03', contenido='Cortes A-A y B-B (planta baja y '
                           'alta) + detalles constructivos',
                           escala='E 1:50 / 1:20 / 1:25', num='A-03', hoja='1 de 1'))
    return s


# ===========================================================================
# A-04 — FACHADAS
# ===========================================================================
def lamina_fachadas():
    s = Sheet(841, 594, codigo='A-04', titulo='FACHADAS', escala='E 1:50')
    marco_lamina(s)
    v1 = View(s, 100, 230, denom=50, nombre='FS')
    fachada(v1, 'S')
    titulo_vista(s, 76, 62, 'FACHADA SUR  ·  PRINCIPAL', 'E 1:50',
                 sub='Ingreso principal — niveles bajo (0,00) y alto (+3,25)', w=200)
    v2 = View(s, 100, 470, denom=50, nombre='FN')
    fachada(v2, 'N')
    titulo_vista(s, 76, 302, 'FACHADA NORTE  ·  POSTERIOR', 'E 1:50',
                 sub='Ventanas de dormitorios en ambos niveles', w=200)
    v3 = View(s, 590, 230, denom=50, nombre='FE')
    fachada(v3, 'E')
    titulo_vista(s, 566, 62, 'FACHADA ESTE', 'E 1:50', w=120,
                 sub='Lavandería, depósito y sala de estudio')
    v4 = View(s, 590, 470, denom=50, nombre='FO')
    fachada(v4, 'O')
    titulo_vista(s, 566, 302, 'FACHADA OESTE', 'E 1:50', w=120,
                 sub='Dormitorios extremos — ambos niveles')
    notas(s, 40, 486, 'ACABADOS DE FACHADA', [
        'Muros tarrajeados y pintados (látex acrílico, 2 manos).',
        'Sobrecimiento visto de concreto 1:8 + 25 % P.M.',
        'Parapeto de azotea con albardilla de concreto.',
        'Bajantes pluviales PVC Ø 4" y montantes empotradas.',
        'Ventanas de aluminio con vidrio templado de 6 mm.',
    ], w_col=230, size=1.85, dy=3.3)
    escala_grafica(s, 250, 486, 50, n=5, seg_m=1.0)
    cuadro_carpinteria(s, 250, 500)
    cajetin_lamina(s, dict(codigo='A-04', contenido='Fachadas sur, norte, este y oeste '
                           '(niveles bajo y alto) con dimensiones', escala='E 1:50',
                           num='A-04', hoja='1 de 1'))
    return s


# ===========================================================================
# A-05 — AZOTEA Y SITUACIÓN
# ===========================================================================
def lamina_azotea_situacion():
    s = Sheet(841, 594, codigo='A-05', titulo='AZOTEA Y SITUACIÓN',
              escala='E 1:75 / 1:330')
    marco_lamina(s)
    v1 = View(s, 60, 176, denom=75, nombre='AZ')
    planta_azotea(v1)
    titulo_vista(s, 40, 20, 'PLANTA DE AZOTEA  ·  N.P.T. +6,20', 'E 1:75',
                 sub='Pendiente 2 % hacia sumideros · parapeto h=0,95 m', w=200)
    v2 = View(s, 430, 470, denom=280, nombre='SIT')
    situacion(v2)
    titulo_vista(s, 412, 108, 'PLANTA DE SITUACIÓN  ·  CONJUNTO', 'E 1:280',
                 sub='Ubicación del Bloque Dormitorios (D) dentro del predio', w=230)
    s.text((412, 497), 'Escala 1:280  ·  predio de 100,00 × 100,00 m', h=2.0,
           layer='texto-suave')
    norte(s, 790, 100, r=15)
    notas(s, 412, 60, 'NOTAS DE AZOTEA E INSTALACIONES', [
        'Losa aligerada con pendiente 2 % hacia sumideros de 2".',
        'Caseta de escalera N.P.T. +9,45 con altura libre de 2,20 m.',
        'Tanque elevado de 2 × 1 100 L sobre la losa de azotea.',
        'Bajantes pluviales: 4 unidades en las esquinas.',
        'Ductos de ventilación de SS.HH. sobresalen de la azotea.',
    ], w_col=230, size=1.85, dy=3.3)
    cuadro_niveles(s, 654, 20, w_cols=[32, 18, 20, 48, 48], h_fila=4.3, size=1.72)
    escala_grafica(s, 412, 100, 75, n=5, seg_m=1.0)
    cajetin_lamina(s, dict(codigo='A-05', contenido='Planta de azotea (cubierta) y '
                           'planta de situación del conjunto',
                           escala='E 1:75 / 1:330', num='A-05', hoja='1 de 1'))
    return s


# ===========================================================================
# A-06 — CORTES Y FACHADAS (BAJA Y ALTA) + SITUACIÓN
# ===========================================================================
def lamina_cortes_fachadas():
    s = Sheet(841, 594, codigo='A-06',
              titulo='CORTES Y FACHADAS — PLANTA BAJA Y ALTA', escala='E 1:100')
    marco_lamina(s)
    v1 = View(s, 70, 150, denom=100, nombre='AA')
    corte_transversal(v1, 12.0)
    titulo_vista(s, 58, 42, 'CORTE A-A  ·  TRANSVERSAL', 'E 1:100',
                 sub='Crujía 9,60 m — ±0,00 · +3,25 · +6,20', w=140, h=3.2)
    v2 = View(s, 240, 150, denom=100, nombre='BB')
    corte_longitudinal(v2, 2.0)
    titulo_vista(s, 226, 42, 'CORTE B-B  ·  LONGITUDINAL', 'E 1:100',
                 sub='Longitud 24,00 m — planta baja y planta alta', w=160, h=3.2)
    v3 = View(s, 70, 380, denom=100, nombre='FS')
    fachada(v3, 'S')
    titulo_vista(s, 58, 272, 'FACHADA SUR  ·  PRINCIPAL (BAJA Y ALTA)', 'E 1:100',
                 sub='Ingreso principal · niveles ±0,00 y +3,25', w=180, h=3.2)
    v4 = View(s, 360, 380, denom=100, nombre='FN')
    fachada(v4, 'N')
    titulo_vista(s, 348, 272, 'FACHADA NORTE (BAJA Y ALTA)', 'E 1:100',
                 sub='Ventanas de dormitorios en los dos niveles', w=180, h=3.2)
    # ---- miniatura de situación ----
    vs = View(s, 630, 500, denom=600, nombre='SIT')
    situacion_mini(vs)
    titulo_vista(s, 617, 296, 'SITUACIÓN DEL BLOQUE (D)', 'E 1:600',
                 sub='Miniatura de emplazamiento en el conjunto', w=120, h=2.8)
    s.text((617, 516), 'Escala 1:600', h=2.0, layer='texto-suave')
    # ---- resumen y cuadros ----
    notas(s, 620, 30, 'CUADRO RESUMEN — BLOQUE DORMITORIOS (D)', [
        'Planta baja: 8 dormitorios dobles, SS.HH., depósito, lavandería y vestíbulo.',
        'Planta alta: 8 dormitorios dobles, SS.HH. y sala de estar y estudio.',
        '16 camas por nivel · 32 camas en total (aforo 32 personas).',
        'Losas aligeradas h = 0,30 m · luces de 3,35 y 3,70 m.',
        'Escalera de 2 tramos: 18 contrahuellas de 0,181 m.',
    ], w_col=200, size=1.85, dy=3.3)
    cuadro_niveles(s, 620, 90, w_cols=[30, 18, 20, 46, 46], h_fila=4.1, size=1.65)
    escala_grafica(s, 620, 132, 100, n=5, seg_m=1.0)
    escala_grafica(s, 620, 148, 600, n=2, seg_m=10.0)
    cajetin_lamina(s, dict(codigo='A-06',
                           contenido='Cortes y fachadas (planta baja y alta) con '
                           'dimensiones + miniatura de situación',
                           escala='E 1:100 / 1:600', num='A-06', hoja='1 de 1'))
    return s


# ===========================================================================
# BLU-01 — BLUEPRINT (cianotipo)
# ===========================================================================
def lamina_blueprint():
    s = Sheet(841, 594, codigo='BLU-01', titulo='BLUEPRINT — BLOQUE DORMITORIOS',
              escala='E 1:75 / 1:100', tema='blueprint')
    marco_lamina(s)
    v1 = View(s, 74, 250, denom=75, nombre='PB')
    planta(v1, 0)
    titulo_vista(s, 40, 108, 'PLANTA BAJA  ·  N.P.T. ±0,00', 'E 1:75', h=3.2, w=170)
    v2 = View(s, 466, 250, denom=75, nombre='PA')
    planta(v2, 1)
    titulo_vista(s, 432, 108, 'PLANTA ALTA  ·  N.P.T. +3,25', 'E 1:75', h=3.2, w=170)
    v3 = View(s, 110, 470, denom=100, nombre='AA')
    corte_transversal(v3, 12.0)
    titulo_vista(s, 98, 370, 'CORTE A-A  ·  TRANSVERSAL', 'E 1:100', h=2.8, w=130)
    v4 = View(s, 330, 470, denom=100, nombre='FS')
    fachada(v4, 'S')
    titulo_vista(s, 318, 370, 'FACHADA SUR  ·  PRINCIPAL', 'E 1:100', h=2.8, w=150)
    # ---- situación ----
    vs = View(s, 668, 300, denom=700, nombre='SIT')
    situacion_mini(vs)
    titulo_vista(s, 656, 96, 'SITUACIÓN DEL BLOQUE (D)', 'E 1:700', h=2.8, w=120)
    s.text((656, 316), 'Escala 1:700', h=2.0, layer='texto-suave')
    notas(s, 620, 336, 'DATOS CLAVE', [
        'Bloque de 24,00 × 9,60 m en planta.',
        '2 niveles: ±0,00 y +3,25 · azotea en +6,20.',
        '16 dormitorios dobles (32 camas).',
        'Pasillo central de 1,70 m.',
        'Escalera: 18 C/H de 0,181 m.',
    ], w_col=180, size=1.9, dy=3.4)
    escala_grafica(s, 620, 400, 100, n=5, seg_m=1.0)
    norte(s, 790, 468, r=13)
    cajetin_lamina(s, dict(codigo='BLU-01',
                           contenido='Blueprint — plantas, corte y fachada del Bloque '
                           'Dormitorios', escala='E 1:75 / 1:100',
                           num='BLU-01', hoja='1 de 1'))
    return s


# ===========================================================================
# S-01 — SITUACIÓN DEL BLOQUE (E 1:200)
# ===========================================================================
def lamina_situacion():
    s = Sheet(841, 594, codigo='S-01',
              titulo='SITUACIÓN DEL BLOQUE DORMITORIOS', escala='E 1:200')
    marco_lamina(s)
    v = View(s, 100, 540, denom=200, nombre='SIT')
    situacion(v)
    titulo_vista(s, 84, 24, 'PLANTA DE SITUACIÓN  ·  BLOQUE DORMITORIOS (D)', 'E 1:200',
                 sub='Predio de 100,00 × 100,00 m — cotas generales en metros', w=300)
    s.text((84, 570), 'Escala 1:200  ·  norte magnético indicado', h=2.0,
           layer='texto-suave')
    norte(s, 800, 60, r=15)
    notas(s, 620, 60, 'DATOS DEL EMPLAZAMIENTO', [
        'Predio: 100,00 × 100,00 m (10 000 m²).',
        'Bloques: aulas, administración y biblioteca, comedor y cocina.',
        'Bloque Dormitorios (D): 24,00 × 9,60 m — 2 niveles.',
        'Vía de acceso de 6,00 m con estacionamiento exterior.',
        'Vereda perimetral de 1,50 m y patio central de 28,00 × 18,00 m.',
    ], w_col=190, size=1.85, dy=3.4)
    escala_grafica(s, 620, 150, 200, n=5, seg_m=1.0)
    escala_grafica(s, 620, 168, 200, n=2, seg_m=10.0)
    cajetin_lamina(s, dict(codigo='S-01', contenido='Planta de situación — ubicación '
                           'del Bloque Dormitorios (D) en el conjunto',
                           escala='E 1:200', num='S-01', hoja='1 de 1'))
    return s


# ===========================================================================
# BLU-02 — BLUEPRINT DE CORTES Y FACHADAS
# ===========================================================================
def lamina_blueprint_cortes():
    s = Sheet(841, 594, codigo='BLU-02', titulo='BLUEPRINT — CORTES Y FACHADAS',
              escala='E 1:100', tema='blueprint')
    marco_lamina(s)
    v1 = View(s, 70, 150, denom=100, nombre='AA')
    corte_transversal(v1, 12.0)
    titulo_vista(s, 58, 42, 'CORTE A-A  ·  TRANSVERSAL', 'E 1:100',
                 sub='Crujía 9,60 m — ±0,00 · +3,25 · +6,20', w=140, h=3.2)
    v2 = View(s, 250, 150, denom=100, nombre='BB')
    corte_longitudinal(v2, 2.0)
    titulo_vista(s, 236, 42, 'CORTE B-B  ·  LONGITUDINAL', 'E 1:100',
                 sub='Longitud 24,00 m — planta baja y planta alta', w=160, h=3.2)
    v3 = View(s, 70, 380, denom=100, nombre='FS')
    fachada(v3, 'S')
    titulo_vista(s, 58, 272, 'FACHADA SUR  ·  PRINCIPAL (BAJA Y ALTA)', 'E 1:100',
                 sub='Ingreso principal · niveles ±0,00 y +3,25', w=180, h=3.2)
    v4 = View(s, 360, 380, denom=100, nombre='FN')
    fachada(v4, 'N')
    titulo_vista(s, 348, 272, 'FACHADA NORTE (BAJA Y ALTA)', 'E 1:100',
                 sub='Ventanas de dormitorios en los dos niveles', w=180, h=3.2)
    vs = View(s, 630, 500, denom=600, nombre='SIT')
    situacion_mini(vs)
    titulo_vista(s, 617, 296, 'SITUACIÓN DEL BLOQUE (D)', 'E 1:600',
                 sub='Miniatura de emplazamiento en el conjunto', w=120, h=2.8)
    s.text((617, 516), 'Escala 1:600', h=2.0, layer='texto-suave')
    notas(s, 620, 30, 'CUADRO RESUMEN — BLOQUE DORMITORIOS (D)', [
        'Planta baja: 8 dormitorios dobles, SS.HH., depósito, lavandería y vestíbulo.',
        'Planta alta: 8 dormitorios dobles, SS.HH. y sala de estar y estudio.',
        '16 camas por nivel · 32 camas en total (aforo 32 personas).',
        'Losas aligeradas h = 0,30 m · luces de 3,35 y 3,70 m.',
        'Escalera de 2 tramos: 18 contrahuellas de 0,181 m.',
    ], w_col=200, size=1.85, dy=3.3)
    cuadro_niveles(s, 620, 90, w_cols=[30, 18, 20, 46, 46], h_fila=4.1, size=1.65)
    escala_grafica(s, 620, 132, 100, n=5, seg_m=1.0)
    escala_grafica(s, 620, 148, 600, n=2, seg_m=10.0)
    cajetin_lamina(s, dict(codigo='BLU-02',
                           contenido='Blueprint — cortes y fachadas (planta baja y '
                           'alta) con situación', escala='E 1:100 / 1:600',
                           num='BLU-02', hoja='1 de 1'))
    return s


# ===========================================================================
# BLU-00 — BLUEPRINT COMPLETO (A0)
# ===========================================================================
def lamina_blueprint_completo():
    """Blueprint de conjunto en A0: plantas, cortes, fachadas/alzados y situación."""
    s = Sheet(1189, 841, codigo='BLU-00',
              titulo='BLUEPRINT — BLOQUE DORMITORIOS (JUEGO COMPLETO)',
              escala='E 1:100 / 1:500', tema='blueprint')
    marco_lamina(s)
    # ---------------- título general ----------------
    s.text((40, 22), 'BLOQUE DORMITORIOS  ·  BLUEPRINT DE CONJUNTO', h=6.4, bold=True)
    s.line((40, 27.5), (620, 27.5), 'marco-medio')
    s.text((40, 33), 'Plantas baja y alta  ·  cortes A-A y B-B  ·  fachadas sur, norte '
           'y este  ·  situación', h=2.6, layer='texto-suave')
    s.text((40, 40), 'Dimensiones en metros  ·  niveles en metros  ·  2026-10-04',
           h=2.2, layer='texto-suave')
    # ---------------- plantas ----------------
    v1 = View(s, 105, 205, denom=100, nombre='PB')
    planta(v1, 0)
    titulo_vista(s, 68, 72, 'PLANTA BAJA  ·  N.P.T. ±0,00', 'E 1:100', h=3.4, w=170)
    v2 = View(s, 415, 205, denom=100, nombre='PA')
    planta(v2, 1)
    titulo_vista(s, 378, 72, 'PLANTA ALTA  ·  N.P.T. +3,25', 'E 1:100', h=3.4, w=170)
    # ---------------- situación ----------------
    vs = View(s, 762, 258, denom=500, nombre='SIT')
    situacion_mini(vs)
    titulo_vista(s, 746, 26, 'SITUACIÓN DEL BLOQUE (D)', 'E 1:500', h=2.8, w=120,
                 sub=None)
    s.text((746, 282), 'Escala 1:500  ·  predio de 100,00 × 100,00 m', h=2.0,
           layer='texto-suave')
    # ---------------- cortes ----------------
    v3 = View(s, 150, 480, denom=100, nombre='AA')
    corte_transversal(v3, 12.0)
    titulo_vista(s, 100, 386, 'CORTE A-A  ·  TRANSVERSAL', 'E 1:100',
                 sub='Crujía 9,60 m — ±0,00 · +3,25 · +6,20', w=150, h=3.0)
    v4 = View(s, 390, 480, denom=100, nombre='BB')
    corte_longitudinal(v4, 2.0)
    titulo_vista(s, 356, 386, 'CORTE B-B  ·  LONGITUDINAL', 'E 1:100',
                 sub='Longitud 24,00 m — planta baja y planta alta', w=170, h=3.0)
    # ---------------- fachadas / alzados ----------------
    v5 = View(s, 760, 470, denom=100, nombre='FS')
    fachada(v5, 'S')
    titulo_vista(s, 700, 366, 'FACHADA SUR  ·  PRINCIPAL', 'E 1:100',
                 sub='Ingreso principal · niveles ±0,00 y +3,25', w=170, h=3.0)
    v6 = View(s, 130, 665, denom=100, nombre='FN')
    fachada(v6, 'N')
    titulo_vista(s, 100, 560, 'FACHADA NORTE', 'E 1:100',
                 sub='Ventanas de dormitorios en ambos niveles', w=170, h=3.0)
    v7 = View(s, 470, 665, denom=100, nombre='FE')
    fachada(v7, 'E')
    titulo_vista(s, 452, 560, 'FACHADA ESTE', 'E 1:100', h=3.0, w=120,
                 sub='Lavandería, depósito y sala de estudio')
    v8 = View(s, 780, 665, denom=100, nombre='FO')
    fachada(v8, 'O')
    titulo_vista(s, 762, 560, 'FACHADA OESTE', 'E 1:100', h=3.0, w=120,
                 sub='Dormitorios extremos — ambos niveles')
    # ---------------- cuadros y notas ----------------
    notas(s, 640, 560, 'DATOS CLAVE DEL BLOQUE', [
        'Bloque de 24,00 × 9,60 m en planta · 2 niveles.',
        'Niveles: ±0,00 · +3,25 (planta alta) · +6,20 (azotea).',
        '16 dormitorios dobles de 11,36 m² · 32 camas.',
        'Pasillo central de 1,70 m libre.',
        'Escalera de 2 tramos: 18 C/H de 0,181 m.',
    ], w_col=250, size=2.1, dy=3.6)
    notas(s, 640, 690, 'NOTAS', [
        'Documento gráfico de conjunto; el desarrollo está en A-01 a A-06 y S-01.',
        'Medidas en metros; cotas de nivel referidas al N.P.T. ±0,00.',
    ], w_col=250, size=1.95, dy=3.4)
    cuadro_areas(s, 990, 560, nivel=None,
                 w_cols=[13, 12, 34, 14, 13, 12, 34, 14], h_fila=4.0, size=1.55)
    escala_grafica(s, 700, 540, 100, n=5, seg_m=1.0)
    escala_grafica(s, 920, 540, 500, n=2, seg_m=10.0)
    norte(s, 1130, 420, r=15)
    # ---------------- situación: rótulo del bloque ----------------
    s.line((786, 176), (742, 210), 'marco-medio')
    s.text((788, 174), 'BLOQUE DORMITORIOS (D) — 24,00 × 9,60 m', h=2.4)
    cajetin_lamina(s, dict(codigo='BLU-00',
                           contenido='Blueprint de conjunto — plantas (baja y alta), '
                           'cortes A-A / B-B, fachadas sur / norte / este y situación',
                           escala='E 1:100 / 1:500', num='BLU-00', hoja='1 de 1'))
    return s


# ===========================================================================
# VERIFICACIÓN DE ENCUADRE
# ===========================================================================
def _pts(it):
    if it['k'] == 'line':
        return [it['a'], it['b']]
    if it['k'] in ('poly', 'fill'):
        return it['pts']
    if it['k'] == 'circle':
        r = it['r']
        return [(it['c'][0] - r, it['c'][1] - r), (it['c'][0] + r, it['c'][1] + r)]
    if it['k'] == 'text':
        ancho = len(str(it['s'])) * it['h'] * 0.72
        x, y = it['p']
        if abs(it.get('rot', 0)) > 45:
            return [(x - it['h'], y - ancho), (x + it['h'], y + ancho)]
        if it['anchor'] == 'middle':
            x -= ancho / 2.0
        elif it['anchor'] == 'end':
            x -= ancho
        return [(x, y - it['h']), (x + ancho, y + it['h'] * 0.3)]
    return []


def verificar(sheet, nombre=''):
    """Informa de elementos fuera del marco o dentro del cajetín."""
    global MX1, MY1
    MX1, MY1 = sheet.w - 12.0, sheet.h - 12.0
    caj = (sheet.w - 12.0 - 190.0, sheet.h - 12.0 - 62.0, sheet.w - 12.0, sheet.h - 12.0)
    fuera, en_caj = 0, 0
    for it in sheet.items:
        p = _pts(it)
        if not p:
            continue
        x0 = min(q[0] for q in p)
        x1 = max(q[0] for q in p)
        y0 = min(q[1] for q in p)
        y1 = max(q[1] for q in p)
        dentro_caj = (x0 > caj[0] - 2 and x1 < caj[2] + 2 and y0 > caj[1] - 2
                      and y1 < caj[3] + 2)
        if (x1 < MX0 - 1 or x0 > MX1 + 1 or y1 < MY0 - 1 or y0 > MY1 + 1
                or x0 < MX0 - 0.5 or x1 > MX1 + 0.5 or y0 < MY0 - 0.5
                or y1 > MY1 + 0.5):
            fuera += 1
            print('   ! %s FUERA DEL MARCO: %s %r' % (nombre, it['k'],
                                                      (round(x0), round(y0))))
        elif dentro_caj and it['layer'] not in ('marco', 'marco-fino', 'marco-medio',
                                                'sombra', 'texto', 'texto-suave'):
            en_caj += 1
    print('   encuadre %-8s fuera=%d  sobre-cajetín=%d' % (nombre, fuera, en_caj))
    return fuera, en_caj


# ===========================================================================
# MAIN
# ===========================================================================
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--dpi', type=int, default=150)
    ap.add_argument('--out', default=os.path.join(os.path.dirname(os.path.dirname(
        os.path.abspath(__file__))), 'entrega'))
    ap.add_argument('--solo', default=None)
    args = ap.parse_args()

    laminas = [
        ('BLU-00_blueprint_completo_A0', lamina_blueprint_completo, None),
        ('A-01_planta_baja', lamina_planta, 0),
        ('A-02_planta_alta', lamina_planta, 1),
        ('A-03_cortes_detalles', lamina_cortes, None),
        ('A-04_fachadas', lamina_fachadas, None),
        ('A-05_azotea_situacion', lamina_azotea_situacion, None),
        ('A-06_cortes_fachadas_situacion', lamina_cortes_fachadas, None),
        ('BLU-01_blueprint', lamina_blueprint, None),
        ('S-01_situacion_bloque', lamina_situacion, None),
        ('BLU-02_blueprint_cortes_fachadas', lamina_blueprint_cortes, None),
    ]
    for base, fn, arg in laminas:
        if args.solo and args.solo not in base:
            continue
        s = fn(arg) if arg is not None else fn()
        verificar(s, base.split('_')[0])
        es_blueprint = base.startswith('BLU')
        r = emitir(s, args.out, base, dpi=args.dpi, jpg=es_blueprint,
                   jpg_dpi=max(args.dpi, 150))
        print('%-34s PDF %5.0f KB  SVG %5.0f KB  PNG %5.0f KB  DXF %5s  JPG %s'
              % (base, os.path.getsize(r['pdf']) / 1024.0,
                 os.path.getsize(r['svg']) / 1024.0,
                 os.path.getsize(r['png']) / 1024.0,
                 ('%5.0f KB' % (os.path.getsize(r['dxf']) / 1024.0)) if r['dxf'] else '—',
                 ('%5.0f KB' % (os.path.getsize(r['jpg']) / 1024.0)) if r['jpg'] else '—'))


if __name__ == '__main__':
    main()

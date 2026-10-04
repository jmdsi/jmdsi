# -*- coding: utf-8 -*-
"""
bloque.py — Definición geométrica y utilidades de dibujo del
BLOQUE DORMITORIOS (2 niveles: planta baja y planta alta).

Sistema: albañilería confinada / aporticado, losa maciza aligerada.
Unidades: metros. Cotas de nivel referidas a ±0,00 = NPT planta baja.
"""
from core import *

# ============================================================================
# PARÁMETROS GENERALES
# ============================================================================
L_BLOQUE = 24.00          # largo exterior (eje A - eje H aprox. 23,75)
D_BLOQUE = 9.60           # ancho exterior
E_MURO = 0.25             # muro perimetral (albañilería confinada)
E_TAB = 0.15              # tabique interior
H_LIBRE_PB = 2.90         # altura libre planta baja (piso terminado a cielo)
NPT_PA = 3.25             # nivel de piso terminado planta alta  (+3,25)
H_LIBRE_PA = 2.60         # altura libre planta alta
E_LOSA = 0.30             # losa aligerada
NPT_CUB = 6.20            # nivel de piso terminado de azotea (cara superior losa)
H_PARAPETO = 0.95
H_TOTAL = 7.15            # altura total sobre ±0,00 (nivel de albardilla)
NIVEL_TERRENO = -0.45     # terreno natural (exterior)

# Cimentación
ZAP_W, ZAP_H = 0.70, 0.25          # zapata/cimiento corrido
ZAP_Z0, ZAP_Z1 = -1.05, -0.80      # cota inferior/superior del cimiento corrido
SOBR_Z0, SOBR_Z1 = -0.80, -0.20    # sobrecimiento
SOL_Z0, SOL_Z1 = -0.20, 0.00       # solera de piso (planta baja)

# Ejes estructurales (coordenadas de eje = eje de muro/tabique)
EJE_X = [('A', 0.125), ('B', 3.525), ('C', 6.875), ('D', 10.225),
         ('E', 13.575), ('F', 16.575), ('G', 20.125), ('H', 23.875)]
EJE_Y = [('1', 0.125), ('2', 3.875), ('3', 5.725), ('4', 9.475)]

# Retícula de ejes: cada eje con el espesor del muro que representa
EJE_ESP_X = {'A': E_MURO, 'B': E_TAB, 'C': E_TAB, 'D': E_TAB, 'E': E_TAB,
             'F': E_TAB, 'G': E_TAB, 'H': E_MURO}
EJE_ESP_Y = {'1': E_MURO, '2': E_TAB, '3': E_TAB, '4': E_MURO}

# Divisiones interiores (caras de muro) — lista de tramos de muro interior en X
TABIQUE_X = [(3.450, 3.600), (6.800, 6.950), (10.150, 10.300), (13.500, 13.650),
             (16.500, 16.650), (20.050, 20.200)]

# Recintos: nombre, x0, y0, x1, y1, código, tipo
def recintos(nivel):
    """nivel: 0 = planta baja, 1 = planta alta"""
    R = []
    # -------- dormitorios hilera sur (y 0,25 - 3,80) --------
    cod_hilera = ('D-1', 'D-2')[nivel]
    for i, (x0, x1) in enumerate([(0.25, 3.45), (3.60, 6.80), (6.95, 10.15),
                                  (10.30, 13.50)]):
        R.append(dict(cod=cod_hilera + '%02d' % (1 + i), nom='Dormitorio doble',
                      x0=x0, y0=0.25, x1=x1, y1=3.80, tipo='dorm', hilera='S',
                      puerta=(0.90, 3.80, 'N')))
    # -------- dormitorios hilera norte (y 5,80 - 9,35) --------
    for i, (x0, x1) in enumerate([(0.25, 3.45), (3.60, 6.80), (6.95, 10.15),
                                  (10.30, 13.50)]):
        R.append(dict(cod=cod_hilera + '%02d' % (5 + i), nom='Dormitorio doble',
                      x0=x0, y0=5.80, x1=x1, y1=9.35, tipo='dorm', hilera='N',
                      puerta=(0.90, 5.80, 'S')))
    # -------- servicios higiénicos --------
    R.append(dict(cod='SS-1' if nivel == 0 else 'SS-2', nom='SS.HH. damas',
                  x0=13.65, y0=0.25, x1=16.50, y1=3.80, tipo='ssh', hilera='S',
                  puerta=(0.80, 3.80, 'N')))
    R.append(dict(cod='SS-3' if nivel == 0 else 'SS-4', nom='SS.HH. varones',
                  x0=13.65, y0=5.80, x1=16.50, y1=9.35, tipo='ssh', hilera='N',
                  puerta=(0.80, 5.80, 'S')))
    # -------- núcleo de escalera / acceso --------
    R.append(dict(cod='E-01', nom='Escalera', x0=16.65, y0=3.95, x1=20.05,
                  y1=9.35, tipo='esc', hilera=None, puerta=None))
    if nivel == 0:
        R.append(dict(cod='V-01', nom='Vestíbulo / Recepción', x0=16.65, y0=0.25,
                      x1=20.05, y1=3.95, tipo='vest', hilera=None, puerta=None))
        R.append(dict(cod='DP-01', nom='Depósito / Cuarto técnico', x0=20.20,
                      y0=0.25, x1=23.75, y1=3.80, tipo='serv', hilera=None,
                      puerta=(0.90, 3.80, 'N')))
        R.append(dict(cod='LV-01', nom='Lavandería', x0=20.20, y0=5.80,
                      x1=23.75, y1=9.35, tipo='lav', hilera=None,
                      puerta=(0.90, 5.80, 'S')))
        R.append(dict(cod='P-01', nom='Pasillo / Distribuidor', x0=0.25, y0=3.95,
                      x1=16.65, y1=5.65, tipo='pas', hilera=None, puerta=None))
        R.append(dict(cod='DI-01', nom='Distribuidor', x0=20.20, y0=3.95,
                      x1=23.75, y1=5.65, tipo='pas', hilera=None, puerta=None))
    else:
        R.append(dict(cod='ES-01', nom='Sala de estar y estudio', x0=16.65,
                      y0=0.25, x1=20.05, y1=3.95, tipo='estar', hilera=None,
                      puerta=None))
        R.append(dict(cod='ES-02', nom='Sala de estudio complementaria',
                      x0=20.20, y0=5.80, x1=23.75, y1=9.35, tipo='estar',
                      hilera=None, puerta=(1.20, 5.80, 'S')))
        R.append(dict(cod='DP-02', nom='Depósito / Ropería', x0=20.20, y0=0.25,
                      x1=23.75, y1=3.80, tipo='serv', hilera=None,
                      puerta=(0.90, 3.80, 'N')))
        R.append(dict(cod='P-02', nom='Pasillo / Distribuidor', x0=0.25, y0=3.95,
                      x1=16.65, y1=5.65, tipo='pas', hilera=None, puerta=None))
        R.append(dict(cod='DI-02', nom='Distribuidor', x0=20.20, y0=3.95,
                      x1=23.75, y1=5.65, tipo='pas', hilera=None, puerta=None))
    return R


# Ventanas: (código, muro, x_centro_o_y_centro, ancho, alto, alféizar)
#   muro: 'N','S','E','O','INT'
def ventanas(nivel):
    z = 0.0 if nivel == 0 else NPT_PA
    V = []
    centros = [1.85, 5.20, 8.55, 11.90]
    for i, cx in enumerate(centros):
        V.append(dict(cod='V-1%02d' % (1 + i + 4 * nivel), muro='N', pos=cx,
                      w=1.50, h=1.50, sill=z + 0.90, tipo='dorm'))
        V.append(dict(cod='V-2%02d' % (1 + i + 4 * nivel), muro='S', pos=cx,
                      w=1.50, h=1.50, sill=z + 0.90, tipo='dorm'))
    # SS.HH. — ventana alta
    V.append(dict(cod='V-3%01d' % (1 + nivel), muro='N', pos=14.65, w=0.50, h=0.80,
                  sill=z + 1.70, tipo='ssh'))
    V.append(dict(cod='V-3%01d' % (3 + nivel), muro='S', pos=14.65, w=0.50, h=0.80,
                  sill=z + 1.70, tipo='ssh'))
    # Escalera — ventanas en fachada norte (sobre el descanso intermedio)
    V.append(dict(cod='V-41' if nivel == 0 else 'V-42', muro='N', pos=18.35,
                  w=1.20, h=0.95 if nivel == 0 else 0.85,
                  sill=1.90 if nivel == 0 else 5.00, tipo='esc'))
    if nivel == 0:
        # Depósito y lavandería — fachada este
        V.append(dict(cod='V-43', muro='E', pos=2.00, w=0.90, h=1.00, sill=1.50,
                      tipo='serv'))
        V.append(dict(cod='V-44', muro='E', pos=7.55, w=1.50, h=1.20, sill=1.00,
                      tipo='lav'))
        # Fachada oeste
        V.append(dict(cod='V-45', muro='O', pos=2.00, w=1.20, h=1.40, sill=0.90,
                      tipo='dorm'))
        V.append(dict(cod='V-46', muro='O', pos=7.55, w=1.20, h=1.40, sill=0.90,
                      tipo='dorm'))
    else:
        V.append(dict(cod='V-47', muro='E', pos=7.10, w=2.00, h=1.70, sill=z + 0.75,
                      tipo='estar'))
        V.append(dict(cod='V-48', muro='E', pos=2.00, w=0.90, h=1.00, sill=z + 1.50,
                      tipo='serv'))
        V.append(dict(cod='V-49', muro='O', pos=2.00, w=1.20, h=1.40, sill=z + 0.90,
                      tipo='dorm'))
        V.append(dict(cod='V-50', muro='O', pos=7.55, w=1.20, h=1.40, sill=z + 0.90,
                      tipo='dorm'))
    return V


PUERTA_PRINCIPAL = dict(cod='P-01', muro='S', pos=18.35, w=1.80, h=2.40)
VENTANA_ESTAR_PA = dict(cod='V-46', muro='E', pos=6.60, w=2.40, h=1.70, sill=4.00)

# Escalera: 18 contrahuellas de 0,181 m; 2 tramos de 9 C/H
ESC = dict(x0=16.65, x1=20.05,          # ancho total del núcleo
           ancho_tramo=1.60, gap=0.20,
           y_ini=5.65,                  # primer peldaño (borde norte del pasillo)
           tread=0.28, riser=0.181,
           n_risers=9,                  # por tramo
           y_fin=7.89,                  # fin tramo 1 = inicio descanso
           y_desc1=7.89, y_desc2=9.35)  # descanso intermedio


# ============================================================================
# UTILIDADES DE DIBUJO
# ============================================================================
def muro(v, x0, y0, x1, y1, espesor, layer_fill='muro-fill',
         layer_line='muro-corte'):
    """Dibuja un muro (polígono relleno) entre dos puntos de eje."""
    import math
    dx, dy = x1 - x0, y1 - y0
    L = math.hypot(dx, dy)
    if L < 1e-9:
        return
    nx, ny = -dy / L * espesor / 2.0, dx / L * espesor / 2.0
    p = [(x0 + nx, y0 + ny), (x1 + nx, y1 + ny), (x1 - nx, y1 - ny),
         (x0 - nx, y0 - ny)]
    v.fill(p, layer=layer_fill)
    v.polyline(p, layer=layer_line, close=True)


def muro_rect(v, x0, y0, x1, y1, layer='muro-fill'):
    v.fill([(x0, y0), (x1, y0), (x1, y1), (x0, y1)], layer=layer)
    v.polyline([(x0, y0), (x1, y0), (x1, y1), (x0, y1)], layer='muro-corte',
               close=True)


def tabique_rect(v, x0, y0, x1, y1):
    v.fill([(x0, y0), (x1, y0), (x1, y1), (x0, y1)], layer='tabique-fill')
    v.polyline([(x0, y0), (x1, y0), (x1, y1), (x0, y1)], layer='muro-corte',
               close=True)


def puerta(v, p0, p1, giro='izq'):
    """Hoja de puerta con arco de barrido. p0 = bisagra, p1 = extremo libre."""
    import math
    v.line(p0, p1, layer='carpinteria')
    ang = math.degrees(math.atan2(p1[1] - p0[1], p1[0] - p0[0]))
    r = math.hypot(p1[0] - p0[0], p1[1] - p0[1])
    v.arc(p0, r, ang, ang + (90 if giro == 'izq' else -90), layer='carpinteria', n=14)
    v.line(p0, (p0[0] + (p1[0] - p0[0]) * 0, p0[1]), layer='carpinteria')


def puerta_en_muro(v, ex, ey, esp, w, hacia=1, bat='izq', muro_dir='y'):
    """Puerta en un muro. muro_dir: 'y' (muro horizontal, eje en Y=ey) o 'x'.
    (ex,ey) = centro de la hoja sobre el eje del muro. hacia: sentido de apertura."""
    h = esp / 2.0
    if muro_dir == 'y':
        v.polyline([(ex - w / 2, ey - h), (ex - w / 2, ey + h)], layer='muro-corte')
        v.polyline([(ex + w / 2, ey - h), (ex + w / 2, ey + h)], layer='muro-corte')
        puerta(v, (ex - w / 2, ey), (ex - w / 2, ey + hacia * w),
               'izq' if bat == 'izq' else 'der')
    else:
        v.polyline([(ex - h, ey - w / 2), (ex + h, ey - w / 2)], layer='muro-corte')
        v.polyline([(ex - h, ey + w / 2), (ex + h, ey + w / 2)], layer='muro-corte')
        puerta(v, (ex, ey - w / 2), (ex + hacia * w, ey - w / 2),
               'izq' if bat == 'izq' else 'der')


def ventana_planta(v, ex, ey, esp, w, muro_dir='y'):
    """Ventana en planta: 4 líneas de carpintería."""
    h = esp / 2.0
    if muro_dir == 'y':
        v.line((ex - w / 2, ey - h), (ex + w / 2, ey - h), layer='carpinteria')
        v.line((ex - w / 2, ey + h), (ex + w / 2, ey + h), layer='carpinteria')
        v.line((ex - w / 2, ey), (ex + w / 2, ey), layer='vidrio')
        v.line((ex - w / 2, ey - h), (ex - w / 2, ey + h), layer='carpinteria')
        v.line((ex + w / 2, ey - h), (ex + w / 2, ey + h), layer='carpinteria')
    else:
        v.line((ex - h, ey - w / 2), (ex - h, ey + w / 2), layer='carpinteria')
        v.line((ex + h, ey - w / 2), (ex + h, ey + w / 2), layer='carpinteria')
        v.line((ex, ey - w / 2), (ex, ey + w / 2), layer='vidrio')
        v.line((ex - h, ey - w / 2), (ex + h, ey - w / 2), layer='carpinteria')
        v.line((ex - h, ey + w / 2), (ex + h, ey + w / 2), layer='carpinteria')


def mobiliario(v, x0, y0, w, hh, cod='', etiquetar=False, h_txt=1.5):
    """Rectángulo de mobiliario; etiqueta opcional centrada."""
    v.polyline([(x0, y0), (x0 + w, y0), (x0 + w, y0 + hh), (x0, y0 + hh)],
               layer='mobiliario', close=True)
    if etiquetar and cod:
        v.text((x0 + w / 2, y0 + hh / 2), cod, h=h_txt, layer='texto-suave',
               anchor='middle')


# ---- cuadro de mobiliario de dormitorio ------------------------------------
def dormitorio_amoblado(v, x0, y0, x1, y1, lado_ventana='N', etiquetas=False):
    """Dormitorio tipo de 3,20 × 3,55 m:
       2 camas de 1,00 × 2,00 · 2 escritorios de 1,20 × 0,60
       ropero de 0,60 × 1,80 · 2 veladores.
    lado_ventana = muro donde está la ventana ('N' o 'S')."""
    w, hh = x1 - x0, y1 - y0

    def Y(val):
        """Distancia medida desde el muro de la ventana hacia el interior (m)."""
        return (y1 - val) if lado_ventana == 'N' else (y0 + val)

    # --- 2 camas contra el tabique oeste, cabecera al muro de la ventana ---
    for k, d in enumerate((0.10, 1.20)):
        yy0 = min(Y(d), Y(d + 1.00))
        mobiliario(v, x0 + 0.05, yy0, 2.00, 1.00, 'CAMA 1,00 × 2,00', etiquetas)
        # almohada (cabecera junto al muro de la ventana)
        mobiliario(v, x0 + 0.05, min(Y(d + 0.55), Y(d + 0.05)), 0.45, 0.50)
    # --- veladores entre las camas ---
    mobiliario(v, x0 + 2.12, min(Y(1.08), Y(1.38)), 0.40, 0.30)
    # --- 2 escritorios contra el tabique este ---
    for k, d in enumerate((0.15, 0.90)):
        yy0 = min(Y(hh - d), Y(hh - d - 0.60))
        mobiliario(v, x1 - 1.25, yy0, 1.20, 0.60, 'ESCRITORIO 1,20 × 0,60',
                   etiquetas)
    # --- ropero contra el tabique este, junto a la puerta ---
    yy0 = min(Y(1.70), Y(3.50))
    if lado_ventana == 'S':
        yy0 = min(Y(1.70), Y(3.50))
    mobiliario(v, x1 - 0.65, yy0, 0.60, 1.80, 'ROPERO 0,60 × 1,80', etiquetas)


def sshh_amoblado(v, x0, y0, x1, y1, lado_ventana='N', etiquetas=False):
    """SS.HH. común de 3,00 × 3,55 m: 3 inodoros, 3 lavabos, 2 duchas y 1 urinario.
    lado_ventana = muro de la ventana ('N' o 'S')."""
    win_n = (lado_ventana == 'N')

    def Y(val):
        return (y1 - val) if win_n else (y0 + val)

    # --- 3 lavabos contra el tabique oeste ---
    for k, d in enumerate((0.20, 0.80, 1.40)):
        yy0 = min(Y(d), Y(d + 0.50))
        mobiliario(v, x0 + 0.10, yy0, 0.60, 0.50, 'LAV.', etiquetas)
    # --- 3 inodoros contra el tabique este (mirando al oeste) ---
    for k, d in enumerate((0.20, 0.80, 1.40)):
        yy0 = min(Y(d), Y(d + 0.70))
        v.polyline([(x1 - 0.20, yy0 + 0.10), (x1 - 0.15, yy0 + 0.10),
                    (x1 - 0.15, yy0 + 0.60), (x1 - 0.20, yy0 + 0.60)],
                   layer='sanitario', close=True)
        v.circle((x1 - 0.40, yy0 + 0.35), 0.19, layer='sanitario')
        v.polyline([(x1 - 0.60, yy0 + 0.16), (x1 - 0.22, yy0 + 0.16),
                    (x1 - 0.22, yy0 + 0.54), (x1 - 0.60, yy0 + 0.54)],
                   layer='sanitario', close=True)
    # --- urinario en el rincón ---
    mobiliario(v, x1 - 0.55, min(Y(2.25), Y(2.90)), 0.40, 0.35, 'UR.', etiquetas)
    v.line((x1 - 0.55, Y(2.25)), (x1 - 0.35, Y(2.90)), layer='sanitario')
    # --- 2 duchas junto a la ventana ---
    for k, xd in enumerate([x0 + 0.25, x0 + 1.35]):
        yy0 = min(Y(0.10), Y(1.05))
        v.polyline([(xd, yy0), (xd + 0.95, yy0), (xd + 0.95, yy0 + 0.95),
                    (xd, yy0 + 0.95)], layer='sanitario', close=True)
        v.line((xd, yy0), (xd + 0.95, yy0 + 0.95), layer='sanitario')
        v.circle((xd + 0.12, yy0 + 0.12), 0.05, layer='sanitario')
        v.circle((xd + 0.48, yy0 + 0.90), 0.06, layer='sanitario')
    # --- ducto de instalaciones en el rincón ---
    v.polyline([(x1 - 0.35, Y(3.55)), (x1, Y(3.55)), (x1, Y(3.20))],
               layer='hatch')


# ============================================================================
# ESCALERA
# ============================================================================
def escalera_planta(v, nivel, etiquetar=True):
    """Escalera de 2 tramos y descanso intermedio: 18 contrahuellas de 0,181 m
    (9 por tramo) y huella de 0,28 m entre PB (±0,00) y PA (+3,25).
    nivel = 0 (planta baja) / 1 (planta alta)."""
    e = ESC
    xT1a, xT1b = e['x0'], e['x0'] + e['ancho_tramo']        # tramo oeste
    xT2a, xT2b = e['x1'] - e['ancho_tramo'], e['x1']        # tramo este
    y0, y1 = e['y_ini'], e['y_fin']
    tread = e['tread']
    n = e['n_risers']                                        # 9 peldaños por tramo
    z_desc = 1.63 if nivel == 0 else NPT_PA + 1.63

    # --- descanso intermedio (norte) ---
    v.polyline([(e['x0'], y1), (e['x1'], y1), (e['x1'], e['y_desc2']),
                (e['x0'], e['y_desc2'])], layer='marco-fino', close=True)
    if etiquetar:
        v.text(((e['x0'] + e['x1']) / 2, (y1 + e['y_desc2']) / 2 - 0.05),
               'DESCANSO ' + nivel_txt(z_desc), h=1.9, layer='texto-suave',
               anchor='middle')

    # --- peldaños ---
    for k in range(n + 1):
        y = y0 + k * tread
        v.line((xT1a, y), (xT1b, y), layer='marco-fino')
        v.line((xT2a, y), (xT2b, y), layer='marco-fino')
    for (xx0, xx1) in [(xT1a, xT1b), (xT2a, xT2b)]:
        v.line((xx0, y0), (xx0, y1), layer='marco-fino')
        v.line((xx1, y0), (xx1, y1), layer='marco-fino')
    # --- viga central / ojo de escalera ---
    v.line(((xT1b + xT2a) / 2, y0), ((xT1b + xT2a) / 2, y1), layer='marco-fino')

    # --- línea de quiebre sobre el tramo que sube ---
    yq = y0 + 0.62 * (y1 - y0)
    v.polyline([(xT1a, yq - 0.32), (xT1b, yq), (xT1a, yq + 0.32)],
               layer='marco-medio')
    # --- flechas de circulación ---
    def flecha(xa, ya, yb, txt):
        v.line((xa, ya), (xa, yb), layer='carpinteria')
        v.circle((xa, ya), 0.10, layer='carpinteria', fill=True)
        s = 0.16 * (1 if yb > ya else -1)
        v.polyline([(xa, yb), (xa - 0.16, yb - s), (xa + 0.16, yb - s)],
                   close=True, layer='carpinteria')
        v.fill([(xa, yb), (xa - 0.16, yb - s), (xa + 0.16, yb - s)],
               layer='carpinteria')
        if etiquetar:
            v.text((xa, yb + (0.55 if yb > ya else -0.55)), txt, h=2.0,
                   layer='texto', anchor='middle')

    xa, xb = (xT1a + xT1b) / 2, (xT2a + xT2b) / 2
    if nivel == 0:
        flecha(xa, y0 + 0.25, y1 - 0.30, 'SUBE N.P.T. +3,25')
        flecha(xb, y1 - 0.25, y0 + 0.35, 'BAJA A DESCANSO +1,63')
    else:
        flecha(xb, y1 - 0.25, y0 + 0.35, 'BAJA N.P.T. ±0,00 (18 C/H)')
        flecha(xa, y0 + 0.25, y0 + 1.10, 'SUBEN 9 C/H HASTA +1,63')
    # --- losa inclinada (huella) bajo el tramo oeste en planta alta: hueco ---
    if nivel == 1:
        v.polyline([(xT1a, y0), (xT1b, y0), (xT1b, y1), (xT1a, y1)],
                   layer='proyeccion', close=True)


# ============================================================================
# EJES Y GLOBOS
# ============================================================================
def ejes_planta(v, globos=True, r_globo=4.2, margen=0.85):
    """Dibuja la retícula de ejes con globos numerados."""
    y0, y1 = 0.0, D_BLOQUE
    x0, x1 = 0.0, L_BLOQUE
    for nom, x in EJE_X:
        v.line((x, -margen), (x, D_BLOQUE + margen), layer='eje')
        if globos:
            globo_eje(v.sheet, (v.X(x), v.Y(D_BLOQUE + margen) - 6.0), nom, r=r_globo)
            globo_eje(v.sheet, (v.X(x), v.Y(-margen) + 6.0), nom, r=r_globo)
    for nom, y in EJE_Y:
        v.line((-margen, y), (L_BLOQUE + margen, y), layer='eje')
        if globos:
            globo_eje(v.sheet, (v.X(-margen) - 7.0, v.Y(y)), nom, r=r_globo)
            globo_eje(v.sheet, (v.X(L_BLOQUE + margen) + 7.0, v.Y(y)), nom, r=r_globo)


def cuadro_ejes(sheet, x, y):
    filas = [['Eje', 'X (m)', 'Entre ejes', 'Eje', 'Y (m)', 'Entre ejes']]
    prev_x = None
    prev_y = None
    for i in range(max(len(EJE_X), len(EJE_Y))):
        fx = ['', '', '']
        fy = ['', '', '']
        if i < len(EJE_X):
            nom, val = EJE_X[i]
            fx = [nom, fmt(val, 2), '—' if prev_x is None else fmt(val - prev_x, 2)]
            prev_x = val
        if i < len(EJE_Y):
            nom, val = EJE_Y[i]
            fy = [nom, fmt(val, 2), '—' if prev_y is None else fmt(val - prev_y, 2)]
            prev_y = val
        filas.append(fx + fy)
    return cuadro(sheet, x, y, filas, [12, 20, 26, 12, 20, 26], h_fila=4.6, h_cab=5.2,
                  size=1.9)


def cuadro_areas(sheet, x, y, nivel=None, w_cols=None, h_fila=4.5, size=1.85):
    """Cuadro de áreas por recinto.  nivel=None -> ambos niveles (8 columnas)."""
    niveles = [0, 1] if nivel is None else [nivel]
    datos = [recintos(n) for n in niveles]
    cab = []
    for n in niveles:
        cab += ['Nivel', 'Cód.', 'Recinto', 'Área (m²)']
    filas = [cab]
    maxlen = max(len(d) for d in datos)
    for i in range(maxlen):
        fila = []
        for k, d in enumerate(datos):
            if i < len(d):
                r = d[i]
                a = (r['x1'] - r['x0']) * (r['y1'] - r['y0'])
                fila += ['P. ' + ('BAJA' if niveles[k] == 0 else 'ALTA'), r['cod'],
                         r['nom'], fmt(a, 2)]
            else:
                fila += ['', '', '', '']
        filas.append(fila)
    defecto = [16, 14, 44, 16, 16, 14, 44, 16]
    w = w_cols if w_cols else defecto[:4 * len(niveles)]
    return cuadro(sheet, x, y, filas, w, h_fila=h_fila, h_cab=5.2, size=size)
# ============================================================================
# UTILIDADES DE DIBUJO
# ============================================================================
def muro(v, x0, y0, x1, y1, espesor, layer_fill='muro-fill',
         layer_line='muro-corte'):
    """Dibuja un muro (polígono relleno) entre dos puntos de eje."""
    import math
    dx, dy = x1 - x0, y1 - y0
    L = math.hypot(dx, dy)
    if L < 1e-9:
        return
    nx, ny = -dy / L * espesor / 2.0, dx / L * espesor / 2.0
    p = [(x0 + nx, y0 + ny), (x1 + nx, y1 + ny), (x1 - nx, y1 - ny),
         (x0 - nx, y0 - ny)]
    v.fill(p, layer=layer_fill)
    v.polyline(p, layer=layer_line, close=True)


def muro_rect(v, x0, y0, x1, y1, layer='muro-fill'):
    v.fill([(x0, y0), (x1, y0), (x1, y1), (x0, y1)], layer=layer)
    v.polyline([(x0, y0), (x1, y0), (x1, y1), (x0, y1)], layer='muro-corte',
               close=True)


def tabique_rect(v, x0, y0, x1, y1):
    v.fill([(x0, y0), (x1, y0), (x1, y1), (x0, y1)], layer='tabique-fill')
    v.polyline([(x0, y0), (x1, y0), (x1, y1), (x0, y1)], layer='muro-corte',
               close=True)


def puerta(v, p0, p1, giro='izq'):
    """Hoja de puerta con arco de barrido. p0 = bisagra, p1 = extremo libre."""
    import math
    v.line(p0, p1, layer='carpinteria')
    ang = math.degrees(math.atan2(p1[1] - p0[1], p1[0] - p0[0]))
    r = math.hypot(p1[0] - p0[0], p1[1] - p0[1])
    v.arc(p0, r, ang, ang + (90 if giro == 'izq' else -90), layer='carpinteria', n=14)
    v.line(p0, (p0[0] + (p1[0] - p0[0]) * 0, p0[1]), layer='carpinteria')


def puerta_en_muro(v, ex, ey, esp, w, hacia=1, bat='izq', muro_dir='y'):
    """Puerta en un muro. muro_dir: 'y' (muro horizontal, eje en Y=ey) o 'x'.
    (ex,ey) = centro de la hoja sobre el eje del muro. hacia: sentido de apertura."""
    h = esp / 2.0
    if muro_dir == 'y':
        v.polyline([(ex - w / 2, ey - h), (ex - w / 2, ey + h)], layer='muro-corte')
        v.polyline([(ex + w / 2, ey - h), (ex + w / 2, ey + h)], layer='muro-corte')
        puerta(v, (ex - w / 2, ey), (ex - w / 2, ey + hacia * w),
               'izq' if bat == 'izq' else 'der')
    else:
        v.polyline([(ex - h, ey - w / 2), (ex + h, ey - w / 2)], layer='muro-corte')
        v.polyline([(ex - h, ey + w / 2), (ex + h, ey + w / 2)], layer='muro-corte')
        puerta(v, (ex, ey - w / 2), (ex + hacia * w, ey - w / 2),
               'izq' if bat == 'izq' else 'der')


def ventana_planta(v, ex, ey, esp, w, muro_dir='y'):
    """Ventana en planta: 4 líneas de carpintería."""
    h = esp / 2.0
    if muro_dir == 'y':
        v.line((ex - w / 2, ey - h), (ex + w / 2, ey - h), layer='carpinteria')
        v.line((ex - w / 2, ey + h), (ex + w / 2, ey + h), layer='carpinteria')
        v.line((ex - w / 2, ey), (ex + w / 2, ey), layer='vidrio')
        v.line((ex - w / 2, ey - h), (ex - w / 2, ey + h), layer='carpinteria')
        v.line((ex + w / 2, ey - h), (ex + w / 2, ey + h), layer='carpinteria')
    else:
        v.line((ex - h, ey - w / 2), (ex - h, ey + w / 2), layer='carpinteria')
        v.line((ex + h, ey - w / 2), (ex + h, ey + w / 2), layer='carpinteria')
        v.line((ex, ey - w / 2), (ex, ey + w / 2), layer='vidrio')
        v.line((ex - h, ey - w / 2), (ex + h, ey - w / 2), layer='carpinteria')
        v.line((ex - h, ey + w / 2), (ex + h, ey + w / 2), layer='carpinteria')


def mobiliario(v, x0, y0, w, hh, cod='', etiquetar=False, h_txt=1.5):
    """Rectángulo de mobiliario; etiqueta opcional centrada."""
    v.polyline([(x0, y0), (x0 + w, y0), (x0 + w, y0 + hh), (x0, y0 + hh)],
               layer='mobiliario', close=True)
    if etiquetar and cod:
        v.text((x0 + w / 2, y0 + hh / 2), cod, h=h_txt, layer='texto-suave',
               anchor='middle')


# ---- cuadro de mobiliario de dormitorio ------------------------------------
def dormitorio_amoblado(v, x0, y0, x1, y1, lado_ventana='N', etiquetas=False):
    """Dormitorio tipo de 3,20 × 3,55 m:
       2 camas de 1,00 × 2,00 · 2 escritorios de 1,20 × 0,60
       ropero de 0,60 × 1,80 · 2 veladores.
    lado_ventana = muro donde está la ventana ('N' o 'S')."""
    w, hh = x1 - x0, y1 - y0

    def Y(val):
        """Distancia medida desde el muro de la ventana hacia el interior (m)."""
        return (y1 - val) if lado_ventana == 'N' else (y0 + val)

    # --- 2 camas contra el tabique oeste, cabecera al muro de la ventana ---
    for k, d in enumerate((0.10, 1.20)):
        yy0 = min(Y(d), Y(d + 1.00))
        mobiliario(v, x0 + 0.05, yy0, 2.00, 1.00, 'CAMA 1,00 × 2,00', etiquetas)
        # almohada (cabecera junto al muro de la ventana)
        mobiliario(v, x0 + 0.05, min(Y(d + 0.55), Y(d + 0.05)), 0.45, 0.50)
    # --- veladores entre las camas ---
    mobiliario(v, x0 + 2.12, min(Y(1.08), Y(1.38)), 0.40, 0.30)
    # --- 2 escritorios contra el tabique este ---
    for k, d in enumerate((0.15, 0.90)):
        yy0 = min(Y(hh - d), Y(hh - d - 0.60))
        mobiliario(v, x1 - 1.25, yy0, 1.20, 0.60, 'ESCRITORIO 1,20 × 0,60',
                   etiquetas)
    # --- ropero contra el tabique este, junto a la puerta ---
    yy0 = min(Y(1.70), Y(3.50))
    if lado_ventana == 'S':
        yy0 = min(Y(1.70), Y(3.50))
    mobiliario(v, x1 - 0.65, yy0, 0.60, 1.80, 'ROPERO 0,60 × 1,80', etiquetas)


def sshh_amoblado(v, x0, y0, x1, y1, lado_ventana='N', etiquetas=False):
    """SS.HH. común de 3,00 × 3,55 m: 3 inodoros, 3 lavabos, 2 duchas y 1 urinario.
    lado_ventana = muro de la ventana ('N' o 'S')."""
    win_n = (lado_ventana == 'N')

    def Y(val):
        return (y1 - val) if win_n else (y0 + val)

    # --- 3 lavabos contra el tabique oeste ---
    for k, d in enumerate((0.20, 0.80, 1.40)):
        yy0 = min(Y(d), Y(d + 0.50))
        mobiliario(v, x0 + 0.10, yy0, 0.60, 0.50, 'LAV.', etiquetas)
    # --- 3 inodoros contra el tabique este (mirando al oeste) ---
    for k, d in enumerate((0.20, 0.80, 1.40)):
        yy0 = min(Y(d), Y(d + 0.70))
        v.polyline([(x1 - 0.20, yy0 + 0.10), (x1 - 0.15, yy0 + 0.10),
                    (x1 - 0.15, yy0 + 0.60), (x1 - 0.20, yy0 + 0.60)],
                   layer='sanitario', close=True)
        v.circle((x1 - 0.40, yy0 + 0.35), 0.19, layer='sanitario')
        v.polyline([(x1 - 0.60, yy0 + 0.16), (x1 - 0.22, yy0 + 0.16),
                    (x1 - 0.22, yy0 + 0.54), (x1 - 0.60, yy0 + 0.54)],
                   layer='sanitario', close=True)
    # --- urinario en el rincón ---
    mobiliario(v, x1 - 0.55, min(Y(2.25), Y(2.90)), 0.40, 0.35, 'UR.', etiquetas)
    v.line((x1 - 0.55, Y(2.25)), (x1 - 0.35, Y(2.90)), layer='sanitario')
    # --- 2 duchas junto a la ventana ---
    for k, xd in enumerate([x0 + 0.25, x0 + 1.35]):
        yy0 = min(Y(0.10), Y(1.05))
        v.polyline([(xd, yy0), (xd + 0.95, yy0), (xd + 0.95, yy0 + 0.95),
                    (xd, yy0 + 0.95)], layer='sanitario', close=True)
        v.line((xd, yy0), (xd + 0.95, yy0 + 0.95), layer='sanitario')
        v.circle((xd + 0.12, yy0 + 0.12), 0.05, layer='sanitario')
        v.circle((xd + 0.48, yy0 + 0.90), 0.06, layer='sanitario')
    # --- ducto de instalaciones en el rincón ---
    v.polyline([(x1 - 0.35, Y(3.55)), (x1, Y(3.55)), (x1, Y(3.20))],
               layer='hatch')


# ============================================================================
# ESCALERA
# ============================================================================
def escalera_planta(v, nivel, etiquetar=True):
    """Escalera de 2 tramos y descanso intermedio: 18 contrahuellas de 0,181 m
    (9 por tramo) y huella de 0,28 m entre PB (±0,00) y PA (+3,25).
    nivel = 0 (planta baja) / 1 (planta alta)."""
    e = ESC
    xT1a, xT1b = e['x0'], e['x0'] + e['ancho_tramo']        # tramo oeste
    xT2a, xT2b = e['x1'] - e['ancho_tramo'], e['x1']        # tramo este
    y0, y1 = e['y_ini'], e['y_fin']
    tread = e['tread']
    n = e['n_risers']                                        # 9 peldaños por tramo
    z_desc = 1.63 if nivel == 0 else NPT_PA + 1.63

    # --- descanso intermedio (norte) ---
    v.polyline([(e['x0'], y1), (e['x1'], y1), (e['x1'], e['y_desc2']),
                (e['x0'], e['y_desc2'])], layer='marco-fino', close=True)
    if etiquetar:
        v.text(((e['x0'] + e['x1']) / 2, (y1 + e['y_desc2']) / 2 - 0.05),
               'DESCANSO ' + nivel_txt(z_desc), h=1.9, layer='texto-suave',
               anchor='middle')

    # --- peldaños ---
    for k in range(n + 1):
        y = y0 + k * tread
        v.line((xT1a, y), (xT1b, y), layer='marco-fino')
        v.line((xT2a, y), (xT2b, y), layer='marco-fino')
    for (xx0, xx1) in [(xT1a, xT1b), (xT2a, xT2b)]:
        v.line((xx0, y0), (xx0, y1), layer='marco-fino')
        v.line((xx1, y0), (xx1, y1), layer='marco-fino')
    # --- viga central / ojo de escalera ---
    v.line(((xT1b + xT2a) / 2, y0), ((xT1b + xT2a) / 2, y1), layer='marco-fino')

    # --- línea de quiebre sobre el tramo que sube ---
    yq = y0 + 0.62 * (y1 - y0)
    v.polyline([(xT1a, yq - 0.32), (xT1b, yq), (xT1a, yq + 0.32)],
               layer='marco-medio')
    # --- flechas de circulación ---
    def flecha(xa, ya, yb, txt):
        v.line((xa, ya), (xa, yb), layer='carpinteria')
        v.circle((xa, ya), 0.10, layer='carpinteria', fill=True)
        s = 0.16 * (1 if yb > ya else -1)
        v.polyline([(xa, yb), (xa - 0.16, yb - s), (xa + 0.16, yb - s)],
                   close=True, layer='carpinteria')
        v.fill([(xa, yb), (xa - 0.16, yb - s), (xa + 0.16, yb - s)],
               layer='carpinteria')
        if etiquetar:
            v.text((xa, yb + (0.55 if yb > ya else -0.55)), txt, h=2.0,
                   layer='texto', anchor='middle')

    xa, xb = (xT1a + xT1b) / 2, (xT2a + xT2b) / 2
    if nivel == 0:
        flecha(xa, y0 + 0.25, y1 - 0.30, 'SUBE N.P.T. +3,25')
        flecha(xb, y1 - 0.25, y0 + 0.35, 'BAJA A DESCANSO +1,63')
    else:
        flecha(xb, y1 - 0.25, y0 + 0.35, 'BAJA N.P.T. ±0,00 (18 C/H)')
        flecha(xa, y0 + 0.25, y0 + 1.10, 'SUBEN 9 C/H HASTA +1,63')
    # --- losa inclinada (huella) bajo el tramo oeste en planta alta: hueco ---
    if nivel == 1:
        v.polyline([(xT1a, y0), (xT1b, y0), (xT1b, y1), (xT1a, y1)],
                   layer='proyeccion', close=True)


# ============================================================================
# EJES Y GLOBOS
# ============================================================================
def ejes_planta(v, globos=True, r_globo=4.2, margen=0.85):
    """Dibuja la retícula de ejes con globos numerados."""
    y0, y1 = 0.0, D_BLOQUE
    x0, x1 = 0.0, L_BLOQUE
    for nom, x in EJE_X:
        v.line((x, -margen), (x, D_BLOQUE + margen), layer='eje')
        if globos:
            globo_eje(v.sheet, (v.X(x), v.Y(D_BLOQUE + margen) - 6.0), nom, r=r_globo)
            globo_eje(v.sheet, (v.X(x), v.Y(-margen) + 6.0), nom, r=r_globo)
    for nom, y in EJE_Y:
        v.line((-margen, y), (L_BLOQUE + margen, y), layer='eje')
        if globos:
            globo_eje(v.sheet, (v.X(-margen) - 7.0, v.Y(y)), nom, r=r_globo)
            globo_eje(v.sheet, (v.X(L_BLOQUE + margen) + 7.0, v.Y(y)), nom, r=r_globo)


def cuadro_ejes(sheet, x, y):
    filas = [['Eje', 'X (m)', 'Entre ejes', 'Eje', 'Y (m)', 'Entre ejes']]
    prev_x = None
    prev_y = None
    for i in range(max(len(EJE_X), len(EJE_Y))):
        fx = ['', '', '']
        fy = ['', '', '']
        if i < len(EJE_X):
            nom, val = EJE_X[i]
            fx = [nom, fmt(val, 2), '—' if prev_x is None else fmt(val - prev_x, 2)]
            prev_x = val
        if i < len(EJE_Y):
            nom, val = EJE_Y[i]
            fy = [nom, fmt(val, 2), '—' if prev_y is None else fmt(val - prev_y, 2)]
            prev_y = val
        filas.append(fx + fy)
    return cuadro(sheet, x, y, filas, [12, 20, 26, 12, 20, 26], h_fila=4.6, h_cab=5.2,
                  size=1.9)

# -*- coding: utf-8 -*-
"""
vistas.py — Vistas del Bloque Dormitorios: plantas, cortes, fachadas,
planta de azotea y planta de situación.
"""
from core import *
from bloque import *

FONDO = 'fondo'


# ============================================================================
# AYUDAS
# ============================================================================
def hueco(v, x0, y0, x1, y1):
    """Borra un tramo de muro (abertura) rellenando con el color de fondo."""
    v.fill([(x0, y0), (x1, y0), (x1, y1), (x0, y1)], layer=FONDO)


def rotulo_recinto(v, r, nivel, h_nom=2.15, h_cod=2.35, con_area=True):
    """Rótulo de recinto centrado (código, nombre, área)."""
    xc = (r['x0'] + r['x1']) / 2.0
    yc = (r['y0'] + r['y1']) / 2.0
    a = (r['x1'] - r['x0']) * (r['y1'] - r['y0'])
    L = r['nom'].split(' / ')
    lineas = [(r['cod'], h_cod, 'texto', True)]
    for ln in L:
        lineas.append((ln, h_nom, 'texto', False))
    if con_area:
        lineas.append((fmt(a, 2) + ' m²', h_nom, 'texto-suave', False))
    n = len(lineas)
    y = yc + (n - 1) * 0.13
    for (t, h, lay, b) in lineas:
        v.text((xc, y), t, h=h, layer=lay, anchor='middle', bold=b)
        y -= 0.27


# ============================================================================
# PLANTA ARQUITECTÓNICA
# ============================================================================
def planta(v, nivel, ejes=True, cotas=True, mobiliario=True, textos=True,
           etiquetas_nivel=True, h_pasillo=None):
    # ---------------- 1. MUROS ----------------
    # perimetrales
    for (x0, y0, x1, y1) in [(0, 0, L_BLOQUE, E_MURO), (0, D_BLOQUE - E_MURO, L_BLOQUE, D_BLOQUE),
                             (0, E_MURO, E_MURO, D_BLOQUE - E_MURO),
                             (L_BLOQUE - E_MURO, E_MURO, L_BLOQUE, D_BLOQUE - E_MURO)]:
        muro_rect(v, x0, y0, x1, y1)
    # tabiques verticales (dos tramos, interrumpidos por el pasillo)
    for (x0, x1) in TABIQUE_X:
        tabique_rect(v, x0, 0.25, x1, 3.80)
        tabique_rect(v, x0, 5.65, x1, 9.35)
    # muros del pasillo (horizontales)
    tabique_rect(v, 0.25, 3.80, 16.65, 3.95)          # lindero sur del pasillo
    tabique_rect(v, 20.20, 3.80, 23.75, 3.95)         # distribuidor este
    tabique_rect(v, 0.25, 5.65, 16.65, 5.80)          # lindero norte del pasillo
    tabique_rect(v, 20.20, 5.65, 23.75, 5.80)         # distribuidor este
    if nivel == 1:
        tabique_rect(v, 16.65, 3.80, 20.05, 3.95)     # estar / distribuidor
        tabique_rect(v, 16.65, 5.65, 20.05, 5.80)     # escalera / pasillo (dintel)

    # ---------------- 2. HUECOS: VENTANAS ----------------
    for win in ventanas(nivel):
        m = win['muro']
        if m == 'N':
            hueco(v, win['pos'] - win['w'] / 2, 9.35, win['pos'] + win['w'] / 2, 9.60)
            ventana_planta(v, win['pos'], 9.475, E_MURO, win['w'], 'y')
        elif m == 'S':
            hueco(v, win['pos'] - win['w'] / 2, 0.0, win['pos'] + win['w'] / 2, 0.25)
            ventana_planta(v, win['pos'], 0.125, E_MURO, win['w'], 'y')
        elif m == 'E':
            hueco(v, 23.75, win['pos'] - win['w'] / 2, 24.0, win['pos'] + win['w'] / 2)
            ventana_planta(v, 23.875, win['pos'], E_MURO, win['w'], 'x')
        elif m == 'O':
            hueco(v, 0.0, win['pos'] - win['w'] / 2, 0.25, win['pos'] + win['w'] / 2)
            ventana_planta(v, 0.125, win['pos'], E_MURO, win['w'], 'x')

    # ---------------- 3. HUECOS: PUERTAS + HOJAS ----------------
    doors = []
    for r in recintos(nivel):
        if r['tipo'] == 'dorm' and r['puerta']:
            w, _, lado = r['puerta']
            xc = r['x0'] + 1.60
            y = 3.875 if lado == 'N' else 5.725
            doors.append(dict(w=w, x=xc, y=y, hacia=-1 if lado == 'N' else 1,
                              bat='der', cod='P-1%02d' % 1))
    if nivel == 0:
        doors.append(dict(w=0.80, x=15.075, y=3.875, hacia=-1, bat='izq'))
        doors.append(dict(w=0.80, x=15.075, y=5.725, hacia=1, bat='izq'))
        doors.append(dict(w=0.90, x=21.975, y=3.875, hacia=-1, bat='izq'))
        doors.append(dict(w=0.90, x=21.975, y=5.725, hacia=1, bat='izq'))
        # puerta principal doble hoja
        hueco(v, 18.35 - 0.90, 0.0, 18.35 + 0.90, 0.25)
        puerta(v, (17.45, 0.125), (17.45 + 0.90 * 1.0, 0.125 + 0.90), 'der')
        puerta(v, (19.25, 0.125), (19.25 - 0.90, 0.125 + 0.90), 'izq')
    else:
        doors.append(dict(w=0.80, x=15.075, y=3.875, hacia=-1, bat='izq'))
        doors.append(dict(w=0.80, x=15.075, y=5.725, hacia=1, bat='izq'))
        doors.append(dict(w=0.90, x=21.975, y=3.875, hacia=-1, bat='izq'))
        doors.append(dict(w=1.20, x=21.975, y=5.725, hacia=1, bat='izq'))
        doors.append(dict(w=1.20, x=18.35, y=3.875, hacia=-1, bat='izq'))
    for d in doors:
        hueco(v, d['x'] - d['w'] / 2, d['y'] - 0.075, d['x'] + d['w'] / 2, d['y'] + 0.075)
        puerta(v, (d['x'] - d['w'] / 2, d['y']),
               (d['x'] - d['w'] / 2, d['y'] + d['hacia'] * d['w']), d['bat'])

    # ---------------- 4. AMOBLAMIENTO ----------------
    for r in recintos(nivel):
        if r['tipo'] == 'dorm':
            dormitorio_amoblado(v, r['x0'], r['y0'], r['x1'], r['y1'],
                                lado_ventana=r['hilera'])
        elif r['tipo'] == 'ssh':
            sshh_amoblado(v, r['x0'], r['y0'], r['x1'], r['y1'],
                          lado_ventana=r['hilera'])
    escalera_planta(v, nivel)

    # ---------------- 5. RÓTULOS ----------------
    if textos:
        for r in recintos(nivel):
            if r['tipo'] in ('pas',):
                rotulo_recinto(v, r, nivel, h_nom=1.9, h_cod=2.1)
            elif r['tipo'] == 'esc':
                rotulo_recinto(v, r, nivel, h_nom=1.9, h_cod=2.1, con_area=False)
            else:
                rotulo_recinto(v, r, nivel)
        # nivel de piso terminado
        z = 0.0 if nivel == 0 else NPT_PA
        v.text_sheet((2.10, 0.60), 'N.P.T. ' + nivel_txt(z), h=2.0,
                     layer='texto-suave')
        v.text_sheet((21.0, 2.90), 'N.P.T. ' + nivel_txt(z), h=2.0,
                     layer='texto-suave')

    # ---------------- 6. EJES Y COTAS ----------------
    if ejes:
        ejes_planta(v, globos=True, r_globo=4.0, margen=0.95)
    if cotas:
        cotas_planta(v)


def cotas_planta(v):
    # cadenas horizontales (debajo)
    dim_h(v, 0.0, L_BLOQUE, 0.0, off=23.0, size=2.6)
    xs = [0.0, 0.25]
    for (x0, x1) in TABIQUE_X:
        xs += [x0, x1]
    xs += [23.75, 24.0]
    dim_chain_h(v, xs, 0.0, off=13.0, size=1.9)
    xe = [x for _, x in EJE_X]
    dim_chain_h(v, xe, 0.0, off=33.0, size=2.1)
    # cadenas verticales (izquierda)
    dim_v(v, 0.0, 0.0, D_BLOQUE, off=-26.0, size=2.6)
    ys = [0.0, 0.25, 3.80, 3.95, 5.65, 5.80, 9.35, 9.60]
    dim_chain_v(v, ys, 0.0, off=-16.0, size=1.9)
    ye = [y for _, y in EJE_Y]
    dim_chain_v(v, ye, 0.0, off=-36.0, size=2.1)


# ============================================================================
# PLANTA DE AZOTEA
# ============================================================================
def planta_azotea(v, cotas=True, ejes=True):
    """Planta de cubierta: losa con pendiente, parapeto, caseta de escalera,
    tanque elevado, ductos y bajantes."""
    # ---- superficie de la losa (trama suave) ----
    v.hatch([(0.25, 0.25), (23.75, 0.25), (23.75, 9.35), (0.25, 9.35)], angle=0,
            spacing=0.55, layer='hatch-2')
    v.rect(0.25, 0.25, 23.75, 9.35, layer='marco-fino')
    # ---- parapeto perimetral ----
    muro_rect(v, 0, 0, L_BLOQUE, 0.25)
    muro_rect(v, 0, 9.35, L_BLOQUE, 9.60)
    muro_rect(v, 0, 0.25, 0.25, 9.35)
    muro_rect(v, 23.75, 0.25, 24.0, 9.35)
    # ---- pendientes hacia sumideros ----
    for (x, y, dx, dy) in [(6.00, 4.80, -1, 0), (18.00, 4.80, 1, 0),
                           (12.00, 2.40, 0, -1), (12.00, 7.20, 0, 1)]:
        v.line((x, y), (x + dx * 4.2, y + dy * 4.2), layer='proyeccion')
        ex, ey = x + dx * 4.6, y + dy * 4.6
        v.fill([(ex, ey), (ex - dx * 0.35 - dy * 0.22, ey - dy * 0.35 - dx * 0.22),
                (ex - dx * 0.35 + dy * 0.22, ey - dy * 0.35 + dx * 0.22)],
               layer='proyeccion')
    v.text((12.00, 8.30), 'PENDIENTE 2 % HACIA SUMIDEROS', h=2.2, layer='texto-suave',
           anchor='middle')
    v.text((12.00, 1.40), 'AZOTEA INACCESIBLE  ·  N.P.T. +6,20', h=2.4,
           anchor='middle')
    v.text((12.00, 0.85), 'APLICAR IMPERMEABILIZANTE Y PROTECCIÓN PÉTREA',
           h=1.9, anchor='middle', layer='texto-suave')
    # ---- sumideros ----
    for (x, y) in [(1.00, 4.80), (12.00, 2.30), (23.00, 4.80)]:
        v.circle((x, y), 0.20, layer='agua', fill=True)
        v.circle((x, y), 0.30, layer='agua')
        v.text((x, y - 0.60), 'SUMIDERO 2"', h=1.7, layer='texto-suave', anchor='middle')
    # ---- caseta de escalera ----
    v.hatch([(16.65, 5.65), (20.05, 5.65), (20.05, 9.35), (16.65, 9.35)],
            angle=45, spacing=0.35, layer='hatch')
    v.rect(16.65, 5.65, 20.05, 9.35, layer='muro-corte', fill=False)
    v.text((18.35, 7.60), 'CASETA DE ESCALERA', h=2.0, anchor='middle')
    v.text((18.35, 7.10), 'N.P.T. +9,45  ·  h libre 2,20 m', h=1.8, anchor='middle',
           layer='texto-suave')
    # ---- tanque elevado ----
    v.rect(17.30, 0.60, 19.40, 2.60, layer='agua', fill=True)
    v.text((18.35, 1.75), 'TANQUE ELEVADO', h=1.9, anchor='middle')
    v.text((18.35, 1.30), '2 × 1 100 L', h=1.8, anchor='middle', layer='texto-suave')
    dim_h(v, 17.30, 19.40, 0.60, off=-6.0, size=1.7)
    # ---- ductos de ventilación ----
    for (x, y) in [(14.90, 1.00), (14.90, 8.60), (13.40, 1.00), (13.40, 8.60)]:
        v.circle((x, y), 0.15, layer='sanitario', fill=True)
    v.text((14.15, 0.55), 'DUCTOS DE VENTILACIÓN', h=1.7, layer='texto-suave',
           anchor='middle')
    # ---- bajantes pluviales ----
    for (x, y) in [(0.55, 0.55), (23.45, 0.55), (0.55, 9.05), (23.45, 9.05)]:
        v.circle((x, y), 0.12, layer='agua', fill=True)
        v.text((x + (0.38 if x < 12 else -0.38), y), 'B.P. 4"', h=1.7,
               layer='texto-suave', anchor='start' if x < 12 else 'end')
    if ejes:
        ejes_planta(v, globos=True, r_globo=4.0, margen=0.95)
    if cotas:
        dim_h(v, 0.0, L_BLOQUE, 0.0, off=22.0, size=2.6)
        dim_v(v, 0.0, 0.0, D_BLOQUE, off=-26.0, size=2.6)
        dim_h(v, 16.65, 20.05, 9.35, off=-9.0, size=1.9)
        dim_v(v, 20.05, 5.65, 9.35, off=9.0, size=1.9)
        dim_h(v, 0.30, 23.70, 4.80, off=-9.0, size=2.2, txt='23,40')


# ============================================================================
# CORTES
# ============================================================================
def _cimiento(v, u0, u1, e_muro=0.25, sobre=True):
    """Cimiento corrido + sobrecimiento + solera bajo un muro (u = eje del muro)."""
    uc = (u0 + u1) / 2.0
    # cimiento corrido (concreto ciclópeo) ancho 0,70 x 0,25
    v.fill([(uc - ZAP_W / 2, ZAP_Z0), (uc + ZAP_W / 2, ZAP_Z0),
            (uc + ZAP_W / 2, ZAP_Z1), (uc - ZAP_W / 2, ZAP_Z1)], layer='hormigon')
    v.polyline([(uc - ZAP_W / 2, ZAP_Z0), (uc + ZAP_W / 2, ZAP_Z0),
                (uc + ZAP_W / 2, ZAP_Z1), (uc - ZAP_W / 2, ZAP_Z1)], close=True,
               layer='muro-corte')
    v.hatch([(uc - ZAP_W / 2, ZAP_Z0), (uc + ZAP_W / 2, ZAP_Z0),
             (uc + ZAP_W / 2, ZAP_Z1), (uc - ZAP_W / 2, ZAP_Z1)],
            angle=-45, spacing=0.22, layer='hatch')
    # sobrecimiento
    if sobre:
        v.fill([(u0, SOBR_Z0), (u1, SOBR_Z0), (u1, SOBR_Z1), (u0, SOBR_Z1)],
               layer='hormigon')
        v.polyline([(u0, SOBR_Z0), (u1, SOBR_Z0), (u1, SOBR_Z1), (u0, SOBR_Z1)],
                   close=True, layer='muro-corte')


def terreno(v, u0, u1, z=0.0):
    """Línea de terreno natural con rayado."""
    v.line((u0, z), (u1, z), layer='terreno')
    import math
    x = u0
    while x < u1:
        v.line((x, z), (x - 0.18, z - 0.20), layer='terreno')
        x += 0.42


def muro_alzado_corte(v, u0, u1, z0, z1, huecos=None, layer='muro-fill',
                      junta=True):
    """Muro visto en alzado dentro de un corte (con huecos opcionales)."""
    v.fill([(u0, z0), (u1, z0), (u1, z1), (u0, z1)], layer='sombra')
    if junta:
        # junta de mortero cada 0,40 m aprox (aparejo)
        pass
    v.polyline([(u0, z0), (u1, z0), (u1, z1), (u0, z1)], close=True,
               layer='marco-fino')
    if huecos:
        for (h0, h1, w0, w1) in huecos:
            v.fill([(w0, h0), (w1, h0), (w1, h1), (w0, h1)], layer=FONDO)
            v.polyline([(w0, h0), (w1, h0), (w1, h1), (w0, h1)], close=True,
                       layer='marco-medio')
            # vidrio y carpintería
            v.line((w0, (h0 + h1) / 2), (w1, (h0 + h1) / 2), layer='vidrio')
            v.line(((w0 + w1) / 2, h0), ((w0 + w1) / 2, h1), layer='carpinteria')
            v.line((w0 + 0.02, h0), (w1 - 0.02, h0), layer='carpinteria')
            v.line((w0 + 0.02, h1), (w1 - 0.02, h1), layer='carpinteria')


def losa_aligerada(v, u0, u1, z0, z1, bovedillas=True):
    """Losa aligerada en corte (capa de compresión + bovedillas)."""
    v.fill([(u0, z0), (u1, z0), (u1, z1), (u0, z1)], layer='hormigon')
    v.polyline([(u0, z0), (u1, z0), (u1, z1), (u0, z1)], close=True,
               layer='muro-corte')
    if bovedillas:
        n = int((u1 - u0) / 0.30)
        for i in range(n):
            x = u0 + 0.15 + i * 0.30
            v.circle((x, z0 + 0.15), 0.085, layer='hatch-2', fill=True)
        v.line((u0, z1 - 0.05), (u1, z1 - 0.05), layer='marco-fino')


def corte_transversal(v, x_corte, titulo_extra='', con_niveles=True):
    """Corte transversal (crujía). u = eje Y del bloque (0..9,60), z = altura."""
    u0, u1 = 0.0, D_BLOQUE
    z_t = NIVEL_TERRENO
    # ---- terreno ----
    terreno(v, -1.20, 0.0, z_t)
    terreno(v, D_BLOQUE, D_BLOQUE + 1.20, z_t)
    for (u0t, u1t) in [(-1.20, 0.0), (9.60, 10.80)]:
        v.hatch([(u0t, z_t - 1.20), (u1t, z_t - 1.20), (u1t, z_t), (u0t, z_t)],
                angle=45, spacing=0.32, layer='terreno')
    # ---- relleno compactado bajo piso ----
    v.hatch([(0.25, z_t), (9.35, z_t), (9.35, -0.25), (0.25, -0.25)], angle=45,
            spacing=0.45, layer='hatch')
    # ---- cimientos ----
    for (a, b) in [(0.0, 0.25), (3.80, 3.95), (5.65, 5.80), (9.35, 9.60)]:
        _cimiento(v, a, b)
    # solera de piso
    v.fill([(0.25, -0.20), (9.35, -0.20), (9.35, -0.05), (0.25, -0.05)],
           layer='hormigon')
    v.polyline([(0.25, -0.20), (9.35, -0.20), (9.35, -0.05), (0.25, -0.05)],
               close=True, layer='muro-corte')
    v.line((0.25, 0.0), (9.35, 0.0), layer='marco-medio')   # piso terminado
    # ---- muros planta baja (sección) ----
    v.fill([(0.0, 0.0), (0.25, 0.0), (0.25, 2.90), (0.0, 2.90)], layer='muro-fill')
    v.polyline([(0.0, 0.0), (0.25, 0.0), (0.25, 2.90), (0.0, 2.90)], close=True,
               layer='muro-corte')
    v.fill([(9.35, 0.0), (9.60, 0.0), (9.60, 2.90), (9.35, 2.90)], layer='muro-fill')
    v.polyline([(9.35, 0.0), (9.60, 0.0), (9.60, 2.90), (9.35, 2.90)], close=True,
               layer='muro-corte')
    _muro_con_hueco(v, 0.0, 0.25, 0.0, 2.90, [(0.90, 2.40, 0.05, 0.20)], hacia='de')
    _muro_con_hueco(v, 9.35, 9.60, 0.0, 2.90, [(0.90, 2.40, 9.40, 9.55)], hacia='de')
    # ---- tabiques internos (sección completa) ----
    for (a, b) in [(3.80, 3.95), (5.65, 5.80)]:
        v.fill([(a, 0.0), (b, 0.0), (b, 2.90), (a, 2.90)], layer='tabique-fill')
        v.polyline([(a, 0.0), (b, 0.0), (b, 2.90), (a, 2.90)], close=True,
                   layer='muro-corte')
    # ---- losa aligerada entre pisos ----
    losa_aligerada(v, 0.0, 9.60, 2.90, 3.20)
    # ---- muros planta alta ----
    _muro_con_hueco(v, 0.0, 0.25, NPT_PA, 5.85, [(4.15, 5.65, 0.05, 0.20)], hacia='de',
                    layer='muro-fill')
    _muro_con_hueco(v, 9.35, 9.60, NPT_PA, 5.85, [(4.15, 5.65, 9.40, 9.55)], hacia='de',
                    layer='muro-fill')
    for (a, b) in [(3.80, 3.95), (5.65, 5.80)]:
        v.fill([(a, NPT_PA), (b, NPT_PA), (b, 5.85), (a, 5.85)], layer='tabique-fill')
        v.polyline([(a, NPT_PA), (b, NPT_PA), (b, 5.85), (a, 5.85)], close=True,
                   layer='muro-corte')
    v.line((0.25, NPT_PA), (9.35, NPT_PA), layer='marco-medio')     # piso PA
    # ---- cubierta ----
    losa_aligerada(v, 0.0, 9.60, 5.85, 6.15)
    v.fill([(0.25, 6.15), (9.35, 6.15), (9.35, 6.20), (0.25, 6.20)], layer='hormigon')
    # parapetos
    for (a, b) in [(0.0, 0.25), (9.35, 9.60)]:
        v.fill([(a, 6.20), (b, 6.20), (b, 7.15), (a, 7.15)], layer='muro-fill')
        v.polyline([(a, 6.20), (b, 6.20), (b, 7.15), (a, 7.15)], close=True,
                   layer='muro-corte')
        v.fill([(a - 0.03, 7.15), (b + 0.03, 7.15), (b + 0.03, 7.20),
                (a - 0.03, 7.20)], layer='hormigon')
        v.polyline([(a - 0.03, 7.15), (b + 0.03, 7.15), (b + 0.03, 7.20),
                    (a - 0.03, 7.20)], close=True, layer='muro-corte')
    # ---- alero / viga de borde ----
    for (a, b, s) in [(0.0, 0.25, -1), (9.35, 9.60, 1)]:
        v.fill([(a, 2.90), (b, 2.90), (b, 3.05), (a, 3.05)], layer='hormigon')
    # ---- cotas de nivel ----
    if con_niveles:
        cota_nivel(v, 0.0, 10.05, off=0, size=2.1, lado='der')
        cota_nivel(v, NPT_PA, 10.05, off=0, size=2.1, lado='der')
        cota_nivel(v, NPT_CUB, 10.05, off=0, size=2.1, lado='der')
        cota_nivel(v, 7.20, 10.05, off=0, size=2.1, lado='der')
        cota_nivel(v, NIVEL_TERRENO, -0.35, off=0, size=2.1, lado='izq',
                   txt='NTN ' + nivel_txt(NIVEL_TERRENO))
        cota_nivel(v, -1.05, -1.35, off=0, size=2.1, lado='izq')
        # alturas libres
        dim_v(v, 9.95, 0.0, 2.90, off=0, size=1.9, txt='2,90')
        dim_v(v, 9.95, NPT_PA, 5.85, off=0, size=1.9, txt='2,60')
    # cotas de vanos
    dim_h(v, 0.0, 0.25, 0.0, off=-8.0, size=1.8)
    dim_h(v, 3.80, 3.95, 0.0, off=-8.0, size=1.8)
    dim_h(v, 3.95, 5.65, 0.0, off=-8.0, size=1.8, txt='1,70')
    dim_h(v, 5.65, 5.80, 0.0, off=-8.0, size=1.8)
    dim_h(v, 9.35, 9.60, 0.0, off=-8.0, size=1.8)
    dim_h(v, 0.0, 9.60, 0.0, off=-19.0, size=2.5)


def _muro_con_hueco(v, a, b, z0, z1, huecos, hacia='de', layer='muro-fill'):
    """Muro en sección con huecos: dibuja tramos llenos + carpintería del hueco."""
    zs = [(z0, z1)]
    tramos = [(z0, z1)]
    for (h0, h1, w0, w1) in huecos:
        nt = []
        for (t0, t1) in tramos:
            if h0 > t0:
                nt.append((t0, h0))
            if h1 < t1:
                nt.append((h1, t1))
        tramos = nt
    for (t0, t1) in tramos:
        v.fill([(a, t0), (b, t0), (b, t1), (a, t1)], layer=layer)
        v.polyline([(a, t0), (b, t0), (b, t1), (a, t1)], close=True, layer='muro-corte')
    for (h0, h1, w0, w1) in huecos:
        # marco y vidrio
        v.polyline([(w0, h0), (w1, h0), (w1, h1), (w0, h1)], close=True,
                   layer='carpinteria')
        v.line((w0, (h0 + h1) / 2), (w1, (h0 + h1) / 2), layer='vidrio')
        v.line(((w0 + w1) / 2, h0), ((w0 + w1) / 2, h1), layer='carpinteria')
        v.line((w0, h0), (w1, h0), layer='carpinteria')
        v.line((w0, h1), (w1, h1), layer='carpinteria')


def corte_longitudinal(v, y_corte=2.00, con_niveles=True):
    """Corte longitudinal (a lo largo del bloque). u = eje X (0..24), z = altura."""
    # ---- terreno ----
    terreno(v, -1.20, 0.0, NIVEL_TERRENO)
    terreno(v, L_BLOQUE, L_BLOQUE + 1.20, NIVEL_TERRENO)
    for (u0t, u1t) in [(-1.20, 0.0), (L_BLOQUE, L_BLOQUE + 1.20)]:
        v.hatch([(u0t, NIVEL_TERRENO - 1.20), (u1t, NIVEL_TERRENO - 1.20),
                 (u1t, NIVEL_TERRENO), (u0t, NIVEL_TERRENO)], angle=45, spacing=0.32,
                layer='terreno')
    v.hatch([(0.25, NIVEL_TERRENO), (23.75, NIVEL_TERRENO), (23.75, -0.25),
             (0.25, -0.25)], angle=45, spacing=0.45, layer='hatch')
    # ---- cimientos bajo cada eje cortado ----
    muros_x = [(0.0, 0.25)] + list(TABIQUE_X) + [(23.75, 24.0)]
    for (a, b) in muros_x:
        _cimiento(v, a, b)
    v.fill([(0.25, -0.20), (23.75, -0.20), (23.75, -0.05), (0.25, -0.05)],
           layer='hormigon')
    v.polyline([(0.25, -0.20), (23.75, -0.20), (23.75, -0.05), (0.25, -0.05)],
               close=True, layer='muro-corte')
    v.line((0.25, 0.0), (23.75, 0.0), layer='marco-medio')
    # ---- muros cortados (planta baja y alta) ----
    for (a, b) in muros_x:
        for (z0, z1) in [(0.0, 2.90), (NPT_PA, 5.85)]:
            layer = 'muro-fill' if (a == 0.0 or b == 24.0) else 'tabique-fill'
            v.fill([(a, z0), (b, z0), (b, z1), (a, z1)], layer=layer)
            v.polyline([(a, z0), (b, z0), (b, z1), (a, z1)], close=True,
                       layer='muro-corte')
    # ---- losas ----
    losa_aligerada(v, 0.0, L_BLOQUE, 2.90, 3.20)
    losa_aligerada(v, 0.0, L_BLOQUE, 5.85, 6.15)
    v.fill([(0.25, 6.15), (23.75, 6.15), (23.75, 6.20), (0.25, 6.20)], layer='hormigon')
    v.line((0.25, NPT_PA), (23.75, NPT_PA), layer='marco-medio')
    # ---- parapetos ----
    for (a, b) in [(0.0, 0.25), (23.75, 24.0)]:
        v.fill([(a, 6.20), (b, 6.20), (b, 7.15), (a, 7.15)], layer='muro-fill')
        v.polyline([(a, 6.20), (b, 6.20), (b, 7.15), (a, 7.15)], close=True,
                   layer='muro-corte')
        v.fill([(a - 0.03, 7.15), (b + 0.03, 7.15), (b + 0.03, 7.20), (a - 0.03, 7.20)],
               layer='hormigon')
    # ---- fondo: muro del pasillo (sur) con puertas + muro fachada norte ----
    # muro del pasillo visto (y = 3,80-3,95), con las puertas de los dormitorios sur
    puertas_sur = [(r['x0'] + 1.60, 0.90) for r in recintos(0) if r['tipo'] == 'dorm'
                   and r['hilera'] == 'S']
    huecos_pb = [(0.0, 2.10, xc - w / 2, xc + w / 2) for (xc, w) in puertas_sur]
    huecos_pb.insert(0, (1.70, 3.20, 14.40, 14.90))
    muro_alzado_corte(v, 0.25, 16.65, 0.0, 2.90, huecos=huecos_pb)
    # vano de la escalera (dintel)
    v.line((16.65, 2.10), (20.05, 2.10), layer='marco-medio')
    # muro de fachada norte al fondo (con ventanas)
    huecos_norte = [(0.90, 2.40, xc - 0.75, xc + 0.75) for xc in
                    (1.85, 5.20, 8.55, 11.90)]
    huecos_norte.append((1.70, 2.50, 14.40, 14.90))
    muro_alzado_corte(v, 0.25, 23.75, 0.0, 2.90, huecos=huecos_norte)
    # planta alta: muro del pasillo norte con puertas + fachada norte
    puertas_norte = [(r['x0'] + 1.60, 0.90) for r in recintos(0) if r['tipo'] == 'dorm'
                     and r['hilera'] == 'N']
    huecos_pa = [(0.0, 2.10, xc - w / 2, xc + w / 2) for (xc, w) in puertas_norte]
    muro_alzado_corte(v, 0.25, 16.65, NPT_PA, 5.85, huecos=huecos_pa)
    huecos_norte_pa = [(4.15, 5.65, xc - 0.75, xc + 0.75) for xc in
                       (1.85, 5.20, 8.55, 11.90)]
    muro_alzado_corte(v, 0.25, 23.75, NPT_PA, 5.85, huecos=huecos_norte_pa)
    # ---- escalera (al fondo) ----
    v.line((16.65, 0.0), (16.65, 2.90), layer='marco-fino')
    v.line((20.05, 0.0), (20.05, 2.90), layer='marco-fino')
    # ---- cotas de nivel ----
    if con_niveles:
        for (z, txt) in [(0.0, None), (NPT_PA, None), (NPT_CUB, None), (7.20, None)]:
            cota_nivel(v, z, 24.35, off=0, size=2.1, lado='der', txt=txt)
        cota_nivel(v, NIVEL_TERRENO, -0.35, off=0, size=2.1, lado='izq',
                   txt='NTN ' + nivel_txt(NIVEL_TERRENO))
        cota_nivel(v, -1.05, -1.35, off=0, size=2.1, lado='izq')
        dim_v(v, 24.25, 0.0, 2.90, off=0, size=1.9, txt='2,90')
        dim_v(v, 24.25, NPT_PA, 5.85, off=0, size=1.9, txt='2,60')
    # ---- cotas horizontales ----
    dim_h(v, 0.0, 24.0, 0.0, off=-22.0, size=2.6)
    xs = [0.0] + [x for (a, b) in TABIQUE_X for x in (a, b)] + [24.0]
    dim_chain_h(v, xs, 0.0, off=-12.0, size=1.8)


# ============================================================================
# FACHADAS
# ============================================================================
def fachada(v, lado, con_niveles=True, con_material=True):
    """lado: 'N','S' -> u = X (0..24) ; 'E','O' -> u = Y (0..9,60)."""
    largo = L_BLOQUE if lado in ('N', 'S') else D_BLOQUE
    z0 = 0.0
    z1 = H_TOTAL
    # ---- terreno ----
    terreno(v, -1.20, 0.0, NIVEL_TERRENO)
    terreno(v, largo, largo + 1.20, NIVEL_TERRENO)
    for (a, b) in [(-1.20, 0.0), (largo, largo + 1.20)]:
        v.hatch([(a, NIVEL_TERRENO - 1.20), (b, NIVEL_TERRENO - 1.20),
                 (b, NIVEL_TERRENO), (a, NIVEL_TERRENO)], angle=45, spacing=0.32,
                layer='terreno')
    # ---- plinto / sobrecimiento (z -0,45 a 0,00) ----
    v.fill([(0.0, NIVEL_TERRENO), (largo, NIVEL_TERRENO), (largo, 0.0), (0.0, 0.0)],
           layer='hormigon')
    v.polyline([(0.0, NIVEL_TERRENO), (largo, NIVEL_TERRENO), (largo, 0.0),
                (0.0, 0.0)], close=True, layer='muro-corte')
    # ---- paño de fachada ----
    v.fill([(0.0, 0.0), (largo, 0.0), (largo, NPT_CUB + 0.30), (0.0, NPT_CUB + 0.30)],
           layer='sombra')
    v.polyline([(0.0, 0.0), (largo, 0.0), (largo, NPT_CUB + 0.30), (0.0, NPT_CUB + 0.30)],
               close=True, layer='muro-visto')
    # ---- vanos ----
    wins = [w for w in ventanas(0)] + [w for w in ventanas(1)]
    for w in wins:
        if w['muro'] != lado:
            continue
        u0 = w['pos'] - w['w'] / 2.0
        u1 = w['pos'] + w['w'] / 2.0
        h0, h1 = w['sill'], w['sill'] + w['h']
        # vano
        v.fill([(u0, h0), (u1, h0), (u1, h1), (u0, h1)], layer=FONDO)
        # marco
        v.polyline([(u0, h0), (u1, h0), (u1, h1), (u0, h1)], close=True,
                   layer='carpinteria')
        v.polyline([(u0 - 0.04, h0 - 0.04), (u1 + 0.04, h0 - 0.04),
                    (u1 + 0.04, h1 + 0.04), (u0 - 0.04, h1 + 0.04)], close=True,
                   layer='marco-medio')
        # hojas: 2 hojas correderas o abatibles con parteluz
        nhojas = 2 if w['w'] > 1.0 else 1
        for k in range(1, nhojas):
            x = u0 + (u1 - u0) * k / nhojas
            v.line((x, h0), (x, h1), layer='carpinteria')
        v.line((u0, h1 - 0.35), (u1, h1 - 0.35), layer='carpinteria')  # travesaño
        # vidrio (rayado diagonal suave)
        v.line((u0 + 0.05, h0 + 0.05), (u1 - 0.05, h1 - 0.05), layer='vidrio')
        # alféizar
        v.line((u0 - 0.06, h0 - 0.03), (u1 + 0.06, h0 - 0.03), layer='marco-medio')
    # ---- puerta de ingreso (solo fachada sur) ----
    if lado == 'S':
        u0, u1 = 18.35 - 0.90, 18.35 + 0.90
        v.fill([(u0, 0.0), (u1, 0.0), (u1, 2.40), (u0, 2.40)], layer=FONDO)
        v.polyline([(u0, 0.0), (u1, 0.0), (u1, 2.40), (u0, 2.40)], close=True,
                   layer='carpinteria')
        v.line((18.35, 0.0), (18.35, 2.40), layer='carpinteria')
        v.line((u0, 2.40), (u1, 2.40), layer='marco-medio')
        v.line((u0, 0.02), (u1, 0.02), layer='marco-medio')
        # vidrio superior
        v.line((u0 + 0.05, 1.95), (u1 - 0.05, 1.95), layer='carpinteria')
        v.line((u1 - 0.10, 1.98), (u0 + 0.10, 2.35), layer='vidrio')
        # escalera de ingreso (3 peldaños) y rampa
        for k in range(4):
            zz = NIVEL_TERRENO + k * (0.45 / 3.0)
            v.line((u0 - 0.90 + k * 0.30, zz), (u1 + 0.90 - k * 0.30, zz),
                   layer='marco-fino')
        v.text((18.35, NIVEL_TERRENO - 0.30), 'INGRESO PRINCIPAL · 3 PELDAÑOS',
               h=1.8, layer='texto-suave', anchor='middle')
    # ---- líneas de nivel / juntas ----
    v.line((0.0, 0.0), (largo, 0.0), layer='marco-medio')                 # NPT ±0,00
    v.line((0.0, 3.20), (largo, 3.20), layer='marco-fino')                # junta losa
    v.line((0.0, NPT_CUB), (largo, NPT_CUB), layer='marco-fino')          # junta cubierta
    # cornisa
    v.fill([(0.0, NPT_CUB), (largo, NPT_CUB), (largo, NPT_CUB + 0.30),
            (0.0, NPT_CUB + 0.30)], layer='hormigon')
    v.polyline([(0.0, NPT_CUB), (largo, NPT_CUB), (largo, NPT_CUB + 0.30),
                (0.0, NPT_CUB + 0.30)], close=True, layer='muro-corte')
    # parapeto
    v.line((0.0, 7.15), (largo, 7.15), layer='muro-corte')
    v.fill([(-0.03, 7.10), (largo + 0.03, 7.10), (largo + 0.03, 7.15), (-0.03, 7.15)],
           layer='hormigon')
    v.polyline([(-0.03, 7.10), (largo + 0.03, 7.10), (largo + 0.03, 7.15),
                (-0.03, 7.15)], close=True, layer='muro-corte')
    # bajantes pluviales (2 por fachada)
    for u in (0.60, largo - 0.60):
        v.line((u - 0.06, NIVEL_TERRENO), (u - 0.06, 6.90), layer='carpinteria')
        v.line((u + 0.06, NIVEL_TERRENO), (u + 0.06, 6.90), layer='carpinteria')
        v.line((u - 0.06, 6.90), (u + 0.06, 6.90), layer='carpinteria')
    if con_material:
        v.text((largo / 2.0, 6.65), 'MURO DE ALBAÑILERÍA TARRAJEADO Y PINTADO',
               h=1.8, layer='texto-suave', anchor='middle')
        v.text((largo / 2.0, -0.30), 'SOBRECIMIENTO DE CONCRETO 1:8 + 25% P.M.',
               h=1.7, layer='texto-suave', anchor='middle')
    if con_niveles:
        cota_nivel(v, 0.0, -1.30, off=0, size=2.1, lado='izq')
        cota_nivel(v, NPT_PA, -1.30, off=0, size=2.1, lado='izq')
        cota_nivel(v, NPT_CUB, -1.30, off=0, size=2.1, lado='izq')
        cota_nivel(v, 7.15, -1.30, off=0, size=2.1, lado='izq')
        cota_nivel(v, 7.20, -1.30, off=-3.4, size=1.9, lado='izq', txt='ALBARDILLA')
        cota_nivel(v, NIVEL_TERRENO, largo + 0.35, off=0, size=2.1, lado='der',
                   txt='NTN ' + nivel_txt(NIVEL_TERRENO))
    dim_h(v, 0.0, largo, 0.0, off=-20.0, size=2.5)
    dim_h(v, 0.0, NIVEL_TERRENO, 0.0, off=-11.0, size=1.8)


# ============================================================================
# SITUACIÓN / EMPLAZAMIENTO (croquis de conjunto)
# ============================================================================
# Bloque en el conjunto: (nombre, x0, y0, x1, y1) en metros de terreno
BLOQUES = [
    ('AULAS / AULAS TALLER', 12.0, 78.0, 48.0, 92.0),
    ('ADMINISTRACIÓN Y BIBLIOTECA', 12.0, 46.0, 32.0, 62.0),
    ('DORMITORIOS (BLOQUE D)', 52.0, 44.0, 76.0, 53.6),
    ('COMEDOR Y COCINA', 12.0, 14.0, 34.0, 30.0),
    ('SERVICIOS / SS.HH. Y DEPÓSITO', 40.0, 14.0, 54.0, 24.0),
    ('CISTERNA Y CUARTO DE MÁQUINAS', 58.0, 14.0, 68.0, 22.0),
    ('PORTERÍA / CONTROL', 44.0, 2.0, 52.0, 8.0),
]
DESTACADO = 'DORMITORIOS (BLOQUE D)'


def terreno_conjunto(v, eje_x=True):
    """Dibuja el predio: cerco, vías, veredas, patio, áreas verdes, estacionamiento."""
    # cerco perimétrico
    v.rect(0, 0, 100.0, 100.0, layer='marco-medio')
    v.hatch([(-4, -6), (104, -6), (104, 0), (-4, 0)], angle=45, spacing=1.2,
            layer='hatch-2')
    # vía de acceso + estacionamiento
    v.rect(0, 0, 100, 8.0, layer='via', fill=True)
    v.hatch([(56, 0), (100, 0), (100, 8), (56, 8)], angle=45, spacing=1.6,
            layer='hatch')
    v.text((78, 4.0), 'ESTACIONAMIENTO  6,00 m', h=2.2, anchor='middle',
           layer='texto-suave')
    v.text((28, 4.0), 'VÍA DE ACCESO  6,00 m', h=2.2, anchor='middle',
           layer='texto-suave')
    # vereda perimetral
    v.rect(0, 8.0, 100, 10.0, layer='marco-fino')
    v.rect(0, 92.0, 100, 100.0, layer='marco-fino')
    v.rect(0, 10.0, 2.0, 92.0, layer='marco-fino')
    v.rect(98.0, 10.0, 100, 92.0, layer='marco-fino')
    v.text((50, 95.5), 'VEREDA PERIMETRAL 1,50 m', h=2.0, anchor='middle',
           layer='texto-suave')
    # patio central / losa deportiva
    v.rect(36.0, 24.0, 74.0, 42.0, layer='marco-fino')
    v.hatch([(36, 24), (74, 24), (74, 42), (36, 42)], angle=0, spacing=2.4,
            layer='hatch-2')
    v.text((55, 33.0), 'PATIO CENTRAL / LOSA DEPORTIVA', h=2.6, anchor='middle')
    v.text((55, 30.4), '28,00 × 18,00 m', h=2.2, anchor='middle', layer='texto-suave')
    # áreas verdes
    v.rect(34.0, 62.0, 50.0, 76.0, layer='vegetal', fill=True)
    v.text((42, 69.0), 'ÁREAS VERDES', h=2.0, anchor='middle')
    v.rect(78.0, 22.0, 98.0, 40.0, layer='vegetal', fill=True)
    v.text((88, 31.0), 'ÁREAS VERDES', h=2.0, anchor='middle')
    # cisterna / tanque
    v.rect(58, 14, 68, 22, layer='edificio', fill=True)
    v.text((63, 18), 'CISTERNA', h=1.9, anchor='middle')
    # patios de maniobra
    v.text((63, 41.0), 'PATIO DE MANIOBRAS', h=2.0, anchor='middle',
           layer='texto-suave')
    # árboles
    for (x, y) in [(8, 34), (8, 52), (8, 70), (30, 66), (36, 88), (52, 96), (96, 48),
                   (96, 62), (86, 78), (26, 8.5), (60, 96), (20, 88), (44, 58)]:
        v.circle((x, y), 1.6, layer='arbol', fill=True)
        v.circle((x, y), 0.25, layer='arbol')
    # bloques
    for (nom, x0, y0, x1, y1) in BLOQUES:
        dest = (nom == DESTACADO)
        lay = 'destacado' if dest else 'edificio'
        v.fill([(x0, y0), (x1, y0), (x1, y1), (x0, y1)], layer=lay)
        v.polyline([(x0, y0), (x1, y0), (x1, y1), (x0, y1)], close=True,
                   layer='marco-medio')
        # cubierta: pendiente
        v.line((x0 + 0.6, y0 + 0.6), (x1 - 0.6, y1 - 0.6), layer='proyeccion')
        lbl = nom.replace(' (BLOQUE D)', '')
        if (x1 - x0) > (y1 - y0) * 1.4:
            v.text(((x0 + x1) / 2.0, (y0 + y1) / 2.0 + 0.9), lbl,
                   h=2.4 if not dest else 2.7, anchor='middle', bold=dest)
            v.text(((x0 + x1) / 2.0, (y0 + y1) / 2.0 - 1.6),
                   fmt(x1 - x0, 1) + ' × ' + fmt(y1 - y0, 1) + ' m',
                   h=2.1, anchor='middle', layer='texto-suave')
        else:
            v.text(((x0 + x1) / 2.0, (y0 + y1) / 2.0), lbl,
                   h=2.3 if not dest else 2.6, anchor='middle', bold=dest)
            v.text(((x0 + x1) / 2.0, (y0 + y1) / 2.0 - 2.4),
                   fmt(x1 - x0, 1) + ' × ' + fmt(y1 - y0, 1) + ' m', h=2.0,
                   anchor='middle', layer='texto-suave')
    # norte y rótulos
    v.text((5.0, 84.0), 'ZONA EDUCATIVA', h=2.6, bold=True)
    v.text((5.0, 81.0), 'TERRENO: 10 000 m²  ·  100,00 × 100,00 m', h=2.2,
           layer='texto-suave')


def situacion(v, destacar=True, cotas=True):
    terreno_conjunto(v)
    if cotas:
        # acotado general del conjunto
        dim_h(v, 0.0, 100.0, 0.0, off=-14.0, size=3.0, txt='100,00 m')
        dim_v(v, 0.0, 0.0, 100.0, off=-14.0, size=3.0, txt='100,00 m')
        # acotado del bloque destacado
        (nom, x0, y0, x1, y1) = [b for b in BLOQUES if b[0] == DESTACADO][0]
        dim_h(v, x0, x1, y1, off=8.0, size=2.4)
        dim_v(v, x1, y0, y1, off=8.0, size=2.4)
        # retícula de ejes del bloque
        for (a, b) in [(0.0, 24.0)]:
            pass
        # vías
        dim_v(v, -1.0, 0.0, 6.0, off=6.0, size=2.2, txt='6,00')


def situacion_mini(v):
    """Miniatura esquemática de la ubicación del bloque (para láminas)."""
    v.rect(-8, -8, 108, 108, layer='marco-fino')
    for (nom, x0, y0, x1, y1) in BLOQUES:
        dest = (nom == DESTACADO)
        lay = 'destacado' if (dest and False) else 'edificio'
        v.fill([(x0, y0), (x1, y0), (x1, y1), (x0, y1)], layer=lay)
        v.polyline([(x0, y0), (x1, y0), (x1, y1), (x0, y1)], close=True,
                   layer='marco-fino')
    # resalta el bloque dormitorios con achurado y rótulo
    (nom, x0, y0, x1, y1) = [b for b in BLOQUES if b[0] == DESTACADO][0]
    v.fill([(x0, y0), (x1, y0), (x1, y1), (x0, y1)], layer='destacado')
    v.polyline([(x0, y0), (x1, y0), (x1, y1), (x0, y1)], close=True,
               layer='marco-medio')
    v.hatch([(x0, y0), (x1, y0), (x1, y1), (x0, y1)], angle=45, spacing=0.30,
            layer='hatch')
    v.line((x0, y0), (0, 8), layer='proyeccion')
    v.text((0.0, 6.0), 'ACCESO', h=3.0, layer='texto')
    for (x, y) in [(8, 34), (8, 52), (8, 70), (30, 66), (96, 48), (26, 8.5)]:
        v.circle((x, y), 2.2, layer='arbol', fill=True)
    v.text((55, 33.0), 'PATIO', h=3.4, anchor='middle', layer='texto-suave')


# ============================================================================
# DETALLES CONSTRUCTIVOS
# ============================================================================
def _tierra(v, u0, u1, z, n=None):
    """Relleno de terreno con rayado de 45°.  u0>u1 si va hacia la izquierda."""
    s = 1.0 if u1 > u0 else -1.0
    v.hatch([(u0, z), (u1, z), (u1, z - 0.60), (u0, z - 0.60)], angle=45,
            spacing=0.16, layer='hatch')


def detalle_cimiento(v, con_textos=True):
    """Detalle 1: cimiento corrido + sobrecimiento + solera (E 1:20)."""
    u_l, u_r = -0.62, 0.62
    # --- terreno natural a ambos lados ---
    _tierra(v, u_l, -0.35, NIVEL_TERRENO)
    _tierra(v, 0.35, u_r, NIVEL_TERRENO)
    v.line((u_l, NIVEL_TERRENO), (-0.35, NIVEL_TERRENO), layer='terreno')
    v.line((0.35, NIVEL_TERRENO), (u_r, NIVEL_TERRENO), layer='terreno')
    # --- relleno compactado bajo piso ---
    v.hatch([(-0.35, NIVEL_TERRENO), (u_r, NIVEL_TERRENO), (u_r, -0.25),
             (-0.35, -0.25)], angle=-45, spacing=0.18, layer='hatch-2')
    # --- cimiento corrido 0,70 x 0,25 ---
    v.fill([(-0.35, -1.05), (0.35, -1.05), (0.35, -0.80), (-0.35, -0.80)],
           layer='hormigon')
    v.polyline([(-0.35, -1.05), (0.35, -1.05), (0.35, -0.80), (-0.35, -0.80)],
               close=True, layer='muro-corte')
    for (uu, zz, r) in [(-0.20, -0.95, 0.055), (0.02, -0.92, 0.048),
                        (0.20, -0.97, 0.052), (-0.05, -1.00, 0.040)]:
        v.circle((uu, zz), r, layer='sanitario')
    # --- sobrecimiento 0,25 x 0,60 ---
    v.fill([(-0.125, -0.80), (0.125, -0.80), (0.125, -0.20), (-0.125, -0.20)],
           layer='hormigon')
    v.polyline([(-0.125, -0.80), (0.125, -0.80), (0.125, -0.20), (-0.125, -0.20)],
               close=True, layer='muro-corte')
    v.line((-0.125, -0.80), (0.125, -0.80), layer='muro-corte')
    # --- solera de piso y falso piso ---
    v.fill([(-0.125, -0.20), (u_r, -0.20), (u_r, -0.05), (-0.125, -0.05)],
           layer='hormigon')
    v.polyline([(-0.125, -0.20), (u_r, -0.20), (u_r, -0.05), (-0.125, -0.05)],
               close=True, layer='muro-corte')
    v.line((-0.125, 0.0), (u_r, 0.0), layer='marco-medio')
    # --- muro de albañilería ---
    v.fill([(-0.125, 0.0), (0.125, 0.0), (0.125, 0.60), (-0.125, 0.60)],
           layer='muro-fill')
    v.polyline([(-0.125, 0.0), (0.125, 0.0), (0.125, 0.60), (-0.125, 0.60)],
               close=True, layer='muro-corte')
    for k in range(6):
        v.line((-0.125 + (k % 2) * 0.0625, 0.10 * k), (0.125, 0.10 * k),
               layer='hatch')
    if con_textos:
        v.text((0.30, -1.02), 'CIMIENTO CORRIDO', h=1.9, layer='texto',
               anchor='middle')
        v.text((0.30, -0.90), '0,70 × 0,25  C:H 1:8 + 25 % P.M.', h=1.8,
               layer='texto-suave', anchor='middle')
        v.text((0.30, -0.58), 'SOBRECIMIENTO 0,25 × 0,60', h=1.8, layer='texto-suave',
               anchor='middle')
        v.text((0.30, -0.14), 'SOLERA / FALSO PISO h=0,15', h=1.8, layer='texto-suave',
               anchor='middle')
        v.text((-0.48, -0.50), 'N.T.N. −0,45', h=1.9, layer='texto-suave',
               anchor='middle')
        v.text((-0.45, -0.90), 'RELLENO COMPACTADO', h=1.8, layer='texto-suave',
               anchor='middle')
        v.text((-0.45, 0.30), 'MURO DE\nALBAÑILERÍA', h=1.8, layer='texto-suave',
               anchor='middle')
    dim_h(v, -0.35, 0.35, -1.05, off=-9.0, size=1.9, txt='0,70')
    dim_h(v, -0.125, 0.125, -0.80, off=-9.0, size=1.9, txt='0,25')
    dim_v(v, 0.35, -1.05, -0.80, off=9.0, size=1.9, txt='0,25')
    dim_v(v, 0.125, -0.80, -0.20, off=-9.0, size=1.8, txt='0,60')
    dim_v(v, 0.35, -1.05, 0.0, off=22.0, size=1.9, txt='1,05')
    cota_nivel(v, 0.0, -0.62, off=0, size=1.9, lado='izq')
    cota_nivel(v, NIVEL_TERRENO, -0.62, off=-3.0, size=1.8, lado='izq',
               txt='NTN −0,45')
    cota_nivel(v, -1.05, 0.62, off=0, size=1.8, lado='der')


def detalle_parapeto(v, con_textos=True):
    """Detalle 2: encuentro losa de azotea / alero / parapeto (E 1:20)."""
    u_l, u_r = -0.55, 0.60
    z0 = 5.55
    # --- losa aligerada 0,30 ---
    v.fill([(u_l, 5.85), (0.325, 5.85), (0.325, 6.15), (u_l, 6.15)], layer='hormigon')
    v.polyline([(u_l, 5.85), (0.325, 5.85), (0.325, 6.15), (u_l, 6.15)], close=True,
               layer='muro-corte')
    for k in range(4):
        v.circle((u_l + 0.20 + k * 0.22, 6.00), 0.055, layer='hatch-2', fill=True)
    # --- viga de borde / alero ---
    v.fill([(0.125, 5.85), (0.325, 5.85), (0.325, 6.15), (0.125, 6.15)],
           layer='hormigon')
    v.polyline([(0.125, 5.85), (0.325, 5.85), (0.325, 6.15), (0.125, 6.15)],
               close=True, layer='muro-corte')
    # --- acabado de azotea con pendiente 2 % ---
    v.line((u_l, 6.15), (0.325, 6.19), layer='marco-medio')
    v.hatch([(u_l, 6.15), (0.325, 6.19), (0.325, 6.21), (u_l, 6.17)], angle=0,
            spacing=0.03, layer='terreno')
    # --- parapeto ---
    v.fill([(0.125, 6.20), (0.375, 6.20), (0.375, 7.15), (0.125, 7.15)],
           layer='muro-fill')
    v.polyline([(0.125, 6.20), (0.375, 6.20), (0.375, 7.15), (0.125, 7.15)],
               close=True, layer='muro-corte')
    for k in range(9):
        v.line((0.125 + (k % 2) * 0.125, 6.30 + 0.10 * k), (0.375, 6.30 + 0.10 * k),
               layer='hatch')
    # --- albardilla ---
    v.fill([(0.085, 7.15), (0.415, 7.15), (0.415, 7.20), (0.085, 7.20)],
           layer='hormigon')
    v.polyline([(0.085, 7.15), (0.415, 7.15), (0.415, 7.20), (0.085, 7.20)],
               close=True, layer='muro-corte')
    # --- muro planta alta (interior) ---
    v.fill([(-0.125, z0), (0.125, z0), (0.125, 5.85), (-0.125, 5.85)],
           layer='muro-fill')
    v.polyline([(-0.125, z0), (0.125, z0), (0.125, 5.85), (-0.125, 5.85)],
               close=True, layer='muro-corte')
    if con_textos:
        v.text((0.60, 6.90), 'PARAPETO h=0,95', h=1.9, anchor='start')
        v.text((0.60, 6.60), 'ALBAÑILERÍA 0,25', h=1.8, anchor='start',
               layer='texto-suave')
        v.text((0.60, 6.28), 'ALBARDILLA DE CONCRETO', h=1.8, anchor='start',
               layer='texto-suave')
        v.text((-0.52, 5.66), 'LOSA ALIGERADA h=0,30', h=1.8, anchor='start',
               layer='texto-suave')
        v.text((-0.52, 6.26), 'N.P.T. +6,20 · PENDIENTE 2 %', h=1.8, anchor='start',
               layer='texto-suave')
        v.text((0.30, 7.34), 'REMATE +7,15', h=1.9, anchor='middle')
    dim_v(v, 0.375, 6.20, 7.15, off=13.0, size=1.9, txt='0,95')
    dim_v(v, 0.375, 7.15, 7.20, off=-9.0, size=1.7, txt='0,05')
    dim_h(v, 0.125, 0.375, 6.20, off=-9.0, size=1.8, txt='0,25')
    dim_v(v, -0.55, 5.85, 6.15, off=-9.0, size=1.8, txt='0,30')


def detalle_escalera(v, con_textos=True):
    """Detalle 3: escalera de 2 tramos (E 1:25). 9 C/H por tramo."""
    tread, riser, n = 0.28, 0.181, 9
    z = 0.0
    perfil = [(0.0, 0.0)]
    u = 0.0
    for k in range(1, n + 1):
        z = k * riser
        perfil.append((u, z))
        u = k * tread
        perfil.append((u, z))
    v.polyline(perfil, layer='marco-medio')
    # losa inclinada del tramo
    v.polyline([(0.0, -0.20), (u, z - 0.20), (u, z), (0.0, 0.0)], close=True,
               layer='marco-fino')
    v.hatch([(0.0, -0.20), (u, z - 0.20), (u, z), (0.0, 0.0)], angle=-45,
            spacing=0.14, layer='hatch')
    # descanso
    v.fill([(u, z - 0.20), (u + 1.46, z - 0.20), (u + 1.46, z), (u, z)],
           layer='hormigon')
    v.polyline([(u, z - 0.20), (u + 1.46, z - 0.20), (u + 1.46, z), (u, z)],
               close=True, layer='muro-corte')
    # viga de descanso y muro
    v.fill([(u + 1.46, z - 0.60), (u + 1.71, z - 0.60), (u + 1.71, z),
            (u + 1.46, z)], layer='muro-fill')
    v.polyline([(u + 1.46, z - 0.60), (u + 1.71, z - 0.60), (u + 1.71, z),
                (u + 1.46, z)], close=True, layer='muro-corte')
    # segundo tramo (sube en sentido contrario, se indica con trazo discontinuo)
    v.polyline([(u + 1.46, z), (u + 1.46, z + 1.63)], layer='proyeccion')
    v.line((u + 1.46, z + 1.63), (u, z + 1.63), layer='proyeccion')
    v.text((u + 0.75, z + 1.75), 'TRAMO 2  ·  SUBE A +3,25', h=1.9, anchor='middle',
           layer='texto-suave')
    if con_textos:
        v.text((0.10, -0.45), 'N.P.T. ±0,00', h=1.9, layer='texto-suave')
        v.text((u + 0.60, z - 0.42), 'DESCANSO +1,63', h=1.9, anchor='middle',
               layer='texto-suave')
        v.text((u * 0.55, 1.85), 'PASAMANOS h=0,90', h=1.8, anchor='middle',
               layer='texto-suave')
        v.text((u * 0.55, 1.62), '18 C/H DE 0,181 m · HUELLA 0,28 m', h=1.8,
               anchor='middle', layer='texto-suave')
    # acotado de huellas y contras
    for k in range(n):
        v.line((k * tread, -0.28), (k * tread, -0.38), layer='cota')
    v.line((0.0, -0.34), (u, -0.34), layer='cota')
    v.text((u / 2, -0.52), '9 × 0,28 = 2,52', h=1.8, anchor='middle',
           layer='cota-texto')
    dim_v(v, 0.0, 0.0, z, off=-14.0, size=1.9, txt='1,63')
    dim_v(v, u + 1.46, z, z + 1.63, off=14.0, size=1.8, txt='1,63')

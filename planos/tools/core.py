# -*- coding: utf-8 -*-
"""
core.py — Motor de dibujo técnico (display-list + renderizadores)
Proyecto: JMDSI — Bloque Dormitorios (Planos de arquitectura / ingeniería civil)

Coordenadas:
  * MODELO : metros, X hacia el Este, Y hacia el Norte (1:1 real).
  * LÁMINA : milímetros de papel, origen ARRIBA-IZQUIERDA, y hacia abajo.

Renderizadores: SVG (nativo), PDF (reportlab), PNG (PIL), DXF (ezdxf).
"""
import math
import os

MM2PT = 72.0 / 25.4
FONT_R = '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'
FONT_B = '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'

# ----------------------------------------------------------------------------
# Capas: color de trazo, espesor (mm de papel), tipo de línea, color de relleno
# ----------------------------------------------------------------------------
LAYERS = {
    'eje':          dict(c='#8a8a8a', w=0.13, dash=(8, 2, 1.5, 2), f=None),
    'muro-corte':   dict(c='#000000', w=0.60, f=None),
    'muro-fill':    dict(c='#000000', w=0.25, f='#3d3d3d'),
    'muro-visto':   dict(c='#000000', w=0.35, f=None),
    'tabique-fill': dict(c='#000000', w=0.30, f='#5a5a5a'),
    'hueco':        dict(c='#000000', w=0.25, f=None),
    'carpinteria':  dict(c='#14456e', w=0.25, f=None),
    'vidrio':       dict(c='#3b7fb0', w=0.18, f='#dceaf5'),
    'mobiliario':   dict(c='#8f8f8f', w=0.18, f=None),
    'sanitario':    dict(c='#8f8f8f', w=0.20, f=None),
    'texto':        dict(c='#101010', w=0.0, f=None),
    'texto-suave':  dict(c='#5c5c5c', w=0.0, f=None),
    'cota':         dict(c='#333333', w=0.13, f=None),
    'cota-texto':   dict(c='#1a1a1a', w=0.0, f=None),
    'nivel':        dict(c='#101010', w=0.20, f='#101010'),
    'terreno':      dict(c='#7a5230', w=0.35, f=None),
    'hormigon':     dict(c='#000000', w=0.30, f='#bcbcbc'),
    'hatch':        dict(c='#a0a0a0', w=0.10, f=None),
    'hatch-2':      dict(c='#c8c8c8', w=0.10, f=None),
    'marco':        dict(c='#000000', w=0.70, f=None),
    'marco-fino':   dict(c='#000000', w=0.25, f=None),
    'marco-medio':  dict(c='#000000', w=0.40, f=None),
    'sombra':       dict(c='#dcdcdc', w=0.0, f='#ededed'),
    'vegetal':      dict(c='#3c7a4a', w=0.20, f='#dcecdc'),
    'arbol':        dict(c='#3c7a4a', w=0.18, f='#cfe6cf'),
    'agua':         dict(c='#2f6f9f', w=0.20, f='#d8e9f5'),
    'via':          dict(c='#6b6b6b', w=0.20, f='#efefef'),
    'edificio':     dict(c='#555555', w=0.25, f='#e4e4e4'),
    'destacado':    dict(c='#b02a2a', w=0.45, f='#f5d6d6'),
    'azul':         dict(c='#14456e', w=0.25, f='#dbe7f1'),
    'cubierta':     dict(c='#8a6d1f', w=0.25, f='#f4e9cd'),
    'proyeccion':   dict(c='#8a8a8a', w=0.15, dash=(3, 1.5), f=None),
    'fondo':        dict(c='#ffffff', w=0.0, f='#ffffff'),
}

# Tema "blueprint" (cianotipo): fondo azul profundo, trazos claros
THEME = {
    'blueprint': dict(
        bg='#08243d',
        map={
            '#000000': '#dbe9ff', '#101010': '#eaf3ff', '#1a1a1a': '#dbe9ff',
            '#333333': '#8fc0e8', '#5c5c5c': '#8fb7d8', '#8a8a8a': '#6f9dc4',
            '#8f8f8f': '#8fb7d8', '#a0a0a0': '#5f8dae', '#c8c8c8': '#4d7898',
            '#3d3d3d': '#9ec9ee', '#5a5a5a': '#9ec9ee', '#bcbcbc': '#7fb0d6',
            '#14456e': '#a8dcff', '#3b7fb0': '#8fd0ff', '#dceaf5': '#123c5e',
            '#7a5230': '#7fb0d6', '#3c7a4a': '#8fd39a', '#dcecdc': '#0d3050',
            '#cfe6cf': '#0d3050', '#2f6f9f': '#7fc4ff', '#d8e9f5': '#0f3557',
            '#6b6b6b': '#8fb7d8', '#efefef': '#0c2f4d', '#555555': '#a9cdea',
            '#e4e4e4': '#0c2f4d', '#b02a2a': '#ff9b7a', '#f5d6d6': '#1d5c8a',
            '#8a6d1f': '#e8c46a', '#f4e9cd': '#123a5c', '#ededed': '#0c2f4d',
            '#dcdcdc': '#0c2f4d', '#ffffff': '#08243d',
            '#101010-fill': '#eaf3ff',
        },
    ),
    'plano': dict(bg='#ffffff', map={}),
}


def col(hexcolor, theme='plano'):
    if hexcolor is None:
        return None
    m = THEME[theme]['map']
    return m.get(hexcolor.lower(), hexcolor)


def fmt(x, dec=2):
    """Formato español: 3,60 / 24,00"""
    s = ('%.' + str(dec) + 'f') % (x + 0.0)
    if s.startswith('-'):
        s = '-' + s[1:]
    return s.replace('.', ',')


def fmt_cm(x):
    """3,60 m -> 3,60 (2 dec) ; para niveles +3,05"""
    return fmt(x, 2)


def nivel_txt(z):
    if abs(z) < 1e-9:
        return '±0,00'
    return ('+' if z > 0 else '-') + fmt(abs(z), 2)


# ----------------------------------------------------------------------------
# Hoja (lámina) y Vistas
# ----------------------------------------------------------------------------
class Sheet:
    def __init__(self, w=841.0, h=594.0, codigo='', titulo='', escala='', tema='plano'):
        self.w, self.h = float(w), float(h)
        self.items = []
        self.codigo = codigo
        self.titulo = titulo
        self.escala = escala
        self.tema = tema

    # ---- primitivas en mm de papel (sin vista) ---------------------------
    def add(self, it):
        it.setdefault('view', None)
        self.items.append(it)

    def line(self, a, b, layer='marco-fino', view=None):
        self.add(dict(k='line', a=a, b=b, layer=layer, view=view))

    def polyline(self, pts, layer='marco-fino', close=False, view=None):
        pts = list(pts)
        if len(pts) > 1:
            self.add(dict(k='poly', pts=pts, layer=layer, close=close, view=view))

    def fill(self, pts, layer='muro-fill', view=None):
        pts = list(pts)
        if len(pts) > 2:
            self.add(dict(k='fill', pts=pts, layer=layer, view=view))

    def circle(self, c, r, layer='marco-fino', fill=False, view=None):
        self.add(dict(k='circle', c=c, r=r, layer=layer, fill=fill, view=view))

    def rect(self, x0, y0, x1, y1, layer='marco-fino', fill=False, view=None):
        if fill:
            self.fill([(x0, y0), (x1, y0), (x1, y1), (x0, y1)], layer=layer)
        else:
            self.polyline([(x0, y0), (x1, y0), (x1, y1), (x0, y1)], layer=layer, close=True)

    def rect_c(self, c, w, h, layer='marco-fino', fill=False, view=None):
        self.rect(c[0] - w / 2, c[1] - h / 2, c[0] + w / 2, c[1] + h / 2, layer=layer, fill=fill)

    def text(self, p, s, h=2.5, layer='texto', anchor='start', rot=0.0, bold=False,
             view=None):
        self.add(dict(k='text', p=p, s=s, h=h, layer=layer, anchor=anchor, rot=rot,
                      bold=bold, view=view))

    def hatch(self, pts, angle=45.0, spacing=3.0, layer='hatch', view=None):
        for a, b in hatch_lines(pts, angle, spacing):
            self.line(a, b, layer)


class View:
    """Ventana de dibujo: transforma MODELO (m) -> LÁMINA (mm)."""

    def __init__(self, sheet, x0, y0, denom=50, ox=0.0, oy=0.0, nombre=''):
        self.sheet = sheet
        self.x0, self.y0 = float(x0), float(y0)
        self.denom = float(denom)
        self.s = 1000.0 / self.denom          # mm de papel por metro
        self.ox, self.oy = float(ox), float(oy)
        self.nombre = nombre
        self.x1 = None
        self.y1 = None

    # transformaciones
    def X(self, mx):
        return self.x0 + (mx - self.ox) * self.s

    def Y(self, my):
        return self.y0 - (my - self.oy) * self.s

    def P(self, p):
        return (self.X(p[0]), self.Y(p[1]))

    def L(self, ml):
        return ml * self.s

    def inv(self, p):
        """LÁMINA (mm) -> MODELO (m)."""
        return ((p[0] - self.x0) / self.s + self.ox,
                self.oy - (p[1] - self.y0) / self.s)

    def bounds(self, x0, y0, x1, y1):
        self.x0 = self.X(x0)
        self.y0 = self.Y(y1)
        self.x1 = self.X(x1)
        self.y1 = self.Y(y0)
        return (self.x0, self.y0, self.x1, self.y1)

    # primitivas en coordenadas de modelo
    def line(self, a, b, layer='marco-fino', **kw):
        self.sheet.add(dict(k='line', a=self.P(a), b=self.P(b), layer=layer, view=self))

    def polyline(self, pts, layer='marco-fino', close=False, **kw):
        pts = [self.P(p) for p in pts]
        if len(pts) > 1:
            self.sheet.add(dict(k='poly', pts=pts, layer=layer, close=close,
                                view=self))

    def fill(self, pts, layer='muro-fill', **kw):
        self.sheet.add(dict(k='fill', pts=[self.P(p) for p in pts], layer=layer, view=self))

    def rect(self, x0, y0, x1, y1, layer='marco-fino', fill=False, **kw):
        pts = [(x0, y0), (x1, y0), (x1, y1), (x0, y1)]
        (self.fill if fill else self.polyline)(pts, layer=layer, close=True)

    def rectf(self, x0, y0, x1, y1, layer='muro-fill', **kw):
        self.fill([(x0, y0), (x1, y0), (x1, y1), (x0, y1)], layer=layer)

    def circle(self, c, r, layer='marco-fino', fill=False, **kw):
        self.sheet.add(dict(k='circle', c=self.P(c), r=self.L(r), layer=layer, fill=fill,
                            view=self))

    def arc(self, c, r, a0, a1, layer='marco-fino', n=24, **kw):
        pts = []
        for i in range(n + 1):
            a = math.radians(a0 + (a1 - a0) * i / n)
            pts.append((c[0] + r * math.cos(a), c[1] + r * math.sin(a)))
        self.polyline(pts, layer=layer)

    def hatch(self, pts, angle=45.0, spacing_m=0.4, layer='hatch', **kw):
        """Sombreado en coordenadas de modelo (spacing en metros)."""
        for a, b in hatch_lines(pts, angle, spacing_m):
            self.line(a, b, layer)

    def text(self, p, s, h=2.5, layer='texto', anchor='start', rot=0.0, bold=False,
             **kw):
        """p en MODELO; h en mm de papel."""
        self.sheet.add(dict(k='text', p=self.P(p), s=s, h=h, layer=layer,
                            anchor=anchor, rot=rot, bold=bold, view=self))

    def text_sheet(self, pm, s, h=2.5, layer='texto', anchor='start', rot=0.0,
                   bold=False, **kw):
        """Texto colocado en coordenadas de MODELO pero SIN escalar tamaño."""
        self.sheet.add(dict(k='text', p=self.P(pm), s=s, h=h, layer=layer,
                            anchor=anchor, rot=rot, bold=bold, view=self))


# ----------------------------------------------------------------------------
# Sombreados
# ----------------------------------------------------------------------------
def hatch_lines(pts, angle=45.0, spacing=3.0):
    """Segmentos de sombreado (en el mismo espacio que pts) a `angle` grados."""
    if len(pts) < 3:
        return []
    a = math.radians(angle)
    ca, sa = math.cos(a), math.sin(a)
    # rotación -a para llevar el rayado a líneas horizontales
    rp = [(x * ca + y * sa, -x * sa + y * ca) for x, y in pts]
    ys = [p[1] for p in rp]
    y0, y1 = min(ys), max(ys)
    segs = []
    n = int((y1 - y0) / spacing) + 1
    for i in range(n + 1):
        yy = y0 + i * spacing
        xs = []
        m = len(rp)
        for j in range(m):
            x1, y1_ = rp[j]
            x2, y2_ = rp[(j + 1) % m]
            if (y1_ - yy) * (y2_ - yy) < 0:
                t = (yy - y1_) / (y2_ - y1_)
                xs.append(x1 + t * (x2 - x1))
        xs.sort()
        for j in range(0, len(xs) - 1, 2):
            if xs[j + 1] - xs[j] < 1e-9:
                continue
            # rotación inversa (+a) al sistema original
            p1 = (xs[j] * ca - yy * sa, xs[j] * sa + yy * ca)
            p2 = (xs[j + 1] * ca - yy * sa, xs[j + 1] * sa + yy * ca)
            segs.append((p1, p2))
    return segs


# ----------------------------------------------------------------------------
# Acotación
# ----------------------------------------------------------------------------
def dim_h(v, x1, x2, y, off=8.0, txt=None, size=2.2, layer='cota', dec=2,
          ticks=True, over=1.5):
    """Cota horizontal (dirección X del modelo) a `off` mm por debajo."""
    ya = v.Y(y) + off
    pa, pb = v.X(x1), v.X(x2)
    v.sheet.line((pa, v.Y(y) + 1.5), (pa, ya + over), layer='cota')
    v.sheet.line((pb, v.Y(y) + 1.5), (pb, ya + over), layer='cota')
    v.sheet.line((pa, ya), (pb, ya), layer=layer)
    if ticks:
        _tick(v.sheet, (pa, ya), 'v', layer)
        _tick(v.sheet, (pb, ya), 'v', layer)
    s = txt if txt is not None else fmt(abs(x2 - x1), dec)
    v.sheet.text(((pa + pb) / 2.0, ya - 1.1), s, h=size, layer='cota-texto',
                 anchor='middle')


def dim_v(v, x, y1, y2, off=8.0, txt=None, size=2.2, layer='cota', dec=2,
          ticks=True, over=1.5):
    """Cota vertical (dirección Y del modelo) a `off` mm a la derecha."""
    xa = v.X(x) + off
    pa, pb = v.Y(y1), v.Y(y2)
    v.sheet.line((v.X(x) - 1.5, pa), (xa - over, pa), layer='cota')
    v.sheet.line((v.X(x) - 1.5, pb), (xa - over, pb), layer='cota')
    v.sheet.line((xa, pa), (xa, pb), layer=layer)
    if ticks:
        _tick(v.sheet, (xa, pa), 'h', layer)
        _tick(v.sheet, (xa, pb), 'h', layer)
    s = txt if txt is not None else fmt(abs(y2 - y1), dec)
    v.sheet.text((xa - 1.1, (pa + pb) / 2.0), s, h=size, layer='cota-texto',
                 anchor='middle', rot=90)


def dim_chain_h(v, xs, y, off=8.0, size=2.2, dec=2, texts=None, layer='cota'):
    for i in range(len(xs) - 1):
        t = texts[i] if texts else None
        dim_h(v, xs[i], xs[i + 1], y, off=off, size=size, dec=dec, txt=t, layer=layer)


def dim_chain_v(v, ys, x, off=8.0, size=2.2, dec=2, texts=None, layer='cota'):
    for i in range(len(ys) - 1):
        t = texts[i] if texts else None
        dim_v(v, x, ys[i], ys[i + 1], off=off, size=size, dec=dec, txt=t, layer=layer)


def _tick(sheet, p, orient, layer):
    """Marca de cota tipo barra oblicua (arquitectónica)."""
    d = 1.5
    if orient == 'v':          # sobre línea horizontal
        sheet.line((p[0] - d, p[1] + d), (p[0] + d, p[1] - d), layer=layer)
    else:                      # sobre línea vertical
        sheet.line((p[0] - d, p[1] - d), (p[0] + d, p[1] + d), layer=layer)


def dim_hs(v, x1, x2, y, off=8.0, size=2.2, dec=2, txt=None):
    """Cota de nivel/zona por encima del dibujo (igual que dim_h pero hacia arriba)."""
    ya = v.Y(y) - off
    pa, pb = v.X(x1), v.X(x2)
    v.sheet.line((pa, v.Y(y) - 1.5), (pa, ya - 1.5), layer='cota')
    v.sheet.line((pb, v.Y(y) - 1.5), (pb, ya - 1.5), layer='cota')
    v.sheet.line((pa, ya), (pb, ya), layer='cota')
    _tick(v.sheet, (pa, ya), 'v', 'cota')
    _tick(v.sheet, (pb, ya), 'v', 'cota')
    s = txt if txt is not None else fmt(abs(x2 - x1), dec)
    v.sheet.text(((pa + pb) / 2.0, ya - 1.1), s, h=size, layer='cota-texto',
                 anchor='middle')


def cota_nivel(v, z, x, off=0.0, size=2.2, lado='der', txt=None, largo=0.0):
    """Marca de cota de nivel (triángulo) en secciones y alzados.
    x = posición en modelo (m), z = cota (m). off = desplazamiento vertical en mm."""
    px, py = v.X(x), v.Y(z) + off
    h = 3.0
    if lado == 'der':
        v.sheet.line((px, py), (px + 26, py), layer='nivel')
        v.sheet.polyline([(px, py), (px + h * 0.9, py - h * 0.55),
                          (px + h * 0.9, py + h * 0.55)], close=True, layer='nivel')
        v.sheet.fill([(px, py), (px + h * 0.9, py - h * 0.55),
                      (px + h * 0.9, py + h * 0.55)], layer='nivel')
        v.sheet.text((px + 4.5, py - 1.2), (txt if txt else nivel_txt(z)), h=size,
                     layer='texto', anchor='start')
    else:
        v.sheet.line((px, py), (px - 30, py), layer='nivel')
        v.sheet.polyline([(px, py), (px - h * 0.9, py - h * 0.55),
                          (px - h * 0.9, py + h * 0.55)], close=True, layer='nivel')
        v.sheet.fill([(px, py), (px - h * 0.9, py - h * 0.55),
                      (px - h * 0.9, py + h * 0.55)], layer='nivel')
        v.sheet.text((px - 4.5, py - 1.2), (txt if txt else nivel_txt(z)), h=size,
                     layer='texto', anchor='end')


def globo_eje(sheet, p, txt, r=4.0, layer='marco-medio', size=2.6):
    sheet.circle(p, r, layer=layer)
    sheet.text((p[0], p[1] + 0.95 * 0.5), txt, h=size, layer='texto', anchor='middle')


def leader(sheet, p0, p1, s, h=2.2, layer='texto', anchor='start', rot=0.0,
           size_line=0.13):
    sheet.line(p0, p1, layer='cota')
    dx = 1.5 if p1[0] >= p0[0] else -1.5
    sheet.line((p1[0], p1[1]), (p1[0] + dx, p1[1]), layer='cota')
    px = p1[0] + dx + (1.0 if dx > 0 else -1.0)
    sheet.text((px, p1[1] - 1.0), s, h=h, layer=layer,
               anchor='start' if dx > 0 else 'end')


def leader_m(v, p0, p1, s, h=2.2, layer='texto'):
    """Directriz en coordenadas de modelo."""
    leader(v.sheet, v.P(p0), v.P(p1), s, h=h, layer=layer,
           anchor='start' if p1[0] >= p0[0] else 'end')


# ----------------------------------------------------------------------------
# Elementos de lámina
# ----------------------------------------------------------------------------
def marco_lamina(sheet, margen_izq=25.0, margen=12.0):
    w, h = sheet.w, sheet.h
    sheet.line((margen_izq, margen), (w - margen, margen), 'marco')
    sheet.line((w - margen, margen), (w - margen, h - margen), 'marco')
    sheet.line((w - margen, h - margen), (margen_izq, h - margen), 'marco')
    sheet.line((margen_izq, h - margen), (margen_izq, margen), 'marco')
    # zonas de plegado (marcas)
    for k in range(1, int((w - margen_izq) // 100) + 1):
        x = margen_izq + 100 * k
        if x < w - margen - 4:
            sheet.line((x, margen), (x, margen + 4), 'marco-fino')


def cajetin(sheet, datos, w=190.0, h=62.0, x=None, y=None):
    """Cajetín (rótulo) normalizado en la esquina inferior derecha."""
    if x is None:
        x = sheet.w - 12.0 - w
    if y is None:
        y = sheet.h - 12.0 - h
    S = sheet
    S.fill([(x, y), (x + w, y), (x + w, y + h), (x, y + h)], layer='sombra')
    S.polyline([(x, y), (x + w, y), (x + w, y + h), (x, y + h)], close=True, layer='marco')
    # divisiones
    S.line((x, y + 14), (x + w, y + 14), 'marco-medio')
    S.line((x, y + 22), (x + w, y + 22), 'marco-fino')
    S.line((x, y + 38), (x + w, y + 38), 'marco-fino')
    S.line((x + 108, y + 22), (x + 108, y + h), 'marco-fino')
    S.line((x, y + 52), (x + 108, y + 52), 'marco-fino')
    S.line((x + 60, y + 52), (x + 60, y + h), 'marco-fino')
    S.line((x + 72, y + 52), (x + 72, y + h), 'marco-fino')
    # textos
    S.text((x + 3, y + 5.0), 'JMDSI · INGENIERÍA Y ARQUITECTURA', h=2.9, bold=True)
    S.text((x + 3, y + 11.0), 'Planos de proyecto — Bloque Dormitorios', h=2.2,
           layer='texto-suave')
    S.text((x + w - 3, y + 5.0), 'LÁMINA ' + datos.get('codigo', ''), h=3.2,
           anchor='end', bold=True)
    S.text((x + w - 3, y + 11.0), 'E ' + datos.get('escala', ''), h=2.4,
           anchor='end', layer='texto-suave')

    def campo(xa, ya, rot, k, val, hk=1.9, hv=2.6, bold=False):
        S.text((xa, ya - 1.0), k, h=hk, layer='texto-suave', rot=rot)
        S.text((xa, ya + 3.0), val, h=hv, rot=rot, bold=bold)

    campo(x + 3, y + 40, 0, 'PROYECTO', datos.get('proyecto', ''), hv=2.5)
    campo(x + 3, y + 53, 0, 'CONTENIDO', datos.get('contenido', ''), hv=2.4)
    campo(x + 62, y + 53, 0, 'ESCALA', datos.get('escala', ''), hv=2.4)
    campo(x + 74, y + 53, 0, 'Nº', datos.get('num', ''), hv=2.4)
    campo(x + 110, y + 23, 0, 'FECHA', datos.get('fecha', ''), hv=2.4)
    campo(x + 110, y + 40, 0, 'DIBUJÓ / REVISÓ', datos.get('autor', ''), hv=2.2)
    campo(x + 3, y + 24, 0, 'EMPLAZAMIENTO / PROMOTOR', datos.get('emplazamiento', ''),
          hv=2.1)
    campo(x + 3, y + 15, 0, 'Nº DE HOJA', datos.get('hoja', ''), hv=2.4)
    campo(x + 62, y + 15, 0, 'MODIFICACIÓN', datos.get('rev', 'Emisión inicial'),
          hv=2.1)
    return (x, y, w, h)


def norte(sheet, x, y, r=14.0, txt='N', rot=0.0):
    """Rosa de los vientos simplificada (apunta hacia arriba = Norte)."""
    S = sheet
    a = math.radians(rot)
    def R(p):
        ca, sa = math.cos(a), math.sin(a)
        return (x + p[0] * ca - p[1] * sa, y + p[0] * sa + p[1] * ca)
    S.circle((x, y), r, layer='marco-medio')
    S.fill([R((0, -r * 0.78)), R((-r * 0.26, r * 0.30)), R((0, r * 0.10))], layer='marco-medio')
    S.polyline([R((0, -r * 0.78)), R((r * 0.26, r * 0.30)), R((0, r * 0.10))],
               close=True, layer='marco-medio')
    S.line(R((0, -r * 1.25)), R((0, r * 0.55)), layer='marco-fino')
    S.text(R((0, -r * 1.55)), txt, h=3.4, anchor='middle', bold=True)


def escala_grafica(sheet, x, y, denom, n=5, seg_m=1.0, alto=3.0, size=2.0):
    """Escala gráfica: n segmentos de seg_m metros a escala 1:denom."""
    S = sheet
    mm = seg_m * 1000.0 / denom
    yy = y
    for i in range(n):
        xx = x + i * mm
        pts = [(xx, yy), (xx + mm, yy), (xx + mm, yy + alto), (xx, yy + alto)]
        if i % 2 == 0:
            S.fill(pts, layer='marco-medio')
        else:
            S.fill(pts, layer='sombra')
        S.polyline(pts, close=True, layer='marco-medio')
    S.text((x - 1.5, yy + alto / 2.0 + 0.9), '0', h=size, anchor='end')
    S.text((x + n * mm + 1.5, yy + alto / 2.0 + 0.9), fmt(n * seg_m, 0) + ' m',
           h=size, anchor='start')


def rotulo(sheet, x, y, texto, escala=None, h=4.2, sub=None, ancho=None):
    S = sheet
    S.text((x, y), texto, h=h, bold=True)
    yy = y + 2.6
    if escala:
        S.text((x, yy), escala, h=2.6, layer='texto-suave')
        yy += 1.2
    ancho = ancho if ancho else max(60.0, len(texto) * h * 0.62)
    S.line((x, yy + 1.0), (x + ancho, yy + 1.0), 'marco-medio')
    if sub:
        S.text((x, yy + 4.0), sub, h=2.2, layer='texto-suave')


def cuadro(sheet, x, y, filas, w_cols, h_fila=5.2, h_cab=5.6, size=2.0,
           layer='marco-fino', bold_first=True):
    """Tabla simple: filas[0] = cabecera."""
    S = sheet
    ancho = sum(w_cols)
    yy = y
    for i, fila in enumerate(filas):
        hh = h_cab if i == 0 else h_fila
        S.rect(x, yy, x + ancho, yy + hh, layer=layer, fill=False)
        if i == 0:
            S.fill([(x, yy), (x + ancho, yy), (x + ancho, yy + hh), (x, yy + hh)],
                   layer='sombra')
            S.rect(x, yy, x + ancho, yy + hh, layer=layer, fill=False)
        else:
            S.fill([(x, yy), (x + ancho, yy), (x + ancho, yy + hh), (x, yy + hh)],
                   layer='sombra') if False else None
        xx = x
        for j, celda in enumerate(fila):
            for kk, ln in enumerate(str(celda).split('\n')):
                S.text((xx + w_cols[j] / 2.0, yy + hh / 2.0 + 0.9 + (kk - 0.0) * 3.0),
                       ln, h=size, anchor='middle',
                       bold=(i == 0 or (bold_first and j == 0)))
            xx += w_cols[j]
        for j in range(1, len(w_cols)):
            xx2 = x + sum(w_cols[:j])
            S.line((xx2, yy), (xx2, yy + hh), 'marco-fino')
        yy += hh
    return yy


# ============================================================================
# RENDERIZADORES
# ============================================================================
def _dash_segments(p1, p2, dash):
    """Divide un segmento en trozos según patrón de guiones (mm)."""
    if not dash:
        return [(p1, p2)]
    dx, dy = p2[0] - p1[0], p2[1] - p1[1]
    L = math.hypot(dx, dy)
    if L < 1e-9:
        return []
    ux, uy = dx / L, dy / L
    pat = list(dash) + list(dash)
    out = []
    t, i = 0.0, 0
    while t < L:
        seg = pat[i % len(pat)]
        t2 = min(t + seg, L)
        if i % 2 == 0:
            out.append(((p1[0] + ux * t, p1[1] + uy * t),
                        (p1[0] + ux * t2, p1[1] + uy * t2)))
        t, i = t2, i + 1
    return out


# ---------------------------------------------------------------- SVG -------
def to_svg(sheet):
    th = THEME[sheet.tema]
    out = []
    out.append('<svg xmlns="http://www.w3.org/2000/svg" version="1.1" '
               'width="%.2fmm" height="%.2fmm" viewBox="0 0 %.2f %.2f">'
               % (sheet.w, sheet.h, sheet.w, sheet.h))
    out.append('<rect x="0" y="0" width="%.2f" height="%.2f" fill="%s"/>'
               % (sheet.w, sheet.h, th['bg']))
    out.append('<g stroke-linecap="round" stroke-linejoin="round" '
               'font-family="DejaVu Sans, Helvetica, Arial, sans-serif">')
    for it in sheet.items:
        lay = LAYERS[it['layer']]
        c = col(lay['c'], sheet.tema)
        sw = lay['w']
        if it['k'] == 'line':
            for a, b in _dash_segments(it['a'], it['b'], lay.get('dash')):
                out.append('<line x1="%.3f" y1="%.3f" x2="%.3f" y2="%.3f" '
                           'stroke="%s" stroke-width="%.3f"/>' % (a[0], a[1], b[0], b[1], c, sw))
        elif it['k'] == 'poly':
            pts = ' '.join('%.3f,%.3f' % p for p in it['pts'])
            tag = 'polygon' if it.get('close') else 'polyline'
            out.append('<%s points="%s" fill="none" stroke="%s" stroke-width="%.3f"/>'
                       % (tag, pts, c, sw))
        elif it['k'] == 'fill':
            pts = ' '.join('%.3f,%.3f' % p for p in it['pts'])
            cc = col(lay.get('f') or '#cccccc', sheet.tema)
            out.append('<polygon points="%s" fill="%s" stroke="none"/>' % (pts, cc))
        elif it['k'] == 'circle':
            cc = col(lay.get('f') or '#cccccc', sheet.tema) if it.get('fill') else 'none'
            out.append('<circle cx="%.3f" cy="%.3f" r="%.3f" fill="%s" stroke="%s" '
                       'stroke-width="%.3f"/>' % (it['c'][0], it['c'][1], it['r'], cc, c, sw))
        elif it['k'] == 'text':
            cc = col(lay['c'], sheet.tema)
            tr = ''
            if abs(it.get('rot', 0)) > 1e-6:
                tr = ' transform="rotate(%.2f %.3f %.3f)"' % (-it['rot'], it['p'][0], it['p'][1])
            anc = {'start': 'start', 'middle': 'middle', 'end': 'end'}[it['anchor']]
            fw = 'bold' if it.get('bold') else 'normal'
            fs = it['h'] * 0.76           # em ≈ 1/0.76 de la altura de caja
            out.append('<text x="%.3f" y="%.3f" font-size="%.3f" fill="%s" '
                       'text-anchor="%s" font-weight="%s"%s>%s</text>'
                       % (it['p'][0], it['p'][1], fs, cc, anc, fw, tr, _esc(it['s'])))
    out.append('</g></svg>')
    return '\n'.join(out)


def _esc(s):
    return (str(s).replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;'))


# ---------------------------------------------------------------- PDF -------
def to_pdf(sheet, path, dpi_meta=300):
    from reportlab.pdfgen import canvas as rl_canvas
    from reportlab.lib.colors import HexColor
    from reportlab.pdfbase import pdfmetrics
    from reportlab.pdfbase.ttfonts import TTFont
    try:
        pdfmetrics.registerFont(TTFont('DJV', FONT_R))
        pdfmetrics.registerFont(TTFont('DJV-B', FONT_B))
        fr, fb = 'DJV', 'DJV-B'
    except Exception:
        fr = fb = 'Helvetica'
    th = THEME[sheet.tema]
    c = rl_canvas.Canvas(path, pagesize=(sheet.w * MM2PT, sheet.h * MM2PT))
    c.setTitle(sheet.titulo or sheet.codigo)
    c.setAuthor('JMDSI')
    c.setCreator('JMDSI · generador de planos')
    H = sheet.h

    def XY(p):
        return (p[0] * MM2PT, (H - p[1]) * MM2PT)

    c.setFillColor(HexColor(th['bg']))
    c.rect(0, 0, sheet.w * MM2PT, sheet.h * MM2PT, stroke=0, fill=1)
    for it in sheet.items:
        lay = LAYERS[it['layer']]
        cc = col(lay['c'], sheet.tema)
        c.setStrokeColor(HexColor(cc))
        c.setFillColor(HexColor(cc))
        c.setLineWidth(max(lay['w'], 0.05) * MM2PT)
        c.setDash([x * MM2PT for x in lay['dash']] if lay.get('dash') else [])
        c.setLineCap(1)
        c.setLineJoin(1)
        if it['k'] == 'line':
            for a, b in _dash_segments(it['a'], it['b'], lay.get('dash')):
                c.line(*XY(a), *XY(b))
        elif it['k'] == 'poly':
            pts = [XY(p) for p in it['pts']]
            path_obj = c.beginPath()
            path_obj.moveTo(*pts[0])
            for p in pts[1:]:
                path_obj.lineTo(*p)
            if it.get('close'):
                path_obj.close()
            c.drawPath(path_obj, stroke=1, fill=0)
        elif it['k'] == 'fill':
            c.setFillColor(HexColor(col(lay.get('f') or '#cccccc', sheet.tema)))
            c.setStrokeColor(HexColor(col(lay.get('f') or '#cccccc', sheet.tema)))
            pts = [XY(p) for p in it['pts']]
            path_obj = c.beginPath()
            path_obj.moveTo(*pts[0])
            for p in pts[1:]:
                path_obj.lineTo(*p)
            path_obj.close()
            c.drawPath(path_obj, stroke=1, fill=1)
        elif it['k'] == 'circle':
            px, py = XY(it['c'])
            c.circle(px, py, it['r'] * MM2PT, stroke=1, fill=0)
            if it.get('fill'):
                c.setFillColor(HexColor(col(lay.get('f') or '#cccccc', sheet.tema)))
                c.circle(px, py, it['r'] * MM2PT, stroke=0, fill=1)
        elif it['k'] == 'text':
            fnt = fb if it.get('bold') else fr
            c.setFont(fnt, it['h'] * 0.76 * MM2PT)     # em = 1/0.76 * altura caja
            c.setFillColor(HexColor(col(lay['c'], sheet.tema)))
            px, py = XY(it['p'])
            c.saveState()
            c.translate(px, py)
            if abs(it.get('rot', 0)) > 1e-6:
                c.rotate(it['rot'])
            if it['anchor'] == 'middle':
                c.drawCentredString(0, 0, it['s'])
            elif it['anchor'] == 'end':
                c.drawRightString(0, 0, it['s'])
            else:
                c.drawString(0, 0, it['s'])
            c.restoreState()
    c.showPage()
    c.save()


# ---------------------------------------------------------------- PNG -------
def to_png(sheet, path, dpi=150):
    from PIL import Image, ImageDraw, ImageFont
    k = dpi / 25.4
    W, H = int(round(sheet.w * k)), int(round(sheet.h * k))
    img = Image.new('RGB', (W, H), THEME[sheet.tema]['bg'])
    d = ImageDraw.Draw(img)
    fonts = {}

    def getf(h, bold):
        key = (round(h, 2), bold)
        if key not in fonts:
            px = max(4, int(round(h * 0.76 * k)))
            fonts[key] = ImageFont.truetype(FONT_B if bold else FONT_R, px)
        return fonts[key]

    def TP(p):
        return (p[0] * k, p[1] * k)

    for it in sheet.items:
        lay = LAYERS[it['layer']]
        c = col(lay['c'], sheet.tema)
        lw = max(1, int(round(max(lay['w'], 0.12) * k)))
        if it['k'] == 'line':
            for a, b in _dash_segments(it['a'], it['b'], lay.get('dash')):
                d.line([TP(a), TP(b)], fill=c, width=lw)
        elif it['k'] == 'poly':
            pts = [TP(p) for p in it['pts']]
            if it.get('close'):
                d.line(pts + [pts[0]], fill=c, width=lw, joint='curve')
            else:
                d.line(pts, fill=c, width=lw, joint='curve')
        elif it['k'] == 'fill':
            pts = [TP(p) for p in it['pts']]
            d.polygon(pts, fill=col(lay.get('f') or '#cccccc', sheet.tema))
        elif it['k'] == 'circle':
            cx, cy = TP(it['c'])
            r = it['r'] * k
            d.ellipse([cx - r, cy - r, cx + r, cy + r], outline=c, width=lw)
            if it.get('fill'):
                d.ellipse([cx - r, cy - r, cx + r, cy + r],
                          fill=col(lay.get('f') or '#cccccc', sheet.tema))
        elif it['k'] == 'text':
            f = getf(it['h'], it.get('bold'))
            anc = {'start': 'l', 'middle': 'm', 'end': 'r'}[it['anchor']]
            rot = it.get('rot', 0.0)
            if abs(rot) < 1e-6:
                d.text(TP(it['p']), it['s'], font=f, fill=col(lay['c'], sheet.tema),
                       anchor=anc + 's')
            else:
                # texto rotado: render horizontal + rotación de mapa de bits
                pad = max(3, int(2 * k))
                tw = int(d.textlength(it['s'], font=f)) + 2 * pad
                th_ = int(it['h'] * 0.76 * k) + 2 * pad
                tmp = Image.new('RGBA', (tw, th_), (0, 0, 0, 0))
                ImageDraw.Draw(tmp).text((pad, th_ - pad), it['s'], font=f,
                                         fill=col(lay['c'], sheet.tema), anchor='ls')
                rimg = tmp.rotate(rot, expand=True, resample=Image.BICUBIC)
                # punto de anclaje en el bitmap sin rotar (centro de la línea base)
                axf = {'l': 0.0, 'm': 0.5, 'r': 1.0}[anc]
                bx = pad + axf * (tw - 2 * pad)
                by = th_ - pad
                thr = math.radians(rot)
                dxp = bx - tw / 2.0
                dyp = by - th_ / 2.0
                mx = rimg.width / 2.0 + (dxp * math.cos(thr) + dyp * math.sin(thr))
                my = rimg.height / 2.0 + (-dxp * math.sin(thr) + dyp * math.cos(thr))
                px, py = TP(it['p'])
                ox, oy = int(round(px - mx)), int(round(py - my))
                img.paste(rimg, (ox, oy), rimg)
    img.save(path)


# ---------------------------------------------------------------- DXF -------
def to_dxf(sheet, path, escala_lamina=50, dxf_version='R2010'):
    """DXF a 1:1 (metros) deshaciendo la escala de cada vista.
    El membrete/marco se sitúa como si estuviera a 1:escala_lamina."""
    import ezdxf
    doc = ezdxf.new(dxf_version, setup=True)
    doc.header['$INSUNITS'] = 6          # metros
    doc.header['$LUNITS'] = 2
    msp = doc.modelspace()
    VALID_LW = [5, 9, 13, 15, 18, 20, 25, 30, 35, 40, 50, 53, 60, 70, 80, 90,
                100, 106, 120, 140, 158, 200, 211]

    def lw(mm):
        v = max(mm, 0.05) * 100.0
        return min(VALID_LW, key=lambda x: abs(x - v))

    for name, lay in LAYERS.items():
        if name not in doc.layers:
            doc.layers.add(name=name, color=7, lineweight=lw(lay['w']),
                           linetype='CONTINUOUS')
    # DXF no soporta grosores <0,05 mm ni tramas: los rellenos -> rayado 45º
    def inv_of(it, escala):
        v = it.get('view')
        if v is not None:
            return v.inv, v.denom
        f = escala_lamina / 1000.0
        return (lambda p: (p[0] * f, -p[1] * f)), escala_lamina

    for it in sheet.items:
        inv, den = inv_of(it, escala_lamina)
        lay = it['layer']
        if it['k'] == 'line':
            msp.add_line(inv(it['a']), inv(it['b']), dxfattribs={'layer': lay})
        elif it['k'] == 'poly':
            pts = [inv(p) for p in it['pts']]
            if it.get('close'):
                msp.add_lwpolyline(pts, close=True, dxfattribs={'layer': lay})
            else:
                msp.add_lwpolyline(pts, dxfattribs={'layer': lay})
        elif it['k'] == 'fill':
            pts = [inv(p) for p in it['pts']]
            msp.add_lwpolyline(pts, close=True, dxfattribs={'layer': lay})
            sp = 2.0 * den / 1000.0
            for a, b in hatch_lines(pts, 45.0, max(sp, 0.02)):
                msp.add_line(a, b, dxfattribs={'layer': 'hatch'})
        elif it['k'] == 'circle':
            msp.add_circle(inv(it['c']), it['r'] * den / 1000.0,
                           dxfattribs={'layer': lay})
        elif it['k'] == 'text':
            h = it['h'] * den / 1000.0
            p = inv(it['p'])
            rot = it.get('rot', 0.0)
            align = {'start': 'LEFT', 'middle': 'CENTER', 'end': 'RIGHT'}[it['anchor']]
            t = msp.add_text(it['s'], height=h,
                             dxfattribs={'layer': lay, 'style': 'Standard'})
            t.dxf.insert = p
            t.dxf.rotation = rot
            t.dxf.halign = {'LEFT': 0, 'CENTER': 1, 'RIGHT': 2}[align]
            t.dxf.valign = 0
            if it['anchor'] == 'middle':
                t.dxf.align_point = (p[0], p[1])
    doc.saveas(path)
    return path


# ---------------------------------------------------------------- Salida ----
def emitir(sheet, outdir, base, dpi=150, dxf=True, escala_dxf=50):
    os.makedirs(outdir, exist_ok=True)
    p_svg = os.path.join(outdir, base + '.svg')
    with open(p_svg, 'w', encoding='utf-8') as f:
        f.write(to_svg(sheet))
    p_pdf = os.path.join(outdir, base + '.pdf')
    to_pdf(sheet, p_pdf)
    p_png = os.path.join(outdir, base + '.png')
    to_png(sheet, p_png, dpi=dpi)
    p_dxf = None
    if dxf:
        p_dxf = os.path.join(outdir, base + '.dxf')
        try:
            to_dxf(sheet, p_dxf, escala_lamina=escala_dxf)
        except Exception as e:      # noqa
            p_dxf = None
            print('   ! DXF no generado:', e)
    return dict(pdf=p_pdf, svg=p_svg, png=p_png, dxf=p_dxf)

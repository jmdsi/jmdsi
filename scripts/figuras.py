#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
F4 · Generación de figuras G-01…G-15 y láminas P-0…P-9 del Proyecto 04 (UMC2030-P04-TOBSHM-R02).
Estilo institucional UMC; todas las láminas llevan cajetín con código, escala, NPT, revisión,
fecha y sello «NO APTO PARA CONSTRUCCIÓN».
Salida: build/fig/*.png  y  build/laminas/*.png  (300 dpi).
"""
import math
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyArrow, Polygon, Circle, Wedge
from matplotlib.lines import Line2D

AZUL = "#0b3c5d"; ACERO = "#1d5b7a"; ROJO = "#a4262c"; OCRE = "#b07d2b"
GRIS = "#7d8b95"; VERDE = "#2e6f4e"; FONDO = "#ffffff"
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 8,
                     "axes.edgecolor": GRIS, "axes.linewidth": .7})

FIG = "build/fig/"; LAM = "build/laminas/"


def guardar(fig, path):
    """PNG 300 dpi siempre; SVG adicional para las figuras G (E4)."""
    fig.savefig(path)
    base = os.path.basename(path)
    if base.startswith("G-"):
        fig.savefig(os.path.splitext(path)[0] + ".svg")
    plt.close(fig)
FECHA = "17-OCT-2026"; REV = "R02"; COD = "UMC2030-P04-TOBSHM-R02"
SELLO = "INGENIERÍA BÁSICA / ANTEPROYECTO — NO APTO PARA CONSTRUCCIÓN"

# ----------------------------------------------------------------------------- utilidades
def nuevo(titulo, sub, w=11.0, h=7.0):
    fig, ax = plt.subplots(figsize=(w, h), dpi=300)
    ax.set_axis_off()
    fig.subplots_adjust(left=.04, right=.96, top=.86, bottom=.10)
    fig.text(.04, .965, titulo, fontsize=12.5, color=AZUL, weight="bold", va="top")
    fig.text(.04, .925, sub, fontsize=8.4, color="#33475a", va="top")
    fig.text(.96, .965, COD, fontsize=7.5, color=ROJO, ha="right", va="top", weight="bold")
    return fig, ax


def cajetin(fig, codigo, denom, escala, npt="—", extra=""):
    """Cajetín inferior con sello obligatorio."""
    fig.text(.04, .045, f"{codigo}   ·   {denom}", fontsize=8.6, color=AZUL, weight="bold")
    fig.text(.04, .016, (f"Escala {escala}   ·   NPT {npt}   ·   Rev. {REV}   ·   {FECHA}   ·   "
                         f"Sistema WGS84 / EPSG:4326 (trabajo UTM 19N)"), fontsize=7.2, color="#33475a")
    fig.text(.96, .045, SELLO, fontsize=7.4, color=ROJO, ha="right", weight="bold")
    if extra:
        fig.text(.96, .016, extra, fontsize=7.0, color="#33475a", ha="right")
    fig.patches.append(Rectangle((.02, .005), .96, .075, transform=fig.transFigure,
                                 fill=False, edgecolor=AZUL, lw=.9))


def txt(ax, x, y, s, **kw):
    kw.setdefault("fontsize", 7.2); kw.setdefault("color", "#12212b")
    kw.setdefault("ha", "left"); kw.setdefault("va", "center")
    return ax.text(x, y, s, **kw)


def tabla(fig, rows, x=.05, y=.55, w=.9, colw=None, fs=7.4, head=True):
    """Tabla de texto sobre la figura (sin axes)."""
    n = len(rows); colw = colw or [1.0 / len(rows[0])] * len(rows[0])
    rh = .032
    for i, r in enumerate(rows):
        yy = y - i * rh
        cx = x
        for j, c in enumerate(r):
            wd = colw[j] * w
            if head and i == 0:
                fig.patches.append(Rectangle((cx, yy - rh * .8), wd, rh * .95,
                                             transform=fig.transFigure, facecolor=AZUL,
                                             edgecolor=AZUL, lw=.4))
                fig.text(cx + .004, yy - rh * .32, c, fontsize=fs, color="white",
                         weight="bold", va="center")
            else:
                if i % 2 == 0:
                    fig.patches.append(Rectangle((cx, yy - rh * .8), wd, rh * .95,
                                                 transform=fig.transFigure, facecolor="#eef2f5",
                                                 edgecolor="#c9d4dc", lw=.3))
                fig.text(cx + .004, yy - rh * .32, str(c), fontsize=fs, color="#12212b", va="center")
            cx += wd
    return y - n * rh


# ----------------------------------------------------------------------------- G-01 implantación
def g01():
    fig, ax = nuevo("G-01 · Implantación general del Área Cultural (sector Proa–Babor)",
                    "Torre de Observación / Puente de Mando · Sala Técnica de Investigación "
                    "Hidrometeorológica · Aula Magna-Auditorio · Plaza de Honor. Escala 1:400.")
    # aula magna (auditorio)
    ax.add_patch(Rectangle((1.0, 1.0), 9.0, 5.0, fc="#dfe8ee", ec=ACERO, lw=1.4))
    txt(ax, 5.5, 3.5, "AULA MAGNA /\nAUDITORIO (F1)", ha="center", fontsize=8, color=AZUL, weight="bold")
    # torre
    ax.add_patch(Rectangle((10.2, 4.6), .90, .94, fc=ROJO, ec=ROJO, lw=1.2, alpha=.85))
    txt(ax, 11.15, 6.1, "TORRE DE OBSERVACIÓN /\nPUENTE DE MANDO  3,60 × 3,75 m",
        fontsize=7.6, color=ROJO, weight="bold")
    # sala (3,61 m del centroide de la torre)
    ax.add_patch(Rectangle((10.35, 2.6), 1.375, 1.75, fc=VERDE, ec=VERDE, lw=1.2, alpha=.8))
    txt(ax, 11.8, 3.0, "SALA TÉCNICA DE INVESTIGACIÓN\nHIDROMETEOROLÓGICA  5,50 × 7,00 m",
        fontsize=7.4, color=VERDE, weight="bold")
    # separación
    ax.add_line(Line2D([10.8, 10.8], [3.55, 4.55], color=OCRE, lw=1.0, ls="--"))
    txt(ax, 10.9, 4.05, "3,61 m", fontsize=7, color=OCRE, weight="bold")
    # plaza de honor + banda de protocolo
    ax.add_patch(Rectangle((12.6, 1.0), 5.5, 5.6, fc="#f3efe2", ec=OCRE, lw=1.0, ls=":"))
    txt(ax, 15.3, 3.8, "PLAZA DE HONOR\ny BANDA DE PROTOCOLO", ha="center", fontsize=7.6, color=OCRE)
    # espina peatonal
    ax.add_patch(Rectangle((1.0, 6.9), 17.1, .8, fc="#e8eef2", ec=GRIS, lw=.6))
    txt(ax, 9.5, 7.3, "ESPINA PEATONAL 4,00 m → corredor tecnológico-administrativo del Plan Maestro",
        fontsize=7, color=GRIS)
    # norte
    ax.add_patch(FancyArrow(18.6, 1.6, 0, 1.6, width=.08, head_width=.4, head_length=.5, fc=AZUL, ec=AZUL))
    txt(ax, 18.6, 3.6, "N\n(Proa)", ha="center", fontsize=7.4, color=AZUL, weight="bold")
    # centroides
    for (x, y, s) in [(10.65, 5.05, "C-TO\n10.60082778\n−67.03229444"),
                      (11.03, 3.45, "C-STH\n10.60085833\n−67.03228333")]:
        ax.add_patch(Circle((x, y), .07, fc="white", ec=ROJO, lw=1.0))
        ax.plot([x - .18, x + .18], [y, y], color=ROJO, lw=.6); ax.plot([x, x], [y - .18, y + .18], color=ROJO, lw=.6)
    txt(ax, 12.4, 5.6, "C-TO: centroide Torre (WGS84)\nC-STH: centroide Sala (WGS84)", fontsize=6.6, color=ROJO)
    ax.set_xlim(0, 20); ax.set_ylim(0, 8.4); ax.set_aspect("equal")
    cajetin(fig, "UMC-G-ARQ-001-R02", "Implantación general del Área Cultural", "1:400",
            extra="Hipótesis de implantación sujeta a RFI-GEO-001/002")
    guardar(fig, FIG + "G-01_implantacion_area_cultural.png")


# ----------------------------------------------------------------------------- G-02 línea de tiempo
def g02():
    fig, ax = nuevo("G-02 · Línea de tiempo patrimonial y sísmica 1951 → 2030",
                    "Cronología documental y constructiva verificada en el Inventario General "
                    "Consolidado y en el documento fuente.")
    ev = [(1951, "28-08-1951\nProyecto original\nFracción 1 (MOP)", ACERO, 1),
          (1955, "1951–1958\nConstrucción inicial:\nAula Magna, Torre, Sala", ACERO, -1),
          (1967, "1960–1975\nAumento de altura\nde la Torre", OCRE, 1),
          (1990, "1975–2010\nEstación de registro\nmeteorológico", VERDE, -1),
          (2018, "2010–2026\nInvestigación\nhidrometeorológica", VERDE, 1),
          (2026.48, "24-06-2026\nDOBLETE SÍSMICO\nM 7,2 y M 7,5", ROJO, -1),
          (2028, "2026–2028\nDiagnóstico, ingeniería\ny restauración", AZUL, 1),
          (2030, "2030\nReequipamiento y\npuesta en servicio", AZUL, -1)]
    ax.add_line(Line2D([1948, 2032], [0, 0], color=GRIS, lw=1.6))
    for yr, s, c, side in ev:
        ax.add_patch(Circle((yr, 0), .45, fc=c, ec="white", lw=1.2, zorder=3))
        yy = 1.15 if side > 0 else -1.15
        ax.add_line(Line2D([yr, yr], [0, yy * .72], color=c, lw=.9, ls=":"))
        txt(ax, yr, yy, s, ha="center", fontsize=7.2, color=c, weight="bold")
    txt(ax, 2026.48, -2.35, "Colapso y afectación de la Torre y la Sala · estado POST-COLAPSO",
        ha="center", fontsize=7.6, color=ROJO, weight="bold")
    ax.set_xlim(1948, 2032); ax.set_ylim(-3.1, 2.4); ax.set_axis_off()
    cajetin(fig, "UMC-T-HIS-001-R02", "Cronología patrimonial y sísmica", "s/e (diagrama)")
    guardar(fig, FIG + "G-02_linea_tiempo.png")


# ----------------------------------------------------------------------------- G-03 alturas
def g03():
    fig, ax = nuevo("G-03 · Comparativa de alturas documentadas y geometría adoptada",
                    "12,20 m (serie 15 DF 30 Nº 86, 28-8-51, ANULADA) · 15,80 m (lectura aparente "
                    "P04-L11-A) · 22,02 m (8.DF.2.362 No. 149, 21-6-52, VIGENTE).")
    xs = [1.0, 3.4, 5.8]
    hs = [12.20, 15.80, 22.02]
    cols = [GRIS, OCRE, ROJO]
    lab = ["ALTURA ORIGINAL\n12,20 m\n(plano 12,00 + losa 0,20)\n15 DF 30 Nº 86 · 28-8-51\nserie ANULADA (P05-008)",
           "LECTURA APARENTE\n15,80 m\nnota de fachada\nP04-L11-A · sin fecha\nRFI-ALT-01",
           "ALTURA ADOPTADA\n22,02 m\nmodificación legal\n8.DF.2.362 No. 149 · 21-6-52\nvigente y verificada p. 73"]
    for x, hh, c, l in zip(xs, hs, cols, lab):
        ax.add_patch(Rectangle((x, 0), 1.3, hh, fc=c, ec=c, alpha=.28 if c != ROJO else .5, lw=1.4))
        for k in range(5):
            ax.add_line(Line2D([x, x + 1.3], [hh * (k + 1) / 5.0] * 2, color=c, lw=.5))
        txt(ax, x + .65, hh + .9, l, ha="center", fontsize=7.2, color=c, weight="bold")
        ax.add_line(Line2D([x + 1.45, x + 1.75], [hh, hh], color=c, lw=.8))
        txt(ax, x + 1.8, hh, f"{hh:.2f} m", fontsize=8, color=c, weight="bold")
    ax.add_line(Line2D([.6, 8.2], [0, 0], color=AZUL, lw=1.4))
    txt(ax, .6, -.9, "NPT ±0,000 (cota pendiente de BM-UMC-01 · RFI-GEO-002)", fontsize=7.2, color=AZUL)
    txt(ax, 4.6, 24.6, "GEOMETRÍA DE PROYECTO: 5 niveles + coronación y asta sobre 22,02 m "
                       "(decisión justificada en cap. 6.3 y 11.5; R4)", ha="center",
        fontsize=8, color=AZUL, weight="bold")
    ax.set_xlim(.2, 8.6); ax.set_ylim(-2, 26); ax.set_axis_off()
    cajetin(fig, "UMC-T-ARQ-002-R02", "Comparativa de alturas documentadas", "s/e (diagrama)")
    guardar(fig, FIG + "G-03_alturas.png")


# ----------------------------------------------------------------------------- G-04 áreas
def g04():
    fig, ax = nuevo("G-04 · Cuadro de áreas por nivel y eficiencia neta/bruta",
                    "Torre: 5 niveles × 13,50 m² = 67,50 m² · Sala: huella verificada 38,50 m² "
                    "(programa declarado 40,00 m²).")
    niv = ["N0 ±0,000", "N1 +4,400", "N2 +8,800", "N3 +13,200", "N4 +17,600"]
    net = [10.8, 10.4, 10.2, 10.6, 11.0]
    cir = [13.5 - v for v in net]
    y = range(len(niv))
    ax.barh(list(y), net, color=ACERO, label="Área neta (m²)")
    ax.barh(list(y), cir, left=net, color="#d7dee4", label="Circulación, núcleo y muros (m²)")
    for i, (a, b) in enumerate(zip(net, cir)):
        txt(ax, a / 2, i, f"{a:.1f}", ha="center", fontsize=7, color="white", weight="bold")
        txt(ax, a + b / 2, i, f"{b:.1f}", ha="center", fontsize=6.6, color="#33475a")
    ax.set_yticks(list(y)); ax.set_yticklabels(niv, fontsize=7.4)
    ax.set_xlabel("m² por nivel (bruto 13,50 m²)", fontsize=7.4)
    ax.legend(fontsize=7, loc="lower right", frameon=False)
    ax.set_xlim(0, 15.5)
    # bloque sala
    txt(ax, 16.4, 3.6, "SALA TÉCNICA\nhuella 38,50 m²\nprograma 40,00 m²\neficiencia 88,6 %",
        fontsize=7.6, color=VERDE, weight="bold")
    txt(ax, 16.4, 1.4, "TORRE\neficiencia neta/bruta\n79,6 %", fontsize=7.6, color=ACERO, weight="bold")
    cajetin(fig, "UMC-T-ARQ-003-R02", "Cuadro de áreas por nivel", "s/e (gráfica)")
    guardar(fig, FIG + "G-04_cuadro_areas.png")


# ----------------------------------------------------------------------------- G-05 zonificación sala
def g05():
    fig, ax = nuevo("G-05 · Zonificación de la Sala Técnica de Investigación Hidrometeorológica",
                    "Distribución documentada (40,00 m²) reescalada a la huella verificada "
                    "5,50 × 7,00 m = 38,50 m² · factor 0,9625 · RFI-ARE-01.")
    f = 0.9625
    zonas = [("Estaciones de trabajo\nmeteorológico", 9.00 * f, "#cfe0ea"),
             ("Servidores / equipos\nde registro", 5.00 * f, "#dbe7dd"),
             ("Circulación y maniobra", 6.00 * f, "#f0f0f0"),
             ("SS anexos", 3.00 * f, "#e6dcd0"),
             ("Mesón / mostrador", 2.25 * f, "#e9e2f0"),
             ("Área libre, muros\ny estructura", 14.75 * f, "#ffffff")]
    # layout manual 5,50 x 7,00
    rect = [(0, 0, 3.0, 3.0), (3.0, 0, 2.5, 2.0), (3.0, 2.0, 2.5, 1.4),
            (0, 3.0, 1.6, 1.6), (1.6, 3.0, 1.4, 1.6), (0, 4.6, 5.5, 2.4)]
    for (n, a, c), (x, y, w, h) in zip(zonas, rect):
        ax.add_patch(Rectangle((x, y), w, h, fc=c, ec=ACERO, lw=1.0))
        txt(ax, x + w / 2, y + h / 2, f"{n}\n{a:.2f} m²", ha="center", fontsize=6.8, color="#12212b")
    ax.add_patch(Rectangle((0, 0), 5.5, 7.0, fill=False, ec=AZUL, lw=1.8))
    txt(ax, 2.75, -0.55, "5,50 m", ha="center", fontsize=7.4, color=AZUL, weight="bold")
    txt(ax, -0.55, 3.5, "7,00 m", ha="center", fontsize=7.4, color=AZUL, weight="bold", rotation=90)
    ax.set_xlim(-1.2, 8.6); ax.set_ylim(-1.2, 8.2); ax.set_aspect("equal"); ax.set_axis_off()
    tabla(fig, [["Zona", "Declarado (m²)", "Adoptado (m²)"],
                ["Estaciones de trabajo", "9,00", "8,66"], ["Servidores / registro", "5,00", "4,81"],
                ["Circulación y maniobra", "6,00", "5,78"], ["SS anexos", "3,00", "2,89"],
                ["Mesón / mostrador", "2,25", "2,17"], ["Área libre / muros", "14,75", "14,19"],
                ["TOTAL", "40,00", "38,50"]], x=.62, y=.62, w=.34, colw=[.5, .25, .25], fs=6.9)
    cajetin(fig, "UMC-S-ARQ-101-R02", "Planta de zonificación de la Sala Técnica", "1:100", "±0,000")
    guardar(fig, FIG + "G-05_zonificacion_sala.png")


# ----------------------------------------------------------------------------- G-06 estructura/refuerzo
def g06():
    fig, ax = nuevo("G-06 · Sistema estructural y estrategia de refuerzo (criterio)",
                    "Pórticos de hormigón armado sobre pilotes y cabezales (P05-023 «cabezales "
                    "pilote»); refuerzo por encamisado y disipación; arriostramiento de la esbeltez.")
    for k in range(6):
        yy = k * 4.4
        ax.add_line(Line2D([1, 4.6], [yy, yy], color=ACERO, lw=2.2))
        for x in (1, 2.2, 3.4, 4.6):
            ax.add_line(Line2D([x, x], [yy, yy + 4.4], color=ACERO, lw=1.6))
    ax.add_patch(Rectangle((.4, -2.2), 4.8, 2.2, fc="#d8cbb6", ec=OCRE, lw=1.2))
    for x in (1.2, 2.4, 3.6, 4.4):
        ax.add_line(Line2D([x, x], [-2.2, -4.6], color=OCRE, lw=2.4))
    txt(ax, 5.0, -3.4, "Cabezales y pilotes\nexistentes (documentados)\nverificación geotécnica RFI-GEOT-01",
        fontsize=7, color=OCRE, weight="bold")
    txt(ax, 5.2, 2.2, "Encamisado de\nmachones N0–N2\n(daño D3–D4)", fontsize=7.2, color=ROJO, weight="bold")
    ax.add_patch(FancyArrow(5.1, 2.2, -1.1, 0, width=.05, head_width=.3, head_length=.3, fc=ROJO, ec=ROJO))
    txt(ax, 5.2, 10.5, "Disipadores / refuerzo\nen niveles N3–N4", fontsize=7.2, color=ROJO, weight="bold")
    ax.add_patch(FancyArrow(5.1, 10.5, -1.0, 0, width=.05, head_width=.3, head_length=.3, fc=ROJO, ec=ROJO))
    txt(ax, 5.2, 19.5, "Coronación y asta:\nreposición distinguible\n+ pararrayos (IEC 62305)",
        fontsize=7.2, color=VERDE, weight="bold")
    ax.add_patch(FancyArrow(5.1, 19.0, -.9, -.6, width=.05, head_width=.3, head_length=.3, fc=VERDE, ec=VERDE))
    ax.add_line(Line2D([2.8, 2.8], [0, 26.6], color=GRIS, lw=.7, ls="--"))
    txt(ax, 2.9, 25.4, "núcleo vertical: escalera Nº 4\n(reponer s/ P0102-L3-E) + plataforma accesible",
        fontsize=7, color=GRIS)
    ax.set_xlim(-1, 10); ax.set_ylim(-6, 28); ax.set_axis_off()
    cajetin(fig, "UMC-T-STR-001-R02", "Criterio estructural y de refuerzo", "s/e (diagrama)")
    guardar(fig, FIG + "G-06_estructura_refuerzo.png")


# ----------------------------------------------------------------------------- G-07 mapa de daño
DAÑO = [  # nivel, elemento, grado D0-D5, decisión
    ("N0 ±0,000", "Machones y muros de planta baja", "D4", "Reconstruir con reintegración"),
    ("N0 ±0,000", "Losa de piso / vigas 1V", "D3", "Reparar y reforzar"),
    ("N1 +4,400", "Machones perimetrales", "D3", "Reparar y encamisar"),
    ("N1 +4,400", "Losa 1L y vigas de borde", "D3", "Reparar y reforzar"),
    ("N2 +8,800", "Machones y cerramientos", "D3", "Reparar y encamisar"),
    ("N2 +8,800", "Escalera Nº 4 (tramos LE)", "D3", "Reparar; reponer tramos colapsados"),
    ("N3 +13,200", "Machones y cerramientos", "D2", "Consolidar y reparar"),
    ("N3 +13,200", "Losa 2L / vigas 2V", "D2", "Consolidar"),
    ("N4 +17,600", "Puente de mando: cerramientos y ventanas", "D3", "Reponer con criterio patrimonial"),
    ("Coronación", "Antepecho, asta y remates", "D4", "Reponer (distinguible)"),
    ("Cimentación", "Pilotes y cabezales", "D1", "Verificar (inspección detallada)"),
    ("Sala", "Muros perimetrales 5,50 × 7,00", "D2", "Consolidar y reparar"),
    ("Sala", "Losa de techo e impermeabilización", "D3", "Reparar / renovar"),
    ("Sala", "Instalaciones y carpinterías", "D2", "Reponer funcionalmente"),
]
COL_D = {"D0": "#9fc59f", "D1": "#cfe0a8", "D2": "#f2d478", "D3": "#e8975a", "D4": "#c0504d", "D5": "#7f1d1d"}


def g07():
    fig, ax = nuevo("G-07 · Mapa de daño post-sísmico por nivel y elemento",
                    "Doblete sísmico del 24-06-2026 (M 7,2 y M 7,5). Evaluación PRELIMINAR sobre "
                    "registro fotográfico y documental; pendiente de inspección detallada (RFI-PAT-01).")
    y0 = .80
    for i, (niv, el, d, dec) in enumerate(DAÑO):
        yy = y0 - i * .0475
        fig.patches.append(Rectangle((.045, yy - .016), .028, .030, transform=fig.transFigure,
                                     facecolor=COL_D[d], edgecolor="white", lw=.6))
        fig.text(.080, yy - .001, f"{niv} · {el}", fontsize=6.9, color="#12212b", va="center")
        fig.text(.455, yy - .001, d, fontsize=7.6, color=COL_D[d], weight="bold", va="center")
        fig.text(.490, yy - .001, dec, fontsize=6.9, color="#33475a", va="center")
    # leyenda horizontal
    leg = [("D1", "ligero"), ("D2", "moderado"), ("D3", "severo"),
           ("D4", "muy severo / colapso parcial"), ("D5", "colapso")]
    xx = .045
    for d, s in leg:
        fig.patches.append(Rectangle((xx, .098), .020, .018, transform=fig.transFigure,
                                     facecolor=COL_D[d], edgecolor="white", lw=.5))
        fig.text(xx + .024, .107, f"{d} {s}", fontsize=6.4, color="#33475a", va="center")
        xx += .028 + .016 * len(s) + .026
    # torre esquemática coloreada por nivel
    ax.set_position([.64, .17, .32, .68]); ax.set_axis_off()
    lv = [("COR", "D4"), ("N4", "D3"), ("N3", "D2"), ("N2", "D3"), ("N1", "D3"), ("N0", "D4")]
    for k, (n, d) in enumerate(lv):
        ax.add_patch(Rectangle((0, (5 - k) * 4.4), 3.6, 4.4, fc=COL_D[d], ec="white", lw=1.2, alpha=.92))
        ax.text(1.8, (5 - k) * 4.4 + 2.2, f"{n}\n{d}", ha="center", va="center", fontsize=8,
                color="white", weight="bold")
    ax.add_patch(Rectangle((-.4, -2.0), 4.4, 2.0, fc=COL_D["D1"], ec="white", lw=1.0))
    ax.text(1.8, -1.0, "CIMENT. D1", ha="center", va="center", fontsize=7, color="#12212b")
    ax.set_xlim(-1.5, 5.5); ax.set_ylim(-3, 28)
    cajetin(fig, "UMC-T-PAT-001-R02", "Mapa de daño post-sísmico", "s/e (diagrama)",
            extra="Clasificación de uso: INSPECCIÓN DETALLADA requerida")
    guardar(fig, FIG + "G-07_mapa_dano.png")


# ----------------------------------------------------------------------------- G-08 estación met
def g08():
    fig, ax = nuevo("G-08 · Estación hidrometeorológica: emplazamiento e instrumentación",
                    "Criterios de emplazamiento referenciales (guías OMM): abrigo a ≥ 2× la altura del "
                    "obstáculo más próximo; anemómetro a 10,00 m sobre superficie despejada.")
    ax.add_patch(Rectangle((0, 0), 24, 10, fc="#eef4ee", ec=GRIS, lw=.6))
    ax.add_patch(Rectangle((1, 1), 3.6, 4.4, fc=VERDE, ec=VERDE, alpha=.85))
    txt(ax, 2.8, 3.2, "SALA\nTÉCNICA", ha="center", fontsize=7.4, color="white", weight="bold")
    ax.add_patch(Rectangle((7, 1.4), 1.1, 1.1, fc="white", ec=AZUL, lw=1.2))
    txt(ax, 7.55, 3.1, "Abrigo meteorológico\ntipo Stevenson", ha="center", fontsize=6.8, color=AZUL)
    ax.add_line(Line2D([10.5, 10.5], [0.6, 10.6], color=AZUL, lw=1.6))
    for yy, s in [(10.6, "anemómetro / veleta 10,00 m"), (8.4, "sensores T/HR 2,00 m"),
                  (6.4, "barómetro / datalogger")]:
        ax.add_line(Line2D([10.5, 11.6], [yy, yy], color=AZUL, lw=.8))
        txt(ax, 11.8, yy, s, fontsize=6.8, color=AZUL)
    ax.add_patch(Rectangle((14.5, .6), 3.0, 2.2, fc="#dfe8ee", ec=ACERO, lw=1.0))
    txt(ax, 16.0, 1.7, "Parcela de sensores\n(pluviómetro, evaporación,\nradiación, nivel)", ha="center",
        fontsize=6.6, color=ACERO)
    ax.add_patch(Rectangle((19.5, 3.0), 3.4, 6.0, fc="#d8cbb6", ec=OCRE, lw=1.0))
    txt(ax, 21.2, 6.0, "TORRE\n(obstáculo:\ndistancia ≥ 2×h\nverificar)", ha="center", fontsize=6.6, color=OCRE)
    ax.add_line(Line2D([18.9, 19.5], [2.0, 2.0], color=ROJO, lw=.8, ls="--"))
    txt(ax, 19.2, 2.6, "separación\nnormativa", ha="center", fontsize=6.4, color=ROJO)
    ax.set_xlim(-1, 25); ax.set_ylim(-1.5, 12.5); ax.set_aspect("equal"); ax.set_axis_off()
    cajetin(fig, "UMC-S-MET-001-R02", "Emplazamiento de la estación hidrometeorológica", "1:200",
            extra="Trazabilidad de dato: OMM-Nº 8 (referencial, por verificar)")
    guardar(fig, FIG + "G-08_estacion_met.png")


# ----------------------------------------------------------------------------- G-09 unifilar
def g09():
    fig, ax = nuevo("G-09 · Unifilar eléctrico y esquema de telemetría",
                    "Cargas críticas: instrumentación meteorológica, registro y alumbrado de "
                    "emergencia. Respaldo UPS + BESS; protección contra descargas del asta.")
    bloques = [(1, 8.4, "Acometida BT\ncampus (corredor\nde redes)", ACERO),
               (4, 8.4, "TGBT-T\n+ ATS", AZUL),
               (7, 9.4, "UPS 10 kVA\ninstrumentación", ROJO),
               (7, 7.2, "Tablero\nalumbrado y\nfuerza", ACERO),
               (7, 5.0, "Tablero\nemergencia y\nbalizamiento", ROJO),
               (10, 9.4, "Datalogger /\nregistro met.", VERDE),
               (10, 7.2, "Cargas de\nsala técnica", VERDE),
               (10, 5.0, "Iluminación\nde puente de\nmando", VERDE),
               (4, 3.2, "BESS / FV\ncubierta (opc.)", OCRE),
               (10, 1.6, "Enlace fibra →\nCDP Torre B\n(telemetría)", AZUL)]
    for x, y, s, c in bloques:
        ax.add_patch(Rectangle((x, y), 2.2, 1.5, fc="white", ec=c, lw=1.3))
        txt(ax, x + 1.1, y + .75, s, ha="center", fontsize=6.6, color=c, weight="bold")
    lin = [((3.2, 9.15), (4, 9.15)), ((6.2, 9.15), (7, 10.15)), ((6.2, 9.15), (7, 7.95)),
           ((6.2, 9.15), (7, 5.75)), ((9.2, 10.15), (10, 10.15)), ((9.2, 7.95), (10, 7.95)),
           ((9.2, 5.75), (10, 5.75)), ((5.1, 4.7), (5.1, 8.4)), ((11.1, 2.3), (11.1, 5.0))]
    for a, b in lin:
        ax.add_line(Line2D([a[0], b[0]], [a[1], b[1]], color=GRIS, lw=1.1))
    ax.add_line(Line2D([13.4, 13.4], [1.0, 11.4], color=ROJO, lw=1.4))
    txt(ax, 13.7, 11.2, "Pararrayos y\nbajante dedicada\n(IEC 62305)\nen el asta", fontsize=6.8,
        color=ROJO, weight="bold")
    ax.set_xlim(0, 17); ax.set_ylim(0, 12.6); ax.set_axis_off()
    cajetin(fig, "UMC-T-ELE-001-R02", "Unifilar conceptual y telemetría", "s/e (diagrama)")
    guardar(fig, FIG + "G-09_unifilar.png")


# ----------------------------------------------------------------------------- G-10 red
def g10():
    fig, ax = nuevo("G-10 · Arquitectura de red e integración con el CDP (Torre B)",
                    "VLAN segregadas: instrumentación, académica, administrativa, seguridad y visita. "
                    "Fibra OS2 desde el MMR del CDP por el corredor de redes enterrado.")
    ax.add_patch(Rectangle((1, 7.6), 3.4, 2.2, fc=AZUL, ec=AZUL))
    txt(ax, 2.7, 8.7, "CDP · TORRE B\nMMR / core", ha="center", fontsize=7.6, color="white", weight="bold")
    ax.add_patch(Rectangle((6.4, 7.6), 3.0, 2.2, fc="white", ec=ACERO, lw=1.4))
    txt(ax, 7.9, 8.7, "IDF Torre\n(patch Cat.6A\n+ ODF fibra)", ha="center", fontsize=7, color=ACERO, weight="bold")
    ax.add_patch(Rectangle((6.4, 4.4), 3.0, 1.8, fc="white", ec=VERDE, lw=1.3))
    txt(ax, 7.9, 5.3, "Datalogger met.\n(VLAN instrum.)", ha="center", fontsize=6.8, color=VERDE, weight="bold")
    ax.add_patch(Rectangle((6.4, 1.6), 3.0, 1.8, fc="white", ec=ROJO, lw=1.3))
    txt(ax, 7.9, 2.5, "CCTV / control\nde acceso torre", ha="center", fontsize=6.8, color=ROJO, weight="bold")
    ax.add_patch(Rectangle((11.4, 4.4), 3.2, 1.8, fc="white", ec=ACERO, lw=1.3))
    txt(ax, 13.0, 5.3, "Wi-Fi 6 plaza\nde honor y actos", ha="center", fontsize=6.8, color=ACERO, weight="bold")
    for y in (5.3, 2.5):
        ax.add_line(Line2D([9.4, 6.4 + 4.0], [y, y], color=GRIS, lw=0))
    ax.add_line(Line2D([4.4, 6.4], [8.7, 8.7], color=AZUL, lw=1.6))
    txt(ax, 5.4, 9.05, "fibra OS2", fontsize=6.8, color=AZUL, weight="bold")
    ax.add_line(Line2D([7.9, 7.9], [7.6, 6.2], color=GRIS, lw=1.1))
    ax.add_line(Line2D([7.9, 7.9], [4.4, 3.4], color=GRIS, lw=1.1))
    ax.add_line(Line2D([9.4, 11.4], [5.3, 5.3], color=GRIS, lw=1.1))
    txt(ax, 11.6, 1.2, "Publicación de dato meteorológico con metadatos y control de calidad "
                       "(serie histórica UMC desde 1975)", fontsize=7, color="#33475a")
    ax.set_xlim(0, 16); ax.set_ylim(0, 11); ax.set_axis_off()
    cajetin(fig, "UMC-T-TEL-001-R02", "Arquitectura de red del Proyecto 04", "s/e (diagrama)")
    guardar(fig, FIG + "G-10_red.png")


# ----------------------------------------------------------------------------- G-11 HBIM
def g11():
    fig, ax = nuevo("G-11 · Estrategia HBIM y gemelo digital",
                    "Nube de puntos de lo existente → modelo federado → AIM → mantenimiento "
                    "predictivo y monitorización estructural.")
    pasos = [("1 · LEVANTAMIENTO\nnube de puntos TLS\n+ fotogrametría\n+ sondeos", GRIS),
             ("2 · MODELO HBIM\nfederado ARQ/STR/MEP\nCDE estados\n01–04", ACERO),
             ("3 · GEMELO DIGITAL\nIoT estructural y\nambiental en tiempo\nreal", VERDE),
             ("4 · AIM\nfichas de activo,\nmantenimiento\npredictivo", AZUL)]
    for i, (s, c) in enumerate(pasos):
        x = .8 + i * 3.6
        ax.add_patch(Rectangle((x, 5), 3.0, 2.6, fc="white", ec=c, lw=1.5))
        txt(ax, x + 1.5, 6.3, s, ha="center", fontsize=7.2, color=c, weight="bold")
        if i:
            ax.add_patch(FancyArrow(x - .55, 6.3, .45, 0, width=.06, head_width=.28,
                                    head_length=.2, fc=c, ec=c))
    txt(ax, 7.6, 3.6, "Codificación: UMC-T-[DISCIPLINA]-[NÚMERO]-[REV] · activos UMC-T-N4-OBS-01 "
                      "(puente de mando), UMC-S-MET-AWS-01 (estación)", ha="center", fontsize=7.2, color="#33475a")
    txt(ax, 7.6, 2.6, "Enfoque humanocéntrico: el gemelo apoya al operador y al cadete; no sustituye "
                      "la observación manual exigida por la formación STCW", ha="center",
        fontsize=7.2, color=ROJO)
    ax.set_xlim(0, 15.4); ax.set_ylim(1.6, 9); ax.set_axis_off()
    cajetin(fig, "UMC-T-BIM-001-R02", "Estrategia HBIM / Digital Twin", "s/e (diagrama)")
    guardar(fig, FIG + "G-11_hbim.png")


# ----------------------------------------------------------------------------- G-12 evacuación
def g12():
    fig, ax = nuevo("G-12 · Evacuación vertical y aforo de la torre",
                    "20 personas en el puente de mando + 5–10 en la sala. Ruta vertical única: "
                    "escalera Nº 4 reconstituida + plataforma accesible; punto de reunión en plaza de honor.")
    for k in range(5):
        yy = k * 4.4
        ax.add_patch(Rectangle((1, yy), 3.6, 4.4, fc="#eef2f5", ec=ACERO, lw=1.2))
        txt(ax, 2.8, yy + 2.2, f"N{k} · aforo {['6','4','4','3','3'][k]}", ha="center", fontsize=7.2, color=ACERO)
    ax.add_patch(Rectangle((1.2, 0), 1.0, 22.0, fc="#f6d9d7", ec=ROJO, lw=1.2))
    txt(ax, 1.7, 11.0, "ESCALERA Nº 4", rotation=90, ha="center", fontsize=7, color=ROJO, weight="bold")
    ax.add_patch(FancyArrow(1.7, 21.5, 0, -20.4, width=.06, head_width=.4, head_length=.8, fc=ROJO, ec=ROJO))
    txt(ax, 5.2, 20.0, "Punto crítico: tramo N4→N3\n(distancia de viaje y ancho\na verificar por cálculo de aforo)",
        fontsize=7, color=ROJO)
    txt(ax, 5.2, 12.0, "Rescate asistido: área de\nrefugio en N2 + protocolo\nde actos ceremoniales", fontsize=7, color=AZUL)
    txt(ax, 5.2, 4.0, "Salida a plaza de honor:\npunto de reunión R-1\n(señalizado y accesible)", fontsize=7, color=VERDE)
    ax.add_patch(Rectangle((1, -3.2), 8, 2.4, fc="#f3efe2", ec=OCRE, lw=1.0))
    txt(ax, 5, -2.0, "PLAZA DE HONOR · PUNTO DE REUNIÓN R-1", ha="center", fontsize=7.4, color=OCRE, weight="bold")
    ax.set_xlim(0, 12); ax.set_ylim(-4.5, 24); ax.set_axis_off()
    cajetin(fig, "UMC-T-SEG-001-R02", "Evacuación vertical y aforo", "s/e (diagrama)",
            extra="El ascensor/plataforma NO sustituye rutas de evacuación")
    guardar(fig, FIG + "G-12_evacuacion.png")


# ----------------------------------------------------------------------------- G-13 ROM
def g13():
    """v3: cada barra identificada con su capítulo (nombre legible + rango anotado) y leyenda
    que explica los dos tramos. Corrige la queja del Rectorado: «no entiendo qué es cada barra»."""
    from matplotlib.patches import Patch
    fig, ax = nuevo("G-13 · Estimación ROM (AACE Clase 5) por capítulo del presupuesto",
                    "Cada barra = un capítulo: tramo azul oscuro hasta el mínimo (−25 %), tramo "
                    "azul claro hasta el máximo (+40 %). Cifras en kUSD (miles de USD).")
    ax.set_axis_on()
    fig.subplots_adjust(left=.255, right=.965, top=.835, bottom=.115)
    cap = ["1 · Estudios previos\n(escaneo, ensayos, patología)",
           "2 · Demolición y gestión de\nescombros patrimoniales",
           "3 · Consolidación y refuerzo\nestructural",
           "4 · Arquitectura y acabados\npatrimoniales",
           "5 · MEP (45 kVA + HVAC\nde precisión)",
           "6 · Instrumentación\nmeteorológica (AWS)",
           "7 · TIC y seguridad\nelectrónica",
           "8 · Obras exteriores y\nplaza de honor",
           "9 · Ingeniería (7 %) y\ncontingencia (18 %)"]
    lo = [180, 90, 420, 380, 150, 220, 110, 260, 280]
    hi = [260, 140, 640, 560, 230, 420, 170, 400, 430]
    y = list(range(len(cap)))
    ax.barh(y, lo, color=ACERO, height=.58)
    ax.barh(y, [b - a for a, b in zip(lo, hi)], left=lo, color="#BBD0DC", height=.58)
    for i, (a, b) in enumerate(zip(lo, hi)):
        ax.plot([(a + b) / 2], [i], marker="D", ms=4.5, color=ROJO, zorder=5,
                clip_on=False)
        txt(ax, b + 14, i, f"{a} – {b} kUSD", fontsize=8.8, color="#12212b", weight="bold")
    ax.set_yticks(y); ax.set_yticklabels(cap, fontsize=8.8)
    ax.tick_params(axis="x", labelsize=8.4)
    ax.set_xlabel("kUSD (miles de dólares de los EE. UU.)", fontsize=9.2)
    ax.set_xlim(0, 860); ax.set_ylim(len(cap) - .5, -2.3)
    ax.grid(axis="x", color="#dde5ea", lw=.6, zorder=0)
    ax.set_axisbelow(True)
    for s in ("top", "right", "left"):
        ax.spines[s].set_visible(False)
    ax.legend(handles=[
        Patch(color=ACERO, label="Del cero al mínimo (−25 %)"),
        Patch(color="#BBD0DC", label="Del mínimo al máximo (+40 %)"),
        Line2D([0], [0], marker="D", ls="", color=ROJO, label="Punto medio")],
        title="TOTAL ROM: 2.090 – 3.250 kUSD", loc="upper center", ncol=3,
        bbox_to_anchor=(0.5, 0.995), fontsize=8.6, title_fontsize=9.2, frameon=True,
        framealpha=1, edgecolor=GRIS, columnspacing=1.4, handlelength=1.6)
    cajetin(fig, "UMC-T-COS-001-R02", "ROM por capítulo (AACE Clase 5)", "s/e (gráfica)")
    guardar(fig, FIG + "G-13_rom.png")


# ----------------------------------------------------------------------------- G-14 gantt
def g14():
    fig, ax = nuevo("G-14 · Cronograma de ejecución con gates",
                    "≈ 30 meses desde la aprobación del anteproyecto. Gates G0–G6 del expediente.")
    fases = [("Fase A · Estudios básicos: escaneo TLS, patología, geotecnia, topografía", 0, 4, ACERO, "G1"),
             ("Fase B · Ingeniería básica y de detalle + especificaciones", 3, 9, AZUL, "G2"),
             ("Fase C · Permisos, patrimonio y licitación (solapada)", 8, 6, OCRE, "G3"),
             ("Fase D · Consolidación, refuerzo, arquitectura y MEP", 12, 12, VERDE, "G4"),
             ("Fase E · Instrumentación, TIC, pruebas y puesta en servicio", 22, 6, ROJO, "G5"),
             ("Operación asistida y cierre del AIM", 28, 4, GRIS, "G6")]
    for i, (n, s, d, c, g) in enumerate(fases):
        ax.add_patch(Rectangle((s, -i), d, .62, fc=c, ec=c, alpha=.85))
        txt(ax, s + d + .4, -i + .31, f"{d} m", fontsize=7, color=c, weight="bold")
        ax.add_patch(Circle((s + d, -i + .31), .30, fc="white", ec=c, lw=1.4, zorder=4))
        txt(ax, s + d, -i + .31, g, ha="center", fontsize=6, color=c, weight="bold", zorder=5)
    ax.set_yticks([-i + .31 for i in range(len(fases))])
    ax.set_yticklabels([f[0] for f in fases], fontsize=7)
    ax.set_xlim(0, 36); ax.set_xticks(range(0, 37, 3))
    ax.set_xlabel("meses desde aprobación", fontsize=7.4)
    ax.grid(axis="x", lw=.4, color="#c9d4dc")
    for s in ("top", "right", "left"):
        ax.spines[s].set_visible(False)
    cajetin(fig, "UMC-T-PLA-001-R02", "Cronograma de referencia con gates", "s/e (Gantt)")
    guardar(fig, FIG + "G-14_cronograma.png")


# ----------------------------------------------------------------------------- G-15 riesgos
RIESGOS = [  # id, prob 1-5, impacto 1-5
    ("R-01", 4, 5), ("R-02", 4, 5), ("R-03", 3, 5), ("R-04", 3, 4), ("R-05", 4, 4),
    ("R-06", 3, 3), ("R-07", 4, 3), ("R-08", 2, 5), ("R-09", 3, 4), ("R-10", 2, 4),
    ("R-11", 3, 3), ("R-12", 2, 3),
]


def g15():
    fig, ax = nuevo("G-15 · Mapa de riesgos (probabilidad × impacto)",
                    "Matriz del capítulo 25.1. El tamaño del marcador es proporcional a la exposición.")
    for p in range(1, 6):
        for i in range(1, 6):
            c = "#e8f0e8" if p * i <= 6 else ("#f7ecc9" if p * i <= 12 else ("#f3d3bd" if p * i <= 16 else "#e7b6b3"))
            ax.add_patch(Rectangle((p - .5, i - .5), 1, 1, fc=c, ec="white", lw=1.2))
    for rid, p, i in RIESGOS:
        ax.add_patch(Circle((p, i), .27, fc=AZUL, ec="white", lw=1.2, zorder=4))
        txt(ax, p, i, rid.replace("R-", ""), ha="center", fontsize=6.4, color="white",
            weight="bold", zorder=5)
    ax.set_xlim(.5, 5.5); ax.set_ylim(.5, 5.5)
    ax.set_xticks(range(1, 6)); ax.set_yticks(range(1, 6))
    ax.set_xlabel("probabilidad →", fontsize=7.6); ax.set_ylabel("impacto →", fontsize=7.6)
    cajetin(fig, "UMC-T-RSK-001-R02", "Mapa de riesgos del Proyecto 04", "s/e (matriz)")
    guardar(fig, FIG + "G-15_mapa_riesgos.png")


# ----------------------------------------------------------------------------- LÁMINAS P
def _cajetin_lamina(ax, codigo, denom, escala, npt, area=""):
    ax.text(.5, .015, f"{codigo} · {denom} · Esc. {escala} · NPT {npt} · Rev. {REV} · {FECHA}",
            transform=ax.transAxes, fontsize=6.6, color=AZUL, ha="center")
    ax.text(.5, -.045, SELLO, transform=ax.transAxes, fontsize=6.8, color=ROJO,
            ha="center", weight="bold")
    if area:
        ax.text(.99, .985, area, transform=ax.transAxes, fontsize=6.6, color="#33475a",
                ha="right", va="top")


def lamina_planta_torre(nivel, npt, prog, codigo, fn):
    fig, ax = plt.subplots(figsize=(8.4, 11.0), dpi=300)
    ax.set_axis_off()
    fig.subplots_adjust(left=.06, right=.94, top=.93, bottom=.10)
    ax.text(.5, .985, f"UMC · TORRE DE OBSERVACIÓN / PUENTE DE MANDO · {nivel}",
            transform=ax.transAxes, fontsize=11, color=AZUL, weight="bold", ha="center")
    # huella 3,60 x 3,75
    W, H = 3.60, 3.75
    ox, oy = 4.0, 6.0
    ax.add_patch(Rectangle((ox, oy), W, H, fc="#f4f7f9", ec=AZUL, lw=2.2))
    # núcleo escalera
    ax.add_patch(Rectangle((ox + .15, oy + .15), 1.05, 1.5, fc="#e5ebef", ec=ACERO, lw=1.0))
    ax.text(ox + .67, oy + .9, "ESCALERA\nNº 4", ha="center", va="center", fontsize=6.2, color=ACERO)
    for x, y, w, h, s in prog:
        ax.add_patch(Rectangle((ox + x, oy + y), w, h, fill=False, ec=GRIS, lw=.8, ls=":"))
        ax.text(ox + x + w / 2, oy + y + h / 2, s, ha="center", va="center", fontsize=6.0, color="#33475a")
    # ejes
    for i, xx in enumerate([0, 1.2, 2.4, 3.6]):
        ax.add_line(Line2D([ox + xx, ox + xx], [oy - .5, oy + H + .5], color=GRIS, lw=.5, ls="--"))
        ax.add_patch(Circle((ox + xx, oy + H + .7), .18, fc="white", ec=AZUL, lw=1.0))
        ax.text(ox + xx, oy + H + .7, str(i + 1), ha="center", va="center", fontsize=6.4, color=AZUL)
    for i, yy in enumerate([0, 1.25, 2.5, 3.75]):
        ax.add_line(Line2D([ox - .5, ox + W + .5], [oy + yy, oy + yy], color=GRIS, lw=.5, ls="--"))
        ax.add_patch(Circle((ox - .7, oy + yy), .18, fc="white", ec=AZUL, lw=1.0))
        ax.text(ox - .7, oy + yy, "ABCD"[i], ha="center", va="center", fontsize=6.4, color=AZUL)
    ax.text(ox + W / 2, oy - .95, "3,60 m", ha="center", fontsize=7.4, color=AZUL, weight="bold")
    ax.text(ox - 1.35, oy + H / 2, "3,75 m", ha="center", fontsize=7.4, color=AZUL,
            weight="bold", rotation=90)
    _cajetin_lamina(ax, codigo, f"Planta {nivel}", "1:200", npt, "huella 13,50 m² · retícula 1,20 m")
    guardar(fig, LAM + fn)


def p_laminas():
    # P-1..P-5 plantas por nivel
    prog_n0 = [(.15, 1.8, 2.1, 1.8, "VESTÍBULO /\nFOYER\nCEREMONIAL"),
               (2.4, 1.8, 1.05, 1.8, "SS +\nlimpieza")]
    prog_n1 = [(1.35, .15, 2.1, 1.5, "PUESTO DE\nOBSERVACIÓN\nY VIGILANCIA"),
               (1.35, 1.8, 2.1, 1.8, "AULA-TALLER DE\nMETEOROLOGÍA\nMARINA")]
    prog_n2 = [(1.35, .15, 2.1, 3.45, "ESTACIÓN DE REGISTRO\nY SERVIDORES\n(sala técnica de\ninstrumentos)")]
    prog_n3 = [(1.35, .15, 2.1, 3.45, "SALA DE INVESTIGACIÓN\nHIDROMETEOROLÓGICA\nY GEMELO DIGITAL")]
    prog_n4 = [(0.15, 0.15, 3.3, 3.45, "PUENTE DE MANDO /\nCUBIERTA DE\nOBSERVACIÓN\naforo 20 personas")]
    datos = [("NIVEL 0", "±0,000", prog_n0, "UMC-T-ARQ-101-PB-R02", "P-01_planta_N0.png"),
             ("NIVEL 1", "+4,400", prog_n1, "UMC-T-ARQ-102-P1-R02", "P-02_planta_N1.png"),
             ("NIVEL 2", "+8,800", prog_n2, "UMC-T-ARQ-103-P2-R02", "P-03_planta_N2.png"),
             ("NIVEL 3", "+13,200", prog_n3, "UMC-T-ARQ-104-P3-R02", "P-04_planta_N3.png"),
             ("NIVEL 4", "+17,600", prog_n4, "UMC-T-ARQ-105-P4-R02", "P-05_planta_N4.png")]
    for d in datos:
        lamina_planta_torre(*d)

    # P-6 planta sala
    fig, ax = plt.subplots(figsize=(8.4, 11.0), dpi=300); ax.set_axis_off()
    fig.subplots_adjust(left=.06, right=.94, top=.93, bottom=.10)
    ax.text(.5, .985, "UMC · SALA TÉCNICA DE INVESTIGACIÓN HIDROMETEOROLÓGICA · PLANTA",
            transform=ax.transAxes, fontsize=11, color=VERDE, weight="bold", ha="center")
    ox, oy = 3.0, 5.0
    ax.add_patch(Rectangle((ox, oy), 5.5, 7.0, fc="#f2f7f2", ec=VERDE, lw=2.2))
    for (x, y, w, h, s) in [(0, 0, 3.0, 3.0, "ESTACIONES DE\nTRABAJO\n8,66 m²"),
                            (3.0, 0, 2.5, 2.0, "SERVIDORES /\nREGISTRO\n4,81 m²"),
                            (3.0, 2.0, 2.5, 1.4, "CIRCULACIÓN\n5,78 m²"),
                            (0, 3.0, 1.6, 1.6, "SS\n2,89 m²"),
                            (1.6, 3.0, 1.4, 1.6, "MESÓN\n2,17 m²"),
                            (0, 4.6, 5.5, 2.4, "ÁREA LIBRE / MUROS / ESTRUCTURA  14,19 m²")]:
        ax.add_patch(Rectangle((ox + x, oy + y), w, h, fill=False, ec=GRIS, lw=.9))
        ax.text(ox + x + w / 2, oy + y + h / 2, s, ha="center", va="center", fontsize=6.2, color="#33475a")
    ax.add_patch(Rectangle((ox + 2.2, oy - .35), 1.1, .35, fc=VERDE))
    ax.text(ox + 2.75, oy - .55, "acceso", ha="center", fontsize=6.4, color=VERDE)
    ax.text(ox + 2.75, oy - 1.1, "5,50 m", ha="center", fontsize=7.6, color=VERDE, weight="bold")
    ax.text(ox - .8, oy + 3.5, "7,00 m", ha="center", fontsize=7.6, color=VERDE, weight="bold", rotation=90)
    _cajetin_lamina(ax, "UMC-S-ARQ-101-R02", "Planta Sala Técnica", "1:200", "±0,000",
                    "huella 38,50 m² · programa 40,00 m²")
    guardar(fig, LAM + "P-06_planta_sala.png")

    # P-7 sección vertical
    fig, ax = plt.subplots(figsize=(8.4, 11.0), dpi=300); ax.set_axis_off()
    fig.subplots_adjust(left=.06, right=.94, top=.93, bottom=.10)
    ax.text(.5, .985, "UMC · TORRE DE OBSERVACIÓN · SECCIÓN VERTICAL A–A",
            transform=ax.transAxes, fontsize=11, color=AZUL, weight="bold", ha="center")
    npt = [("N0", 0.0), ("N1", 4.4), ("N2", 8.8), ("N3", 13.2), ("N4", 17.6)]
    for n, z in npt:
        ax.add_patch(Rectangle((4, z), 3.6, .35, fc=ACERO, ec=ACERO))
        ax.text(3.6, z + .18, f"{n}  +{z:05.3f}".replace("+00.000", "±0.000"),
                ha="right", fontsize=7, color=AZUL, weight="bold")
    for z in (0, 4.4, 8.8, 13.2, 17.6):
        ax.add_line(Line2D([4, 7.6], [z, z + 4.4], color=ACERO, lw=0))
    for x in (4, 7.6):
        ax.add_line(Line2D([x, x], [0, 22.02], color=ACERO, lw=2.0))
    ax.add_line(Line2D([3.4, 8.2], [22.02, 22.02], color=ROJO, lw=2.2))
    ax.text(8.5, 22.02, "coronación +22,02 m\n(altura adoptada)", fontsize=7.2, color=ROJO, weight="bold")
    ax.add_line(Line2D([5.8, 5.8], [22.02, 26.0], color=ROJO, lw=1.6))
    ax.text(6.0, 25.0, "asta y pararrayos\n(reposición distinguible)", fontsize=6.8, color=ROJO)
    ax.add_line(Line2D([3.4, 8.2], [12.2, 12.2], color=GRIS, lw=1.0, ls=":"))
    ax.text(8.5, 12.2, "12,20 m · altura original\n(15 DF 30 Nº 86, ANULADA)", fontsize=6.8, color=GRIS)
    ax.add_patch(Rectangle((3.2, -2.4), 5.2, 2.4, fc="#d8cbb6", ec=OCRE, lw=1.2))
    ax.text(5.8, -1.2, "cabezales y pilotes existentes", ha="center", fontsize=6.8, color=OCRE)
    for z in (0, 4.4, 8.8, 13.2, 17.6, 22.02):
        ax.add_line(Line2D([2.6, 2.9], [z, z], color=GRIS, lw=.6))
    ax.set_xlim(0, 16); ax.set_ylim(-4, 28)
    _cajetin_lamina(ax, "UMC-T-ARQ-301-R02", "Sección vertical A–A", "1:100", "±0,000 → +22,020")
    guardar(fig, LAM + "P-07_seccion_vertical.png")

    # P-8 fachadas
    fig, axes = plt.subplots(1, 4, figsize=(15.0, 8.0), dpi=300)
    fig.subplots_adjust(left=.03, right=.97, top=.88, bottom=.14)
    fig.text(.03, .965, "UMC · TORRE DE OBSERVACIÓN · FACHADAS (4)", fontsize=12,
             color=AZUL, weight="bold")
    for k, (nm, ax) in enumerate(zip(["NORTE (Proa)", "ESTE", "SUR (Popa)", "OESTE (Babor)"], axes)):
        ax.set_axis_off()
        ax.add_patch(Rectangle((0, 0), 3.6, 22.02, fc="#eef2f5", ec=ACERO, lw=1.6))
        for z in (4.4, 8.8, 13.2, 17.6):
            ax.add_line(Line2D([0, 3.6], [z, z], color=ACERO, lw=.9))
        for z in (0.9, 5.3, 9.7, 14.1, 18.5):
            ax.add_patch(Rectangle((.5, z), 2.6, 2.2, fc="#cfe0ea", ec=ACERO, lw=.7))
        ax.add_line(Line2D([-.6, 4.2], [22.02, 22.02], color=ROJO, lw=1.8))
        ax.text(1.8, 23.4, nm, ha="center", fontsize=8.4, color=AZUL, weight="bold")
        ax.text(1.8, -1.6, "bandas horizontales blancas · vidriado azul-verde\nde control solar · coronamiento técnico plano",
                ha="center", fontsize=6.2, color="#33475a")
        ax.set_xlim(-1.4, 5.0); ax.set_ylim(-3, 25)
    _cajetin_lamina(axes[1], "UMC-T-ARQ-201/204-R02", "Fachadas (4)", "1:200", "—")
    guardar(fig, LAM + "P-08_fachadas.png")

    # P-9 cubierta técnica
    fig, ax = plt.subplots(figsize=(8.4, 11.0), dpi=300); ax.set_axis_off()
    fig.subplots_adjust(left=.06, right=.94, top=.93, bottom=.10)
    ax.text(.5, .985, "UMC · TORRE DE OBSERVACIÓN · CUBIERTA TÉCNICA E INSTRUMENTOS",
            transform=ax.transAxes, fontsize=10.4, color=AZUL, weight="bold", ha="center")
    ox, oy = 4.0, 6.0
    ax.add_patch(Rectangle((ox, oy), 3.6, 3.75, fc="#f4f7f9", ec=AZUL, lw=2.0))
    ax.add_patch(Circle((ox + 1.0, oy + 1.0), .28, fc=ROJO, ec=ROJO))
    ax.text(ox + 1.5, oy + 1.0, "base de asta\n+ pararrayos", fontsize=6.2, color=ROJO)
    ax.add_patch(Rectangle((ox + 2.2, oy + .3), 1.0, 1.0, fc="#dfe8ee", ec=ACERO, lw=1.0))
    ax.text(ox + 2.7, oy + .8, "FV\n2,0 kWp", ha="center", va="center", fontsize=5.8, color=ACERO)
    ax.add_patch(Rectangle((ox + 2.2, oy + 1.7), 1.0, .8, fc="#dbe7dd", ec=VERDE, lw=1.0))
    ax.text(ox + 2.7, oy + 2.1, "AWS /\nantenas", ha="center", va="center", fontsize=5.8, color=VERDE)
    ax.add_patch(Rectangle((ox + .3, oy + 2.4), 1.4, 1.0, fc="#e5ebef", ec=GRIS, lw=.9))
    ax.text(ox + 1.0, oy + 2.9, "salida\nescalera", ha="center", va="center", fontsize=5.8, color=GRIS)
    ax.text(ox + 1.8, oy - .8, "terraza de observación perimetral\ncon baranda de seguridad h = 1,20 m",
            ha="center", fontsize=6.4, color="#33475a")
    _cajetin_lamina(ax, "UMC-T-ARQ-106-CT-R02", "Cubierta técnica", "1:100", "+22,020")
    guardar(fig, LAM + "P-09_cubierta_tecnica.png")

    # P-0 implantación (versión lámina)
    fig, ax = plt.subplots(figsize=(15.0, 8.4), dpi=300); ax.set_axis_off()
    fig.subplots_adjust(left=.03, right=.97, top=.88, bottom=.14)
    fig.text(.03, .965, "UMC · IMPLANTACIÓN GENERAL GEORREFERENCIADA DEL ÁREA CULTURAL · ESCALA 1:400",
             fontsize=12, color=AZUL, weight="bold")
    ax.add_patch(Rectangle((1.0, 1.0), 9.0, 5.0, fc="#dfe8ee", ec=ACERO, lw=1.4))
    ax.text(5.5, 3.5, "AULA MAGNA / AUDITORIO (F1)", ha="center", fontsize=8.4, color=AZUL, weight="bold")
    ax.add_patch(Rectangle((10.2, 4.6), .90, .94, fc=ROJO, ec=ROJO, alpha=.85))
    ax.add_patch(Rectangle((10.35, 2.6), 1.375, 1.75, fc=VERDE, ec=VERDE, alpha=.8))
    ax.add_patch(Rectangle((12.6, 1.0), 5.5, 5.6, fc="#f3efe2", ec=OCRE, lw=1.0, ls=":"))
    ax.text(15.3, 3.8, "PLAZA DE HONOR", ha="center", fontsize=8, color=OCRE)
    ax.add_patch(Rectangle((1.0, 6.9), 17.1, .8, fc="#e8eef2", ec=GRIS, lw=.6))
    ax.text(9.5, 7.3, "ESPINA PEATONAL 4,00 m", fontsize=7, color=GRIS)
    rows = [["Punto", "Lat (WGS84)", "Lon (WGS84)", "Condición"],
            ["C-TO (torre)", "10,60082778", "−67,03229444", "centroide documental"],
            ["C-STH (sala)", "10,60085833", "−67,03228333", "centroide documental"],
            ["PI (VRA)", "10,59797222", "−67,03075556", "control del expediente P03"]]
    tabla(fig, rows, x=.60, y=.42, w=.37, colw=[.28, .24, .26, .22], fs=6.8)
    ax.set_xlim(0, 20); ax.set_ylim(0, 8.6); ax.set_aspect("equal")
    _cajetin_lamina(ax, "UMC-G-ARQ-001-R02", "Implantación general georreferenciada", "1:400", "—")
    guardar(fig, LAM + "P-00_implantacion_general.png")


if __name__ == "__main__":
    import os
    os.makedirs(FIG, exist_ok=True); os.makedirs(LAM, exist_ok=True)
    for f in (g01, g02, g03, g04, g05, g06, g07, g08, g09, g10, g11, g12, g13, g14, g15):
        f(); print("  fig OK", f.__name__)
    p_laminas(); print("  láminas OK")
    print("TOTAL figs:", len(os.listdir(FIG)), "| láminas:", len(os.listdir(LAM)))

# -*- coding: utf-8 -*-
"""
memoria.py — Memoria descriptiva del proyecto "Bloque Dormitorios"
Genera un PDF A4 con la memoria del trabajo y el listado de láminas.

Uso:  python3 memoria.py [--out DIR]
"""
import argparse
import os
import sys

from reportlab.lib import colors
from reportlab.lib.enums import TA_JUSTIFY, TA_CENTER
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.platypus import (BaseDocTemplate, Frame, Image, PageTemplate, Paragraph,
                                Spacer, Table, TableStyle, KeepTogether)

AZUL = colors.HexColor('#14456e')
GRIS = colors.HexColor('#555555')
CLARO = colors.HexColor('#eef3f8')

FECHA = '4 de octubre de 2026'
PROYECTO = 'Bloque Dormitorios — dos niveles (planta baja y planta alta)'
PROMOTOR = 'JMDSI · Área de Proyectos'

ESTILOS = getSampleStyleSheet()


def E(nombre, **kw):
    base = dict(fontName='Helvetica', fontSize=9.6, leading=13.2,
                textColor=colors.HexColor('#1a1a1a'), alignment=TA_JUSTIFY,
                spaceAfter=4)
    base.update(kw)
    return ParagraphStyle(nombre, **base)


S_TIT = E('tit', fontName='Helvetica-Bold', fontSize=17, leading=20,
          alignment=TA_CENTER, textColor=AZUL, spaceAfter=2)
S_SUB = E('sub', fontSize=11, leading=14, alignment=TA_CENTER, textColor=GRIS,
          spaceAfter=10)
S_H1 = E('h1', fontName='Helvetica-Bold', fontSize=12.4, leading=15, textColor=AZUL,
         spaceBefore=12, spaceAfter=4, alignment=0)
S_H2 = E('h2', fontName='Helvetica-Bold', fontSize=10.4, leading=13, textColor=GRIS,
         spaceBefore=8, spaceAfter=3, alignment=0)
S_P = E('p')
S_B = E('b', bulletIndent=2, leftIndent=12, spaceAfter=2.5)
S_CH = E('ch', fontName='Helvetica', fontSize=8.2, leading=10.4, alignment=0)
S_CHC = E('chc', fontName='Helvetica', fontSize=8.2, leading=10.4, alignment=TA_CENTER)
S_CHB = E('chb', fontName='Helvetica-Bold', fontSize=8.2, leading=10.4,
          textColor=colors.white, alignment=TA_CENTER)
S_NOTA = E('nota', fontSize=8.4, leading=11, textColor=GRIS)


EST = dict(p=S_P, b=S_B, h1=S_H1, h2=S_H2, ch=S_CH, chc=S_CHC, chb=S_CHB,
           nota=S_NOTA, tit=S_TIT, sub=S_SUB)


def P(t, s='p'):
    return Paragraph(t, EST[s])


def tabla(datos, anchos, alinear_derecha=()):
    filas = []
    for i, fila in enumerate(datos):
        r = []
        for j, celda in enumerate(fila):
            if i == 0:
                r.append(Paragraph(str(celda), S_CHB))
            else:
                r.append(Paragraph(str(celda), S_CHC if j in alinear_derecha else S_CH))
        filas.append(r)
    t = Table(filas, colWidths=anchos, repeatRows=1)
    est = [('BACKGROUND', (0, 0), (-1, 0), AZUL),
           ('GRID', (0, 0), (-1, -1), 0.4, colors.HexColor('#9bb3c8')),
           ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
           ('TOPPADDING', (0, 0), (-1, -1), 2.4),
           ('BOTTOMPADDING', (0, 0), (-1, -1), 2.4)]
    for i in range(1, len(filas)):
        if i % 2 == 0:
            est.append(('BACKGROUND', (0, i), (-1, i), CLARO))
    t.setStyle(TableStyle(est))
    return t


# ---------------------------------------------------------------------------
def cabecera_pie(canvas, doc):
    canvas.saveState()
    canvas.setStrokeColor(AZUL)
    canvas.setLineWidth(0.8)
    canvas.rect(14 * mm, 14 * mm, A4[0] - 28 * mm, A4[1] - 28 * mm)
    canvas.setFillColor(AZUL)
    canvas.rect(14 * mm, A4[1] - 22 * mm, A4[0] - 28 * mm, 8 * mm, stroke=0, fill=1)
    canvas.setFillColor(colors.white)
    canvas.setFont('Helvetica-Bold', 8.6)
    canvas.drawString(16 * mm, A4[1] - 19.4 * mm,
                      'MEMORIA DEL TRABAJO  ·  BLOQUE DORMITORIOS  ·  JMDSI')
    canvas.drawRightString(A4[0] - 16 * mm, A4[1] - 19.4 * mm, '2026-10-04')
    canvas.setFillColor(GRIS)
    canvas.setFont('Helvetica', 7.6)
    canvas.drawString(16 * mm, 16.6 * mm,
                      'JMDSI · Ingeniería y Arquitectura — documentación de proyecto '
                      '(revisión 01)')
    canvas.drawRightString(A4[0] - 16 * mm, 16.6 * mm, 'Página %d' % doc.page)
    canvas.restoreState()


def construir(path, outdir):
    doc = BaseDocTemplate(path, pagesize=A4, title='Memoria del trabajo — Bloque '
                          'Dormitorios', author='JMDSI',
                          subject='Memoria descriptiva y de cálculo',
                          leftMargin=18 * mm, rightMargin=18 * mm,
                          topMargin=24 * mm, bottomMargin=20 * mm)
    marco = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height, id='n')
    doc.addPageTemplates([PageTemplate(id='all', frames=[marco],
                                       onPage=cabecera_pie)])

    F = []
    F.append(Spacer(1, 6))
    F.append(P('MEMORIA DESCRIPTIVA Y DE DISEÑO', 'tit'))
    F.append(P('Bloque Dormitorios — planta baja y planta alta<br/>'
               'Arquitectura · estructuras · instalaciones (esquemático)', 'sub'))

    F.append(tabla([
        ['Dato', 'Contenido'],
        ['Proyecto', PROYECTO],
        ['Promotor / autor', PROMOTOR],
        ['Ubicación', 'Campus JMDSI — predio de 100,00 × 100,00 m (10 000 m²)'],
        ['Fecha', FECHA],
        ['Documentos', 'Láminas A-01 a A-06, S-01 y BLU-00 / BLU-01 / BLU-02 '
         '(blueprint, también en JPG) + presente memoria'],
        ['Normativa de referencia', 'Criterios de diseño de alojamientos colectivos: '
         'circulación ≥ 1,20 m, puertas ≥ 0,80 m, altura libre ≥ 2,50 m'],
    ], [40 * mm, 132 * mm]))

    # ------------------------------------------------------------------ 1
    F.append(P('1. Objeto y alcance', 'h1'))
    F.append(P('La presente memoria acompaña al juego de planos del <b>Bloque '
               'Dormitorios</b>, edificio de dos niveles destinado a alojamiento de '
               'estudiantes, y describe la solución arquitectónica, los criterios '
               'estructurales y las instalaciones previstas. El alcance corresponde a '
               'un <b>anteproyecto avanzado / proyecto básico</b>: define geometría, '
               'dimensionado, niveles, materiales y sistema constructivo, con detalles '
               'que deberán completarse en la fase de proyecto de detalle y de '
               'especialidades.'))
    F.append(P('Los planos que desarrollan la memoria son: A-01 planta baja, A-02 '
               'planta alta, A-03 cortes A-A y B-B con detalles, A-04 fachadas, A-05 '
               'planta de azotea y situación, A-06 cortes y fachadas (niveles bajo y '
               'alto) con miniatura de situación, S-01 planta de situación a escala y '
               'BLU-00, BLU-01 y BLU-02 en versión blueprint (cianotipo), también '
               'en JPG.'))

    # ------------------------------------------------------------------ 2
    F.append(P('2. Descripción del edificio', 'h1'))
    F.append(P('El bloque se resuelve como una <b>barra de 24,00 m de longitud por '
               '9,60 m de ancho</b> con un <b>pasillo central de 1,70 m</b> de ancho '
               'libre que organiza los recintos en dos hileras: ocho dormitorios '
               'dobles y los servicios higiénicos. El núcleo de circulación vertical '
               '(escalera de dos tramos) más el vestíbulo de acceso ocupan el extremo '
               'este de la planta baja, y la escalera junto con la sala de estar y '
               'estudio el de la planta alta.'))
    F.append(P('La estructura es <b>aporticada-confinada</b>: muros de albañilería '
               'de 0,25 m en las fachadas y 0,15 m en los tabiques, confinados con '
               'columnas y vigas de amarre, y <b>losas aligeradas de 0,30 m</b> de '
               'espesor en los dos niveles. Las luces libres de la losa son de 3,35 m '
               'en los dormitorios y 3,70 m en el núcleo, ambas dentro del rango '
               'habitual para este sistema.'))
    F.append(P('La comunicación vertical se resuelve con una escalera de dos tramos y '
               'descanso intermedio: <b>18 contrahuellas de 0,181 m</b> y huella de '
               '0,28 m, lo que arroja una pendiente de 33°, dentro de los límites '
               'recomendados para escaleras principales.'))

    F.append(P('2.1. Niveles y alturas', 'h2'))
    F.append(tabla([
        ['Nivel', 'Cota', 'Altura libre', 'Destino'],
        ['Terreno natural (NTN)', '−0,45', '—', 'Exterior / veredas'],
        ['N.P.T. planta baja', '±0,00', '2,90 m',
         '8 dormitorios, 2 SS.HH., depósito, lavandería, vestíbulo'],
        ['N.P.T. planta alta', '+3,25', '2,60 m',
         '8 dormitorios, 2 SS.HH., sala de estar y estudio'],
        ['N.P.T. azotea', '+6,20', '—', 'Cubierta inaccesible con pendiente 2 %'],
        ['Remate de parapeto', '+7,15', '0,95 m', 'Parapeto perimetral + albardilla'],
    ], [36 * mm, 18 * mm, 22 * mm, 96 * mm], alinear_derecha=(1,)))

    # ------------------------------------------------------------------ 3
    F.append(P('3. Programa arquitectónico y áreas', 'h1'))
    F.append(P('Se anexa el cuadro de áreas por recinto (superficies útiles '
               'interiores). La planta baja y la planta alta son simétricas en la '
               'hilera de dormitorios, lo que optimiza la estructura y las '
               'instalaciones.'))
    filas = [['Nivel', 'Recinto tipo', 'Dimensiones', 'Área', 'Cant.', 'Área total']]
    prog = [
        ['Baja', 'Dormitorio doble (2 camas)', '3,20 × 3,55 m', '11,36 m²', '8', '90,88 m²'],
        ['Baja', 'SS.HH. (3 inod. / 3 lav. / 2 duchas)', '2,85 × 3,55 m', '10,12 m²', '2', '20,24 m²'],
        ['Baja', 'Vestíbulo / recepción', '3,40 × 3,70 m', '12,58 m²', '1', '12,58 m²'],
        ['Baja', 'Depósito / cuarto técnico', '3,55 × 3,55 m', '12,60 m²', '1', '12,60 m²'],
        ['Baja', 'Lavandería', '3,55 × 3,55 m', '12,60 m²', '1', '12,60 m²'],
        ['Baja', 'Pasillo / distribuidor', '16,40 × 1,70 m', '27,80 m²', '1', '27,80 m²'],
        ['Alta', 'Dormitorio doble (2 camas)', '3,20 × 3,55 m', '11,36 m²', '8', '90,88 m²'],
        ['Alta', 'SS.HH. (3 inod. / 3 lav. / 2 duchas)', '2,85 × 3,55 m', '10,12 m²', '2', '20,24 m²'],
        ['Alta', 'Sala de estar y estudio', '3,40 × 3,70 m', '12,58 m²', '1', '12,58 m²'],
        ['Alta', 'Sala de estudio complementaria', '3,55 × 3,55 m', '12,60 m²', '1', '12,60 m²'],
        ['Alta', 'Depósito / ropería', '3,55 × 3,55 m', '12,60 m²', '1', '12,60 m²'],
        ['Alta', 'Pasillo / distribuidor', '16,40 × 1,70 m', '27,80 m²', '1', '27,80 m²'],
    ]
    filas += prog
    F.append(tabla(filas, [16 * mm, 68 * mm, 30 * mm, 20 * mm, 14 * mm, 24 * mm],
                   alinear_derecha=(3, 4, 5)))
    F.append(Spacer(1, 3))
    F.append(P('Ocupación: 32 camas (16 por nivel) en 16 dormitorios dobles. '
               'Superficie construida aproximada: 2 × 24,00 × 9,60 = <b>460,80 m²</b> '
               'más caseta de escalera en azotea (13,60 m²).', 'nota'))

    # ------------------------------------------------------------------ 4
    F.append(P('4. Criterios de diseño y verificación normativa', 'h1'))
    ver = [
        ['Requisito', 'Valor exigido', 'Valor de proyecto', 'Estado'],
        ['Ancho libre de pasillo', '≥ 1,20 m', '1,70 m', 'Cumple'],
        ['Ancho de puerta de dormitorio', '≥ 0,80 m', '0,90 m', 'Cumple'],
        ['Ancho de puerta de SS.HH.', '≥ 0,70 m', '0,80 m', 'Cumple'],
        ['Altura libre de piso a cielo', '≥ 2,50 m', '2,90 / 2,60 m', 'Cumple'],
        ['Ventilación e iluminación natural', '≥ 1/8 del área', '1,50 × 1,50 m por '
         'dormitorio', 'Cumple'],
        ['Escalera: contrahuella / huella', 'máx. 0,18 / mín. 0,28 m',
         '0,181 / 0,28 m', 'Cumple'],
        ['Escalera: ancho de tramo', '≥ 1,20 m', '1,60 m', 'Cumple'],
        ['Distancia máxima de recorrido', '≤ 45 m', '≈ 26 m', 'Cumple'],
        ['Accesibilidad: rampa o peldaños de ingreso', '3 peldaños ≤ 0,15 m',
         '3 × 0,15 m + descanso', 'Cumple'],
    ]
    F.append(tabla(ver, [58 * mm, 34 * mm, 46 * mm, 20 * mm]))
    F.append(P('Los criterios se adoptan de prácticas habituales para alojamientos '
               'colectivos y vivienda multifamiliar; en fase de proyecto se ajustarán '
               'a la norma nacional aplicable y a las condiciones de la autoridad '
               'competente.', 'nota'))

    F.append(P('4.1. Ventilación e iluminación', 'h2'))
    F.append(P('Todos los dormitorios cuentan con <b>ventilación cruzada</b>: cada '
               'recinto tiene ventana a fachada y la puerta al pasillo, que a su vez '
               'ventila por el núcleo. Los SS.HH. disponen de ventana alta (0,50 × '
               '0,80 m) y ducto de ventilación vertical que sobresale en azotea.'))

    F.append(P('4.2. Seguridad y evacuación', 'h2'))
    F.append(P('Se prevé señalización de emergencia, extintores cada 20 m de '
               'recorrido y alumbrado de emergencia en pasillo y escalera. En fase '
               'de detalle se verificará la resistencia al fuego de la estructura y '
               'la compartimentación de la escalera respecto del vestíbulo.'))

    # ------------------------------------------------------------------ 5
    F.append(P('5. Solución estructural', 'h1'))
    F.append(P('5.1. Cimentación', 'h2'))
    F.append(P('Cimiento corrido de concreto ciclópeo de <b>0,70 × 0,25 m</b>, '
               'desplantado a <b>−1,05 m</b> (fondo) y sobrecimiento de 0,25 × '
               '0,60 m hasta la solera. Sobre el terreno natural apisonado se '
               'coloca relleno compactado y falso piso. En losas de piso se prevé '
               'junta de construcción con malla electrosoldada.'))
    F.append(P('5.2. Muros', 'h2'))
    F.append(P('Muros de albañilería confinada de 0,25 m (perimetrales) y 0,15 m '
               '(tabiques), con columnas de amarre en la intersección de ejes y '
               'vigas soleras en cada nivel. Se prevén mochetas y ductos verticales '
               'en los SS.HH.'))
    F.append(P('5.3. Losas y cubierta', 'h2'))
    F.append(P('Losas aligeradas de <b>h = 0,30 m</b> en el entrepiso y en la '
               'cubierta, con capa de compresión de 5 cm y ladrillo de techo '
               '(bovedilla). Las luces libres a cubrir son de 3,35 y 3,70 m. La '
               'cubierta es inaccesible, con <b>pendiente del 2 %</b> hacia '
               'sumideros y parapeto perimetral de 0,95 m con albardilla de '
               'concreto.'))
    F.append(P('5.4. Predimensionado de losas (referencia)', 'h2'))
    F.append(tabla([
        ['Losa', 'Luz libre', 'c (cm)', 'h (cm)', 'Predimensionado'],
        ['Dormitorios (tramo con muros perpendiculares)', '3,35 m', '25', '30',
         'h = L/16 ≈ 21 cm → <b>se adopta 30 cm</b>'],
        ['Núcleo / pasillo con luces mayores', '3,70 m', '25', '30',
         'h = L/16 ≈ 23 cm → <b>se adopta 30 cm</b>'],
        ['Voladizos y aleros', '0,60 m', '—', '—', 'Viga de borde peraltada'],
    ], [64 * mm, 20 * mm, 16 * mm, 16 * mm, 42 * mm], alinear_derecha=(1, 2, 3)))
    F.append(P('El predimensionado es referencial y deberá verificarse con el '
               'análisis estructural definitivo (norma de concreto armado y norma '
               'sismorresistente vigentes).', 'nota'))

    # ------------------------------------------------------------------ 6
    F.append(P('6. Instalaciones (esquemático)', 'h1'))
    F.append(P('6.1. Sanitarias', 'h2'))
    F.append(P('Se proyectan dos baterías de SS.HH. por nivel sobre los mismos '
               'ejes, para concentrar montantes y ductos. Cisterna de 12 m³ y '
               'tanque elevado de 2 × 1 100 L en azotea, con alimentación por '
               'bombeo. Redes de desagüe de PVC Ø 4" con ventilación vertical y '
               'montantes cortas hasta el ducto común.'))
    F.append(P('6.2. Pluviales', 'h2'))
    F.append(P('Cuatro bajantes pluviales de PVC Ø 4" en las esquinas, con '
               'sumideros de 2" en la azotea y pendiente de 2 % hacia ellos.'))
    F.append(P('6.3. Eléctricas', 'h2'))
    F.append(P('Tablero general en vestíbulo de planta baja y tablero de '
               'distribución por nivel. Circuitos independientes para alumbrado y '
               'tomacorrientes; previsión de circuito para equipos de cómputo en '
               'escritorios y de fuerza para bombas y terma.'))
    F.append(P('6.4. Comunicaciones', 'h2'))
    F.append(P('Tubería para red de datos en cada dormitorio y sala de estudio, '
               'con rack de comunicaciones en el cuarto técnico de planta baja.'))

    # ------------------------------------------------------------------ 7
    F.append(P('7. Vanos, acabados y mobiliario', 'h1'))
    F.append(tabla([
        ['Código', 'Tipo', 'Medidas', 'Ubicación', 'Cant.'],
        ['P-1', 'Puerta 1 hoja', '0,90 × 2,10', 'Dormitorios, depósito, lavandería',
         '20'],
        ['P-2', 'Puerta 1 hoja', '0,80 × 2,10', 'SS.HH. (por nivel)', '4'],
        ['P-3', 'Puerta 2 hojas', '1,80 × 2,40', 'Ingreso principal', '1'],
        ['V-1', 'Ventana corredera 2 hojas', '1,50 × 1,50',
         'Dormitorios (ambos niveles)', '16'],
        ['V-2', 'Ventana alta', '0,50 × 0,80', 'SS.HH. (por nivel)', '4'],
        ['V-3', 'Ventanal', '2,00 × 1,70', 'Sala de estudio (planta alta)', '1'],
    ], [16 * mm, 44 * mm, 26 * mm, 62 * mm, 14 * mm], alinear_derecha=(4,)))
    F.append(Spacer(1, 3))
    F.append(P('Mobiliario de dormitorio tipo (11,36 m²): 2 camas de 1,00 × 2,00 m, '
               '2 escritorios de 1,20 × 0,60 m con silla, 1 ropero de 0,60 × 1,80 m '
               'y velador. SS.HH.: 3 inodoros, 3 lavabos, 2 duchas y 1 urinario.'))
    F.append(P('Acabados: muros tarrajeados y pintados con látex acrílico (2 manos); '
               'pisos de cerámico antideslizante en SS.HH. y porcelanato en '
               'dormitorios y pasillos; zócalos sanitarios en SS.HH.; carpintería de '
               'aluminio con vidrio templado de 6 mm en ventanas; puertas de madera '
               'también con marco de aluminio.'))
    F.append(KeepTogether([P('7.1. Cuadro de ejes (retícula estructural)', 'h2'),
                           tabla([
                               ['Eje', 'X (m)', 'Entre ejes', 'Eje', 'Y (m)',
                                'Entre ejes'],
                               ['A', '0,125', '—', '1', '0,125', '—'],
                               ['B', '3,525', '3,40', '2', '3,875', '3,75'],
                               ['C', '6,875', '3,35', '3', '5,725', '1,85'],
                               ['D', '10,225', '3,35', '4', '9,475', '3,75'],
                               ['E', '13,575', '3,35', '—', '—', '—'],
                               ['F', '16,575', '3,00', '—', '—', '—'],
                               ['G', '20,125', '3,55', '—', '—', '—'],
                               ['H', '23,875', '3,75', '—', '—', '—'],
                           ], [14 * mm, 20 * mm, 22 * mm, 14 * mm, 20 * mm, 22 * mm],
                               alinear_derecha=(1, 2, 4, 5))]))

    # ------------------------------------------------------------------ 8
    F.append(P('8. Listado de láminas', 'h1'))
    F.append(tabla([
        ['Lámina', 'Título', 'Escala', 'Formato'],
        ['A-01', 'Planta baja (±0,00) — arquitectura amoblada, ejes y cotas',
         '1:50', 'A1'],
        ['A-02', 'Planta alta (+3,25) — arquitectura amoblada, ejes y cotas',
         '1:50', 'A1'],
        ['A-03', 'Cortes A-A y B-B + detalles constructivos',
         '1:50 / 1:20 / 1:25', 'A1'],
        ['A-04', 'Fachadas sur, norte, este y oeste', '1:50', 'A1'],
        ['A-05', 'Planta de azotea y planta de situación', '1:75 / 1:280', 'A1'],
        ['A-06', 'Cortes y fachadas (baja y alta) con dimensiones + miniatura de '
         'situación', '1:100 / 1:600', 'A1'],
        ['S-01', 'Planta de situación del bloque en el conjunto', '1:200', 'A1'],
        ['BLU-00', 'Blueprint de conjunto — plantas, cortes, alzados y situación',
         '1:100 / 1:500', 'A0'],
        ['BLU-01', 'Blueprint — plantas baja y alta, corte y fachada', '1:75 / 1:100',
         'A1'],
        ['BLU-02', 'Blueprint — cortes y fachadas + situación', '1:100 / 1:600',
         'A1'],
    ], [18 * mm, 110 * mm, 26 * mm, 18 * mm]))
    F.append(Spacer(1, 3))
    F.append(P('Cada lámina se entrega en PDF (vectorial, listo para imprimir), SVG '
               '(editable), PNG (vista rápida) y DXF (CAD, dibujado a escala 1:1 en '
               'metros). Las versiones <b>blueprint</b> (BLU-00, BLU-01 y BLU-02) se '
               'entregan además en <b>JPG</b> para su uso directo en presentaciones y '
               'mensajería.', 'nota'))

    # ------------------------------------------------------------------ 9
    img = os.path.join(outdir, 'A-06_cortes_fachadas_situacion.png')
    if os.path.exists(img):
        from PIL import Image as PILImage
        w, h = PILImage.open(img).size
        ancho = 168 * mm
        F.append(P('9. Extracto de la lámina A-06', 'h1'))
        F.append(P('A continuación se reproduce la lámina A-06 «Cortes y fachadas '
                   '(planta baja y alta) con dimensiones y miniatura de situación», '
                   'que resume el partido adoptado para el bloque.', 'p'))
        F.append(Image(img, width=ancho, height=ancho * h / w))

    # ------------------------------------------------------------------ 10
    F.append(P('10. Prelación de documentos y observaciones', 'h1'))
    F.append(P('En caso de discrepancia entre documentos prevalece, en orden: '
               '(1) los planos de plantas A-01 y A-02 respecto de la geometría y '
               'dimensionado; (2) los cortes A-03 y A-06 respecto de niveles y '
               'alturas; (3) esta memoria respecto de criterios y especificaciones; '
               '(4) las versiones blueprint, que son reproducciones gráficas de las '
               'anteriores.'))
    F.append(P('Se advierte que este documento corresponde a una fase de proyecto '
               'básico: el dimensionado definitivo de la estructura, el detalle de '
               'las instalaciones y el cumplimiento de la normativa local deberán '
               'ser validados por profesional habilitado antes de la ejecución.'))

    doc.build(F)
    return path


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--out', default=os.path.join(os.path.dirname(os.path.dirname(
        os.path.abspath(__file__))), 'entrega'))
    args = ap.parse_args()
    os.makedirs(args.out, exist_ok=True)
    p = construir(os.path.join(args.out, 'MEMORIA_bloque_dormitorios.pdf'), args.out)
    print('Memoria generada:', p, '%.0f KB' % (os.path.getsize(p) / 1024.0))


if __name__ == '__main__':
    main()

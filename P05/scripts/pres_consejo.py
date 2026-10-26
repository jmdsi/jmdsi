# -*- coding: utf-8 -*-
"""PRESENTACION_UMC_2025-2030_CONSEJO-UNIVERSITARIO — Edición consolidada R05 (26-10-2026).
Genera HTML + PPTX. Fuentes: PDF R04 (P01–P03, Drive 1mNFzMc4de_hut8f27loJh4C5JEakMVXS),
expediente P04-R02 y expediente P05-R01 (este repositorio)."""
import base64, glob, html as H, os

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "entregables")
FIGD = os.path.join(OUT, "figuras")
BASE = "PRESENTACION_UMC_2025-2030_CONSEJO-UNIVERSITARIO"
FECHA = "26 de octubre de 2026"
SELLO = ("INGENIERÍA BÁSICA / ANTEPROYECTO — EMITIDO PARA COORDINACIÓN Y "
         "PRESUPUESTO PRELIMINAR — NO APTO PARA CONSTRUCCIÓN")
CONF = "Uso institucional UMC – Marina Mercante de Venezuela"

def figpng(cod):
    g = glob.glob(os.path.join(FIGD, "*FIGURA-%s_*.png" % cod))
    return g[0] if g else None

# Cada slide: dict(k=kicker, t=título, b=bullets, tab=(headers,rows), img=path, note=pie)
S = []
def sl(k, t, b=None, tab=None, img=None, note=None):
    S.append(dict(k=k, t=t, b=b or [], tab=tab, img=img, note=note))

sl("UNIVERSIDAD MARÍTIMA DEL CARIBE — MARINA MERCANTE DE VENEZUELA",
   "PLAN MAESTRO 2025–2030 · PROYECTO DE PLANTA FÍSICA E INFRAESTRUCTURA",
   ["Presentación para el Consejo Universitario y el Rectorado",
    "EDICIÓN CONSOLIDADA R05 · " + FECHA + " (actualiza la R04 del 14-09-2026)",
    "Expedientes: UMC2030-P01-CTSTCW-R04 · P02-CDP-R04 · P03-VRA-R04 · P04-TOBSHM-R02 · P05-EXTPCH-R01",
    "Cap. Alt. / Dr. Guillermo Antonio Riut Hernández — Rector",
    "Plan Maestro: Prof. Jhonny Da Silva Izquierdo, MSc. Ing. Lic. (CIV 95787)",
    "⚠ " + SELLO])

sl("NATURALEZA, ALCANCE Y LÍMITES", "CÓMO LEER ESTA PRESENTACIÓN",
   ["QUÉ ES: ingeniería básica/anteproyecto de cinco expedientes del Plan Maestro, coordinados como un único "
    "modelo de implantación; instrumento para decidir (programa, superficies, ROM AACE Clase 5, programación, riesgos).",
    "QUÉ NO ES: no es proyecto ejecutivo (sin cálculo estructural, memorias ni planos firmados); no es apto para "
    "replanteo ni construcción; no sustituye permisos; no acredita certificación del Centro de Datos.",
    "NOVEDAD R05: incorpora la respuesta al doblete sísmico del 24-06-2026 (Mw 7,2 + Mw 7,5) — expedientes "
    "P04 (Torre de Observación y Sala Técnica, R02) y P05 (Patio / Cubierta de Honor, R01).",
    "Todas las cifras son de anteproyecto; las condicionantes suspensivas se recogen al final."])

sl("CONTENIDO DE LA EXPOSICIÓN", "AGENDA",
   ["1 · Marco y antecedentes — Plan Maestro 2030, situación actual, alcance",
    "2 · El conjunto P01–P03 — implantación, corredor tecnológico-administrativo, síntesis",
    "3 · Los tres proyectos — Torre A STCW · Torre B CDP · Vicerrectorado Administrativo",
    "4 · NUEVO: el evento sísmico del 24-06-2026 y la Proa Central — P04 y P05",
    "5 · Inversión y plazos — ROM Clase 5 consolidado, programación, priorización",
    "6 · Riesgos y decisiones — condicionantes, RFI abiertas, acuerdos solicitados"])

sl("INSTRUMENTO RECTOR", "MARCO: EL PLAN MAESTRO UMC 2025–2030",
   ["Elaborado por el Prof. Jhonny Da Silva Izquierdo (MSc. Ing. Lic.) — zonificación del campus y doce proyectos estratégicos.",
    "Proyecto Nº 1 — Centro Tecnológico STCW «Ecosistemas – Laboratorios Marítimos Integrados» (Torre A), con Biblioteca UMC.",
    "Proyecto Nº 3 — Centro de Datos Principal CDP UMC Catia La Mar (Torre B), con Ciberseguridad y Sistemas.",
    "Edificación de tres plantas para el Vicerrectorado Administrativo.",
    "Proyectos complementarios: Talleres y Canal de Ensayos Hidrodinámicos, Piscina Olímpica, Aula Magna, "
    "sostenibilidad, señalización y paisajismo.",
    "Patrimonio de la Proa Central (obra MOP 1951–1958, Arq. L. Malaussena): Torre de Observación, Sala Técnica "
    "y Patio / Cubierta de Honor — hoy objeto de los expedientes P04 y P05."],
   note="Imágenes de zonificación y vistas satelitales: ver PDF fuente R04 en Drive (no reproducidas aquí).")

sl("PUNTO DE PARTIDA", "SITUACIÓN DEL CAMPUS: 2024 → 2026",
   ["2024: campus consolidado con déficit de simulación, laboratorios tecnológicos y servicios de gobierno; "
    "CDP actual sin condiciones para sostener la plataforma de simulación ni el Campus Virtual; enlace E-1 (CANTV) "
    "reubicable; sin residencias de Oficiales de Planta ni sala de seguridad integral.",
    "Respuesta P01–P03: 3 edificaciones nuevas · 9.745,92 m² de obra nueva · corredor de ≈ 119,4 m.",
    "24-06-2026 — DOBLETE SÍSMICO Mw 7,2 + Mw 7,5: afectación del litoral y del campus; la Proa Central ceremonial "
    "queda comprometida (Torre de Observación dañada, Patio de Honor inhabilitado, punto de evacuación R-1 suspendido).",
    "Respuesta P04–P05: consolidación de la Torre/Sala (P04-R02) y restauración integral del Patio de Honor (P05-R01)."])

sl("UNA SOLA IMPLANTACIÓN COORDINADA", "EL CONJUNTO P01–P03: CORREDOR TECNOLÓGICO-ADMINISTRATIVO ≈ 119,4 m (E1→E2→E3)",
   ["Espina peatonal continua de 4,00 m que articula las tres edificaciones.",
    "Corredor de redes enterrado único (MT/BT, fibra, datos, agua potable y contra-incendios).",
    "Anillo vehicular y de emergencia de 6,00 m común · separación entre edificios ≈ 15 m (acceso de bomberos).",
    "Un solo modelo de evacuación, señalización y seguridad perimetral.",
    "Retícula modular compartida de 1,20 m · profundidad 21,60 m · corredor central 2,40 m · núcleo con dos escaleras y ascensor.",
    "Regla rectora: ninguna obra puede modificar la implantación general sin revisión aprobada del Plan de Implantación."],
   note="Lámina de implantación UMC-G-ARQ-001-R04 (escala 1:400): ver PDF fuente R04.")

sl("SUPERFICIES, NIVELES, USO E INVERSIÓN", "SÍNTESIS DEL CONJUNTO P01–P03",
   [],
   tab=(["Edificación", "Planta (m²)", "Niv.", "Construido (m²)", "Neta (m²)", "Uso principal", "ROM (M USD)"],
        [["E1 · Vicerrectorado Administrativo", "829,44", "3", "2.488,32", "1.832,00", "Gobierno, servicios y residencias", "5,54 – 8,48"],
         ["E2 · Centro Tecnológico STCW (Torre A)", "933,12", "4", "3.732,48", "2.734,00", "Simulación marítima y Biblioteca UMC", "12,43 – 20,19"],
         ["E3 · Centro de Datos Principal (Torre B)", "881,28", "4", "3.525,12", "2.619,00", "CDP, ciberseguridad y campus virtual", "11,21 – 18,51"],
         ["Módulo Exterior de Pañoles", "110,00", "1", "110,00", "110,00", "Deportes y equipo de buceo", "incluido"],
         ["TOTAL OBRA NUEVA P01–P03", "—", "—", "9.745,92", "7.295,00", "—", "29,18 – 47,18"]]),
   note="ROM AACE Clase 5 (−25 % / +40 %). Conceptos: «El Puente Tecnológico» (Torre A) · «Faro Digital» (Torre B) · «Gobierno y Bienestar» (VRA).")

sl("UMC2030-P01-CTSTCW-R04", "TORRE A · CENTRO TECNOLÓGICO STCW",
   ["43,20 × 21,60 m por planta · 4 niveles + cubierta técnica · 3.732,48 m² construidos · coronación +18,00 m.",
    "PB ±0,000: Biblioteca UMC, vestíbulo, ECDIS, GMDSS, EPIRB/SAR · N1 +4,200: Puente Full Mission 360°, VTS.",
    "N2 +8,200: Sala de Máquinas (SSM), energía y propulsión, carga líquida, CFD · N3 +12,200: telecom, IA, Digital Twin, coworking.",
    "Eficiencia neta/bruta 73,25 % (2.734,00 / 3.732,48 m²) — adecuada para recintos de simulación.",
    "Decisión técnica: el Canal de Ensayos Hidrodinámicos (45×3×2 m ≈ 270 t) NO va en la Torre A; se mantiene en la "
    "remodelación de Talleres (UMC-P01-STCW-TAL) por cargas y geometría.",
    "Los NUEVE componentes STCW del Plan Maestro se preservan íntegros (los nº 8 y 9 en Talleres, con justificación)."])

sl("UMC2030-P02-CDP-R04 · PRIMERA OBRA A EJECUTAR", "TORRE B · CENTRO DE DATOS PRINCIPAL",
   ["40,80 × 21,60 m por planta · 4 niveles · 3.525,12 m² construidos · cubierta +16,70 m.",
    "PB: UPS, baterías, HVAC, Entrance Room, MMR, muelle · N1 +4,500: Data Hall Fase 1 (255 m²) + reserva (145 m²), NOC, CER.",
    "N2 +8,700: Cyber Range, SOC académico, forense, IoT, OT/ICS · N3 +12,700: LMS/Moodle, cloud académico, multimedia.",
    "Estándar normalizado a ANSI/TIA-942-C — Rated-1 (Basic), con reserva de evolución a Rated-2; sin declarar certificación.",
    "PRIORIDAD ESTRATÉGICA: nodo de red del campus y condición habilitante del Campus Virtual, la simulación y los "
    "sistemas académico-administrativos."])

sl("UMC2030-P03-VRA-R04", "E1 · VICERRECTORADO ADMINISTRATIVO",
   ["829,44 m² por planta · 3 niveles · 2.488,32 m² construidos · 1.832,00 m² netos.",
    "Programa: gobierno universitario, servicios a la comunidad marítima, residencias de Oficiales de Planta y "
    "sala de seguridad integral.",
    "Concepto «Gobierno y Bienestar» · vanos de 6,40 m sobre la retícula común de 1,20 m.",
    "Módulo Exterior de Pañoles de 110,00 m² (deportes y equipo de buceo) resuelto fuera del volumen principal.",
    "ROM: 5,54 – 8,48 M USD (AACE Clase 5)."])

sl("NUEVO BLOQUE POST-SÍSMICO", "24-06-2026: EL DOBLETE SÍSMICO Y LA PROA CENTRAL",
   ["Evento: Mw 7,2 + Mw 7,5 — afectación general; la Proa Central ceremonial (obra MOP 1951–1958) es la zona crítica.",
    "Torre de Observación (CUL-TOO-02) y Sala Técnica (ACA-STH-15): daño estructural → expediente P04-TOBSHM-R02.",
    "Patio / Cubierta de Honor (EXT-PCH-04): 1.625,00 m² INHABILITADOS; punto de evacuación R-1 del Sector Proa "
    "SUSPENDIDO sin alterno designado → RFI-EVA-01 (CRÍTICA).",
    "El 100 % del pavimento presenta daño: D3 severo 680,00 m² · D2 moderado 565,00 m² · D4 inducido 380,00 m² "
    "(escombros de la Torre, borde Babor).",
    "Acervo documental rescatado: 198 planos PDF + 487 fotografías (5 tubos portaplanos, inventario firmado 12-10-2026)."],
   img=figpng("G07"))

sl("UMC2030-P04-TOBSHM-R02 (SÍNTESIS)", "P04 · TORRE DE OBSERVACIÓN Y SALA TÉCNICA",
   ["Consolidación estructural de la Torre (coronación +22,02 m; altura original 12,20 m en revisión — RFI-ALT-01) "
    "y de la Sala Técnica; estación hidrometeorológica asociada.",
    "Alcance del borde Babor del patio incluido en su BOQ: 380,00 m² de pavimento y juntas (incl. Banda de "
    "Protocolo de 210,00 m²) — USD 330.000 (banda 260.000 – 400.000).",
    "CONDICIÓN SUSPENSIVA para P05: la consolidación de la Torre precede a toda obra del borde occidental del patio.",
    "Expediente y presentación propios ya emitidos (R02) — disponibles en el Drive institucional."])

sl("UMC2030-P05-EXTPCH-R01", "P05 · PATIO / CUBIERTA DE HONOR — QUÉ SE RESTAURA",
   ["Restauración integral de la explanada ceremonial de 50,00 × 32,50 m: pavimento con reintegración del acabado "
    "granítico/martelinado 1951 (junta-testigo datada, sin falso histórico).",
    "Saneamiento de subbase + sustitución de colectores PEAD SN8 (Ø300–400, 140 m) + 180 m de canaletas C250 + 8 "
    "tanquillas (Tr 25 años; Q 73,13/145 L/s).",
    "Asta Mayor Ceremonial 12,00 m restaurada/repuesta · Mástil OMM 10,00 m · 12 luminarias LED IP66/IK10 · "
    "malla de tierra ≤ 5 Ω + SPDA IEC 62305 · señalización R-1 y accesibilidad.",
    "Aforos: 1.300 cadetes en formación · 1.625 personas en actos · punto R-1 1.080–1.625.",
    "Conciliación con P04: 380,00 m² EXCLUIDOS del BOQ P05 (regla de no doble presupuestación)."],
   img=figpng("G03"))

sl("AACE CLASE 5 · USD REFERENCIAL", "P05 · INVERSIÓN ROM EN CASCADA",
   ["ROM integral (1.625,00 m²): USD 895.000 = 765.000 directo + 53.550 ingeniería/ensayos (7 %) + 76.450 contingencia.",
    "Rango integral: USD 750.000 – 1.120.000 (−25 % / +40 %).",
    "(−) USD 330.000 ya presupuestados en P04-R02 (borde Babor) = PRESUPUESTO NETO ADICIONAL P05: USD 565.000.",
    "Rango neto: USD 490.000 – 720.000 · 470,77 USD/m² integral."],
   img=figpng("G13"))

sl("PROGRAMACIÓN DE REFERENCIA", "PLAZOS: CONJUNTO P01–P03 Y RESTAURACIÓN P05",
   ["P01–P03: ≈ 45–48 meses de ejecución del conjunto; Torre B priorizada como primera obra (nodo de red).",
    "P05: ≈ 9 meses en 5 fases con gates — A estudios previos (2,0) · B demolición controlada (2,0) · C subbase y "
    "colectores (2,5) · D pavimento (3,0) · E asta, eléctrica y comisionamiento (1,5), con solapes.",
    "Restricciones duras P05: secuencia P04 → borde Babor · calendario ceremonial (graduaciones) · ventana de "
    "lluvias · punto R-1 alterno operativo durante toda la obra."],
   img=figpng("G14"))

sl("CONDICIONANTES Y RFI", "RIESGOS Y DECISIONES PENDIENTES",
   ["Comunes P01–P03: topografía certificada (GEO-001/002), estudio geotécnico, Plan de Capacidad IT — condición "
    "suspensiva para inicio de obra.",
    "Definido con precisión: programa verificado recinto a recinto, geometría modular, implantación de conjunto, "
    "ROM Clase 5, matriz de riesgos y gates 0–10.",
    "NO definido aún: cimentaciones, cálculo estructural, memorias MEP, BM de cota, topografía de detalle.",
    "P05 — RFI críticas: RFI-EVA-01 (punto R-1 alterno, MÁXIMA prioridad) · RFI-GEO-01 (BM-UMC-01) · RFI-GEOT-01 "
    "(subbase/colectores) · RFI-NOR-01 (vigencia normativa) · RFI-ARE-05 (acta de transferencia del borde a P04).",
    "Coordenadas consignadas = puntos de control sujetos a verificación topográfica."])

sl("PROPUESTA DE RESOLUCIÓN", "ACUERDOS QUE SE SOLICITAN AL CONSEJO UNIVERSITARIO",
   ["1 · APROBAR los expedientes de anteproyecto P01, P02 y P03 como base para contratar topografía, geotecnia e "
    "ingeniería de detalle.",
    "2 · AUTORIZAR la priorización de la Torre B (CDP) como primera obra del conjunto.",
    "3 · ORDENAR el cierre de las RFI críticas (GEO-001/002, geotécnica, Plan de Capacidad IT) como condición suspensiva.",
    "4 · APROBAR la reubicación del Canal de Ensayos a Talleres y el Módulo de Pañoles de 110 m² · RATIFICAR "
    "ANSI/TIA-942-C Rated-1 con reserva Rated-2.",
    "5 · APROBAR la banda ROM consolidada: 29,18 – 47,18 M USD (P01–P03) + USD 0,565 M netos (P05) + alcance P04 "
    "según su expediente R02, con actualización trimestral.",
    "6 · NUEVO — DESIGNAR el punto de reunión R-1 alterno del Sector Proa (RFI-EVA-01) ANTES de cualquier obra en el patio.",
    "7 · NUEVO — RATIFICAR la secuencia P04 → borde Babor y el acta de transferencia de los 380,00 m² (RFI-ARE-05); "
    "DESIGNAR proyectista habilitado y custodio del Entorno Común de Datos."])

sl("CAMPUS-BUQUE DIGITAL UMC", "CIERRE",
   ["Cinco expedientes, un solo conjunto: el corredor tecnológico-administrativo (9.745,92 m² de obra nueva, "
    "7.295,00 m² netos) y la Proa Central ceremonial restaurada (1.625,00 m² patrimoniales).",
    "La formación marítima de Venezuela articulada con la infraestructura digital del siglo XXI — y con su "
    "patrimonio moderno de 1951 recuperado.",
    "Cap. Alt. / Dr. Guillermo Antonio Riut Hernández — Rector · Consejo Universitario UMC",
    "Expedientes UMC2030-P01-CTSTCW-R04 · P02-CDP-R04 · P03-VRA-R04 · P04-TOBSHM-R02 · P05-EXTPCH-R01",
    "⚠ " + SELLO])

# ----------------------------- HTML -----------------------------
def build_html():
    css = """body{font-family:Helvetica,Arial,sans-serif;margin:0;background:#1c2b3a}
.slide{width:1220px;min-height:700px;margin:26px auto;background:#fff;position:relative;box-shadow:0 4px 18px rgba(0,0,0,.4);display:flex;flex-direction:column}
.bar{background:#0d2c54;color:#fff;padding:20px 46px}.bar .k{color:#d9b64a;font-size:12.5px;letter-spacing:1.6px;font-weight:700}
.bar h1{margin:4px 0 0;font-size:27px}.body{padding:24px 46px;flex:1}
ul{font-size:16.5px;line-height:1.75;color:#20334a;padding-left:24px;margin:6px 0}li{margin-bottom:7px}
table{border-collapse:collapse;width:100%;font-size:13px;margin:8px 0}
th{background:#0d2c54;color:#fff;padding:6px 8px;text-align:left}td{border:1px solid #c8d2dd;padding:5px 8px}
tr:nth-child(even) td{background:#f4f7fa}tr:last-child td{font-weight:bold;background:#eef3f8}
.fig{text-align:center;margin-top:8px}.fig img{max-width:980px;max-height:420px}
.note{font-size:11.5px;color:#667;font-style:italic;padding:0 46px 8px}
.ft{display:flex;justify-content:space-between;padding:8px 20px;font-size:10.5px}
.ft .s{color:#b8860b;font-weight:700}.ft .n{color:#8aa}"""
    parts = ['<!DOCTYPE html><html lang="es"><head><meta charset="utf-8"><title>%s — R05</title><style>%s</style></head><body>' % (BASE, css)]
    for i, d in enumerate(S, 1):
        parts.append('<div class="slide"><div class="bar"><div class="k">%s</div><h1>%s</h1></div><div class="body">' % (H.escape(d["k"]), H.escape(d["t"])))
        if d["b"]:
            parts.append("<ul>%s</ul>" % "".join("<li>%s</li>" % H.escape(x) for x in d["b"]))
        if d["tab"]:
            hd, rows = d["tab"]
            parts.append("<table><tr>%s</tr>%s</table>" % (
                "".join("<th>%s</th>" % H.escape(x) for x in hd),
                "".join("<tr>%s</tr>" % "".join("<td>%s</td>" % H.escape(c) for c in r) for r in rows)))
        if d["img"]:
            b64 = base64.b64encode(open(d["img"], "rb").read()).decode()
            parts.append('<div class="fig"><img src="data:image/png;base64,%s" alt="figura"></div>' % b64)
        parts.append("</div>")
        if d["note"]:
            parts.append('<div class="note">%s</div>' % H.escape(d["note"]))
        parts.append('<div class="ft"><span class="s">NO APTO PARA CONSTRUCCIÓN · %s</span>'
                     '<span class="n">R05 · %s · lámina %d/%d</span></div></div>' % (H.escape(CONF), FECHA, i, len(S)))
    parts.append("</body></html>")
    p = os.path.join(OUT, BASE + ".html")
    open(p, "w", encoding="utf-8").write("".join(parts))
    return p

# ----------------------------- PPTX -----------------------------
def build_pptx():
    from pptx import Presentation
    from pptx.util import Inches, Pt, Emu
    from pptx.dml.color import RGBColor
    from pptx.enum.text import PP_ALIGN
    AZUL = RGBColor(0x0D, 0x2C, 0x54); ORO = RGBColor(0xD9, 0xB6, 0x4A)
    ORO2 = RGBColor(0x7A, 0x59, 0x00); TXT = RGBColor(0x20, 0x33, 0x4A); GR = RGBColor(0x8A, 0x9A, 0xAA)
    prs = Presentation(); prs.slide_width = Inches(13.333); prs.slide_height = Inches(7.5)
    blank = prs.slide_layouts[6]
    SW, SH = prs.slide_width, prs.slide_height

    def box(sld, l, t, w, h, fill=None):
        from pptx.enum.shapes import MSO_SHAPE
        sh = sld.shapes.add_shape(MSO_SHAPE.RECTANGLE, l, t, w, h)
        sh.line.fill.background()
        if fill is not None: sh.fill.solid(); sh.fill.fore_color.rgb = fill
        else: sh.fill.background()
        sh.shadow.inherit = False
        return sh

    def txt(sld, l, t, w, h, lines, size=14, color=TXT, bold=False, align=PP_ALIGN.LEFT, bullet=False):
        tb = sld.shapes.add_textbox(l, t, w, h); tf = tb.text_frame
        tf.word_wrap = True
        for j, line in enumerate(lines):
            p = tf.paragraphs[0] if j == 0 else tf.add_paragraph()
            p.text = ("•  " + line) if bullet else line
            p.alignment = align
            p.space_after = Pt(6)
            for r in p.runs:
                r.font.size = Pt(size); r.font.bold = bold; r.font.color.rgb = color
                r.font.name = "Calibri"
        return tb

    for i, d in enumerate(S, 1):
        sld = prs.slides.add_slide(blank)
        box(sld, 0, 0, SW, SH, RGBColor(0xFF, 0xFF, 0xFF))
        box(sld, 0, 0, SW, Inches(1.25), AZUL)
        txt(sld, Inches(0.55), Inches(0.12), SW - Inches(1.1), Inches(0.35), [d["k"]], 11, ORO, True)
        tsize = 24 if len(d["t"]) < 60 else 19
        txt(sld, Inches(0.55), Inches(0.46), SW - Inches(1.1), Inches(0.75), [d["t"]], tsize, RGBColor(0xFF, 0xFF, 0xFF), True)
        y = Inches(1.5)
        if d["b"]:
            n = len(d["b"]); longest = max(len(x) for x in d["b"])
            bsize = 15 if (n <= 5 and longest < 150) else 13 if n <= 6 else 12
            bh = Inches(0.52) * n * (2 if longest > 160 else 1.4)
            bh = min(bh, SH - y - Inches(0.6))
            txt(sld, Inches(0.7), y, SW - Inches(1.4), bh, d["b"], bsize, TXT, bullet=True)
            y = y + bh + Inches(0.1)
        if d["tab"]:
            hd, rows = d["tab"]
            gt = sld.shapes.add_table(len(rows) + 1, len(hd), Inches(0.55), y,
                                      SW - Inches(1.1), Inches(0.42) * (len(rows) + 1)).table
            for c, hcell in enumerate(hd):
                cell = gt.cell(0, c); cell.text = hcell
                cell.fill.solid(); cell.fill.fore_color.rgb = AZUL
                for p in cell.text_frame.paragraphs:
                    for r in p.runs: r.font.size = Pt(10.5); r.font.bold = True; r.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
            for rr, row in enumerate(rows, 1):
                for c, v in enumerate(row):
                    cell = gt.cell(rr, c); cell.text = v
                    last = rr == len(rows)
                    cell.fill.solid()
                    cell.fill.fore_color.rgb = RGBColor(0xEE, 0xF3, 0xF8) if last else (RGBColor(0xF4, 0xF7, 0xFA) if rr % 2 == 0 else RGBColor(0xFF, 0xFF, 0xFF))
                    for p in cell.text_frame.paragraphs:
                        for r in p.runs: r.font.size = Pt(9.5); r.font.bold = last; r.font.color.rgb = TXT
            y = y + Inches(0.42) * (len(rows) + 1) + Inches(0.1)
        if d["img"]:
            from PIL import Image
            iw, ih = Image.open(d["img"]).size
            avail_h = SH - y - Inches(0.55)
            avail_w = SW - Inches(1.6)
            sc = min(avail_w / Emu(1) / (iw / 96 * 914400 / Emu(1)), 1e9)  # placeholder
            # cálculo simple en EMU
            w_emu = int(iw / 96 * 914400); h_emu = int(ih / 96 * 914400)
            k = min(avail_w / w_emu, avail_h / h_emu)
            w2, h2 = int(w_emu * k), int(h_emu * k)
            sld.shapes.add_picture(d["img"], int((SW - w2) / 2), int(y), w2, h2)
        if d["note"]:
            txt(sld, Inches(0.55), SH - Inches(0.78), SW - Inches(1.1), Inches(0.3), [d["note"]], 9, GR)
        txt(sld, Inches(0.3), SH - Inches(0.42), Inches(8.5), Inches(0.3),
            ["NO APTO PARA CONSTRUCCIÓN · " + CONF], 8, ORO2, True)
        txt(sld, SW - Inches(4.3), SH - Inches(0.42), Inches(4.0), Inches(0.3),
            ["R05 · %s · %d/%d" % (FECHA, i, len(S))], 8, GR, align=PP_ALIGN.RIGHT)
    p = os.path.join(OUT, BASE + ".pptx")
    prs.save(p)
    return p

if __name__ == "__main__":
    print("HTML:", os.path.basename(build_html()))
    print("PPTX:", os.path.basename(build_pptx()))
    print("láminas:", len(S))

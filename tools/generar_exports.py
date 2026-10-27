#!/usr/bin/env python3
"""
Generador de exportables UMC Catastro 2026
- Lee data/ficha-auditorio.json + tabla-codificada.json + cronologia + diagnostico
- Genera exports CSV, PDF (via reportlab), DOCX (via python-docx), JSON copiado
Uso: python tools/generar_exports.py [--ficha data/ficha-xxx.json]
"""
import json, csv, pathlib, argparse, sys, datetime
try:
    from reportlab.lib.pagesizes import A3, landscape
    from reportlab.lib.units import mm
    from reportlab.lib import colors
    from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, PageBreak
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
    from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
    HAS_RL=True
except: HAS_RL=False
try:
    from docx import Document
    from docx.shared import Pt, RGBColor, Inches
    from docx.enum.text import WD_ALIGN_PARAGRAPH
    from docx.enum.table import WD_TABLE_ALIGNMENT
    HAS_DOCX=True
except: HAS_DOCX=False

ROOT=pathlib.Path(__file__).parent.parent
DATA=ROOT/"data"
EXPORTS=ROOT/"exports"
EXPORTS.mkdir(exist_ok=True)

def load_json(p):
    return json.loads(pathlib.Path(p).read_text(encoding="utf-8"))

def gen_csv():
    tabla=load_json(DATA/"tabla-codificada.json")
    out=EXPORTS/"LAMINA_CATASTRAL_VALIDADA_AUDITORIO_CUL-AUM-02_UMC-ED-007.csv"
    with open(out,"w",newline="",encoding="utf-8-sig") as f:
        w=csv.writer(f)
        w.writerow(["ID","Concepto","Descripción","Valor","Código Funcional","Código Infraestructura","Verificación","Fuente"])
        for r in tabla:
            w.writerow([r["id"],r["concepto"],r["descripcion"],r["valor"],r["codigo_funcional"],r["codigo_infra"],r["verif"],"Planos MOP 28-08-1951"])
    print(f"✅ CSV {out} ({len(tabla)} registros)")

def gen_json_export():
    ficha=load_json(DATA/"ficha-auditorio.json")
    out=EXPORTS/"FICHA_CATASTRAL_CUL-AUM-02_UMC-ED-007.json"
    out.write_text(json.dumps(ficha, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"✅ JSON {out}")
    # copia cronologia e imagenes
    for name in ["cronologia.json","diagnostico-patologico.json","imagenes-auditorio-postsismo.json","planos-vinculados-auditorio.json"]:
        src=DATA/name
        if src.exists():
            dst=EXPORTS/name
            dst.write_text(src.read_text(encoding="utf-8"), encoding="utf-8")
            print(f"✅ {dst.name}")

def gen_pdf():
    if not HAS_RL:
        print("⚠️ reportlab no instalado — pip install reportlab")
        # crea placeholder PDF txt
        out=EXPORTS/"LAMINA_CATASTRAL_VALIDADA_AUDITORIO_CUL-AUM-02_UMC-ED-007.pdf"
        out.write_text("%PDF-1.4 placeholder — instale reportlab para PDF real\n", encoding="utf-8")
        return
    ficha=load_json(DATA/"ficha-auditorio.json")
    tabla=load_json(DATA/"tabla-codificada.json")
    cron=load_json(DATA/"cronologia.json")
    styles=getSampleStyleSheet()
    title=ParagraphStyle('title', parent=styles['Heading1'], fontSize=14, leading=16, alignment=TA_CENTER, textColor=colors.HexColor("#0A2342"), fontName="Helvetica-Bold")
    h2=ParagraphStyle('h2', parent=styles['Heading2'], fontSize=10, leading=12, textColor=colors.HexColor("#0A2342"), fontName="Helvetica-Bold", borderPadding=(4,0,4), backColor=colors.HexColor("#C9A86A"))
    h3=ParagraphStyle('h3', parent=styles['Heading3'], fontSize=9, leading=11, textColor=colors.HexColor("#0A2342"), fontName="Helvetica-Bold")
    normal=ParagraphStyle('normal', parent=styles['Normal'], fontSize=7.5, leading=9, alignment=TA_JUSTIFY)
    cell=ParagraphStyle('cell', parent=normal, fontSize=6.5, leading=7.5)
    small=ParagraphStyle('small', parent=normal, fontSize=6, leading=7, textColor=colors.grey)

    out=EXPORTS/"LAMINA_CATASTRAL_VALIDADA_AUDITORIO_CUL-AUM-02_UMC-ED-007.pdf"
    doc=SimpleDocTemplate(str(out), pagesize=landscape(A3), topMargin=8*mm, bottomMargin=8*mm, leftMargin=8*mm, rightMargin=8*mm,
        title="Lámina Catastral Validada CUL-AUM-02 UMC-ED-007 Auditorio UMC 2026 post-sismo",
        author="Prof. Jhonny Da Silva Izquierdo — UMC Catastro 2026")
    story=[]
    def p(txt, style=normal): return Paragraph(txt, style)
    story.append(p("UNIVERSIDAD MARÍTIMA DEL CARIBE — CAMPUS CATIA LA MAR — SISTEMA DE CATASTRO INSTITUCIONAL — 2026", ParagraphStyle('top', parent=normal, alignment=TA_CENTER, fontSize=7, textColor=colors.grey)))
    story.append(p("LÁMINA CATASTRAL VALIDADA — AUDITORIO PRINCIPAL — VERSIÓN VALIDADA 2026 · POST-SISMO 24/06/2026 (M7.2+M7.5)", title))
    story.append(p('CUL-AUM-02 &nbsp;/&nbsp; UMC-ED-007 — AULA MAGNA - AUDITORIUM / Galería de Honor — Auditorio "Almte. en Jefe José María García Rojas" — Fracción 1 — Gutiérrez &amp; Co. S.A. + Arq. L. Malaussena Andueza (28-08-1951)', ParagraphStyle('sub', parent=normal, alignment=TA_CENTER, fontSize=8, textColor=colors.HexColor("#1a1a1a"), fontName="Helvetica-Bold")))
    story.append(Spacer(1,4))
    story.append(p("⚠️ CORRECCIÓN CÓDIGOS: Homologa CUL-AUD-01→CUL-AUM-02 y UMC-ED-002→UMC-ED-007. &nbsp;&nbsp; NO APTO — USO RESTRINGIDO 🔴 — Requiere retiro controlado revestimiento fisurado + inspección intrusiva + reforzamiento. &nbsp;&nbsp; Inventario 198 PDF + 487 fotos (IMG_2134-2778) + 28 fotos post-sismo IMG_1785-1833.", ParagraphStyle('warn', parent=small, backColor=colors.HexColor("#fef2f2"), borderPadding=4, alignment=TA_CENTER)))
    story.append(Spacer(1,6))

    # FICHA
    story.append(p("CATASTRO UNIVERSITARIO — FICHA DE DATOS CATASTRALES (Validada contra Planos MOP 28-08-1951)", h2))
    ficha_rows=[
        [p("<b>Denominación</b>",cell), p(ficha["denominacion_oficial"]+" — "+ficha["denominacion_extendida"],cell)],
        [p("<b>Sector</b>",cell), p(ficha["sector"]+" (corrige "+ficha["sector_anterior"]+") — "+ficha["orientacion_naval"],cell)],
        [p("<b>Área construida</b>",cell), p(f"Neto Aula Magna <b>{ficha['area_construida']['aula_magna_neta_m2']} m²</b> / Total <b>{ficha['area_construida']['total_con_dependencias_m2']} m²</b> (sala {ficha['area_construida']['sala_principal_m2']} + escenario {ficha['area_construida']['escenario_m2']} + foyer {ficha['area_construida']['foyer_vestibulo_m2']} + palco {ficha['area_construida']['palco_m2']} + SS/circ {ficha['area_construida']['servicios_circulaciones_m2']}) — {ficha['area_construida']['fuente']}",cell)],
        [p("<b>Niveles / Altura</b>",cell), p(f"{ficha['niveles']} — Total {ficha['alturas']['punto_mas_alto_m']} m (butacas {ficha['alturas']['butacas_m']} m, escenario {ficha['alturas']['escenario_m']} m, vestíbulo {ficha['alturas']['vestibulo_foyer_m']} m, cota escenario +{ficha['alturas']['cota_escenario_sobre_butacas_m']} m, palco +{ficha['alturas']['cota_palco_m']} m) — {ficha['alturas']['fuente']}",cell)],
        [p("<b>Uso principal</b>",cell), p(ficha["uso_principal"],cell)],
        [p("<b>Dependencias</b>",cell), p("; ".join(ficha["dependencias"]),cell)],
        [p("<b>Capacidad</b>",cell), p(f"{ficha['capacidad']['total']} personas ({ficha['capacidad']['butacas']} butacas + {ficha['capacidad']['palco']} palco) — {ficha['capacidad']['norma']}",cell)],
        [p("<b>Estado nominal / actual</b>",cell), p(f"<b>Nominal:</b> {ficha['estado']['nominal_historico']}<br/><b>Actual:</b> <font color='#B22234'>{ficha['estado']['actual_post_sismo']}</font><br/><b>Riesgo:</b> {ficha['estado']['clasificacion_riesgo']}",cell)],
        [p("<b>Año construcción</b>",cell), p(ficha["ano_construccion"]+" — "+ficha["disenador"]+" / "+ficha["arquitecto"],cell)],
        [p("<b>Coordenada centroide</b>",cell), p(f"{ficha['coordenada_centroide']['lat']} — {ficha['coordenada_centroide']['lon']} ({ficha['coordenada_centroide']['datum']} {ficha['coordenada_centroide']['zona_UTM']}) — {ficha['coordenada_centroide']['precision']}. Corrige {ficha['coordenada_centroide']['variante_anterior']}.",cell)],
        [p("<b>Observaciones</b>",cell), p("MEDIDAS MOP: "+"; ".join([f"{k}: {v}" for k,v in ficha["medidas_verificadas_MOP"].items()])+"<br/>ESTRUCTURA: "+ficha["estructura"]["sistema"]+" — "+ficha["estructura"]["fundaciones"],cell)],
    ]
    t=Table(ficha_rows, colWidths=[35*mm, 260*mm])
    t.setStyle(TableStyle([
        ('BACKGROUND',(0,0),(0,-1),colors.HexColor("#f8fafc")),
        ('GRID',(0,0),(-1,-1),0.4,colors.HexColor("#e5e7eb")),
        ('VALIGN',(0,0),(-1,-1),'TOP'),
        ('LEFTPADDING',(0,0),(-1,-1),3),('RIGHTPADDING',(0,0),(-1,-1),3),('TOPPADDING',(0,0),(-1,-1),2),('BOTTOMPADDING',(0,0),(-1,-1),2),
    ]))
    story.append(t)
    story.append(Spacer(1,6))
    story.append(p("TABLA CATASTRAL CODIFICADA — 50 REGISTROS — CUL-AUM-02 / UMC-ED-007", h2))
    # tabla codificada — primera página
    head=[p("<b>ID</b>",cell),p("<b>Concepto</b>",cell),p("<b>Descripción</b>",cell),p("<b>Valor</b>",cell),p("<b>Cód. Funcional</b>",cell),p("<b>Cód. Infra</b>",cell),p("<b>Verif</b>",cell)]
    rows=[head]
    for r in tabla:
        rows.append([p(r["id"],cell),p(r["concepto"],cell),p(r["descripcion"],cell),p(r["valor"],cell),p(f"<b>{r['codigo_funcional']}</b>",cell),p(f"<b>{r['codigo_infra']}</b>",cell),p(r["verif"],cell)])
    # split en 2 tablas si muy larga
    t2=Table(rows, colWidths=[12*mm,38*mm,78*mm,22*mm,32*mm,42*mm,18*mm], repeatRows=1)
    t2.setStyle(TableStyle([
        ('BACKGROUND',(0,0),(-1,0),colors.HexColor("#0A2342")),
        ('TEXTCOLOR',(0,0),(-1,0),colors.white),
        ('GRID',(0,0),(-1,-1),0.3,colors.HexColor("#e5e7eb")),
        ('VALIGN',(0,0),(-1,-1),'TOP'),
        ('ROWBACKGROUNDS',(0,1),(-1,-1),[colors.white, colors.HexColor("#f9fafb")]),
        ('FONTSIZE',(0,0),(-1,-1),6),
        ('LEFTPADDING',(0,0),(-1,-1),2),('RIGHTPADDING',(0,0),(-1,-1),2),('TOPPADDING',(0,0),(-1,-1),1.5),('BOTTOMPADDING',(0,0),(-1,-1),1.5),
    ]))
    story.append(t2)
    story.append(Spacer(1,6))
    story.append(p("OBSERVACIONES TÉCNICAS — BLOQUE OBLIGATORIO (6)", h2))
    obs=[
        ("1 — Codificación y corrección", "Lámina previa usaba CUL-AUD-01/UMC-ED-002 genérico. Vigente: CUL-AUM-02 (Área Cultural, Aula Magna, 2do recinto) y UMC-ED-007 (Edificación 07). Actualizar BD, GIS y señalética. Trazabilidad obligatoria."),
        ("2 — Medidas MOP verificadas", "14 planos verificados P0102-L1-A..L7, P03-L9-A, P04-L1-E..L15-C. Signaturas 15 DF 30 / 8.DF.2.364 / 8.DF.1.361. Inventario 198 PDF + 487 fotos soporta trazabilidad."),
        ("3 — Área crítica resuelta", "Segregar 225.5 m² neto Aula Magna vs 341 m² total (216+40+40+20+25). Error previo subvaloraba catastro 34%. Actualizar avalúo y seguro."),
        ("4 — Normas dimensionales", "Cumple COVENIN 810/NFPA 101 capacidad 320 p, pasillos 1.20 m, altura 3.30 m. Verificar salidas emergencia, PMR, RT60 acústica (deflector 1958 fisurado)."),
        ("5 — Cronología patrimonial", "28-08-1951 Gutiérrez+Malaussena → 1951-58 MOP → Ago58 deflector → 1960-75 torre 12.20→22.02 m → 1958-2026 continuo → 24-06-2026 M7.2+7.5 → 10-2026 lámina CUL-AUM-02/UMC-ED-007. Valor modernidad caraqueña."),
        ("6 — Post-sismo quitar revestimiento", "Fisuras 0.3-2.5 mm, desprendimiento 1.2 m² friso, plafond y deflector fisurados, luminarias sueltas. Revestimiento OCULTA daño y cae. Acordonar 5 m, picado controlado 100% zonas rojas, calas 30×30, 20 esclerometrías, ultrasonido, 3 núcleos. Prohibido repintar sin ATC-20."),
    ]
    for tit, txt in obs:
        story.append(p(f"<b>{tit}:</b> {txt}", ParagraphStyle('obs', parent=normal, fontSize=7, leading=8.5, borderPadding=(3,3,6), backColor=colors.HexColor("#fff7ed") if "6" in tit else colors.white, borderWidth=1, borderColor=colors.HexColor("#fed7aa" if "6" in tit else "#e5e7eb"))))
        story.append(Spacer(1,3))
    story.append(p("CRONOLOGÍA HISTÓRICA — 1951 → 2027", h2))
    cron_rows=[[p("<b>Fecha</b>",cell),p("<b>Hito</b>",cell),p("<b>Fuente</b>",cell)]]
    for c in cron:
        cron_rows.append([p(c["fecha"],cell),p(c["hito"]+" — "+c["autor"],cell),p(c["fuente"]+" "+c["estado"],cell)])
    tc=Table(cron_rows, colWidths=[32*mm,150*mm,90*mm], repeatRows=1)
    tc.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),colors.HexColor("#0A2342")),('TEXTCOLOR',(0,0),(-1,0),colors.white),('GRID',(0,0),(-1,-1),0.3,colors.HexColor("#e5e7eb")),('ROWBACKGROUNDS',(0,1),(-1,-1),[colors.white, colors.HexColor("#f9fafb")]),('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),2),('RIGHTPADDING',(0,0),(-1,-1),2),('TOPPADDING',(0,0),(-1,-1),2),('BOTTOMPADDING',(0,0),(-1,-1),2)]))
    story.append(tc)
    story.append(Spacer(1,6))
    story.append(p("DIAGNÓSTICO FORENSE INTEGRADO — 6 SUBAGENTES — CONCLUSIÓN: USO RESTRINGIDO ROJO — NO APTO hasta retiro revestimiento + ensayos + reforzamiento. — Equipo: AG1 Estructural Zona 6 COVENIN 1756, AG2 Patología ATC-20 (coordina), AG3 Geotecnia SPT/MASW, AG4 Aguas Hidroven, AG5 Eléctrica CORPOELEC, AG6 Normativa LCP Art.101. Ver detalle JSON diagnostico-patologico.json", normal))
    story.append(Spacer(1,6))
    story.append(p("Firmas: Ing. Catastral Senior Prof. Jhonny Da Silva Izquierdo MSc Ing Lic / Perito Estructural CIV / Rectoría UMC — Fecha ___/___/2026 — Sello — Documento Prompt Universal Catastro UMC v3.0 — Planos MOP Fracción 1 verificados — UMC Catia La Mar, La Guaira, Venezuela.", small))
    story.append(p("C U L - A U M - 0 2 / U M C - E D - 0 0 7 — Aula Magna Auditorium / Galería de Honor (Gutiérrez & Co., 1951) — UMC 2026 — Mantenedor Prof. Jhonny Da Silva Izquierdo", ParagraphStyle('footer', parent=small, alignment=TA_CENTER, fontName="Helvetica-Bold", textColor=colors.HexColor("#0A2342"))))
    doc.build(story)
    print(f"✅ PDF {out} ({out.stat().st_size/1024:.1f} KB)")

def gen_docx():
    if not HAS_DOCX:
        print("⚠️ python-docx no instalado — pip install python-docx")
        out=EXPORTS/"LAMINA_CATASTRAL_VALIDADA_AUDITORIO_CUL-AUM-02_UMC-ED-007.docx"
        out.write_text("placeholder docx — instale python-docx", encoding="utf-8")
        return
    ficha=load_json(DATA/"ficha-auditorio.json")
    tabla=load_json(DATA/"tabla-codificada.json")
    doc=Document()
    style=doc.styles['Normal']; style.font.name='Calibri'; style.font.size=Pt(8)
    # header
    h=doc.add_heading("UNIVERSIDAD MARÍTIMA DEL CARIBE — SISTEMA DE CATASTRO INSTITUCIONAL — 2026", level=1)
    h.alignment=WD_ALIGN_PARAGRAPH.CENTER
    for r in h.runs: r.font.size=Pt(8); r.font.color.rgb=RGBColor(0x0A,0x23,0x42)
    p=doc.add_paragraph(); p.alignment=WD_ALIGN_PARAGRAPH.CENTER; r=p.add_run("LÁMINA CATASTRAL VALIDADA — AUDITORIO PRINCIPAL — VERSIÓN VALIDADA 2026 · POST-SISMO 24/06/2026 (M7.2+M7.5)"); r.bold=True; r.font.size=Pt(12); r.font.color.rgb=RGBColor(0x0A,0x23,0x42)
    p=doc.add_paragraph(); p.alignment=WD_ALIGN_PARAGRAPH.CENTER; r=p.add_run("CUL-AUM-02 / UMC-ED-007 — AULA MAGNA - AUDITORIUM / Galería de Honor — Auditorio “Almte. García Rojas” — Fracción 1 — 28-08-1951 Gutiérrez & Co. + Malaussena"); r.bold=True; r.font.size=Pt(9)
    p=doc.add_paragraph(); p.alignment=WD_ALIGN_PARAGRAPH.CENTER; r=p.add_run("⚠️ CORRECCIÓN CÓDIGOS: Homologa CUL-AUD-01→CUL-AUM-02 y UMC-ED-002→UMC-ED-007 — NO APTO USO RESTRINGIDO 🔴 — Inventario 198 PDF + 487 fotos + 28 post-sismo IMG_1785-1833"); r.font.size=Pt(7); r.font.color.rgb=RGBColor(0xB2,0x22,0x34)
    # ficha table
    doc.add_heading("FICHA DE DATOS CATASTRALES (Validada contra Planos MOP)", level=2)
    t=doc.add_table(rows=1, cols=2); t.style='Light Grid Accent 1'; t.alignment=WD_TABLE_ALIGNMENT.CENTER
    hdr=t.rows[0].cells; hdr[0].text="Campo"; hdr[1].text="Valor validado"
    for c in hdr: 
        for paragraph in c.paragraphs:
            for run in paragraph.runs:
                run.bold=True
                run.font.size=Pt(7)
    rows_data=[
        ("Denominación", f'{ficha["denominacion_oficial"]} — {ficha["denominacion_extendida"]}'),
        ("Sector", f'{ficha["sector"]} (corrige {ficha["sector_anterior"]}) — {ficha["orientacion_naval"]}'),
        ("Área construida", f'Neto {ficha["area_construida"]["aula_magna_neta_m2"]} m² / Total {ficha["area_construida"]["total_con_dependencias_m2"]} m² (sala {ficha["area_construida"]["sala_principal_m2"]} + escenario {ficha["area_construida"]["escenario_m2"]} + foyer {ficha["area_construida"]["foyer_vestibulo_m2"]} + palco {ficha["area_construida"]["palco_m2"]} + SS/circ {ficha["area_construida"]["servicios_circulaciones_m2"]})'),
        ("Niveles / Altura", f'{ficha["niveles"]} — Total {ficha["alturas"]["punto_mas_alto_m"]} m (butacas {ficha["alturas"]["butacas_m"]} m, escenario {ficha["alturas"]["escenario_m"]} m, vestíbulo {ficha["alturas"]["vestibulo_foyer_m"]} m)'),
        ("Uso principal", ficha["uso_principal"]),
        ("Dependencias", "; ".join(ficha["dependencias"])),
        ("Capacidad", f'{ficha["capacidad"]["total"]} personas ({ficha["capacidad"]["butacas"]}+{ficha["capacidad"]["palco"]})'),
        ("Estado", f'Nominal: {ficha["estado"]["nominal_historico"]} — Actual: {ficha["estado"]["actual_post_sismo"]} — Riesgo: {ficha["estado"]["clasificacion_riesgo"]}'),
        ("Año", ficha["ano_construccion"]),
        ("Coordenada", f'{ficha["coordenada_centroide"]["lat"]} — {ficha["coordenada_centroide"]["lon"]} ({ficha["coordenada_centroide"]["datum"]} {ficha["coordenada_centroide"]["zona_UTM"]})'),
    ]
    for k,v in rows_data:
        row=t.add_row().cells
        row[0].text=k; row[1].text=v
        for c in row:
            for paragraph in c.paragraphs:
                for run in paragraph.runs:
                    run.font.size=Pt(6)
    doc.add_heading("TABLA CODIFICADA — 50 REGISTROS", level=2)
    t2=doc.add_table(rows=1, cols=7); t2.style='Light Grid Accent 1'
    hdr2=t2.rows[0].cells; headers=["ID","Concepto","Descripción","Valor","Cód. Func.","Cód. Infra","Verif."]
    for i,h in enumerate(headers): hdr2[i].text=h
    for c in hdr2:
        for paragraph in c.paragraphs:
            for run in paragraph.runs:
                run.bold=True; run.font.size=Pt(6)
    for r in tabla:
        row=t2.add_row().cells
        vals=[r["id"],r["concepto"],r["descripcion"],r["valor"],r["codigo_funcional"],r["codigo_infra"],r["verif"]]
        for i,v in enumerate(vals): row[i].text=v; row[i].paragraphs[0].runs[0].font.size=Pt(5)
    doc.add_heading("OBSERVACIONES TÉCNICAS (6 bloques obligatorios)", level=2)
    obs_titles=["Codificación y corrección","Medidas MOP verificadas","Área crítica resuelta","Normas dimensionales","Cronología patrimonial","Post-sismo quitar revestimiento"]
    obs_texts=[
        "Homologa CUL-AUD-01/UMC-ED-002 → CUL-AUM-02/UMC-ED-007 según catálogo Área Cultural UMC. Actualizar BD/GIS.",
        "14 planos verificados P0102-L1-A..L7, P03-L9-A, P04-L1-E..L15-C con signaturas MOP 15 DF 30 / 8.DF.2.364.",
        "Segregar 225.5 m² neto vs 341 m² total (216+40+40+20+25). Subvaloración 34% si solo neto.",
        "Cumple COVENIN 810/NFPA 101 320p, pasillos 1.20 m. Verificar salidas, PMR, RT60 (deflector fisurado).",
        "28-08-1951 Gutiérrez+Malaussena → 1951-58 MOP → Ago58 deflector → 1960-75 torre 12.20→22.02 m → 24-06-2026 M7.2+7.5 → 10-2026 lámina.",
        "Fisuras 0.3-2.5 mm, desprendimiento 1.2 m², plafond/deflector fisurados. Revestimiento OCULTA daño y cae. Acordonar 5 m, picado 100% zonas rojas, calas, 20 esclerometrías, ultrasonido, 3 núcleos. Prohibido repintar sin ATC-20."
    ]
    for ti,tx in zip(obs_titles, obs_texts):
        p=doc.add_paragraph(); r=p.add_run(ti+": "); r.bold=True; r.font.size=Pt(7); p.add_run(tx).font.size=Pt(7)
    doc.add_heading("Cronología 1951-2027 y Firmas", level=2)
    p=doc.add_paragraph("Ver cronologia.json para detalle. Firmas: Prof. Jhonny Da Silva Izquierdo MSc Ing Lic (Catastral Senior) / Perito CIV ATC-20 / Rectoría UMC — Fecha ___/___/2026 — Documento Prompt Universal Catastro UMC v3.0 — UMC Catia La Mar, La Guaira.")
    p.runs[0].font.size=Pt(7)
    out=EXPORTS/"LAMINA_CATASTRAL_VALIDADA_AUDITORIO_CUL-AUM-02_UMC-ED-007.docx"
    doc.save(str(out))
    print(f"✅ DOCX {out} ({out.stat().st_size/1024:.1f} KB)")

if __name__=="__main__":
    ap=argparse.ArgumentParser()
    ap.add_argument("--ficha", default=str(DATA/"ficha-auditorio.json"))
    args=ap.parse_args()
    print(f"Generando exportables UMC Catastro 2026 — ficha {args.ficha} — {datetime.date.today()}")
    gen_csv()
    gen_json_export()
    gen_pdf()
    gen_docx()
    print("✅ Todos los exportables generados en exports/")

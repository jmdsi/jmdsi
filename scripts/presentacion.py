#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""E6 · Presentación para el Consejo Universitario — 27 láminas con gráficas.
Renderer propio a PDF apaisado (ReportLab) y HTML autocontenido."""
import base64
import os

AZUL = "#0b3c5d"; ACERO = "#1d5b7a"; ROJO = "#a4262c"; OCRE = "#b07d2b"; VERDE = "#2e6f4e"
COD = "UMC2030-P04-TOBSHM-R02"
FECHA = "17 de octubre de 2026"
SELLO = "INGENIERÍA BÁSICA / ANTEPROYECTO — EMITIDO PARA COORDINACIÓN Y PRESUPUESTO PRELIMINAR — NO APTO PARA CONSTRUCCIÓN"
F = "build/fig/"

S = []
def slide(t, st, **kw):
    S.append(dict(t=t, st=st, **kw))

slide("Torre de Observación / Puente de Mando y Sala Técnica de Investigación Hidrometeorológica",
      "Proyecto 04 del Plan Maestro UMC 2025–2030 · Restauración patrimonial y reequipamiento "
      "post-sísmico · Presentación para el Consejo Universitario y el Rectorado",
      kpis=[("106,00 m²", "de intervención patrimonial"), ("22,02 m", "coronación adoptada"),
            ("2", "edificaciones patrimoniales"), ("≈ 30", "meses de ejecución"),
            ("2,09 – 3,25", "MUSD · ROM Clase 5")],
      nota=f"Cap. Alt. / Dr. Guillermo Antonio Riut Hernández – Rector · {FECHA} · Expediente {COD}")

slide("Cómo leer esta presentación", "Naturaleza, alcance y límites del documento",
      col_izq=("Qué ES este documento", [
          "El desarrollo en nivel de INGENIERÍA BÁSICA / ANTEPROYECTO de la restauración de la "
          "Torre de Observación y de la Sala Técnica de Investigación Hidrometeorológica.",
          "Un instrumento para decidir: programa, geometría adoptada, diagnóstico post-sísmico, "
          "estimación ROM, cronograma y riesgos.",
          "La base técnica para contratar el levantamiento, la geotecnia, la inspección "
          "estructural detallada y la ingeniería de detalle."]),
      col_der=("Qué NO es este documento", [
          "No es un proyecto ejecutivo: no contiene cálculo estructural, memorias firmadas ni "
          "planos de replanteo.",
          "No es apto para replanteo ni construcción, y no sustituye permisos ni la autorización "
          "del órgano de patrimonio.",
          "No acredita inspección estructural realizada: el diagnóstico es preliminar y está "
          "sujeto a RFI-PAT-01."]))

slide("Agenda", "Contenido de la exposición ante el Consejo Universitario",
      tabla=[["#", "Bloque", "Láminas"],
             ["1", "Marco, patrimonio y evento sísmico", "4 – 6"],
             ["2", "El conjunto: implantación y programa", "7 – 10"],
             ["3", "Diagnóstico y doctrina de intervención", "11 – 13"],
             ["4", "Ingeniería: estructura, MEP, instrumentación, Industria 5.0", "14 – 18"],
             ["5", "Inversión, plazos y riesgos", "19 – 24"],
             ["6", "Condición de emisión y acuerdos solicitados", "25 – 27"]])

slide("Marco: el Plan Maestro UMC 2025–2030", "Instrumento rector y posición del Proyecto 04",
      bullets=[
          "El Plan Maestro declara doce proyectos estratégicos; este expediente desarrolla el "
          "cuarto: la restauración del conjunto patrimonial del Área Cultural.",
          "Se coordina como un solo modelo de implantación con el Proyecto 01 (Torre A – Centro "
          "Tecnológico STCW), el Proyecto 02 (Torre B – CDP) y el Proyecto 03 (Vicerrectorado).",
          "El corredor tecnológico-administrativo de ≈ 119,4 m y el corredor de redes enterrado "
          "son infraestructura común que este proyecto no modifica.",
          "Autoría del documento fuente: Prof. Jhonny Da Silva Izquierdo (MSc. Ing. Lic.)."],
      nota="Ningún plano de este proyecto modifica la implantación general del Plan Maestro sin "
           "revisión aprobada del Plan de Implantación.")

slide("Patrimonio: la Escuela Náutica de Venezuela y Malaussena",
      "El valor que se protege: modernidad venezolana 1951–1958",
      tabla=[["Campo", "Registro documental"],
             ["Denominación original", "Escuela Náutica de Venezuela («Catia La Mar» en 1957-58)"],
             ["Arquitecto", "Luis Raimundo Malaussena Andueza"],
             ["Estructural", "Oficina Técnica Gutiérrez & Co. S.A. / Gutiérrez y Acuña"],
             ["Contratante", "MOP – Dirección de Edificios"],
             ["Cronología", "1951 · 1952-53 · 1956-57 · 1958"],
             ["Archivo", "198 PDF y 487 fotografías (Portaplanos Nº 01–05)"]],
      nota="La Torre y la Sala forman parte de la Fracción 1, concebida el 28-08-1951 como una "
           "sola pieza con el Aula Magna.")

slide("El doblete sísmico del 24 de junio de 2026", "Condición de partida: estado POST-COLAPSO",
      kpis=[("M 7,2", "primer evento"), ("M 7,5", "segundo evento"), ("24-06-2026", "fecha"),
            ("D4", "daño máximo preliminar")],
      bullets=[
          "Secuencia inusual: el segundo evento, de mayor magnitud, actuó sobre una estructura "
          "ya fisurada; el daño es acumulativo y debe evaluarse como secuencia.",
          "La Torre presenta colapso parcial en planta baja y pérdida de elementos en coronación; "
          "la Sala, a 3,61 m, resultó afectada por el mismo evento.",
          "Clasificación de uso propuesta: INSPECCIÓN DETALLADA. No se libera acceso sin "
          "apuntalamiento y monitoreo.",
          "La serie histórica meteorológica (activa desde 1975) no debe interrumpirse: estación "
          "provisional desde el mes 1."],
      img=F + "G-02_linea_tiempo.png")

slide("Implantación del Área Cultural", "Un solo conjunto en el sector Proa–Babor",
      img=F + "G-01_implantacion_area_cultural.png",
      bullets=[
          "Torre adosada al Auditorio de la Fracción 1; Sala a 3,61 m del centroide de la Torre.",
          "Plaza de honor y banda de protocolo como espacio ceremonial y punto de reunión R-1.",
          "Acometidas tomadas del corredor de redes enterrado, mediante cámara propia.",
          "Vialidad de emergencia del Área Cultural preservida íntegra durante toda la obra."])

slide("La Torre de Observación / Puente de Mando", "Ficha del objeto · CUL-TOO-02 · UMC-ED-003",
      kpis=[("3,60 × 3,75 m", "huella por nivel"), ("5", "niveles"), ("67,50 m²", "construidos"),
            ("20", "personas en el puente de mando"), ("1960-75 / 1951-58", "data en disputa (RFI-FEC-01)")],
      bullets=[
          "Emblema institucional: formación, actos y ceremonias; dependencia del Auditorio, "
          "vestíbulo y foyer.",
          "Geometría verificada por el propio inventario: huella, niveles y áreas concilian "
          "exactamente.",
          "Cimentación profunda documentada: pilotes con cabezales (lámina P05-023).",
          "Escalera original identificada: Escalera Nº 4 (P0102-L3-E)."])

slide("Programa por niveles", "Cinco plataformas más coronación sobre 22,02 m",
      tabla=[["Nivel", "NPT", "Contenido", "Neta (m²)"],
             ["N0", "±0,000", "Vestíbulo y foyer ceremonial; núcleo vertical; SS", "10,80"],
             ["N1", "+4,400", "Puesto de observación y vigilancia; aula-taller de meteorología", "10,40"],
             ["N2", "+8,800", "Estación de registro y servidores; área de refugio", "10,20"],
             ["N3", "+13,200", "Sala de investigación hidrometeorológica y gemelo digital", "10,60"],
             ["N4", "+17,600", "Puente de mando / cubierta de observación (aforo 20)", "11,00"],
             ["Cub.", "+22,020", "Asta, pararrayos, FV 2,0 kWp, AWS y antenas", "—"],
             ["", "", "TOTAL", "53,00"]],
      img=F + "G-04_cuadro_areas.png")

slide("La Sala Técnica de Investigación Hidrometeorológica",
      "Ficha del objeto · ACA-STH-15 · ex «Sala Meteorología»",
      kpis=[("40,00 m²", "programa declarado"), ("38,50 m²", "huella verificada"),
            ("3,30 m", "altura"), ("5–10", "personas"), ("1975", "inicio de la serie de registro")],
      bullets=[
          "Unidad operativa que el documento fuente exige modernizar con tecnología antivandálica "
          "y enfoque marítimo-portuario.",
          "Distribución documentada: estaciones 9,00 · servidores 5,00 · circulación 6,00 · "
          "SS 3,00 · mesón 2,25 · área libre 14,75 m².",
          "Inconsistencia abierta: el programa suma 40,00 m² pero la huella geométrica es de "
          "38,50 m² (RFI-ARE-01). Se adopta la huella y se reescala el programa.",
          "No existe lámina individualizada de la Sala en el inventario Portaplanos: RFI-DOC-01."],
      img=F + "G-05_zonificacion_sala.png")

slide("Diagnóstico patológico post-sísmico", "Evaluación preliminar por nivel y elemento",
      img=F + "G-07_mapa_dano.png",
      bullets=[
          "Planta baja con daño D4: reconstrucción con reintegración patrimonial.",
          "Niveles intermedios D2–D3: consolidación, encamisado y reparación.",
          "Coronación y asta D4: reposición distinguible, sin falsificación histórica.",
          "Cimentación D1 sin evidencia visible: verificación obligatoria antes de cualquier "
          "decisión (RFI-GEOT-01, RFI-PAT-01)."])

slide("Doctrina de intervención", "Conservar · consolidar · reintegrar · reponer · retirar",
      bullets=[
          "CONSOLIDAR la materialidad de 1951-1958 siempre que el diagnóstico lo permita: es "
          "parte del valor del bien.",
          "REINTEGRAR lo perdido con distinguibilidad: la intervención de 2026-2028 se lee como "
          "tal, nunca como obra original.",
          "REPONER con fidelidad documental lo que tiene lámina verificada (escalera Nº 4, "
          "geometría de plantas).",
          "RETIRAR solo lo irrecuperable o inseguro, con acta, registro fotográfico y acopio "
          "clasificado de piezas.",
          "ALTURA ADOPTADA: 22,02 m, documentación vigente de 1952; los 12,20 m originales "
          "pertenecen a la serie 15 DF 30, anulada por el plano P05-008."],
      nota="Precedencia documental verificada en el archivo: la anulación de 15 DF 30 sustenta "
           "la vigencia de 8.DF.2.362 (22,02 m). RFI-ALT-01 permanece abierta para verificación "
           "física.")

slide("Concepto arquitectónico: «El Vigía de la Memoria»",
      "La misma vertical que sostiene el puente de mando sostiene el mástil de instrumentos",
      img=F + "G-03_alturas.png",
      bullets=[
          "Volumen prismático esbelto de hormigón visto, bandas horizontales blancas y vidriado "
          "azul-verde de control solar: el lenguaje del conjunto de Malaussena.",
          "Dos vocaciones en una pieza: la ceremonia y la medición.",
          "Coronamiento técnico plano con asta, pararrayos, fotovoltaica y estación AWS."])

slide("Estructura, cimentación y acción sísmica", "Esbeltez ≈ 6,1: el comportamiento dinámico manda",
      img=F + "G-06_estructura_refuerzo.png",
      bullets=[
          "Pórticos de hormigón armado sobre pilotes y cabezales existentes.",
          "Refuerzo por encamisado en N0–N2 y disipación en niveles altos.",
          "Diseño por secuencia sísmica: el segundo evento actuó sobre estructura fisurada.",
          "Verificación de viento y confort en el puente de mando y fatiga de la unión "
          "asta-coronación."])

slide("MEP y protección contra descargas", "Cargas críticas: instrumentación, registro y emergencia",
      img=F + "G-09_unifilar.png",
      bullets=[
          "45 kVA estimados; TGBT con ATS; UPS de 10 kVA para instrumentación y registro.",
          "Sala de servidores con equipo de precisión y redundancia N+1; rango 18–27 °C y "
          "40–60 % HR.",
          "Pararrayos y bajante dedicada en el asta, separada de las redes de datos (IEC 62305).",
          "PCI: detección en todos los niveles, extinción portátil y hidrante exterior del anillo "
          "en la plaza de honor."])

slide("Instrumentación meteorológica y telemetría", "La estación como infraestructura crítica del campus",
      img=F + "G-08_estacion_met.png",
      bullets=[
          "Mástil de 10,00 m con anemómetro y veleta; abrigo tipo Stevenson; parcela de sensores.",
          "Datalogger con registro local y replicación al CDP (Torre B) por fibra OS2.",
          "Control de calidad del dato con metadatos y certificados de calibración vigentes.",
          "Serie histórica desde 1975: migración y publicación como activo institucional "
          "(RFI-MET-01)."])

slide("Industria 5.0, HBIM y gemelo digital", "Patrimonio monitorizado, no patrimonio museificado",
      img=F + "G-11_hbim.png",
      bullets=[
          "Escaneo láser y fotogrametría de lo existente antes de cualquier demolición.",
          "Modelo federado en CDE con estados 01–04 y codificación UMC-T / UMC-S.",
          "Acelerómetros e inclinómetros en N2 y coronación tras el doblete sísmico.",
          "Enfoque humanocéntrico: la tecnología apoya la observación manual, no la sustituye."])

slide("Accesibilidad, aforo y evacuación vertical", "Una sola escalera: el caso crítico del proyecto",
      img=F + "G-12_evacuacion.png",
      bullets=[
          "Aforo de diseño: 20 personas en el puente de mando; 5–10 en la Sala.",
          "Plataforma elevadora accesible sin sustituir rutas de evacuación.",
          "Compensaciones: área de refugio en N2, comunicación por voz, emergencia redundante y "
          "protocolo de desalojo previo a actos con aforo completo.",
          "El cálculo de recorrido y ancho confirmará la solución o exigirá segunda salida "
          "(RFI-PRO-01)."])

slide("Obras exteriores y subproyecto patrimonial", "Plaza de honor, banda de protocolo y Fracción 1",
      tabla=[["Interfaz", "Contenido"],
             ["Torre ↔ Sala", "Junta estructural y de servicios a 3,61 m; drenaje y telemetría comunes"],
             ["Torre ↔ Aula Magna", "Adosamiento y arriostramiento; foyer y ceremonia compartidos"],
             ["Torre ↔ Torre B (CDP)", "Fibra OS2, replicación de dato, ciberseguridad, respaldo"],
             ["Conjunto ↔ Campus", "Corredor de redes, anillo de emergencia, drenaje, paisajismo"]],
      bullets=[
          "La Fracción 1 se interviene como una sola unidad: un levantamiento, un modelo HBIM, "
          "una matriz de daño y una cronología coordinada.",
          "Condición suspensiva: no se inicia obra del Área Cultural sin levantamiento y "
          "diagnóstico completos de la Fracción 1."])

slide("Especificaciones y cómputos", "28 capítulos de especificación · BOQ Rev.0 derivado de la geometría",
      tabla=[["Partida principal", "Unid.", "Cantidad", "Base"],
             ["Encamisados y refuerzo de machones", "m²", "96", "10 × 2,40 × 4,00 m"],
             ["Recreación de losas y vigas N0–N2", "m²", "40,50", "3 × 13,50 m²"],
             ["Reposición de cerramientos y fachada", "m²", "129", "40 % de 323 m²"],
             ["Demolición y escombros patrimoniales", "m³", "35", "colapso N0 y coronación"],
             ["Obras exteriores y plaza de honor", "m²", "380", "urbanismo inmediato"],
             ["Estación hidrometeorológica completa", "gl", "1", "AWS + mástil + abrigo"]],
      nota="Los equipos e instrumentos son partidas separadas de bienes muebles con "
           "especificación por fabricante.")

slide("Inversión estimada", "Estimación ROM · AACE Clase 5 · banda −25 % / +40 %",
      img=F + "G-13_rom.png",
      kpis=[("2,09", "MUSD mínimo"), ("3,25", "MUSD máximo"), ("7 %", "ingeniería y gerencia"),
            ("18 %", "contingencia")],
      nota="No es presupuesto de licitación. La instrumentación meteorológica concentra la mayor "
           "varianza y se licitará por desempeño.")

slide("Programación de referencia", "≈ 30 meses con seis gates de control",
      img=F + "G-14_cronograma.png",
      bullets=[
          "Fase A (4 m): escaneo TLS, patología, geotecnia y topografía — cierra la información "
          "de campo.",
          "Fases B y C solapadas: ingeniería, autorización patrimonial y licitación.",
          "Fase D (12 m): consolidación, refuerzo, arquitectura, MEP y exteriores.",
          "Estación provisional instalada en el mes 1 para no interrumpir la serie histórica."])

slide("Riesgos principales y tratamiento", "Matriz del capítulo 25.1",
      img=F + "G-15_mapa_riesgos.png",
      tabla=[["Riesgo", "Tratamiento"],
             ["Réplica sísmica durante la obra", "Apuntalamiento, protocolo y monitoreo desde el mes 1"],
             ["Geotecnia y pilotes sin verificar", "Campaña en Fase A; condición suspensiva"],
             ["Precedencia documental y tres alturas", "Verificación archivística y física (RFI-ALT-01)"],
             ["Pérdida de piezas en el desescombro", "Desmontaje por elementos con acta y trazabilidad"]])

slide("Información pendiente (RFI críticas)", "Lo que el Consejo debe ordenar cerrar",
      tabla=[["Código", "Información requerida", "Responsable"],
             ["RFI-ALT-01", "Verificación de las alturas 12,20 / 15,80 / 22,02 m y de la anulación de 15 DF 30", "Archivo y topografía"],
             ["RFI-GEO-002", "Polígono de parcela certificado y BM-UMC-01", "Topografía"],
             ["RFI-GEOT-01", "Geotecnia con verificación de pilotes y cabezales", "Geotecnia"],
             ["RFI-PAT-01", "Inspección estructural detallada con ensayos y testigos", "Especialista estructural"],
             ["RFI-DOC-01", "Lámina individualizada de la Sala en el archivo MOP u otros fondos", "Archivo"],
             ["RFI-NOR-01", "Normativa vigente y autoridades competentes, incluido patrimonio", "Asesor legal-técnico"]])

slide("Condición de emisión y límites de uso", "Lo que el Consejo Universitario debe conocer antes de aprobar",
      col_izq=("No está definido ni calculado", [
          "Cimentación: sin geotecnia no es posible definir el refuerzo definitivo de pilotes.",
          "Estructura: no hay cálculo estructural ni armaduras.",
          "Instalaciones: no hay memorias de cálculo firmadas.",
          "Cotas: no existe BM definido; las alturas son relativas al NPT ±0,000.",
          "Diagnóstico: la evaluación de daño es preliminar y requiere inspección detallada."]),
      col_der=("Sí está definido con precisión", [
          "Programa funcional completo y verificado, con sumas de áreas exactas.",
          "Geometría adoptada justificada sobre precedencia documental del archivo MOP.",
          "Doctrina patrimonial de intervención y criterio de distinguibilidad.",
          "Estimación ROM Clase 5, cronograma con gates y matriz de riesgos.",
          "Listado auditado de planos y fotografías del inventario Portaplanos 01–05."]))

slide("Acuerdos que se solicitan al Consejo Universitario", "Propuesta de resolución",
      bullets=[
          "1. APROBAR el expediente UMC2030-P04-TOBSHM-R02 como base de ingeniería básica para "
          "contratar levantamiento, geotecnia, inspección estructural e ingeniería de detalle.",
          "2. ORDENAR el cierre de las RFI críticas (ALT-01, GEO-002, GEOT-01, PAT-01, DOC-01, "
          "NOR-01) como condición suspensiva para el inicio de obra.",
          "3. APROBAR la altura de proyecto de 22,02 m sobre la base de la precedencia documental, "
          "manteniendo 12,20 m como antecedente histórico.",
          "4. RATIFICAR la doctrina patrimonial de intervención con distinguibilidad de lo "
          "contemporáneo y someterla al órgano de patrimonio cultural.",
          "5. AUTORIZAR la estación meteorológica provisional desde el mes 1 para preservar la "
          "serie histórica iniciada en 1975.",
          "6. APROBAR la banda de inversión ROM de 2,09 – 3,25 MUSD (AACE Clase 5) y su "
          "actualización trimestral.",
          "7. DESIGNAR la instancia responsable de la coordinación del Área Cultural y de la "
          "custodia del Entorno Común de Datos."])

slide("Campus-Buque Digital UMC · El Vigía de la Memoria",
      "Dos edificaciones patrimoniales, una sola intervención: la ceremonia y la medición",
      kpis=[("106,00 m²", "de intervención"), ("22,02 m", "coronación"),
            ("3,61 m", "entre Torre y Sala"), ("≈ 30", "meses"),
            ("1951 → 2030", "continuidad patrimonial")],
      nota=f"Consejo Universitario UMC · Cap. Alt. / Dr. Guillermo Antonio Riut Hernández – Rector "
           f"· Expediente {COD}")


# ------------------------------------------------------------------ render PDF
def render_pdf(path):
    from reportlab.lib.pagesizes import landscape, A4
    from reportlab.lib.units import mm
    from reportlab.lib import colors
    from reportlab.lib.styles import ParagraphStyle
    from reportlab.lib.enums import TA_LEFT
    from reportlab.pdfgen import canvas as _c
    from reportlab.lib.utils import ImageReader
    W, H = landscape(A4)
    c = _c.Canvas(path, pagesize=landscape(A4))
    c.setTitle("UMC · Presentación Consejo Universitario · Proyecto 04 · R02")
    c.setAuthor("Universidad Marítima del Caribe – UMC")
    s_t = ParagraphStyle("t", fontName="Helvetica-Bold", fontSize=17, leading=20,
                         textColor=colors.white)
    s_st = ParagraphStyle("st", fontName="Helvetica", fontSize=9.2, leading=12,
                          textColor=colors.HexColor("#cfe0ea"))
    s_b = ParagraphStyle("b", fontName="Helvetica", fontSize=9.0, leading=12.4,
                         textColor=colors.HexColor("#12212b"))
    s_bh = ParagraphStyle("bh", fontName="Helvetica-Bold", fontSize=9.6, leading=12,
                          textColor=colors.HexColor("#0b3c5d"))
    s_k1 = ParagraphStyle("k1", fontName="Helvetica-Bold", fontSize=15, leading=17,
                          textColor=colors.HexColor("#0b3c5d"), alignment=1)
    s_k2 = ParagraphStyle("k2", fontName="Helvetica", fontSize=7.2, leading=9,
                          textColor=colors.HexColor("#33475a"), alignment=1)
    s_n = ParagraphStyle("n", fontName="Helvetica", fontSize=8.2, leading=10.6,
                         textColor=colors.HexColor("#7d1f24"))
    s_tb = ParagraphStyle("tb", fontName="Helvetica", fontSize=7.6, leading=9.6,
                          textColor=colors.HexColor("#12212b"))
    s_tbh = ParagraphStyle("tbh", fontName="Helvetica-Bold", fontSize=7.6, leading=9.6,
                           textColor=colors.white)
    from reportlab.platypus import Paragraph, Table, TableStyle

    for i, sl in enumerate(S, 1):
        # banda superior
        c.setFillColor(colors.HexColor(AZUL)); c.rect(0, H - 34 * mm, W, 34 * mm, fill=1, stroke=0)
        c.setFillColor(colors.HexColor(ROJO)); c.rect(0, H - 35.6 * mm, W, 1.6 * mm, fill=1, stroke=0)
        p = Paragraph(sl["t"], s_t); w, h = p.wrap(W - 30 * mm, 20 * mm)
        p.drawOn(c, 12 * mm, H - 14 * mm - h)
        p = Paragraph(sl["st"], s_st); w2, h2 = p.wrap(W - 30 * mm, 12 * mm)
        p.drawOn(c, 12 * mm, H - 14 * mm - h - h2 - 1)
        y = H - 44 * mm
        x0 = 12 * mm
        content_w = W - 24 * mm
        img = sl.get("img")
        left_w = content_w * (0.52 if img else 1.0)
        # KPIs
        if sl.get("kpis"):
            ks = sl["kpis"]; kw = content_w / len(ks)
            for j, (v, l) in enumerate(ks):
                xx = x0 + j * kw
                c.setFillColor(colors.HexColor("#eef2f5"))
                c.rect(xx + 1.5 * mm, y - 16 * mm, kw - 3 * mm, 16 * mm, fill=1, stroke=0)
                c.setFillColor(colors.HexColor(ACERO))
                c.rect(xx + 1.5 * mm, y - 16 * mm, kw - 3 * mm, 1.2 * mm, fill=1, stroke=0)
                pp = Paragraph(v, s_k1); _, hh = pp.wrap(kw - 6 * mm, 10 * mm)
                pp.drawOn(c, xx + 3 * mm, y - 7.5 * mm)
                pp = Paragraph(l, s_k2); pp.wrap(kw - 6 * mm, 8 * mm)
                pp.drawOn(c, xx + 3 * mm, y - 14 * mm)
            y -= 20 * mm
        # columnas o bullets
        if sl.get("col_izq"):
            for k, key in enumerate(("col_izq", "col_der")):
                if key not in sl:
                    continue
                tit, items = sl[key]
                xx = x0 + k * (content_w / 2)
                cw = content_w / 2 - 6 * mm
                pp = Paragraph(tit, s_bh); _, hh = pp.wrap(cw, 10 * mm)
                pp.drawOn(c, xx, y - hh)
                yy = y - hh - 4 * mm
                col = ROJO if k else ACERO
                c.setFillColor(colors.HexColor(col)); c.rect(xx, yy + 1 * mm, 24 * mm, .9 * mm,
                                                             fill=1, stroke=0)
                for it in items:
                    pp = Paragraph("•  " + it, s_b)
                    _, hh = pp.wrap(cw, 60 * mm)
                    pp.drawOn(c, xx, yy - hh)
                    yy -= hh + 2.2 * mm
        elif sl.get("bullets"):
            yy = y
            for it in sl["bullets"]:
                pp = Paragraph("•  " + it, s_b)
                _, hh = pp.wrap(left_w - 4 * mm, 60 * mm)
                pp.drawOn(c, x0, yy - hh)
                yy -= hh + 2.4 * mm
        if sl.get("tabla"):
            rows = sl["tabla"]
            data = [[Paragraph(cc, s_tbh if ii == 0 else s_tb) for cc in r]
                    for ii, r in enumerate(rows)]
            t = Table(data, colWidths=[left_w * (0.18 if len(rows[0]) == 3 else 0.30),
                                       *[left_w * ((0.82 if len(rows[0]) == 3 else 0.70) /
                                                   (len(rows[0]) - 1))] * (len(rows[0]) - 1)],
                      hAlign="LEFT")
            t.setStyle(TableStyle([
                ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor(AZUL)),
                ("GRID", (0, 0), (-1, -1), .4, colors.HexColor("#c9d4dc")),
                ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#f1f4f6")]),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 3), ("RIGHTPADDING", (0, 0), (-1, -1), 3),
                ("TOPPADDING", (0, 0), (-1, -1), 2), ("BOTTOMPADDING", (0, 0), (-1, -1), 2)]))
            tw, th = t.wrap(left_w, 200 * mm)
            t.drawOn(c, x0, y - th - (0 if not sl.get("bullets") else 0))
        if img and os.path.exists(img):
            ir = ImageReader(img); iw, ih = ir.getSize()
            box_w = content_w * 0.46; box_h = H - 62 * mm
            sc = min(box_w / iw, box_h / ih)
            c.drawImage(img, x0 + left_w + 2 * mm, y - box_h + (box_h - ih * sc) / 2,
                        width=iw * sc, height=ih * sc, preserveAspectRatio=True, mask="auto")
        if sl.get("nota"):
            pp = Paragraph(sl["nota"], s_n)
            _, hh = pp.wrap(content_w - 8 * mm, 30 * mm)
            c.setFillColor(colors.HexColor("#fdf3f3"))
            c.rect(x0, 10 * mm, content_w, hh + 5 * mm, fill=1, stroke=0)
            c.setFillColor(colors.HexColor(ROJO)); c.rect(x0, 10 * mm, 1.6 * mm, hh + 5 * mm,
                                                          fill=1, stroke=0)
            pp.drawOn(c, x0 + 4 * mm, 12.5 * mm)
        # pie
        c.setStrokeColor(colors.HexColor(AZUL)); c.setLineWidth(.6)
        c.line(12 * mm, 8 * mm, W - 12 * mm, 8 * mm)
        c.setFont("Helvetica", 6.2); c.setFillColor(colors.HexColor("#a4262c"))
        c.drawString(12 * mm, 5.4 * mm, SELLO)
        c.setFont("Helvetica-Bold", 7.4); c.setFillColor(colors.HexColor(AZUL))
        c.drawRightString(W - 12 * mm, 5.4 * mm, f"{i} / {len(S)}")
        c.showPage()
    c.save()


# ------------------------------------------------------------------ render HTML
def render_html(path):
    def b64(p):
        if not os.path.exists(p):
            return ""
        return "data:image/png;base64," + base64.b64encode(open(p, "rb").read()).decode()
    secs = []
    for i, sl in enumerate(S, 1):
        parts = [f"<section><h2>{i} · {sl['t']}</h2><p class='st'>{sl['st']}</p>"]
        if sl.get("kpis"):
            parts.append("<div class='kpis'>" + "".join(
                f"<div class='kpi'><b>{v}</b><span>{l}</span></div>" for v, l in sl["kpis"]) + "</div>")
        if sl.get("col_izq"):
            parts.append("<div class='cols'>")
            for key in ("col_izq", "col_der"):
                if key in sl:
                    tit, items = sl[key]
                    parts.append(f"<div class='col'><h3>{tit}</h3><ul>" +
                                 "".join(f"<li>{x}</li>" for x in items) + "</ul></div>")
            parts.append("</div>")
        if sl.get("bullets"):
            parts.append("<ul>" + "".join(f"<li>{x}</li>" for x in sl["bullets"]) + "</ul>")
        if sl.get("tabla"):
            rows = sl["tabla"]
            parts.append("<table><thead><tr>" + "".join(f"<th>{c}</th>" for c in rows[0]) +
                         "</tr></thead><tbody>" + "".join(
                             "<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>"
                             for r in rows[1:]) + "</tbody></table>")
        if sl.get("img"):
            parts.append(f"<img src='{b64(sl['img'])}'/>")
        if sl.get("nota"):
            parts.append(f"<div class='nota'>{sl['nota']}</div>")
        parts.append("</section>")
        secs.append("".join(parts))
    html = f"""<!DOCTYPE html><html lang='es'><head><meta charset='utf-8'>
<title>UMC · Presentación Consejo Universitario · Proyecto 04 · R02</title>
<style>body{{font-family:"Segoe UI",Arial,sans-serif;margin:0;background:#e8ecef;color:#12212b}}
section{{max-width:1000px;margin:22px auto;background:#fff;padding:30px 38px;
box-shadow:0 2px 14px rgba(0,0,0,.14);border-top:6px solid #0b3c5d}}
h2{{color:#0b3c5d;font-size:1.35rem;margin:0 0 .2em}}
.st{{color:#33475a;font-size:.9rem;margin-top:0}}
h3{{color:#1d5b7a;font-size:.95rem;margin:.4em 0}}
li{{font-size:.87rem;margin:.25em 0}}
table{{border-collapse:collapse;width:100%;font-size:.78rem;margin:.7em 0}}
th{{background:#0b3c5d;color:#fff;padding:5px 7px;border:1px solid #0b3c5d;text-align:left}}
td{{border:1px solid #c9d4dc;padding:4px 7px;vertical-align:top}}
tr:nth-child(even){{background:#f4f6f8}}
.kpis{{display:flex;gap:10px;flex-wrap:wrap;margin:.8em 0}}
.kpi{{background:#eef2f5;border-top:3px solid #1d5b7a;padding:8px 14px;min-width:120px}}
.kpi b{{display:block;color:#0b3c5d;font-size:1.25rem}}
.kpi span{{font-size:.72rem;color:#33475a}}
.cols{{display:flex;gap:22px}}.col{{flex:1}}
img{{max-width:100%;margin:.6em 0;border:1px solid #c9d4dc}}
.nota{{border-left:5px solid #a4262c;background:#fdf3f3;padding:.6em .9em;font-size:.82rem;
margin-top:.8em}}
@media print{{section{{margin:0;box-shadow:none;page-break-after:always;max-width:none}}}}</style>
</head><body>{''.join(secs)}
<section><p class='nota'>INGENIERÍA BÁSICA / ANTEPROYECTO — EMITIDO PARA COORDINACIÓN Y
PRESUPUESTO PRELIMINAR — NO APTO PARA CONSTRUCCIÓN · {COD} · {FECHA}</p></section>
</body></html>"""
    open(path, "w", encoding="utf-8").write(html)


if __name__ == "__main__":
    os.makedirs("entregables", exist_ok=True)
    base = f"entregables/{COD}_PRESENTACION-CONSEJO-UNIVERSITARIO"
    render_pdf(base + ".pdf")
    render_html(base + ".html")
    print("slides:", len(S), "->", base + ".pdf / .html")

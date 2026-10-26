# -*- coding: utf-8 -*-
"""PRESENTACION_UMC_2025-2030_CONSEJO-UNIVERSITARIO — Proyecto 05 · R01.
Contenido: Patio / Cubierta de Honor (EXT-PCH-04). Formato homólogo a la
«Presentación Consejo Universitario · Proyecto 04 · R02» (32 láminas:
portada con cifras, cómo leer, siglas, agenda por bloques, fichas con chips,
doctrina, ingeniería, inversión, acuerdos, cierre). Genera HTML + PPTX."""
import base64, glob, html as H, os

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "entregables")
FIGD = os.path.join(OUT, "figuras")
BASE = "PRESENTACION_UMC_2025-2030_CONSEJO-UNIVERSITARIO"
COD = "UMC2030-P05-EXTPCH-R01"
FECHA = "26 de octubre de 2026"
SELLO = ("INGENIERÍA BÁSICA / ANTEPROYECTO — EMITIDO PARA COORDINACIÓN Y "
         "PRESUPUESTO PRELIMINAR — NO APTO PARA CONSTRUCCIÓN")
CONF = "Uso institucional UMC – Marina Mercante de Venezuela"

def figpng(cod):
    g = glob.glob(os.path.join(FIGD, "*FIGURA-%s_*.png" % cod))
    return g[0] if g else None

S = []
def sl(t, sub, stats=None, b=None, tab=None, img=None, note=None, k=""):
    S.append(dict(t=t, sub=sub, stats=stats or [], b=b or [], tab=tab, img=img, note=note, k=k))

# 1 ─ PORTADA
sl("Patio / Cubierta de Honor — Explanada Ceremonial y Punto de Reunión R-1",
   "Proyecto 05 del Plan Maestro UMC 2025–2030 · Restauración patrimonial post-sísmica · "
   "Presentación para el Consejo Universitario y el Rectorado",
   stats=[("1.625,00 m²", "de explanada patrimonial"), ("100 %", "del pavimento con daño D2–D4"),
          ("1.300", "cadetes en formación"), ("≈ 9", "meses de ejecución"),
          ("0,57 – 0,90", "MUSD · ROM Clase 5 (neto–integral)")],
   b=["Cap. Alt. / Dr. Guillermo Antonio Riut Hernández – Rector · %s · Expediente %s" % (FECHA, COD)])

# 2 ─ CÓMO LEER
sl("Cómo leer esta presentación", "Naturaleza, alcance y límites del documento",
   b=["QUÉ ES — El desarrollo en nivel de INGENIERÍA BÁSICA / ANTEPROYECTO de la restauración integral del "
      "Patio / Cubierta de Honor (EXT-PCH-04): programa, geometría, diagnóstico post-sísmico, estimación ROM, "
      "cronograma y riesgos.",
      "QUÉ ES — Un instrumento para decidir y la base técnica para contratar la topografía (TLS), la geotecnia, "
      "la videoinspección de colectores y la ingeniería de detalle.",
      "QUÉ NO ES — No es un proyecto ejecutivo: no contiene cálculo estructural del pavimento, memorias firmadas "
      "ni planos de replanteo.",
      "QUÉ NO ES — No es apto para replanteo ni construcción, y no sustituye permisos ni la autorización del "
      "órgano de patrimonio.",
      "QUÉ NO ES — No acredita inspección realizada: el mapa espacial de daño es hipótesis de trabajo sujeta a "
      "TLS (RFI-PAT-01)."])

# 3 ─ SIGLAS
sl("Siglas y abreviaturas de la exposición", "Guía de lectura rápida: todos los términos de esta exposición",
   b=["AACE — Association for the Advancement of Cost Engineering (clases de estimación) · AIM — Asset Information Model",
      "BOQ — Bill of Quantities: cómputos y presupuesto · C250 — clase de carga de rejilla (EN 124, referencial)",
      "CDE — Entorno Común de Datos BIM · COVENIN — Comisión Venezolana de Normas Industriales",
      "D0–D4 — escala referencial de daño post-sísmico (adaptada ATC-20/condición de pavimentos)",
      "EXT-PCH-04 — código funcional del Patio / Cubierta de Honor · HBIM — Heritage BIM",
      "IEC 62305 — protección contra descargas atmosféricas · IP66/IP67/IK10 — grados de protección",
      "MOP — Ministerio de Obras Públicas (archivo 1951, Malaussena) · MR — módulo de rotura del concreto",
      "NPT — Nivel de Piso Terminado (±0,000 = foyer del Aula Magna) · OMI/STCW — convenios marítimos",
      "OMM — Organización Meteorológica Mundial · PDC — penetrómetro dinámico de cono",
      "PEAD SN8 — polietileno de alta densidad, rigidez anular 8 kN/m² · R-1 — punto de reunión primario",
      "RFI — Request for Information (17 en R01) · ROM — Rough Order of Magnitude (−25 %/+40 %)",
      "SPDA — sistema de protección contra descargas atmosféricas · TLS — escaneo láser terrestre",
      "Tr — período de retorno (25 años) · UTM — Universal Transverse Mercator (huso 19N)"],
   note="Fuente: anexo C del expediente R01 (§27), ampliado con los términos propios de esta exposición.")

# 4 ─ AGENDA
sl("Agenda", "Contenido de la exposición ante el Consejo Universitario",
   tab=(["#", "Bloque", "Láminas"],
        [["1", "Marco, patrimonio y evento sísmico", "5 – 7"],
         ["2", "El objeto: implantación, ficha y programa", "8 – 12"],
         ["3", "Diagnóstico y doctrina de intervención", "13 – 15"],
         ["4", "Ingeniería: pavimento, drenaje, eléctrica, asta/OMM, redes, Industria 5.0", "16 – 22"],
         ["5", "Evacuación R-1, interfaces, especificaciones, inversión, plazos y riesgos", "23 – 29"],
         ["6", "Condición de emisión y acuerdos solicitados", "30 – 32"]]))

# 5 ─ MARCO
sl("Marco: el Plan Maestro UMC 2025–2030", "Instrumento rector y posición del Proyecto 05",
   b=["El Plan Maestro declara doce proyectos estratégicos; este expediente desarrolla el quinto: la restauración "
      "del espacio ceremonial central de la Proa.",
      "Se coordina como un solo modelo de implantación con el Proyecto 01 (Torre A – STCW), el Proyecto 02 "
      "(Torre B – CDP), el Proyecto 03 (Vicerrectorado) y el Proyecto 04 (Torre de Observación y Sala Técnica).",
      "El corredor tecnológico-administrativo y el corredor de redes enterrado son infraestructura común que este "
      "proyecto no modifica; la acometida se toma mediante cámara propia.",
      "Autoría del documento fuente: Prof. Jhonny Da Silva Izquierdo (MSc. Ing. Lic., CIV 95787).",
      "Ningún plano de este proyecto modifica la implantación general del Plan Maestro sin revisión aprobada del "
      "Plan de Implantación."])

# 6 ─ PATRIMONIO
sl("Patrimonio: la Escuela Náutica de Venezuela y Malaussena", "El valor que se protege: modernidad venezolana 1951–1958",
   tab=(["Campo", "Registro documental"],
        [["Denominación original", "Plaza de Armas de la Escuela Náutica de Venezuela («Catia La Mar»)"],
         ["Arquitecto", "Luis Raimundo Malaussena Andueza"],
         ["Estructural", "Oficina Técnica Gutiérrez & Co. S.A."],
         ["Contratante", "MOP – Dirección de Edificios"],
         ["Cronología", "proyecto estructural 28-08-1951 (15 DF 30 · 8.DF.2.364) · urbanismo 24-10-1953 (P04-L5-A) · obras 1956–1958"],
         ["Archivo", "198 PDF y 487 fotografías (Portaplanos Nº 01–05; 26 láminas/series pertinentes al patio — entregable E1)"]]),
   note="El patio fue concebido el 28-08-1951 como una sola pieza con las Fracciones 1 y 2: la explanada que el "
        "Aula Magna y la Torre enmarcan. Registro histórico: Lámina 3 de PATIO_HONOR CATASTRO.pdf.")

# 7 ─ EVENTO
sl("El doblete sísmico del 24 de junio de 2026", "Condición de partida: explanada INHABILITADA y punto R-1 suspendido",
   stats=[("M 7,2", "primer evento"), ("M 7,5", "segundo evento"), ("24-06-2026", "fecha"),
          ("D4", "daño máximo (inducido)"), ("0", "personas: uso suspendido")],
   b=["El segundo evento, de mayor magnitud, actuó sobre losas ya fisuradas: el daño del pavimento es acumulativo "
      "y cubre el 100 % de la poligonal (D3 680,00 m² · D2 565,00 m² · D4 380,00 m²).",
      "El borde Babor recibió el impacto de escombros de la Torre de Observación (coronación +22,02 m): zona de "
      "exclusión vigente, alcance transferido al P04.",
      "Clasificación de uso propuesta: INHABILITADO para paradas y desfiles; función R-1 SUSPENDIDA sin alterno "
      "designado → RFI-EVA-01 (CRÍTICA).",
      "Evidencia forense: Lámina 4 «POST SISMO» de PATIO_HONOR CATASTRO.pdf + dictamen de la Ficha EXT-PCH-04 "
      "(entregable E5). No se fabrican imágenes."])

# 8 ─ IMPLANTACIÓN
sl("Implantación de la Proa Central", "Un solo conjunto ceremonial entre las tres fracciones",
   b=["Explanada de 50,00 × 32,50 m enmarcada por la Fracción 1 (Aula Magna, NPT ±0,000), la Fracción 2 "
      "(13 módulos × 4,00 m = 52,00 m) y la Fracción 3 (dormitorios).",
      "Borde Babor: Torre CUL-TOO-02 y Sala ACA-STH-15 (Proyecto 04) a 34,81 m del centroide (ΔE +32,21 / ΔN −13,21).",
      "Centroide UTM 19N: E 715.324,40 / N 1.172.523,10 (10°36'02,55\"N · 67°01'55,20\"O) · BM-UMC-01 por establecer.",
      "Vialidad de emergencia perimetral preservada íntegra durante toda la obra."],
   img=figpng("G01"))

# 9 ─ EMBLEMA
sl("El emblema vigente: la cubierta de formación", "La explanada de honor: el valor ceremonial que el proyecto protege y restituye",
   b=["El plano horizontal donde la institución forma, pasa revista y gradúa a sus oficiales frente al asta del "
      "Pabellón: paradas navales, graduaciones OMI/STCW, izada y arriada diarias.",
      "El registro histórico (1951–1959) documenta la explanada en pleno uso: formaciones de cadetes, el asta "
      "mayor, el frente del Auditorio y los corredores cubiertos EXT-CTC-15.",
      "La Cubierta de Honor opera además como Punto de Reunión y Evacuación Sísmica Primario R-1 del Sector Proa "
      "(1.080–1.625 personas).",
      "Contraste documental: la misma composición en la fotografía histórica de Malaussena y en el registro "
      "institucional UMC 2026 (anexo D del expediente)."],
   note="Registro fotográfico: Lámina 3 (histórico) y Lámina 4 (post-sismo) de PATIO_HONOR CATASTRO.pdf — Drive institucional.")

# 10 ─ FICHA
sl("El Patio / Cubierta de Honor", "Ficha del objeto · EXT-PCH-04 · UMC-ED-000 (normalización UMC-EXT-004 en trámite, RFI-COD-05)",
   stats=[("50,00 × 32,50 m", "poligonal pavimentada"), ("1.625,00 m²", "= 100 % del objeto"),
          ("±0,000", "NPT (foyer Fracción 1)"), ("1,2 – 1,5 %", "pendiente pluvial"),
          ("12,00 m", "Asta Mayor Ceremonial")],
   b=["Pavimento rígido con acabado granítico / cemento martelinado de 1951, modulado sobre la retícula "
      "estructural de 4,00 m.",
      "Interfaz dual EXT (Espacios Exteriores) / CUL (Área Cultural y Ceremonial) · sector Proa Central.",
      "Geometría verificada por el propio inventario: 13 módulos × 4,00 m = 52,00 m de crujía (P04-L5-A, "
      "P0102-L6-F/H/I); huella neta 50,00 × 32,50 = 1.625,00 m² ✔.",
      "Elementos asociados: asta mayor (12,00 m), tribuna de honor (RFI-PRO-01), mástil OMM nuevo (10,00 m)."])

# 11 ─ PROGRAMA
sl("Programa funcional y zonificación ceremonial", "La explanada organizada para formar, desfilar y evacuar",
   tab=(["Zona", "Ubicación", "Magnitud", "Función"],
        [["Campo de formación", "centro de la poligonal", "1.300 cadetes a 1,25 m²/ef.", "formaciones por compañías"],
         ["Eje ceremonial e izada", "eje del asta, frente F1", "franja ≈ 6 m [HIPÓTESIS]", "izada/arriada del Pabellón"],
         ["Banda de Protocolo", "borde occidental", "210,00 m²", "ceremonial (interfaz P04, sin partidas P05)"],
         ["Tribuna de Honor y podio", "frente Estribor", "por dimensionar (RFI-PRO-01)", "autoridades; podio accesible"],
         ["Punto R-1", "toda la explanada", "1.080 – 1.625 personas", "evacuación sísmica del Sector Proa"],
         ["Parcela OMM", "cuadrante NE [HIPÓTESIS]", "mástil 10,00 m", "estación de superficie (interfaz P04)"]]),
   img=None, note="Distribución espacial: hipótesis de anteproyecto (figura G-05 y lámina P-6 del expediente).")

# 12 ─ ÁREAS
sl("Cuadro de áreas y conciliación con el Proyecto 04", "Conjuntos anidados: prohibida la doble presupuestación (regla R4)",
   b=["1.625,00 m² totales ⊃ 380,00 m² del borde occidental (23,38 %, en BOQ P04-R02) ⊃ 210,00 m² de Banda de "
      "Protocolo · explanada remanente neta: 1.245,00 m² (76,62 %).",
      "Verificación: 380,00 + 1.245,00 = 1.625,00 ✔ — los subconjuntos NO se suman entre sí.",
      "Deducción económica asociada: USD 330.000 ya presupuestados en el P04 (banda 260.000 – 400.000)."],
   img=figpng("G03"))

# 13 ─ DIAGNÓSTICO
sl("Diagnóstico patológico post-sísmico", "Evaluación preliminar por zonas: el 100 % del pavimento afectado",
   b=["D3 SEVERO — 680,00 m² (41,85 %): fractura diagonal de paños y escalonamientos de 1,5–4,5 cm → demolición y "
      "reposición con reintegración.",
      "D2 MODERADO — 565,00 m² (34,77 %): fisuración y pérdida de sellos → reparación de juntas y resellado integral.",
      "D4 INDUCIDO — 380,00 m² (23,38 %): impacto de escombros de la Torre (borde Babor) → TRANSFERIDO a P04.",
      "Subbase y rellenos asentados sobre trincheras; colectores de ≈ 75 años con fuga/colapso presunto; sellos de "
      "juntas (≈ 980 m) perdidos; asta por inspeccionar."],
   img=figpng("G07"))

# 14 ─ DOCTRINA
sl("Doctrina de intervención patrimonial", "Conservar · consolidar · reintegrar · reponer · sustituir",
   b=["CONSERVAR los paños D0–D1 que la inspección de detalle confirme sanos.",
      "CONSOLIDAR bordes, brocales y franjas de transición originales.",
      "REINTEGRAR el acabado granítico/martelinado con mortero y granulometría compatibles.",
      "REPONER los paños D3 con losa contemporánea distinguible mediante JUNTA-TESTIGO DATADA — distinguibilidad "
      "de lo contemporáneo, sin falsificación histórica.",
      "SUSTITUIR las redes enterradas agotadas (colectores PEAD SN8, red eléctrica).",
      "Los fragmentos del acabado original con valor documental se registran e integran al archivo patrimonial; "
      "la doctrina se somete al órgano de patrimonio cultural (normativa citada como referencia a verificar)."])

# 15 ─ E5
sl("Registro patológico E5: siete fichas de daño", "Escala D0–D4 declarada referencial (adaptada ATC-20 / condición de pavimentos)",
   tab=(["ID", "Elemento", "Grado", "Decisión"],
        [["PAT-01", "Paños centrales (680,00 m²)", "D3 — severo", "demoler y reponer con reintegración"],
         ["PAT-02", "Paños orientales (565,00 m²)", "D2 — moderado", "reparar juntas + resellado"],
         ["PAT-03", "Borde Babor (380,00 m²)", "D4 — inducido", "transferido a P04 (condición suspensiva)"],
         ["PAT-04", "Subbase y rellenos s/ trincheras", "asentamiento dif.", "sanear + recompactar + geotextil"],
         ["PAT-05", "Colectores enterrados (≈ 140 m)", "fuga/colapso presunto", "sustituir por PEAD SN8 + estanqueidad"],
         ["PAT-06", "Sellos y flejes (≈ 980 m)", "envejecimiento + sismo", "resellado elastomérico integral"],
         ["PAT-07", "Asta Mayor y pedestal", "por inspeccionar", "restaurar/reponer s/ inspección (RFI-PAT-02)"]]),
   note="Inspecciones requeridas: TLS (RFI-PAT-01) · calicatas + PDC (RFI-GEOT-01) · videoinspección + estanqueidad (RFI-PAT-03) · georradar (RFI-PAT-04).")

# 16 ─ PAVIMENTO
sl("Ingeniería del pavimento", "Paquete estructural propuesto y retícula de juntas",
   b=["Losa de concreto (MR y espesor por calcular; preliminar e ≈ 15–18 cm [HIPÓTESIS]) sobre subbase granular "
      "mejorada y saneada (e ≈ 20–30 cm [HIPÓTESIS]) — ambos CONDICIONADOS a la geotecnia (RFI-GEOT-01).",
      "Paños de vaciado compatibles con la retícula de 4,00 m (≈ 4,00 × 5,00 m [HIPÓTESIS]); juntas de contracción "
      "selladas en ambas direcciones.",
      "Juntas sísmicas de desacople losa–Fracciones 1/2 y losa–cabezales piloteados: e = 25–50 mm, ≈ 980 m de "
      "sellado elastomérico PU.",
      "Reintegración del acabado granítico/martelinado con paños piloto aprobados antes de la producción."],
   img=figpng("G06"))

# 17 ─ GEOTECNIA
sl("Geotecnia y saneamiento de subbase", "La causa raíz del daño se verifica antes de decidir",
   b=["Hipótesis de causa: densificación/licuación local de rellenos sobre zanjas; pérdida de soporte por fuga de "
      "colectores antiguos; ausencia de desacople sísmico; envejecimiento de sellos; impacto de escombros en Babor.",
      "Campaña Fase A (≈ 2 meses): calicatas + PDC en subbase y rellenos; videoinspección y prueba de estanqueidad "
      "de colectores; georradar de trincheras; TLS del pavimento (mapa real de escalonamientos).",
      "Saneamiento: retiro de rellenos inadecuados, recompactación controlada y geotextil de separación.",
      "Ninguna decisión estructural definitiva se toma sin cerrar RFI-GEOT-01 y RFI-PAT-01…04."])

# 18 ─ DRENAJE
sl("Drenaje pluvial", "Instalación crítica: el patio como activo de resiliencia del Sector Proa",
   stats=[("73,13 / 145 L/s", "caudal propio / con faldones"), ("Tr 25", "años, período de retorno"),
          ("180 m", "canaletas con rejilla C250"), ("140 m", "PEAD SN8 Ø 300–400 mm"), ("8", "tanquillas/sumideros")],
   b=["Canaletas lineales perimetrales con rejilla clase C250 antivandálica; colectores PEAD doble pared SN8 con "
      "prueba de estanqueidad obligatoria.",
      "Descarga coordinada con el canal y la toma de quebrada documentados en el Paquete 05 del archivo (láminas "
      "R-19/R-20).",
      "Pendiente superficial restituida: 1,2 – 1,5 % (diseño original 1,0 – 1,5 % s/ P03-ENV-002)."],
   img=figpng("G08"))

# 19 ─ ELÉCTRICA
sl("Eléctrica, alumbrado y protección atmosférica", "Red subterránea nueva con juntas sísmicas flexibles",
   b=["12 luminarias LED marinas IP66 / IK10 (100–150 lux) + alumbrado de emergencia autónomo del punto R-1.",
      "2 cajas de piso IP67 para la Banda de Protocolo (megafonía y servicios de actos).",
      "Bancadas PVC/PEAD Ø 4\" con juntas sísmicas; sustituye la red histórica P03-L3-B (1951).",
      "Malla de puesta a tierra R ≤ 5 Ω y SPDA del asta y del mástil según IEC 62305.",
      "Telegestión y medición dedicada integradas al BMS/EMS del campus (CDP – Torre B)."],
   img=figpng("G09"))

# 20 ─ ASTA/OMM
sl("Asta Mayor Ceremonial y Mástil OMM", "Los dos verticales del plano ceremonial",
   stats=[("12,00 m", "Asta Mayor (partida E3.03)"), ("10,00 m", "Mástil OMM nuevo"),
          ("≤ 5 Ω", "malla de tierra común"), ("22,02 m", "Torre colindante (contexto P04)")],
   b=["Asta: fundación independiente, pedestal de concreto visto, drizas navales y podio de protocolo accesible; "
      "restauración o reposición según inspección (RFI-PAT-02).",
      "Mástil OMM: parcela de sensores con cerramiento bajo; emplazamiento condicionado al estudio de obstáculos "
      "del borde Babor (RFI-OMM-01).",
      "Telemetría integrada a la estación hidrometeorológica del P04 (Sala ACA-STH-15): un solo sistema de "
      "adquisición y registro — prohibida la duplicación (regla R12)."],
   img=figpng("G10"))

# 21 ─ REDES
sl("Redes, TIC y seguridad electrónica", "El patio conectado al Campus-Buque Digital",
   b=["Canalización subterránea de reserva TIC en las mismas bancadas eléctricas (separación normativa), con "
      "enlace al CDP / Torre B.",
      "Megafonía protocolar (cajas de piso + perímetro) y CCTV de explanada con grabación en el CDP.",
      "Protección antivandálica: luminarias IK10, rejillas atornilladas antirrobo, cerramiento bajo del mástil.",
      "Gestión de multitudes en graduaciones (1.625 personas): separación de flujos protocolares y públicos; "
      "control perimetral removible en actos."])

# 22 ─ INDUSTRIA 5.0
sl("Industria 5.0: HBIM y gemelo digital", "Del plano MOP 1951 al gemelo digital 2030",
   b=["Nube de puntos TLS del estado 2026 + restitución del estado 1951 desde las 26 láminas del listado E1 → "
      "modelo HBIM federado en el CDE con estados (1951 · 2026 · proyecto).",
      "Codificación documental UMC-[ACTIVO]-[DISCIPLINA]-[NÚMERO]-[REV]; base GIS/BIM con el desdoblamiento "
      "catastral UMC-EXT-004 / UMC-ED-000-PCH04 (RFI-COD-05).",
      "Sensorización: hitos de asentamiento en paños repuestos, niveles en tanquillas, pluviómetro del mástil, "
      "conteo de aforo en actos.",
      "Enfoque humanocéntrico: el cadete en formación, el operador de mantenimiento y la seguridad de evacuación "
      "son los usuarios de diseño."],
   img=figpng("G11"))

# 23 ─ R-1
sl("Accesibilidad, aforo y evacuación R-1", "Capítulo crítico de seguridad humana",
   stats=[("1.300", "cadetes (1,25 m²/ef.)"), ("1.625", "personas en actos (1,00 m²/p.)"),
          ("1.080 – 1.625", "capacidad punto R-1"), ("0", "hoy: R-1 suspendido")],
   b=["Rutas de aproximación desde las Fracciones 1, 2 y 3 y corredores EXT-CTC-15; señalización COVENIN 810/187; "
      "franjas podotáctiles Fondonorma 2733; itinerario accesible al podio.",
      "CONDICIÓN TRANSITORIA CRÍTICA: con el patio inhabilitado, las fuentes NO identifican punto R-1 alterno "
      "para el Sector Proa → RFI-EVA-01, prioridad MÁXIMA, responsable Planta Física + Seguridad Integral.",
      "El punto alterno debe estar designado y señalizado ANTES del inicio de obra y mantenerse durante toda la ejecución."],
   img=figpng("G12"))

# 24 ─ INTERFACES
sl("Obras exteriores e interfaces", "Matriz de coordinación del Proyecto 05",
   tab=(["Interfaz", "Objeto", "Regla"],
        [["P05 ↔ P04", "380,00 m² borde Babor · Banda 210,00 m² · Torre", "condición suspensiva + deducción USD 330.000 · lámina P-9"],
         ["P05 ↔ Fracción 1", "foyer NPT ±0,000, frente ceremonial", "no alterar accesos del Aula Magna · desacople sísmico"],
         ["P05 ↔ Fracción 2", "crujía 52,00 m · tribuna", "desacople sísmico · coordinación de actos"],
         ["P05 ↔ Fracción 3", "flujo diario de cadetes", "ruta protegida durante la obra"],
         ["P05 ↔ EXT-CTC-15", "corredores techados perimetrales", "franja de transición 1,00 m · drenaje de faldones"],
         ["P05 ↔ red PCI", "hidrante/toma siamesa borde Norte", "válvula de seccionamiento · coord. P04 Cap. 12.4"],
         ["P05 ↔ CDP Torre B", "telemetría, CCTV, telegestión", "canalización de reserva · VLAN de instrumentación"]]))

# 25 ─ ESPECIFICACIONES
sl("Especificaciones técnicas: contenido mínimo", "Dieciséis capítulos para la ingeniería de detalle",
   b=["01 Condiciones generales y seguridad con campus operativo · 02 Replanteo, TLS y BM-UMC-01 · 03 Diagnóstico "
      "y ensayos in situ · 04 Demolición controlada y gestión patrimonial de escombros",
      "05 Saneamiento geotécnico y geotextiles · 06 Colectores PEAD SN8 y estanqueidad · 07 Pavimento rígido: "
      "vaciado, curado, juntas y sellos · 08 Reintegración del acabado granítico (junta-testigo)",
      "09 Canaletas, rejillas C250 y tanquillas · 10 Asta Mayor: fundación, pedestal e izado · 11 Red eléctrica, "
      "tierra y SPDA · 12 Mástil OMM: fundación, instrumentación y calibración",
      "13 Señalización R-1 y accesibilidad · 14 Paisajismo halófilo · 15 Monitorización IoT del gemelo · "
      "16 Comisionamiento de alumbrado y drenaje"])

# 26 ─ BOQ
sl("Cómputos métricos preliminares (BOQ Rev.0)", "Partidas E1–E6 de la Ficha · no contractuales",
   tab=(["Partida", "Descripción", "Cantidad", "Asignación"],
        [["E1.01 / E1.02", "Retiro D3 + reparación D2", "680,00 + 565,00 m²", "P05-neto"],
         ["E2.01", "Saneamiento de subbase y rellenos", "≈ 1.245,00 m²", "P05-neto"],
         ["E3.01 / E3.02", "Losa nueva + sellado de juntas", "680,00 m² + 980 m", "P05-neto"],
         ["E3.03", "Asta Mayor: fundación, pedestal, podio", "gl (USD 38.500)", "P05-neto"],
         ["E4.01 / E4.02", "Drenaje completo + hidrante PCI", "gl (USD 112.000 + 14.500)", "P05-neto"],
         ["E5.01", "Eléctrica integral + tierra + SPDA", "gl (USD 96.000)", "P05-neto"],
         ["E6.01", "Señalización, paisajismo, comisionamiento", "gl (USD 28.395)", "P05-neto"],
         ["—", "Borde occidental (pavimento + juntas + Banda)", "380,00 m²", "P04 (EXCLUIDO)"]]),
   note="El mástil OMM y su instrumentación van en partida separada de equipos (RFI-OMM-01). Métricas a re-derivar del TLS y la geotecnia.")

# 27 ─ ROM
sl("Inversión estimada (ROM — AACE Clase 5)", "USD referencial · exactitud −25 % / +40 %",
   stats=[("895.000", "USD · ROM integral (1.625 m²)"), ("−330.000", "USD ya en P04-R02"),
          ("565.000", "USD · NETO adicional P05"), ("490 – 720", "kUSD · rango neto")],
   b=["Composición del integral: 765.000 directo + 53.550 ingeniería y ensayos (7,0 %) + 76.450 contingencia "
      "(10 % nominal = 76.500; redondeo de cierre declarado).",
      "Rango integral: USD 750.000 – 1.120.000 · 470,77 USD/m² (integral) · 550,77 USD/m² con cargas.",
      "Precios unitarios a sustituir por cotizaciones locales en la ingeniería de detalle; actualización trimestral."],
   img=figpng("G13"))

# 28 ─ PLAZOS
sl("Cronograma de ejecución", "≈ 9 meses en cinco fases con gates",
   b=["A Estudios previos (≈ 2,0 meses) → gate: geotecnia cierra RFI-GEOT-01 · B Demolición controlada (≈ 2,0) → "
      "gate: borde Babor consolidado por P04 · C Subbase y colectores (≈ 2,5) → gate: estanqueidad aprobada · "
      "D Pavimento (≈ 3,0) → gate: paños piloto aprobados · E Asta, eléctrica y comisionamiento (≈ 1,5).",
      "Restricciones duras: secuencia P04 → borde Babor; calendario académico-ceremonial (graduaciones); ventana "
      "de lluvias (subbase nunca abierta en pico pluvial); punto R-1 alterno operativo toda la obra.",
      "Procuración de largo plazo: rejillas C250 AISI 316, luminarias marinas, asta e instrumentación OMM."],
   img=figpng("G14"))

# 29 ─ RIESGOS
sl("Riesgos y organización", "Once riesgos gestionados · equipo de trece especialistas (A0–A12)",
   b=["Mayores (P×I): R02 colectores en peor estado (4×4) · R07 inhabilitación prolongada del R-1 (3×5) · R04 "
      "desfase del P04 bloquea el borde (3×4) · R05 pérdida de acabado histórico (3×4) · R10 demora permisológica (4×3).",
      "Mitigaciones clave: videoinspección temprana, RFI-EVA-01 antes de obra, etapabilidad frente oriental "
      "primero, protocolo patrimonial de retiro con registro fotogramétrico, expediente patrimonial anticipado.",
      "Organización: A0 dirección · A1 arquitectura patrimonial · A2 patología estructural · A3 geotecnia/pavimento · "
      "A4 hidráulica · A5 OMM · A6 eléctrica · A7 TIC · A8 costos/programación · A9 normativa · A10 control "
      "documental · A11 QA · A12 asesor legal-técnico."],
   img=figpng("G15"))

# 30 ─ CONDICIÓN
sl("Condición de emisión y límites de uso", "Lo que el Consejo Universitario debe conocer antes de aprobar",
   b=["NO ESTÁ DEFINIDO — Pavimento: sin geotecnia no hay espesor ni MR definitivos. Estructura: no hay cálculo "
      "ni armaduras. Instalaciones: no hay memorias firmadas. Cotas: no existe BM; alturas relativas al NPT "
      "±0,000. Diagnóstico espacial: el mapa de daño por bandas es hipótesis sujeta a TLS.",
      "SÍ ESTÁ DEFINIDO — Programa funcional completo con sumas de áreas exactas (1.625 = 380 + 1.245 ✔; "
      "680 + 565 + 380 = 1.625 ✔). Geometría verificada sobre el archivo MOP. Doctrina patrimonial con "
      "distinguibilidad. ROM Clase 5 conciliado con P04 sin doble presupuestación. Cronograma con gates, matriz "
      "de riesgos y listado auditado E1 (26 láminas de 198 PDF · 77 de 487 fotos).",
      "Las coordenadas consignadas son puntos de control sujetos a verificación topográfica."])

# 31 ─ ACUERDOS
sl("Acuerdos que se solicitan al Consejo Universitario", "Propuesta de resolución",
   b=["1. APROBAR el expediente UMC2030-P05-EXTPCH-R01 como base de ingeniería básica para contratar TLS, "
      "geotecnia, videoinspección e ingeniería de detalle.",
      "2. DESIGNAR de inmediato el punto de reunión R-1 alterno del Sector Proa (RFI-EVA-01, prioridad máxima), "
      "antes de cualquier obra.",
      "3. ORDENAR el cierre de las RFI críticas (EVA-01, GEO-01, GEOT-01, PAT-01…04, NOR-01) como condición "
      "suspensiva para el inicio de obra.",
      "4. RATIFICAR la secuencia P04 → borde Babor y formalizar el acta de transferencia de los 380,00 m² "
      "(RFI-ARE-05), manteniendo la deducción de USD 330.000.",
      "5. RATIFICAR la doctrina patrimonial de intervención con junta-testigo datada y someterla al órgano de "
      "patrimonio cultural.",
      "6. APROBAR la banda de inversión ROM: USD 895.000 integral / USD 565.000 neto adicional (AACE Clase 5) y "
      "su actualización trimestral.",
      "7. DESIGNAR el proyectista habilitado y la instancia responsable de la coordinación de la Proa Central y "
      "de la custodia del Entorno Común de Datos."])

# 32 ─ CIERRE
sl("Campus-Buque Digital UMC · La Cubierta de Formación", "Una explanada patrimonial, una sola intervención: la ceremonia y la seguridad",
   stats=[("1.625,00 m²", "de intervención"), ("100 %", "del daño atendido (P05+P04)"),
          ("12,00 m", "asta del Pabellón"), ("≈ 9", "meses"), ("1951 → 2030", "continuidad patrimonial")],
   b=["Restauración del pavimento ceremonial con reintegración del acabado de 1951, drenaje Tr 25, alumbrado "
      "marino, asta restituida, mástil OMM y punto R-1 rehabilitado.",
      "Consejo Universitario UMC · Cap. Alt. / Dr. Guillermo Antonio Riut Hernández – Rector · Expediente " + COD,
      "Fuente documental: Prof. Jhonny Da Silva Izquierdo (CIV 95787) · Proyectista: Por designar"])

N = len(S)

# ----------------------------- HTML -----------------------------
def build_html():
    css = """body{font-family:Helvetica,Arial,sans-serif;margin:0;background:#1c2b3a}
.slide{width:1240px;min-height:700px;margin:26px auto;background:#fff;position:relative;box-shadow:0 4px 18px rgba(0,0,0,.4);display:flex;flex-direction:column}
.bar{background:#0d2c54;color:#fff;padding:18px 46px}
.bar h1{margin:0;font-size:27px}.bar .sub{color:#d9b64a;font-size:14px;margin-top:5px}
.body{padding:20px 46px;flex:1}
.chips{display:flex;gap:14px;margin:10px 0 16px;flex-wrap:wrap}
.chip{flex:1;min-width:150px;background:#eef3f8;border-top:4px solid #b8860b;padding:12px 14px;text-align:center}
.chip .b{font-size:23px;font-weight:800;color:#0d2c54}.chip .s{font-size:11px;color:#56677a;margin-top:3px}
ul{font-size:15.5px;line-height:1.7;color:#20334a;padding-left:24px;margin:6px 0}li{margin-bottom:7px}
table{border-collapse:collapse;width:100%;font-size:13px;margin:8px 0}
th{background:#0d2c54;color:#fff;padding:6px 8px;text-align:left}td{border:1px solid #c8d2dd;padding:5px 8px}
tr:nth-child(even) td{background:#f4f7fa}
.fig{text-align:center;margin-top:6px}.fig img{max-width:1000px;max-height:400px}
.note{font-size:11.5px;color:#667;font-style:italic;padding:0 46px 6px}
.ft{display:flex;justify-content:space-between;padding:8px 20px;font-size:10.5px;border-top:1px solid #e3e9f0}
.ft .s{color:#b8860b;font-weight:700}.ft .n{color:#8aa}"""
    parts = ['<!DOCTYPE html><html lang="es"><head><meta charset="utf-8"><title>%s — Proyecto 05 · R01</title><style>%s</style></head><body>' % (BASE, css)]
    for i, d in enumerate(S, 1):
        parts.append('<div class="slide"><div class="bar"><h1>%s</h1><div class="sub">%s</div></div><div class="body">' % (H.escape(d["t"]), H.escape(d["sub"])))
        if d["stats"]:
            parts.append('<div class="chips">%s</div>' % "".join(
                '<div class="chip"><div class="b">%s</div><div class="s">%s</div></div>' % (H.escape(a), H.escape(b)) for a, b in d["stats"]))
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
        parts.append('<div class="ft"><span class="s">%s</span><span class="n">%s · %d / %d</span></div></div>' %
                     (H.escape(SELLO), COD, i, N))
    parts.append("</body></html>")
    p = os.path.join(OUT, BASE + ".html")
    open(p, "w", encoding="utf-8").write("".join(parts))
    return p

# ----------------------------- PPTX -----------------------------
def build_pptx():
    from pptx import Presentation
    from pptx.util import Inches, Pt
    from pptx.dml.color import RGBColor
    from pptx.enum.text import PP_ALIGN
    from pptx.enum.shapes import MSO_SHAPE
    from PIL import Image
    AZUL = RGBColor(0x0D, 0x2C, 0x54); ORO = RGBColor(0xD9, 0xB6, 0x4A)
    ORO2 = RGBColor(0x7A, 0x59, 0x00); TXT = RGBColor(0x20, 0x33, 0x4A); GR = RGBColor(0x8A, 0x9A, 0xAA)
    CHIPBG = RGBColor(0xEE, 0xF3, 0xF8)
    prs = Presentation(); prs.slide_width = Inches(13.333); prs.slide_height = Inches(7.5)
    blank = prs.slide_layouts[6]; SW, SH = prs.slide_width, prs.slide_height

    def rect(sld, l, t, w, h, fill):
        sh = sld.shapes.add_shape(MSO_SHAPE.RECTANGLE, l, t, w, h)
        sh.line.fill.background(); sh.fill.solid(); sh.fill.fore_color.rgb = fill
        sh.shadow.inherit = False
        return sh

    def txt(sld, l, t, w, h, lines, size=13, color=TXT, bold=False, align=PP_ALIGN.LEFT, bullet=False):
        tb = sld.shapes.add_textbox(l, t, w, h); tf = tb.text_frame; tf.word_wrap = True
        for j, line in enumerate(lines):
            p = tf.paragraphs[0] if j == 0 else tf.add_paragraph()
            p.text = ("•  " + line) if bullet else line
            p.alignment = align; p.space_after = Pt(5)
            for r in p.runs:
                r.font.size = Pt(size); r.font.bold = bold; r.font.color.rgb = color; r.font.name = "Calibri"
        return tb

    for i, d in enumerate(S, 1):
        sld = prs.slides.add_slide(blank)
        rect(sld, 0, 0, SW, SH, RGBColor(0xFF, 0xFF, 0xFF))
        rect(sld, 0, 0, SW, Inches(1.18), AZUL)
        tsize = 22 if len(d["t"]) < 62 else 18
        txt(sld, Inches(0.5), Inches(0.1), SW - Inches(1.0), Inches(0.62), [d["t"]], tsize, RGBColor(0xFF, 0xFF, 0xFF), True)
        txt(sld, Inches(0.5), Inches(0.72), SW - Inches(1.0), Inches(0.4), [d["sub"]], 11.5, ORO, False)
        y = Inches(1.4)
        if d["stats"]:
            n = len(d["stats"]); gap = Inches(0.18)
            cw = int((SW - Inches(1.0) - gap * (n - 1)) / n)
            x = Inches(0.5)
            for a, bsm in d["stats"]:
                rect(sld, x, y, cw, Inches(1.0), CHIPBG)
                rect(sld, x, y, cw, Inches(0.06), RGBColor(0xB8, 0x86, 0x0B))
                bs = 17 if len(a) <= 12 else 13
                txt(sld, x, y + Inches(0.14), cw, Inches(0.45), [a], bs, AZUL, True, PP_ALIGN.CENTER)
                txt(sld, x, y + Inches(0.6), cw, Inches(0.35), [bsm], 8.5, RGBColor(0x56, 0x67, 0x7A), False, PP_ALIGN.CENTER)
                x += cw + gap
            y = y + Inches(1.15)
        if d["b"]:
            nlines = sum(1 + len(x) // 120 for x in d["b"])
            bsize = 13 if nlines <= 10 else 11.5 if nlines <= 14 else 10.5
            bh = Inches(0.33) * nlines + Inches(0.2)
            bh = min(bh, SH - y - Inches(0.55))
            txt(sld, Inches(0.6), y, SW - Inches(1.2), bh, d["b"], bsize, TXT, bullet=True)
            y = y + bh + Inches(0.05)
        if d["tab"]:
            hd, rows = d["tab"]
            rh = Inches(0.37)
            gt = sld.shapes.add_table(len(rows) + 1, len(hd), Inches(0.5), y, SW - Inches(1.0), rh * (len(rows) + 1)).table
            for c, hcell in enumerate(hd):
                cell = gt.cell(0, c); cell.text = hcell
                cell.fill.solid(); cell.fill.fore_color.rgb = AZUL
                for p in cell.text_frame.paragraphs:
                    for r in p.runs: r.font.size = Pt(10); r.font.bold = True; r.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
            for rr, row in enumerate(rows, 1):
                for c, v in enumerate(row):
                    cell = gt.cell(rr, c); cell.text = v
                    cell.fill.solid()
                    cell.fill.fore_color.rgb = RGBColor(0xF4, 0xF7, 0xFA) if rr % 2 == 0 else RGBColor(0xFF, 0xFF, 0xFF)
                    for p in cell.text_frame.paragraphs:
                        for r in p.runs: r.font.size = Pt(9); r.font.color.rgb = TXT
            y = y + rh * (len(rows) + 1) + Inches(0.08)
        if d["img"]:
            iw, ih = Image.open(d["img"]).size
            avail_h = SH - y - Inches(0.5); avail_w = SW - Inches(1.4)
            if avail_h > Inches(0.9):
                w_emu = int(iw / 96 * 914400); h_emu = int(ih / 96 * 914400)
                k = min(avail_w / w_emu, avail_h / h_emu)
                w2, h2 = int(w_emu * k), int(h_emu * k)
                sld.shapes.add_picture(d["img"], int((SW - w2) / 2), int(y), w2, h2)
        if d["note"]:
            txt(sld, Inches(0.5), SH - Inches(0.74), SW - Inches(1.0), Inches(0.3), [d["note"]], 8.5, GR)
        txt(sld, Inches(0.3), SH - Inches(0.4), Inches(10.5), Inches(0.3), [SELLO], 7.5, ORO2, True)
        txt(sld, SW - Inches(2.6), SH - Inches(0.4), Inches(2.3), Inches(0.3), ["%d / %d" % (i, N)], 8, GR, align=PP_ALIGN.RIGHT)
    p = os.path.join(OUT, BASE + ".pptx")
    prs.save(p)
    return p

if __name__ == "__main__":
    print("HTML:", os.path.basename(build_html()))
    print("PPTX:", os.path.basename(build_pptx()))
    print("láminas:", N)

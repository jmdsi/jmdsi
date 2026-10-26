# -*- coding: utf-8 -*-
"""E6 — Presentación Ejecutiva P05 (26 láminas) en el estilo documental del
RESUMEN-EJECUTIVO-CONSEJO-3FPAG_UMC_2025-2030 (Calibri/Carlito, página blanca,
títulos azul marino #1f4e79, cabecera corrida, sello rojo al pie, Pág. n de N).
Genera HTML paginado + PDF A4."""
import base64, glob, html as H, os
from common import COD, FECHA, CONF, SELLO, F_FICHA, F_CAT, F_P04, F_PM

BASE = os.path.dirname(os.path.abspath(__file__))
ENT = os.path.join(BASE, "..", "entregables")
FIGD = os.path.join(ENT, "figuras")
FNT = os.path.join(BASE, "fonts")
STEM = COD + "_PRESENTACION-EJECUTIVA_PATIO-CUBIERTA-DE-HONOR"

NAVY, AZUL2, ROJO = "#1f4e79", "#2e74b5", "#c00000"
TOTBG, WARNBG, LINEA = "#ddebf7", "#fbe9e9", "#bfbfbf"
HDR = ("UNIVERSIDAD MARÍTIMA DEL CARIBE – PLAN MAESTRO UMC 2025-2030  |  "
       "PROYECTO 05 · PATIO / CUBIERTA DE HONOR (EXT-PCH-04) · CAMPUS CATIA LA MAR")
PIE = ("INGENIERÍA BÁSICA / ANTEPROYECTO — EMITIDO PARA COORDINACIÓN Y PRESUPUESTO "
       "PRELIMINAR — NO APTO PARA CONSTRUCCIÓN")

def figpng(g):
    m = glob.glob(os.path.join(FIGD, "*FIGURA-%s_*.png" % g.replace("G-", "G")))
    return m[0] if m else None

# ---------------------------------------------------------------- CONTENIDO
# Bloques: ("h",sub) ("p",texto) ("b",[items]) ("t",enc,filas,resaltar_ultima)
#          ("fig","G-nn") ("warn",titulo,cuerpo)
L = []
def lam(t, *b): L.append((t, list(b)))

lam("PORTADA")  # tratamiento especial

lam("LO ESENCIAL",
 ("b", ["El Patio / Cubierta de Honor (EXT-PCH-04): 1.625,00 m² (50,00 × 32,50 m) de explanada ceremonial de la Proa Central, patrimonio moderno de Malaussena (MOP, 1951–1958).",
        "Doblete sísmico del 24-06-2026 (Mw 7,2 y Mw 7,5): patio INHABILITADO para paradas y desfiles; punto de reunión R-1 fuera de servicio.",
        "Daño por zonas: D3 severo 680,00 m² (reponer) · D2 moderado 565,00 m² (reparar) · D4 inducido 380,00 m² (borde Babor, alcance P04).",
        "Restauración integral: pavimento con acabado granítico reintegrado, drenaje Tr 25 años, Asta Mayor 12,00 m, alumbrado R-1, Mástil OMM 10,00 m.",
        "ROM integral USD 895.000 · neto adicional P05 USD 565.000 (deducidos USD 330.000 ya presupuestados en el P04-R02).",
        "Plazo estimado ≈ 9 meses en 5 fases (A–E), condicionado a la consolidación previa de la Torre por el P04."]),
 ("t", ["Magnitud", "Valor", "Fuente"],
  [["Superficie total / neta P05", "1.625,00 m² / 1.245,00 m²", "Ficha EXT-PCH-04"],
   ["Aforo (formación / actos / R-1)", "1.300 ef. · 1.625 p. · 1.080–1.625 p.", "Ficha, Técnico 2"],
   ["ROM integral / neto", "USD 895.000 / USD 565.000", "AACE Clase 5 (−25 %/+40 %)"],
   ["Plazo", "≈ 9 meses (fases A–E)", "hipótesis A8"]], True),
 ("warn", "ADVERTENCIA TÉCNICA",
  "Expediente de Ingeniería Básica / Anteproyecto. NO apto para construcción, replanteo ni licitación. "
  "Cifras AACE Clase 5 (−25 % / +40 %), USD referencial, a sustituir por cotizaciones locales."))

lam("EL ACTIVO Y SU HISTORIA (1951–2026)",
 ("b", ["Plaza de Armas de la Escuela Náutica de Venezuela: proyecto MOP, Arq. Luis Raimundo Malaussena Andueza; estructura Gutiérrez & Co. S.A.",
        "Proyecto estructural base 28-08-1951 (signaturas 15 DF 30 y 8.DF.2.364); lámina de urbanismo P04-L5-A del 24-10-1953; operación 1951–1959.",
        "Acervo: 198 PDF y 487 fotografías (IMG_2134–IMG_2778) en Tubos Portaplanos 01–05; registro histórico y forense en PATIO_HONOR CATASTRO.pdf (4 láminas).",
        "75 años de servicio continuo como espacio protocolar: formaciones, graduaciones OMI/STCW, izada del Pabellón Nacional."]),
 ("fig", "G-02"))

lam("EMPLAZAMIENTO Y GEORREFERENCIACIÓN",
 ("t", ["Punto", "Coordenadas", "Sistema"],
  [["Centroide EXT-PCH-04", "10°36'02,55\" N · 67°01'55,20\" O", "WGS84 / EPSG:4326"],
   ["Centroide (UTM)", "E 715.324,40 · N 1.172.523,10", "UTM 19N / EPSG:32619"],
   ["Torre C-TO (P04)", "ΔE +32,21 m · ΔN −13,21 m · d = 34,81 m", "relativa al centroide"],
   ["BM-UMC-01 (cota Z)", "POR ESTABLECER", "RFI-GEO-01"]], False),
 ("b", ["Bordes: Proa (N) Aula Magna · Estribor (E) Fracción 2 · Popa (S) Fracción 3 · Babor (O) Torre de Observación y Sala Técnica.",
        "Retícula estructural de 4,00 m (13 módulos = 52,00 m, Fracción 2); huella neta pavimentada 50,00 × 32,50 m.",
        "Se corrige la inversión de rótulos X/E–Y/N detectada en el borrador catastral."]),
 ("fig", "G-01"))

lam("EVENTO CONDICIONANTE: DOBLETE SÍSMICO 24-06-2026",
 ("b", ["Dos eventos Mw 7,2 y Mw 7,5 el 24-06-2026: condición POST-SISMO de todo el sector Proa.",
        "Lámina 4 del catastro (registro forense): fractura diagonal de paños, escalonamientos de 1,5–4,5 cm, hundimientos sobre trincheras, escombros en el borde de la Torre.",
        "Consecuencia operativa inmediata: patio INHABILITADO (0 personas para paradas) y punto R-1 primario fuera de servicio — sin alterno designado en las fuentes (RFI-EVA-01 CRÍTICA).",
        "Hipótesis causales: densificación/licuación local de rellenos, fuga de colectores antiguos, ausencia de desacople sísmico, envejecimiento de sellos (75 años), impacto de escombros."]),
 ("warn", "CONDICIÓN CRÍTICA DE SEGURIDAD HUMANA",
  "Mientras el patio esté inhabilitado, el Sector Proa NO tiene punto de reunión sísmica designado. "
  "La designación y señalización del punto R-1 alterno debe resolverse ANTES del inicio de la obra."))

lam("DIAGNÓSTICO DE DAÑO POR ZONAS (D2 / D3 / D4)",
 ("t", ["Zona", "Área", "Daño", "Decisión"],
  [["Paños centrales", "680,00 m²", "D3 — fractura y escalonamientos 1,5–4,5 cm", "demoler y reponer con reintegración"],
   ["Paños orientales", "565,00 m²", "D2 — fisuración y pérdida de sellos", "reparar juntas + resellado"],
   ["Borde Babor", "380,00 m²", "D4 — inducido por escombros de la Torre", "TRANSFERIDO al P04 (consolidación previa)"],
   ["Subbase y colectores", "—", "asentamientos y fugas presuntas", "sanear + sustituir PEAD SN8"]], False),
 ("p", "Escala D0–D4 declarada referencial (adaptada de ATC-20 / condición de pavimentos rígidos). "
       "Inspección detallada previa a demolición: TLS, calicatas + PDC, estanqueidad, georradar."),
 ("fig", "G-07"))

lam("CONCILIACIÓN DE ÁREAS (REGLA DE NO DUPLICACIÓN)",
 ("t", ["Componente", "m²", "%", "Asignación"],
  [["Borde occidental Proa–Babor (incluye Banda de Protocolo 210,00 m²)", "380,00", "23,38 %", "P04-R02 (excluido del BOQ P05)"],
   ["Explanada central remanente", "1.245,00", "76,62 %", "P05 — objeto presupuestario neto"],
   ["TOTAL EXT-PCH-04", "1.625,00", "100,00 %", "conciliado"]], True),
 ("b", ["Verificación: 380,00 + 1.245,00 = 1.625,00 ✔ · conjuntos anidados, no sumables entre sí.",
        "Deducción económica asociada: USD 330.000 (banda P04: USD 260.000–400.000).",
        "Condición suspensiva: el borde Babor no se restaura antes de la consolidación de la Torre (P04)."]),
 ("fig", "G-03"))

lam("CONCEPTO: «LA CUBIERTA DE FORMACIÓN»",
 ("b", ["El patio es la cubierta principal del Campus-Buque Digital UMC: el plano donde la institución forma, pasa revista y gradúa a sus oficiales frente al asta del Pabellón.",
        "Valor del espacio = su vacío modulado: lámina pétrea continua enmarcada por los cuerpos de Malaussena; único protagonista vertical: el asta.",
        "Lenguaje: modernidad venezolana de los 1950 — paños sobre retícula de 4,00 m, acabado granítico/martelinado, NPT ±0,000 con el foyer del Aula Magna.",
        "Doctrina patrimonial: CONSERVAR · CONSOLIDAR · REINTEGRAR · REPONER con junta-testigo datada · SUSTITUIR redes agotadas — sin falsificación histórica."]),
 ("fig", "G-05"))

lam("PAVIMENTO: SECCIÓN CONSTRUCTIVA PROPUESTA",
 ("b", ["Losa de concreto (MR y espesor por calcular) sobre subbase granular saneada y mejorada; acabado granítico/cemento martelinado reintegrado.",
        "Paños ≈ 4,00 × 5,00 m compatibles con la retícula original; juntas de contracción selladas (PU bicomponente, UV/salinidad).",
        "Juntas sísmicas de desacople losa–estructuras, e = 25–50 mm; ≈ 980 m de sellado elastomérico.",
        "Predimensionado preliminar: losa e ≈ 15–18 cm · subbase e ≈ 20–30 cm — CONDICIONADOS al estudio geotécnico (RFI-GEOT-01)."]),
 ("fig", "G-06"))

lam("DRENAJE PLUVIAL (INSTALACIÓN CRÍTICA)",
 ("t", ["Parámetro", "Valor"],
  [["Caudal propio / con faldones", "73,13 L/s · ≈ 145 L/s (Tr = 25 años)"],
   ["Canaletas perimetrales clase C250", "≈ 180 m"],
   ["Colectores PEAD doble pared SN8 Ø 300–400 mm", "≈ 140 m"],
   ["Tanquillas / sumideros", "8 ud"],
   ["Pendiente superficial", "1,2 % – 1,5 %"]], False),
 ("b", ["Sustitución íntegra de colectores antiguos con prueba de estanqueidad y videoinspección previa.",
        "Descarga coordinada con el canal/toma de quebrada documentados en el Paquete 05 (R-19, R-20)."]),
 ("fig", "G-08"))

lam("SISTEMA ELÉCTRICO Y PROTECCIÓN ATMOSFÉRICA",
 ("b", ["Red subterránea nueva en bancadas PVC/PEAD Ø 4\" con juntas sísmicas flexibles (sustituye la red histórica P03-L3-B).",
        "12 luminarias LED marinas IP66/IK10 (100–150 lux) + alumbrado de emergencia autónomo del punto R-1.",
        "2 cajas de piso IP67 para la Banda de Protocolo (megafonía y servicios de actos).",
        "Malla de puesta a tierra R ≤ 5 Ω y SPDA del asta y del mástil según IEC 62305.",
        "Hidrante / toma siamesa en el borde Norte conectado al anillo PCI del campus (coordinación P04-R02 Cap. 12.4)."]),
 ("fig", "G-09"))

lam("ASTA MAYOR CEREMONIAL Y MÁSTIL OMM",
 ("t", ["Elemento", "Altura", "Alcance P05"],
  [["Asta Mayor Ceremonial", "12,00 m", "fundación independiente, pedestal de concreto visto, podio accesible, drizas navales (partida E3.03)"],
   ["Mástil Hidrometeorológico OMM", "10,00 m", "fundación y parcela de sensores; instrumentación en partida separada (interfaz P04)"],
   ["Torre de Observación (contexto)", "22,02 m / 12,20 m (RFI-ALT-01)", "alcance P04 — radio de caída de escombros"]], False),
 ("b", ["Emplazamiento del mástil condicionado al estudio de obstáculos del borde Babor (RFI-OMM-01).",
        "Telemetría integrada a la estación hidrometeorológica del P04: un solo sistema de adquisición (regla de no duplicación)."]),
 ("fig", "G-10"))

lam("EVACUACIÓN R-1, AFOROS Y ACCESIBILIDAD",
 ("t", ["Condición", "Aforo", "Base"],
  [["Formación (orden cerrado)", "1.300 cadetes", "1,25 m²/efectivo"],
   ["Actos masivos", "1.625 personas", "1,00 m²/persona"],
   ["Punto de reunión R-1", "1.080 – 1.625 personas", "Ficha, Técnico 2"]], True),
 ("b", ["Rutas de aproximación desde las Fracciones 1, 2 y 3 y corredores EXT-CTC-15.",
        "Señalización COVENIN 810/187 · franjas podotáctiles Fondonorma 2733 · itinerario accesible al podio.",
        "RFI-EVA-01 (CRÍTICA): punto R-1 alterno del Sector Proa por designar antes de obra."]),
 ("fig", "G-12"))

lam("INDUSTRIA 5.0 · HBIM · GEMELO DIGITAL",
 ("b", ["HBIM del espacio exterior: nube de puntos TLS (estado 2026) + restitución del estado 1951 desde las láminas MOP; modelo federado en CDE.",
        "Codificación UMC-[ACTIVO]-[DISCIPLINA]-[NÚMERO]-[REV]; desdoblamiento catastral UMC-EXT-004 / UMC-ED-000-PCH04 (RFI-COD-05).",
        "Sensorización: hitos de asentamiento, nivel en tanquillas, pluviómetro del mástil, conteo de aforo en actos.",
        "Enfoque humanocéntrico: cadete en formación, operador de mantenimiento y seguridad de evacuación como usuarios de diseño."]),
 ("fig", "G-11"))

lam("CÓMPUTOS MÉTRICOS PRELIMINARES (BOQ REV.0)",
 ("t", ["Partida", "Descripción", "Cant."],
  [["E1.01", "Retiro controlado de pavimento D3 (gestión patrimonial de escombros)", "680,00 m²"],
   ["E1.02", "Reparación de paños y juntas zona D2", "565,00 m²"],
   ["E2.01", "Saneamiento de subbase y rellenos", "≈ 1.245,00 m²"],
   ["E3.01", "Losa nueva con acabado reintegrado", "680,00 m²"],
   ["E3.02", "Sellado elastomérico de juntas (e = 25–50 mm)", "980,00 m"],
   ["E3.03", "Asta Mayor: fundación, pedestal, restauración + podio", "1,00 gl"],
   ["E4.01", "Drenaje: canaletas 180 m + PEAD 140 m + 8 tanquillas", "1,00 gl"],
   ["E4.02", "Hidrante / toma siamesa borde Norte", "1,00 ud"],
   ["E5.01", "Red eléctrica, 12 luminarias, tierra, SPDA", "1,00 gl"],
   ["E6.01", "Señalización R-1, podotáctil, paisajismo, comisionamiento", "1,00 gl"]], False),
 ("p", "El borde occidental (380,00 m²) queda EXCLUIDO: ya presupuestado en el P04-R02 (Cap. 21, Partida 26). "
       "NO son cómputos contractuales; se re-derivarán del TLS y la geotecnia."))

lam("ESTIMACIÓN DE INVERSIÓN — ROM (AACE CLASE 5)",
 ("t", ["Concepto", "USD"],
  [["Subtotal costo directo (1.625,00 m² · 470,77 USD/m²)", "765.000,00"],
   ["Ingeniería de detalle, ensayos y supervisión patrimonial (7,0 %)", "53.550,00"],
   ["Contingencia ROM (10,0 %)", "76.450,00"],
   ["ROM INTEGRAL (rango 750.000 – 1.120.000)", "895.000,00"],
   ["(−) Porción ya presupuestada en P04-R02 (380,00 m²)", "−330.000,00"],
   ["(=) PRESUPUESTO NETO ADICIONAL P05 (rango 490.000 – 720.000)", "565.000,00"]], True),
 ("p", "Verificaciones: 765.000 + 53.550 + 76.450 = 895.000 ✔ · 895.000 − 330.000 = 565.000 ✔. "
       "Moneda USD referencial; orden de magnitud, no presupuesto de licitación."),
 ("fig", "G-13"))

lam("CRONOGRAMA: 5 FASES · ≈ 9 MESES",
 ("t", ["Fase", "Denominación", "Duración", "Hito / gate"],
  [["A", "Estudios previos (TLS, calicatas, PDC, BM, videoinspección)", "≈ 2,0 meses", "cierra RFI-GEOT-01"],
   ["B", "Desescombro y demolición controlada", "≈ 2,0 meses", "GATE: Babor consolidado por P04"],
   ["C", "Saneamiento de subbase + colectores PEAD", "≈ 2,5 meses", "estanqueidad aprobada"],
   ["D", "Pavimento: losas, juntas, reintegración", "≈ 3,0 meses", "paños piloto aprobados"],
   ["E", "Asta, eléctrica, señalización R-1, comisionamiento", "≈ 1,5 meses", "habilitación protocolar y R-1"]], False),
 ("b", ["Restricciones duras: secuencia P04 → borde Babor · calendario ceremonial · lluvias (subbase nunca abierta en pico pluvial) · R-1 alterno operativo durante toda la obra."]),
 ("fig", "G-14"))

lam("MAPA DE RIESGOS",
 ("t", ["ID", "Riesgo", "P×I", "Mitigación"],
  [["R02", "Colectores en peor estado del previsto", "4×4", "videoinspección temprana + partida contingente"],
   ["R07", "Inhabilitación prolongada del punto R-1", "3×5", "punto alterno ANTES de obra (RFI-EVA-01)"],
   ["R04", "Desfase del P04 bloquea el borde Babor", "3×4", "frente oriental primero; gate contractual"],
   ["R05", "Pérdida de acabado histórico en desescombro", "3×4", "protocolo patrimonial + fotogrametría"],
   ["R01", "Réplica sísmica durante la obra", "2×5", "protocolo de paralización y exclusión"],
   ["R10", "Demora permisológica y patrimonial", "4×3", "expediente patrimonial anticipado"]], False),
 ("fig", "G-15"))

lam("INFORMACIÓN PENDIENTE — REGISTRO RFI (16 ABIERTAS)",
 ("t", ["ID", "Enunciado", "Prioridad"],
  [["RFI-EVA-01", "Punto R-1 alterno del Sector Proa sin designar", "CRÍTICA"],
   ["RFI-GEOT-01", "Subbase, rellenos y colectores: calicatas, PDC, estanqueidad", "ALTA"],
   ["RFI-GEO-01", "BM-UMC-01 y cota Z sin establecer", "ALTA"],
   ["RFI-NOR-01", "Vigencia de normas COVENIN / Fondonorma / IEC", "ALTA"],
   ["RFI-OMM-01", "Emplazamiento del mástil y alcance económico de instrumentación", "MEDIA"],
   ["RFI-ARE-05", "Acta de transferencia del borde (380,00 m²) con el P04", "MEDIA"],
   ["RFI-PAT-01…04", "TLS, asta, videoinspección, georradar", "MEDIA"],
   ["RFI-COD-05 / SIG-01 / INV-01 / PRO-01 / ALT-01", "codificación, signaturas, inventarios, tribuna, altura Torre", "ORDINARIA"]], False),
 ("warn", "NO ESTÁ CALCULADO EN ESTA FASE",
  "Diseño de losa por fatiga/MR · armaduras y despieces · memorias de instalaciones · cotas absolutas · "
  "topografía con curvas de nivel · presupuesto contractual con precios locales."))

lam("PLANOS DEL EXPEDIENTE (ANEXO P · P-0 A P-9)",
 ("t", ["Código", "Denominación", "Escala"],
  [["UMC-PCH-P-0", "Implantación general georreferenciada", "1:400"],
   ["UMC-PCH-P-1", "Planta general de paños, juntas y pendientes", "1:200"],
   ["UMC-PCH-P-2", "Planta de demolición/retiro por zonas de daño", "1:250"],
   ["UMC-PCH-P-3", "Planta de drenaje pluvial y colectores", "1:250"],
   ["UMC-PCH-P-4", "Planta eléctrica, alumbrado y canalizaciones", "1:250"],
   ["UMC-PCH-P-5", "Señalización, accesibilidad y evacuación R-1", "1:250"],
   ["UMC-PCH-P-6", "Zonificación ceremonial y protocolo", "1:250"],
   ["UMC-PCH-P-7", "Sección de pavimento + perfil de colectores", "1:20 / 1:100H"],
   ["UMC-PCH-P-8", "Detalles del Asta Mayor, podio y Mástil OMM", "1:50"],
   ["UMC-PCH-P-9", "Interfaz con P04: borde Babor y junta de transferencia", "1:250"]], False),
 ("p", "Láminas esquemáticas de anteproyecto: definen programa, dimensiones y relaciones funcionales; "
       "NO incluyen detalles constructivos ni replanteo. Sello en cada lámina: NO APTO PARA CONSTRUCCIÓN."))

lam("ENTREGABLES DEL EXPEDIENTE (E1–E8)",
 ("t", ["E", "Entregable", "Formato"],
  [["E1", "Listado de planos e imágenes fuente (198 PDF · 487 fotos)", "CSV · HTML · SVG/PNG"],
   ["E2", "Expediente de Ingeniería Básica — 28 capítulos", "HTML · PDF · DOCX"],
   ["E2-P", "Anexo P: láminas P-0…P-9", "PDF · HTML"],
   ["E3", "Figuras técnicas G-01…G-15", "SVG · PNG"],
   ["E4", "Láminas de anteproyecto P-0…P-9", "SVG · PNG"],
   ["E5", "Registro patológico post-sísmico", "HTML · SVG/PNG"],
   ["E6", "Presentación ejecutiva (este documento)", "HTML · PDF"],
   ["E7", "Matriz de trazabilidad dato→fuente", "CSV"],
   ["E8", "Memoria de decisiones y registro RFI", "MD"]], False),
 ("b", ["Codificación documental: UMC2030-P05-EXTPCH-R01_<ENTREGABLE>_<TÍTULO>.",
        "Custodia en CDE institucional; carpeta del expediente en Google Drive UMC."]))

lam("INTERFAZ CON EL PROYECTO 04 (TORRE Y SALA TÉCNICA)",
 ("b", ["El borde occidental del patio (380,00 m², zona D4) pertenece al alcance del P04-R02: pavimento, juntas y consolidación incluidos en su BOQ (Cap. 21, Partida 26).",
        "Condición suspensiva D-08: la consolidación de la Torre de Observación PRECEDE a toda obra del pavimento en ese borde.",
        "Junta de transferencia de alcance materializada en la lámina P-9; acta formal pendiente (RFI-ARE-05).",
        "Deducción económica conciliada: USD 330.000 — prohibida la doble presupuestación (regla R4/R12).",
        "Interfaz técnica adicional: telemetría del Mástil OMM integrada a la estación hidrometeorológica del P04 (Sala ACA-STH-15)."]))

lam("GOBERNANZA, PERMISOLOGÍA Y PATRIMONIO",
 ("b", ["Obra MOP 1951–1958 (Malaussena): la normativa patrimonial venezolana se cita como referencia a verificar; expediente patrimonial anticipado como mitigación (R10).",
        "Permisología institucional: Rectorado, Dirección de Planta Física, Seguridad Integral y autoridades competentes.",
        "Gestión de escombros con valor patrimonial: registro fotogramétrico, selección de fragmentos documentales, archivo institucional.",
        "Supervisión patrimonial independiente durante demolición y reintegración del acabado (incluida en el 7,0 % de ingeniería)."]))

lam("CONDICIONES PARA PASAR A «APTO PARA CONSTRUCCIÓN»",
 ("t", ["N°", "Condición", "RFI asociada"],
  [["1", "Levantamiento topográfico con BM-UMC-01 y cota Z", "RFI-GEO-01"],
   ["2", "Estudio geotécnico de subbase, rellenos y colectores", "RFI-GEOT-01"],
   ["3", "Ingeniería de detalle firmada por profesional habilitado", "—"],
   ["4", "Verificación de vigencia normativa", "RFI-NOR-01"],
   ["5", "Permisología institucional y patrimonial", "—"],
   ["6", "Cómputos y presupuesto contractuales con cotizaciones locales", "—"],
   ["7", "Coordinación de interfaces aprobada con el P04-R02", "RFI-ARE-05"],
   ["8", "Consolidación previa del borde Babor por el P04", "D-08 (suspensiva)"]], False))

lam("ACUERDOS SOLICITADOS AL CONSEJO UNIVERSITARIO",
 ("t", ["N°", "Acuerdo"],
  [["1", "APROBAR el expediente UMC2030-P05-EXTPCH-R01 como ingeniería básica del Plan Maestro UMC 2025–2030."],
   ["2", "DESIGNAR el punto de reunión R-1 alterno del Sector Proa y ordenar su señalización inmediata (RFI-EVA-01)."],
   ["3", "ORDENAR el cierre de las RFI críticas: topografía (GEO-01), geotecnia (GEOT-01) y vigencia normativa (NOR-01)."],
   ["4", "RATIFICAR la secuencia P04 → borde Babor, el acta de transferencia de los 380,00 m² y la deducción de USD 330.000."],
   ["5", "ADOPTAR la doctrina de junta-testigo datada para la reintegración patrimonial del pavimento."],
   ["6", "APROBAR la reserva presupuestaria ROM: USD 895.000 integral / USD 565.000 neto adicional (AACE Clase 5)."],
   ["7", "DESIGNAR al proyectista responsable habilitado y ordenar la custodia del expediente en el CDE institucional."]], False))

lam("CIERRE Y CONTROL DOCUMENTAL",
 ("t", ["Ítem", "Registro"],
  [["Código", COD],
   ["Revisión y fecha", "R01 · " + FECHA],
   ["Documento rector", F_FICHA],
   ["Documento base catastral", F_CAT],
   ["Expediente colindante", F_P04],
   ["Marco", F_PM],
   ["Aprobación", "Rectorado UMC – Cap. Alt. / Dr. Guillermo Antonio Riut Hernández"],
   ["Autoría del documento fuente", "Prof. Jhonny Da Silva Izquierdo (MSc. Ing. Lic., CIV 95787)"],
   ["Proyectista responsable", "Por designar – profesional habilitado"],
   ["Confidencialidad", CONF]], False),
 ("warn", "SELLO DE EMISIÓN", SELLO),
 ("p", "El Patio / Cubierta de Honor volverá a ser lo que fue desde 1951: la cubierta donde la "
       "Universidad Marítima del Caribe forma a sus oficiales frente al Pabellón Nacional."))

NTOT = len(L)

PORTADA_META = [
 ("Documento", "Presentación Ejecutiva — Expediente de Ingeniería Básica"),
 ("Objeto", "Patio / Cubierta de Honor (EXT-PCH-04) · «La Cubierta de Formación»"),
 ("Código", COD), ("Revisión y fecha", "R01 · " + FECHA),
 ("Proyecto", "Proyecto 05 del Plan Maestro UMC 2025–2030"),
 ("Clase de estimación", "AACE Clase 5 (ROM) · exactitud −25 % / +40 %"),
 ("Aprobación", "Rectorado UMC – Cap. Alt. / Dr. Guillermo Antonio Riut Hernández"),
 ("Autoría del documento fuente", "Prof. Jhonny Da Silva Izquierdo (MSc. Ing. Lic., CIV 95787)"),
 ("Confidencialidad", CONF),
]

# ---------------------------------------------------------------- HTML
def esc(t): return H.escape(t, quote=False)

def build_html():
    css = """
@font-face{font-family:Carlito;src:local('Carlito'),local('Calibri')}
body{margin:0;background:#9aa5ad;font-family:Calibri,Carlito,'Segoe UI',Arial,sans-serif;color:#1a1a1a}
.page{position:relative;width:210mm;min-height:297mm;margin:10px auto;background:#fff;
 box-shadow:0 2px 14px rgba(0,0,0,.35);padding:22mm 18mm 24mm;box-sizing:border-box}
.hdr{position:absolute;top:8mm;left:18mm;right:18mm;text-align:center;color:%(navy)s;
 font-weight:bold;font-size:7.6pt;letter-spacing:.2px;border-bottom:1.2px solid %(navy)s;padding-bottom:2.2mm}
.ftr{position:absolute;bottom:8mm;left:18mm;right:18mm;text-align:center}
.ftr .sello{color:%(rojo)s;font-weight:bold;font-size:7.6pt}
.ftr .pag{font-size:7.6pt;color:#333;margin-top:1mm}
h1.tit{color:%(navy)s;font-size:16.5pt;margin:2mm 0 4mm;letter-spacing:.2px}
h2.sub{color:%(azul2)s;font-size:12pt;margin:4mm 0 2mm}
p{font-size:9.5pt;line-height:1.45;margin:2mm 0}
ul{margin:2mm 0 3mm;padding-left:6mm}
li{font-size:9.5pt;line-height:1.5;margin-bottom:1.6mm}
table{border-collapse:collapse;width:100%%;margin:3mm 0;font-size:8.6pt}
th{background:%(navy)s;color:#fff;font-size:8.2pt;text-align:left;padding:1.6mm 2mm;border:1px solid %(navy)s}
td{border:1px solid %(linea)s;padding:1.4mm 2mm;vertical-align:top}
tr.tot td{background:%(totbg)s;font-weight:bold}
.warn{border:1px solid %(rojo)s;background:%(warnbg)s;margin:3mm 0;font-size:9pt}
.warn .wt{color:%(rojo)s;font-weight:bold;padding:1.6mm 2.5mm 0}
.warn .wb{padding:1mm 2.5mm 2mm;line-height:1.45}
figure{margin:3mm 0;text-align:center}
figure img{max-width:100%%;max-height:120mm;border:1px solid %(linea)s}
figcaption{font-size:7.8pt;color:#555;font-style:italic;margin-top:1mm}
.cen{text-align:center}
@media print{body{background:#fff}.page{margin:0;box-shadow:none;page-break-after:always}}
""" % dict(navy=NAVY, azul2=AZUL2, rojo=ROJO, linea=LINEA, totbg=TOTBG, warnbg=WARNBG)

    pages = []
    for i, (tit, blo) in enumerate(L):
        n = i + 1
        inner = []
        if tit == "PORTADA":
            inner.append(
             "<div class='cen' style='margin-top:10mm'>"
             "<p style='font-size:10pt;font-weight:bold;margin-bottom:1mm'>REPÚBLICA BOLIVARIANA DE VENEZUELA</p>"
             "<p style='font-size:9.5pt;margin:1mm 0'>MINISTERIO DEL PODER POPULAR PARA EL TRANSPORTE</p>"
             "<p style='font-size:9.5pt;margin:1mm 0'>MARINA MERCANTE DE VENEZUELA</p>"
             "<p style='font-size:15pt;font-weight:bold;color:%s;margin:9mm 0 1mm'>UNIVERSIDAD MARÍTIMA DEL CARIBE – UMC</p>"
             "<p style='font-size:9.5pt;margin:0 0 9mm'>Campus Catia La Mar · estado La Guaira</p>"
             "<p style='font-size:26pt;font-weight:bold;color:%s;margin:2mm 0'>PRESENTACIÓN EJECUTIVA</p>"
             "<p style='font-size:13pt;font-weight:bold;color:%s;margin:1mm 0 10mm'>PATIO / CUBIERTA DE HONOR (EXT-PCH-04)<br>«LA CUBIERTA DE FORMACIÓN» · PROYECTO 05</p></div>"
             % (NAVY, NAVY, AZUL2))
            inner.append("<table>")
            for k, v in PORTADA_META:
                inner.append("<tr><td style='width:34%%;background:#f2f2f2;font-weight:bold'>%s</td><td>%s</td></tr>" % (esc(k), esc(v)))
            inner.append("</table>")
            inner.append("<div class='warn'><div class='wt'>ADVERTENCIA TÉCNICA</div><div class='wb'>%s</div></div>"
                         % esc("Documento de Ingeniería Básica / Anteproyecto. NO apto para construcción, replanteo ni "
                               "licitación. Estimaciones AACE Clase 5 (−25 % / +40 %), moneda USD referencial."))
        else:
            inner.append("<h1 class='tit'>%d. %d · %s</h1>" % (n - 1, n - 1, esc(tit)))
            for b in blo:
                if b[0] == "p":
                    inner.append("<p style='font-style:italic;color:#444'>%s</p>" % esc(b[1]))
                elif b[0] == "h":
                    inner.append("<h2 class='sub'>%s</h2>" % esc(b[1]))
                elif b[0] == "b":
                    inner.append("<ul>" + "".join("<li>%s</li>" % esc(x) for x in b[1]) + "</ul>")
                elif b[0] == "t":
                    enc, filas, tot = b[1], b[2], b[3]
                    t = ["<table><thead><tr>"] + ["<th>%s</th>" % esc(c) for c in enc] + ["</tr></thead><tbody>"]
                    for j, f in enumerate(filas):
                        cls = " class='tot'" if (tot and j == len(filas) - 1) else ""
                        t.append("<tr%s>" % cls + "".join("<td>%s</td>" % esc(c) for c in f) + "</tr>")
                    t.append("</tbody></table>")
                    inner.append("".join(t))
                elif b[0] == "warn":
                    inner.append("<div class='warn'><div class='wt'>%s</div><div class='wb'>%s</div></div>"
                                 % (esc(b[1]), esc(b[2])))
                elif b[0] == "fig":
                    p = figpng(b[1])
                    if p:
                        d = base64.b64encode(open(p, "rb").read()).decode()
                        inner.append("<figure><img src='data:image/png;base64,%s' alt='%s'>"
                                     "<figcaption>Figura %s · %s · NO APTO PARA CONSTRUCCIÓN</figcaption></figure>"
                                     % (d, b[1], b[1], COD))
        pages.append("<div class='page'><div class='hdr'>%s</div>%s"
                     "<div class='ftr'><div class='sello'>%s</div><div class='pag'>Pág. %d de %d</div></div></div>"
                     % (esc(HDR), "".join(inner), esc(PIE), n, NTOT))
    doc = ("<!DOCTYPE html><html lang='es'><head><meta charset='utf-8'>"
           "<meta name='viewport' content='width=device-width,initial-scale=1'>"
           "<title>%s — Presentación Ejecutiva</title><style>%s</style></head><body>%s</body></html>"
           % (COD, css, "".join(pages)))
    out = os.path.join(ENT, STEM + ".html")
    open(out, "w", encoding="utf-8").write(doc)
    print("HTML", out, os.path.getsize(out))

# ---------------------------------------------------------------- PDF
def build_pdf():
    from reportlab.lib.pagesizes import A4
    from reportlab.lib.units import mm
    from reportlab.lib import colors
    from reportlab.lib.styles import ParagraphStyle
    from reportlab.pdfbase import pdfmetrics
    from reportlab.pdfbase.ttfonts import TTFont
    from reportlab.platypus import (BaseDocTemplate, PageTemplate, Frame, Paragraph, Spacer,
                                    Table, TableStyle, Image, PageBreak, KeepInFrame)
    from PIL import Image as PImage
    pdfmetrics.registerFont(TTFont("Calibri", os.path.join(FNT, "Carlito-Regular.ttf")))
    pdfmetrics.registerFont(TTFont("Calibri-Bold", os.path.join(FNT, "Carlito-Bold.ttf")))
    pdfmetrics.registerFont(TTFont("Calibri-Italic", os.path.join(FNT, "Carlito-Italic.ttf")))
    pdfmetrics.registerFont(TTFont("Calibri-BoldItalic", os.path.join(FNT, "Carlito-BoldItalic.ttf")))
    pdfmetrics.registerFontFamily("Calibri", normal="Calibri", bold="Calibri-Bold",
                                  italic="Calibri-Italic", boldItalic="Calibri-BoldItalic")
    cNavy, cAz2, cRojo = colors.HexColor(NAVY), colors.HexColor(AZUL2), colors.HexColor(ROJO)
    cTot, cWarn, cLin = colors.HexColor(TOTBG), colors.HexColor(WARNBG), colors.HexColor(LINEA)
    W, Hh = A4
    ML = MR = 18 * mm; MT = 20 * mm; MB = 20 * mm
    CW = W - ML - MR

    S = lambda **k: ParagraphStyle(k.pop("name"), **k)
    st_tit = S(name="tit", fontName="Calibri-Bold", fontSize=16, leading=19, textColor=cNavy, spaceAfter=7)
    st_sub = S(name="sub", fontName="Calibri-Bold", fontSize=11.5, leading=14, textColor=cAz2,
               spaceBefore=6, spaceAfter=3)
    st_p = S(name="p", fontName="Calibri", fontSize=9.5, leading=13, spaceAfter=4)
    st_pi = S(name="pi", fontName="Calibri-Italic", fontSize=9, leading=12.4,
              textColor=colors.HexColor("#444444"), spaceAfter=4)
    st_li = S(name="li", fontName="Calibri", fontSize=9.5, leading=13.4, leftIndent=5 * mm,
              bulletIndent=1.5 * mm, spaceAfter=2.6, bulletFontName="Calibri", bulletFontSize=9.5)
    st_cell = S(name="c", fontName="Calibri", fontSize=8.4, leading=10.6)
    st_cellb = S(name="cb", fontName="Calibri-Bold", fontSize=8.4, leading=10.6)
    st_cellh = S(name="ch", fontName="Calibri-Bold", fontSize=8.2, leading=10.4, textColor=colors.white)
    st_wt = S(name="wt", fontName="Calibri-Bold", fontSize=9, leading=12, textColor=cRojo)
    st_wb = S(name="wb", fontName="Calibri", fontSize=9, leading=12.2)
    st_cap = S(name="cap", fontName="Calibri-Italic", fontSize=7.8, leading=10,
               textColor=colors.HexColor("#555555"), alignment=1, spaceBefore=2)
    cen = lambda sz, col, b=True, sa=2: S(name="x%d%s" % (sz, col), alignment=1,
          fontName="Calibri-Bold" if b else "Calibri", fontSize=sz, leading=sz * 1.22,
          textColor=colors.HexColor(col), spaceAfter=sa)

    def tabla(enc, filas, tot):
        data = [[Paragraph(c, st_cellh) for c in enc]]
        for j, f in enumerate(filas):
            sty = st_cellb if (tot and j == len(filas) - 1) else st_cell
            data.append([Paragraph(c, sty) for c in f])
        nc = len(enc)
        if nc == 2: cw = [CW * .55, CW * .45] if enc[0] != "N°" else [CW * .08, CW * .92]
        elif nc == 3: cw = [CW * .22, CW * .5, CW * .28]
        else: cw = [CW / nc] * nc
        t = Table(data, colWidths=cw, repeatRows=1)
        s = [("BACKGROUND", (0, 0), (-1, 0), cNavy),
             ("GRID", (0, 0), (-1, -1), .5, cLin),
             ("VALIGN", (0, 0), (-1, -1), "TOP"),
             ("LEFTPADDING", (0, 0), (-1, -1), 4.5), ("RIGHTPADDING", (0, 0), (-1, -1), 4.5),
             ("TOPPADDING", (0, 0), (-1, -1), 3.2), ("BOTTOMPADDING", (0, 0), (-1, -1), 3.2)]
        if tot:
            s.append(("BACKGROUND", (0, len(data) - 1), (-1, len(data) - 1), cTot))
        t.setStyle(TableStyle(s))
        return t

    def warn(tit, cuerpo):
        t = Table([[Paragraph(tit, st_wt)], [Paragraph(cuerpo, st_wb)]], colWidths=[CW])
        t.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, -1), cWarn),
                               ("BOX", (0, 0), (-1, -1), .8, cRojo),
                               ("LEFTPADDING", (0, 0), (-1, -1), 7), ("RIGHTPADDING", (0, 0), (-1, -1), 7),
                               ("TOPPADDING", (0, 0), (0, 0), 5), ("BOTTOMPADDING", (0, 0), (0, 0), 1),
                               ("TOPPADDING", (0, 1), (0, 1), 1), ("BOTTOMPADDING", (0, 1), (0, 1), 5)]))
        return t

    def fig(g, maxh=118 * mm):
        p = figpng(g)
        if not p: return []
        iw, ih = PImage.open(p).size
        w = CW; h = w * ih / iw
        if h > maxh: w, h = maxh * iw / ih, maxh
        return [Spacer(1, 4), Image(p, width=w, height=h),
                Paragraph("Figura %s · %s · NO APTO PARA CONSTRUCCIÓN" % (g, COD), st_cap)]

    story = []
    for i, (tit, blo) in enumerate(L):
        n = i + 1
        page = []
        if tit == "PORTADA":
            page += [Spacer(1, 16 * mm),
                     Paragraph("REPÚBLICA BOLIVARIANA DE VENEZUELA", cen(10, "#1a1a1a")),
                     Paragraph("MINISTERIO DEL PODER POPULAR PARA EL TRANSPORTE", cen(9.5, "#1a1a1a", False)),
                     Paragraph("MARINA MERCANTE DE VENEZUELA", cen(9.5, "#1a1a1a", False)),
                     Spacer(1, 9 * mm),
                     Paragraph("UNIVERSIDAD MARÍTIMA DEL CARIBE – UMC", cen(15, NAVY)),
                     Paragraph("Campus Catia La Mar · estado La Guaira", cen(9.5, "#1a1a1a", False)),
                     Spacer(1, 9 * mm),
                     Paragraph("PRESENTACIÓN EJECUTIVA", cen(25, NAVY)),
                     Paragraph("PATIO / CUBIERTA DE HONOR (EXT-PCH-04)", cen(13, AZUL2)),
                     Paragraph("«LA CUBIERTA DE FORMACIÓN» · PROYECTO 05", cen(13, AZUL2)),
                     Spacer(1, 9 * mm)]
            meta = [[Paragraph(k, st_cellb), Paragraph(v, st_cell)] for k, v in PORTADA_META]
            tm = Table(meta, colWidths=[CW * .34, CW * .66])
            tm.setStyle(TableStyle([("GRID", (0, 0), (-1, -1), .5, cLin),
                                    ("BACKGROUND", (0, 0), (0, -1), colors.HexColor("#f2f2f2")),
                                    ("VALIGN", (0, 0), (-1, -1), "TOP"),
                                    ("LEFTPADDING", (0, 0), (-1, -1), 4.5), ("RIGHTPADDING", (0, 0), (-1, -1), 4.5),
                                    ("TOPPADDING", (0, 0), (-1, -1), 3), ("BOTTOMPADDING", (0, 0), (-1, -1), 3)]))
            page += [tm, Spacer(1, 5 * mm),
                     warn("ADVERTENCIA TÉCNICA",
                          "Documento de Ingeniería Básica / Anteproyecto. NO apto para construcción, replanteo ni "
                          "licitación. Estimaciones AACE Clase 5 (−25 % / +40 %), moneda USD referencial.")]
        else:
            page.append(Paragraph("%d. %d · %s" % (n - 1, n - 1, tit), st_tit))
            for b in blo:
                if b[0] == "p": page.append(Paragraph(b[1], st_pi))
                elif b[0] == "h": page.append(Paragraph(b[1], st_sub))
                elif b[0] == "b":
                    for x in b[1]:
                        page.append(Paragraph(x, st_li, bulletText="•"))
                elif b[0] == "t":
                    page.append(Spacer(1, 2)); page.append(tabla(b[1], b[2], b[3])); page.append(Spacer(1, 3))
                elif b[0] == "warn": page.append(Spacer(1, 2)); page.append(warn(b[1], b[2]))
                elif b[0] == "fig": page += fig(b[1])
        story.append(KeepInFrame(CW, Hh - MT - MB - 2 * mm, page, mode="shrink"))
        if n < NTOT: story.append(PageBreak())

    out = os.path.join(ENT, STEM + ".pdf")
    doc = BaseDocTemplate(out, pagesize=A4, leftMargin=ML, rightMargin=MR, topMargin=MT,
                          bottomMargin=MB, title=COD + " Presentación Ejecutiva",
                          author="UMC — Plan Maestro 2025-2030")

    def decor(canv, d):
        canv.saveState()
        canv.setFont("Calibri-Bold", 7.4); canv.setFillColor(cNavy)
        canv.drawCentredString(W / 2, Hh - 11 * mm, HDR)
        canv.setStrokeColor(cNavy); canv.setLineWidth(1)
        canv.line(ML, Hh - 13 * mm, W - MR, Hh - 13 * mm)
        canv.setFont("Calibri-Bold", 7.4); canv.setFillColor(cRojo)
        canv.drawCentredString(W / 2, 11.5 * mm, PIE)
        canv.setFont("Calibri", 7.4); canv.setFillColor(colors.HexColor("#333333"))
        canv.drawCentredString(W / 2, 7.5 * mm, "Pág. %d de %d" % (canv.getPageNumber(), NTOT))
        canv.restoreState()

    fr = Frame(ML, MB, CW, Hh - MT - MB, id="f")
    doc.addPageTemplates([PageTemplate(id="p", frames=[fr], onPage=decor)])
    doc.build(story)
    data = open(out, "rb").read()
    print("PDF", out, os.path.getsize(out), "págs:",
          data.count(b"/Type /Page") - data.count(b"/Type /Pages"))

if __name__ == "__main__":
    build_html()
    build_pdf()

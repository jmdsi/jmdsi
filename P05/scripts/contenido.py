# -*- coding: utf-8 -*-
"""Contenido de los 28 capítulos del expediente UMC2030-P05-EXTPCH-R01.
Bloques: ("p", texto) · ("h3", texto) · ("box", texto) · ("fig", "G-nn")
         ("t", [enc], [filas], nota_pie)"""
from common import *

FTE = "[FUENTE: " + F_FICHA + "]"
FTEC = "[FUENTE: " + F_CAT + "]"
FTEI = "[FUENTE: inventarios Portaplanos 01–05, lectura 26-10-2026]"
FTEP4 = "[FUENTE: " + F_P04 + ", Cap. 21 Partida 26 y Cap. 22]"

CAP = []
def cap(n, t, *bloques):
    CAP.append((n, t, list(bloques)))

cap(1, "CONTROL DOCUMENTAL Y ADVERTENCIA TÉCNICA",
 ("t", ["Ítem", "Registro"],
  [["Documento", "Expediente de Ingeniería Básica / Anteproyecto — Patio / Cubierta de Honor (EXT-PCH-04)"],
   ["Código", COD],
   ["Revisión", "R01 — primera emisión del P05"],
   ["Fecha de emisión", FECHA],
   ["Fase", "Ingeniería Básica / Anteproyecto (no apto para construcción)"],
   ["Estado de emisión", "EMITIDO PARA COORDINACIÓN Y PRESUPUESTO PRELIMINAR"],
   ["Clase de estimación", "AACE Clase 5 (ROM), exactitud −25 % / +40 %"],
   ["Documento rector", F_FICHA],
   ["Documento base", F_CAT + " (4 láminas; ID Drive vigente 13QVyI4oS9JcaPjhvKHE15BiduCaXChb5)"],
   ["Proyectista responsable", "Por designar – profesional habilitado (Ley de Ejercicio de la Ingeniería, la Arquitectura y Profesiones Afines)"],
   ["Revisor UMC", "Dirección de Planta Física / Vicerrectorado Administrativo"],
   ["Aprobación", "Rectorado UMC – Cap. Alt. / Dr. Guillermo Antonio Riut Hernández"],
   ["Autoría del documento fuente", "Prof. Jhonny Da Silva Izquierdo (MSc. Ing. Lic., CIV 95787) — Plan Maestro y levantamiento catastral-documental, no la nueva ingeniería"],
   ["Confidencialidad", CONF]], ""),
 ("box", "ADVERTENCIA TÉCNICA – LÍMITE DE USO. Este expediente NO es apto para construcción, replanteo, "
  "licitación ni compromiso contractual. Condiciones para pasar a «Apto para Construcción»: "
  "(1) levantamiento topográfico con BM-UMC-01 y cota Z [RFI-GEO-01]; (2) estudio geotécnico de subbase, "
  "rellenos y colectores (calicatas, PDC, estanqueidad) [RFI-GEOT-01]; (3) ingeniería de detalle firmada por "
  "profesional habilitado; (4) verificación de vigencia normativa [RFI-NOR-01]; (5) permisología institucional y "
  "patrimonial; (6) cómputos y presupuesto contractuales con cotizaciones locales; (7) coordinación de interfaces "
  "aprobada con P04-R02. CONDICIÓN ADICIONAL POST-SÍSMICA: la consolidación del borde Babor (Torre CUL-TOO-02, "
  "alcance P04) precede a toda obra del pavimento en los 380,00 m² del borde occidental."))

cap(2, "OBJETO Y ALCANCE DEL PROYECTO",
 ("h3", "2.1 Objeto general"),
 ("p", "Restaurar integralmente el Patio / Cubierta de Honor (EXT-PCH-04, Proa Central) del Campus UMC Catia La Mar "
  "— 1.625,00 m² de explanada ceremonial pavimentada de 50,00 × 32,50 m " + FTE + " — devolviéndole su función "
  "protocolar (paradas navales, graduaciones OMI/STCW, orden cerrado) y su función de seguridad humana como Punto "
  "de Reunión y Evacuación Sísmica Primario R-1, tras el doblete sísmico del 24-06-2026 (Mw 7,2 y Mw 7,5)."),
 ("h3", "2.2 Objetos específicos"),
 ("p", "• Diagnosticar el daño del pavimento rígido por zonas (D2/D3/D4) y decidir la intervención por zona. "
  "• Reponer el paquete de pavimento con reintegración del acabado granítico/martelinado de 1951. "
  "• Sanear la subbase y sustituir los colectores enterrados (PEAD SN8). "
  "• Restaurar/reponer el Asta Mayor Ceremonial (h = 12,00 m) y dotar alumbrado, señalización R-1 y accesibilidad. "
  "• Emplazar el Mástil Hidrometeorológico OMM (h = 10,00 m) en interfaz con la estación del P04."),
 ("h3", "2.3 Alcance incluido"),
 ("p", "Los 1.245,00 m² (76,62 %) de explanada central remanente como objeto presupuestario neto, más las partidas "
  "integrales no solapadas (drenaje, eléctrica, asta, señalización, comisionamiento) " + FTE + "."),
 ("h3", "2.4 Alcance excluido (explícito)"),
 ("box", "EXCLUIDO: los 380,00 m² (23,38 %) del borde occidental Proa–Babor —que contienen los 210,00 m² de la Banda "
  "de Protocolo— ya incluidos en el BOQ del expediente P04-R02 " + FTEP4 + ", así como la consolidación estructural "
  "de la Torre de Observación y la Sala Técnica (alcance íntegro del P04). Regla R4/R12: prohibida la doble "
  "presupuestación; la deducción económica es de USD 330.000 (Cap. 22)."),
 ("fig", "G-03"))

cap(3, "ANTECEDENTES Y BASE DOCUMENTAL",
 ("p", "La explanada nace como Plaza de Armas de la Escuela Náutica de Venezuela (MOP, Dirección de Edificios; "
  "Arq. Luis Raimundo Malaussena Andueza; estructura Oficina Técnica Gutiérrez & Co. S.A.). El proyecto estructural "
  "base de las Fracciones 1 y 2 es del 28-08-1951 (signaturas 15 DF 30 y 8.DF.2.364); la lámina de Situación General "
  "y Urbanismo P04-L5-A es del 24-10-1953; obras complementarias 1956–1958 y operación inaugural 1951–1959 " + FTE + "."),
 ("p", "El registro histórico (Lámina 3 de " + F_CAT + ") documenta la explanada en pleno uso ceremonial: formaciones "
  "de cadetes, el asta mayor, el frente del Auditorio y la Torre, y los corredores cubiertos perimetrales EXT-CTC-15 "
  + FTEC + ". El registro forense (Lámina 4, «POST SISMO») evidencia el agrietamiento severo de losas, pérdida de "
  "sello, desniveles entre paños, hundimientos sobre trincheras y escombros en el borde de la Torre."),
 ("p", "Acervo documental: 198 PDF y 487 fotografías (IMG_2134–IMG_2778) en los Tubos Portaplanos 01–05 " + FTEI +
  ". Los expedientes P01 (esquema rector), P02, P03 y P04-R02 (colindante a conciliar) constituyen la base de "
  "coordinación del Plan Maestro 2025–2030."),
 ("fig", "G-02"))

cap(4, "MARCO NORMATIVO Y REFERENCIAS TÉCNICAS",
 ("t", ["Ámbito", "Referencia", "Aplicación en el P05", "Estado"],
  [["Sismorresistencia", "COVENIN 1756", "Juntas sísmicas de desacople; evaluación post-sísmica", "vigencia por verificar [RFI-NOR-01]"],
   ["Concreto estructural", "COVENIN 1753", "Losa de pavimento, fundación del asta", "vigencia por verificar [RFI-NOR-01]"],
   ["Eléctrico", "COVENIN 200 (CEN)", "Red subterránea, alumbrado, tierra", "vigencia por verificar [RFI-NOR-01]"],
   ["Señalización/evacuación", "COVENIN 810 / 187", "Punto R-1, rutas y señalética", "vigencia por verificar [RFI-NOR-01]"],
   ["Accesibilidad", "Fondonorma 2733", "Franjas podotáctiles, podio accesible", "vigencia por verificar [RFI-NOR-01]"],
   ["Drenaje urbano", "Criterio Tr = 25 años (Ficha, Técnico 4)", "Canaletas, colectores, tanquillas", "fuente del criterio por consolidar [RFI-NOR-01]"],
   ["Marítimo-académico", "OMI / STCW", "Función ceremonial de graduaciones de oficiales", "referencial"],
   ["Meteorología", "OMM — Guía de Instrumentos (emplazamiento)", "Mástil OMM y parcela de sensores", "referencial [RFI-OMM-01]"],
   ["Descargas atmosféricas", "IEC 62305", "SPDA del asta y mástil; malla R ≤ 5 Ω", "vigencia por verificar [RFI-NOR-01]"],
   ["Patrimonio cultural", "Normativa venezolana de protección patrimonial", "Obra MOP 1951–1958 (Malaussena)", "referencia a verificar; no se acredita cumplimiento"]],
  "Ninguna norma se declara cumplida: toda cita es referencial hasta la verificación de vigencia (R10)."))

cap(5, "EMPLAZAMIENTO, GEORREFERENCIACIÓN Y TOPOGRAFÍA",
 ("h3", "5.1 Zona de intervención"),
 ("p", "Proa Central del campus (eje Proa–Babor a Proa–Estribor), interfaz dual EXT (Espacios Exteriores "
  "Institucionales) / CUL (Área Cultural y Ceremonial). Bordes: Proa (N) Fracción 1 — Aula Magna; Estribor (E) "
  "Fracción 2; Popa (S) Fracción 3; Babor (O) Torre CUL-TOO-02 y Sala ACA-STH-15 " + FTE + "."),
 ("h3", "5.2 Puntos de control georreferenciados"),
 ("t", ["Punto", "Lat / Lon (WGS84)", "Decimal", "UTM 19N (EPSG:32619)", "Observación"],
  [["Centroide EXT-PCH-04", "10°36'02,55\" N · 67°01'55,20\" O", "10,60070833° · −67,03200000°",
    "E 715.324,40 · N 1.172.523,10", "Se corrige la inversión de rótulos X/E–Y/N del borrador " + FTEC],
   ["Torre C-TO (referencia)", "—", "—", "ΔE = +32,21 m · ΔN = −13,21 m", "distancia radial d = 34,81 m " + FTE],
   ["BM-UMC-01", "—", "—", "—", "POR ESTABLECER — cota Z pendiente [RFI-GEO-01]"]], ""),
 ("h3", "5.3 Control geométrico preliminar"),
 ("p", "Cuerpo de la Fracción 2: 13 módulos estructurales de 4,00 m = 52,00 m × 48,75 m, verificado en P04-L5-A, "
  "P0102-L6-F/H/I y P04-L1-C/D [FUENTE: Ficha §3.2; inventarios]. Huella neta pavimentada: 50,00 m (E-O) × 32,50 m "
  "(N-S) = 1.625,00 m² [DERIVADO: 50,00 × 32,50 = 1.625,00 ✔], descontando franjas de transición de 1,00 m hacia "
  "los corredores EXT-CTC-15 (3,00–3,60 m)."),
 ("h3", "5.4 Sistema cartográfico"),
 ("p", "Referencia WGS84 / EPSG:4326; trabajo en UTM huso 19N / EPSG:32619 (compatible REGVEN). Conversión DMS↔decimal "
  "en Anexo B."),
 ("h3", "5.5 Topografía y movimiento de tierras"),
 ("p", "Obra de restauración con movimiento de tierra marginal (saneamiento de subbase y zanjas de colectores). "
  "Pendiente pluvial proyectada 1,2 %–1,5 % (diseño original 1,0 %–1,5 % s/ P03-ENV-002 " + FTEI + "). La nivelación "
  "de escalonamientos (1,5–4,5 cm) exige topografía TLS de detalle [RFI-PAT-01]."),
 ("fig", "G-01"))

cap(6, "CONCEPTO ARQUITECTÓNICO",
 ("h3", "6.1 Concepto rector: «La Cubierta de Formación»"),
 ("p", "El patio es la cubierta principal del Campus-Buque Digital UMC: el plano horizontal donde la institución "
  "forma, pasa revista y gradúa a sus oficiales frente al asta del Pabellón. Se decide este concepto (y no una "
  "metáfora vertical) porque el valor del espacio es su vacío modulado: una lámina pétrea continua, enmarcada por "
  "los cuerpos de Malaussena, cuyo único protagonista vertical es el asta. [HIPÓTESIS: decisión de diseño A1, "
  "justificada en la lectura del registro histórico 1951–1959 " + FTEC + "]"),
 ("h3", "6.2 Lenguaje"),
 ("p", "Modernidad venezolana de los 1950: paños modulados sobre la retícula de 4,00 m, acabado granítico/cemento "
  "martelinado, bandas y brocales horizontales, relación directa con el foyer del Aula Magna (NPT ±0,000) y los "
  "corredores EXT-CTC-15."),
 ("h3", "6.3 Doctrina de intervención patrimonial"),
 ("box", "CONSERVAR los paños D0–D1 que la inspección de detalle confirme sanos · CONSOLIDAR bordes y brocales "
  "originales · REINTEGRAR el acabado granítico/martelinado con mortero y granulometría compatibles · REPONER los "
  "paños D3 con losa nueva distinguible mediante JUNTA-TESTIGO DATADA (distinguibilidad de lo contemporáneo, sin "
  "falsificación histórica) · SUSTITUIR las redes enterradas agotadas. La normativa patrimonial se cita como "
  "referencia a verificar (R9/R10)."))

cap(7, "PARÁMETROS URBANÍSTICOS Y DE DISEÑO",
 ("t", ["Parámetro", "Valor", "Trazabilidad"],
  [["Tipología", "Espacio abierto ceremonial — 0 niveles sobre rasante", FTE],
   ["Altura", "0,00 m (corrección de la errata «0 m²» del borrador)", FTEC + " / " + FTE],
   ["Elementos verticales asociados", "Asta Mayor 12,00 m · Mástil OMM 10,00 m · (contexto: Torre colindante 22,02 m / 12,20 m original — RFI-ALT-01 heredada)", FTE],
   ["Pendiente superficial", "1,2 % – 1,5 %", FTE],
   ["Aforo de diseño", "1.300 cadetes (1,25 m²/ef.) · 1.625 personas (1,00 m²/p.) · R-1: 1.080–1.625", FTE + " [DERIVADO: 1.625/1,25 = 1.300 ✔]"],
   ["Cargas de uso", "Formaciones + vehículo de emergencia/mantenimiento sobre losa", "[HIPÓTESIS: carga vehicular a definir en detalle]"],
   ["Accesibilidad", "Franjas podotáctiles, podio de protocolo accesible", "Fondonorma 2733 (referencial)"],
   ["Condición singular", "Espacio protocolar emblema + Punto R-1 del Sector Proa", FTE]], ""))

cap(8, "PROGRAMA FUNCIONAL Y CUADRO GENERAL DE ÁREAS",
 ("h3", "8.1 Explanada ceremonial"),
 ("p", "Zonas de formación por compañías, calle de revista y eje de desfile paralelo al frente del Aula Magna; "
  "izada/arriada del Pabellón Nacional en el eje del asta. [Distribución espacial: HIPÓTESIS de anteproyecto, G-05]"),
 ("h3", "8.2 Banda de Protocolo (interfaz)"),
 ("p", "210,00 m² (12,92 %) dentro del borde occidental del P04 — solo coordinación, sin partidas en este expediente " + FTEP4 + "."),
 ("h3", "8.3 Elementos protocolares"),
 ("p", "Asta Mayor Ceremonial h = 12,00 m con fundación independiente, pedestal de concreto visto y podio accesible "
  "(partida E3.03 de la Ficha); Tribuna de Honor y zona de autoridades en el frente Estribor."),
 ("h3", "8.4 Mástil Hidrometeorológico OMM"),
 ("p", "h = 10,00 m con parcela de sensores; emplazamiento condicionado al estudio de obstáculos del borde Babor "
  "[RFI-OMM-01]; telemetría integrada a la estación del P04 (sin duplicar adquisición)."),
 ("h3", "8.5 Función R-1"),
 ("p", "Zonas de concentración y rutas de aproximación desde las Fracciones 1, 2 y 3 (capítulo 17)."),
 ("h3", "8.6 Resumen del cuadro de áreas"),
 ("t", ["Componente", "Área (m²)", "%", "Asignación"],
  [["Borde occidental Proa–Babor (incl. Banda de Protocolo 210,00 m²)", "380,00", "23,38 %", "P04-R02 (excluido del BOQ P05)"],
   ["Explanada central remanente", "1.245,00", "76,62 %", "P05 (objeto presupuestario neto)"],
   ["TOTAL EXT-PCH-04", "1.625,00", "100,00 %", "conciliado " + FTE]],
  "Verificación: 380,00 + 1.245,00 = 1.625,00 ✔ · conjuntos anidados, no sumables entre sí (R4)."),
 ("fig", "G-05"), ("fig", "G-10"))

cap(9, "COMPONENTES FUNCIONALES – FICHAS",
 ("t", ["Componente", "Ubicación", "Área / dimensión", "Capacidad / función", "Estado"],
  [["Explanada de formación", "Centro de la poligonal", "≈ 650 m² útiles de formación [HIPÓTESIS]", "1.300 cadetes a 1,25 m²/ef. (campo total)", "a reponer (D3/D2)"],
   ["Eje ceremonial e izada", "Eje del asta, frente F1", "franja ≈ 6 m [HIPÓTESIS]", "izada/arriada del Pabellón", "a reponer"],
   ["Banda de Protocolo", "Borde occidental", "210,00 m² " + FTE, "banda ceremonial", "interfaz P04 (sin partidas P05)"],
   ["Tribuna de Honor y podio", "Frente Estribor", "por dimensionar [RFI-PRO-01]", "autoridades y rectoría", "a restaurar/reponer"],
   ["Punto R-1", "Toda la explanada", "1.625,00 m²", "1.080–1.625 personas", "INHABILITADO (transitorio)"],
   ["Mástil OMM + parcela", "Cuadrante NE [HIPÓTESIS]", "h = 10,00 m", "estación de superficie (interfaz P04)", "nuevo"],
   ["Alumbrado ceremonial/emergencia", "Perímetro + cajas de piso", "12 luminarias IP66/IK10", "100–150 lux + emergencia R-1", "nuevo (sustituye P03-L3-B)"],
   ["Drenaje pluvial", "Perímetro + colectores", "180 m canaletas · 140 m PEAD · 8 tanquillas", "Q = 73,13/145 L/s, Tr 25 años", "nuevo"],
   ["Señalización y accesibilidad", "Accesos y rutas", "COVENIN 810/187 + 2733", "R-1 + podotáctil", "nuevo"]],
  "Matriz de cumplimiento estilo P01: componente → ubicación → área → estado. Cifras sin etiqueta propia provienen de la Ficha (partidas E1–E6)."))

cap(10, "ARQUITECTURA – PAVIMENTO, MATERIALES Y ACABADOS",
 ("h3", "10.1 Criterios generales"),
 ("p", "Ambiente marino costero (cloruros, UV, ciclos de humectación): materiales de larga vida y sin pares "
  "galvánicos entre rejillas, flejes, astas y luminarias. Compatibilidad cromática y de textura con la obra 1951–58."),
 ("h3", "10.2 Cuadro de materiales y acabados (referencial)"),
 ("t", ["Elemento", "Material", "Acabado / condición"],
  [["Losa de pavimento", "Concreto vaciado en sitio (MR por diseño)", "Acabado granítico / cemento martelinado reintegrado"],
   ["Juntas", "Sello elastomérico PU bicomponente + backer rod", "resistente a UV y salinidad; e = 25–50 mm en juntas sísmicas " + FTE],
   ["Rejillas de canaleta", "Fundición dúctil / AISI 316, clase C250", "antivandálica, apta tránsito de mantenimiento"],
   ["Asta Mayor", "Acero galvanizado en caliente / AISI 316", "drizas navales; pedestal de concreto visto " + FTE],
   ["Luminarias", "LED marinas IP66 / IK10", "100–150 lux; emergencia autónoma"],
   ["Señalización", "COVENIN 810/187 + podotáctil Fondonorma 2733", "R-1 y accesibilidad"],
   ["Paisajismo", "Especies halófilas perimetrales", "bajo mantenimiento " + FTE]], ""),
 ("h3", "10.3 Reintegración de elementos perdidos"),
 ("p", "Los paños D3 demolidos se reponen con losa contemporánea distinguible (junta-testigo datada); los fragmentos "
  "del acabado original con valor documental se registran e integran al archivo patrimonial (gestión de escombros "
  "con valor patrimonial, Cap. 20). Ningún elemento se replica como falso histórico (R9)."),
 ("h3", "10.4 Confort exterior"),
 ("p", "Control de temperatura superficial y deslumbramiento del acabado claro; sombra de borde en corredores "
  "EXT-CTC-15; ventilación natural franca del vacío central."),
 ("fig", "G-06"))

cap(11, "CRITERIOS ESTRUCTURALES Y GEOTÉCNICOS DEL PAVIMENTO",
 ("h3", "11.1 Paquete estructural propuesto"),
 ("p", "Losa de concreto sobre subbase granular mejorada y saneada, con módulo de rotura y espesor POR CALCULAR en "
  "detalle, CONDICIONADOS al estudio geotécnico [RFI-GEOT-01]. El esquema comparativo existente/propuesto se "
  "presenta en G-06."),
 ("h3", "11.2 Retícula de paños y juntas"),
 ("p", "Paños de vaciado compatibles con la retícula estructural de 4,00 m (≈ 4,00 × 5,00 m [HIPÓTESIS]); juntas de "
  "contracción en ambas direcciones, selladas."),
 ("h3", "11.3 Juntas sísmicas de desacople"),
 ("p", "Desacople perimetral losa–Fracciones 1/2 y losa–cabezales piloteados, e = 25–50 mm, ≈ 980 m de sellado "
  "elastomérico [FUENTE: Ficha, partida E3.02 — «desacople losa–cabezales piloteados»]."),
 ("h3", "11.4 Predimensionamiento preliminar"),
 ("t", ["Elemento", "Sección / dimensión preliminar", "Base", "Verificación requerida"],
  [["Losa de pavimento", "e ≈ 15–18 cm [HIPÓTESIS]", "uso peatonal masivo + vehículo de emergencia", "diseño por fatiga/MR con geotecnia"],
   ["Subbase mejorada", "e ≈ 20–30 cm [HIPÓTESIS]", "saneamiento de rellenos asentados", "CBR/PDC en calicatas [RFI-GEOT-01]"],
   ["Fundación del asta (12,00 m)", "zapata/pedestal independientes " + FTE, "viento + IEC 62305", "cálculo de detalle"],
   ["Fundación del mástil OMM (10,00 m)", "por dimensionar", "viento + criterios OMM", "cálculo de detalle [RFI-OMM-01]"]],
  "Ningún valor de esta tabla es constructivo."),
 ("h3", "11.5 Diagnóstico patológico post-sísmico (síntesis F2)"),
 ("t", ["Zona / elemento", "Daño", "Evidencia", "Decisión de intervención"],
  [["Paños centrales (680,00 m²)", "D3 — fractura diagonal de paños, escalonamientos 1,5–4,5 cm", "Lámina 4 " + FTEC + "; dictamen " + FTE, "demoler y reponer con reintegración"],
   ["Paños orientales (565,00 m²)", "D2 — fisuración, pérdida de sellos", "ídem", "reparar juntas + resellado; reponer paños puntuales"],
   ["Borde Babor (380,00 m²)", "D4 inducido — impacto/caída de escombros de la Torre (N0 y coronación +22,02 m)", "ídem", "TRANSFERIDO a P04 (consolidación previa)"],
   ["Subbase / rellenos s/ zanjas", "asentamientos diferenciales", "hundimientos sobre trincheras " + FTEC, "sanear + recompactar + geotextil"],
   ["Colectores enterrados", "fugas/colapso presuntos [HIPÓTESIS causal]", "hundimientos coincidentes con trazados", "sustituir por PEAD SN8 + prueba de estanqueidad"],
   ["Sellos y flejes de juntas (≈980 m)", "envejecimiento 75 años + sismo", "pérdida de sellos " + FTE, "resellar integralmente"],
   ["Asta y pedestal", "estado por inspeccionar", "—", "restaurar/reponer s/ partida E3.03 [RFI-PAT-02]"]],
  "Escala D0–D4 declarada REFERENCIAL (adaptada de ATC-20/condición de pavimentos rígidos, citadas como referencia). "
  "Clasificación de uso: INHABILITADO para paradas/desfiles; INSPECCIÓN DETALLADA requerida antes de demolición."),
 ("h3", "11.6 Hipótesis de causa y requerimientos de inspección"),
 ("p", "Hipótesis: densificación/licuación local de rellenos sobre zanjas; pérdida de soporte por fuga de colectores "
  "antiguos; ausencia de desacople sísmico contra las estructuras; envejecimiento de sellos; impacto de escombros "
  "en el borde Babor. Inspecciones: TLS de escalonamientos [RFI-PAT-01], calicatas + PDC [RFI-GEOT-01], prueba de "
  "estanqueidad y videoinspección de colectores [RFI-PAT-03], inspección del asta [RFI-PAT-02], georradar de "
  "trincheras [RFI-PAT-04]."),
 ("fig", "G-04"), ("fig", "G-07"))

cap(12, "INSTALACIONES MEP",
 ("h3", "12.1 Sistema eléctrico exterior"),
 ("p", "Red subterránea nueva en bancadas PVC/PEAD Ø 4\" con juntas sísmicas flexibles; 12 luminarias LED marinas "
  "IP66/IK10 (100–150 lux); alumbrado de emergencia R-1; 2 cajas de piso IP67 para la Banda de Protocolo; malla de "
  "puesta a tierra R ≤ 5 Ω y SPDA del asta y del mástil (IEC 62305) [FUENTE: Ficha, partida E5.01]. Sustituye la "
  "red histórica P03-L3-B (1:200) " + FTEI + "."),
 ("h3", "12.2 Drenaje pluvial (instalación crítica)"),
 ("p", "Q propio = 73,13 L/s; con faldones aportantes ≈ 145 L/s; Tr = 25 años. Canaletas lineales perimetrales con "
  "rejilla clase C250 (≈ 180 m); colectores PEAD doble pared SN8 Ø 300–400 mm (≈ 140 m); 8 tanquillas/sumideros "
  "[FUENTE: Ficha, partida E4.01 y Técnico 4]. Descarga coordinada con el canal/toma de quebrada documentados en el "
  "Paquete 05 (R-19, R-20) " + FTEI + "."),
 ("h3", "12.3 Protección contra incendios"),
 ("p", "Hidrante de columna / toma siamesa en el borde Norte con válvula de seccionamiento en el anillo PCI del "
  "campus, coordinado con el Cap. 12.4 del P04-R02 [FUENTE: Ficha, partida E4.02]."),
 ("h3", "12.4 Otros servicios"),
 ("p", "Riego del paisajismo halófilo perimetral solo si la red AGU existente lo sustenta (láminas P03-L2-D, P05 "
  "R-25/R-28) — por verificar en detalle."),
 ("fig", "G-08"), ("fig", "G-09"))

cap(13, "TELECOMUNICACIONES Y CAMPUS",
 ("p", "13.1 Canalizaciones subterráneas de reserva TIC en las mismas bancadas eléctricas (separación normativa), "
  "con enlace al CDP/Torre B según arquitectura de red del Plan Maestro [FUENTE: " + F_PM + ", referencial]. "
  "13.2 Megafonía protocolar (cajas de piso de la Banda + perímetro) y CCTV de la explanada (Cap. 14). "
  "13.3 Interfaz de datos del Mástil OMM con la estación hidrometeorológica del P04 (Sala ACA-STH-15): telemetría "
  "integrada, un solo sistema de adquisición y registro — prohibida la duplicación de registradores (R12)."))

cap(14, "SEGURIDAD FÍSICA Y CONTROL",
 ("p", "Espacio abierto de acceso público en actos: protección antivandálica de luminarias (IK10), rejillas "
  "atornilladas antirrobo, señalización antivandálica; control perimetral removible en ceremonias; CCTV de explanada "
  "con grabación en el CDP; protección física del mástil OMM y de la parcela de sensores (cerramiento bajo "
  "normativo OMM); gestión de multitudes en graduaciones (1.625 personas) con separación de flujos protocolares y "
  "públicos. [Criterios de anteproyecto; diseño de detalle por especialista]"))

cap(15, "SOSTENIBILIDAD, ENERGÍA Y AMBIENTE MARINO",
 ("p", "15.1 Alumbrado LED eficiente con telegestión y medición dedicada. 15.2 Durabilidad costera: concretos de "
  "baja permeabilidad, sellos UV, metales AISI 316/galvanizado en caliente, mantenimiento programado de sellos "
  "(vida útil del sello < vida de la losa — plan AIM). 15.3 El drenaje del patio como activo de resiliencia "
  "climática del sector Proa: gestión de 145 L/s de pico con Tr 25 años y datos del mástil OMM alimentando la "
  "operación del campus y el gemelo digital. 15.4 Paisajismo halófilo perimetral de bajo consumo " + FTE + "."))

cap(16, "INDUSTRIA 5.0, BIM Y GEMELO DIGITAL",
 ("p", "16.1 HBIM del espacio exterior: nube de puntos TLS del pavimento dañado (estado 2026) + restitución del "
  "estado 1951 desde las láminas MOP del listado E1; modelo federado en CDE con estados; codificación documental "
  "UMC-[ACTIVO]-[DISCIPLINA]-[NÚMERO]-[REV]. La base GIS/BIM adopta el desdoblamiento catastral UMC-EXT-004 / "
  "UMC-ED-000-PCH04 dictaminado por el Ingeniero Catastral Senior [FUENTE: Ficha §3.1] — resolución de RFI-COD-05 "
  "pendiente de acto administrativo."),
 ("p", "16.2 Sensorización: hitos de asentamiento en paños repuestos, sensores de nivel en tanquillas, pluviómetro "
  "del mástil, conteo de aforo en actos. 16.3 Enfoque humanocéntrico: el cadete en formación, el operador de "
  "mantenimiento y la seguridad de evacuación son los usuarios de diseño; la tecnología apoya la función ceremonial "
  "sin sustituirla."),
 ("fig", "G-11"))

cap(17, "ACCESIBILIDAD, AFORO Y EVACUACIÓN (CAPÍTULO CRÍTICO)",
 ("p", "El patio ES el Punto de Reunión y Evacuación Sísmica Primario R-1 del Sector Proa " + FTE + ". Aforos: "
  "1.300 cadetes en formación (1,25 m²/ef.), 1.625 personas en actos (1,00 m²/p.), 1.080–1.625 como punto R-1 "
  "[DERIVADO: verificaciones aritméticas ✔]. Rutas de aproximación desde Fracciones 1, 2 y 3 y corredores "
  "EXT-CTC-15; señalización COVENIN 810/187; franjas podotáctiles Fondonorma 2733; alumbrado de emergencia "
  "autónomo; itinerario accesible al podio de protocolo."),
 ("box", "CONDICIÓN TRANSITORIA CRÍTICA: con el patio INHABILITADO (0 personas para paradas desde 24-06-2026), las "
  "fuentes NO identifican un punto R-1 alterno para el Sector Proa. Se abre RFI-EVA-01 (responsable: Dirección de "
  "Planta Física + Seguridad Integral) con prioridad MÁXIMA: designar y señalizar el punto alterno antes del inicio "
  "de la obra, y mantenerlo durante toda la ejecución."),
 ("fig", "G-12"))

cap(18, "OBRAS EXTERIORES E INFRAESTRUCTURA COMÚN",
 ("h3", "18.1 Bordes y transiciones"),
 ("p", "Brocales y franjas de transición de 1,00 m hacia los corredores EXT-CTC-15 (3,00–3,60 m); vialidad de "
  "emergencia perimetral preservada; accesos desde las tres fracciones."),
 ("h3", "18.2 Sección tipo de la trinchera de servicios"),
 ("t", ["Servicio", "Conducto", "Separación / condición"],
  [["Pluvial", "PEAD SN8 Ø 300–400 mm", "cama de arena, relleno compactado controlado, prueba de estanqueidad"],
   ["Eléctrico", "Bancada PVC/PEAD Ø 4\" + juntas sísmicas", "separación normativa de pluvial; cinta de señalización"],
   ["TIC (reserva)", "Ducto en la misma bancada eléctrica", "separación según práctica ANSI/TIA (referencial)"],
   ["Tierra", "Malla + electrodos R ≤ 5 Ω", "registros de inspección accesibles"]],
  "Trazados definitivos tras georradar [RFI-PAT-04]."),
 ("h3", "18.3 Matriz de interfaces del P05"),
 ("t", ["Interfaz", "Objeto", "Regla"],
  [["P05 ↔ P04 (Torre/Sala/borde Babor)", "380,00 m², Banda 210,00 m², consolidación de Torre", "condición suspensiva + deducción USD 330.000; junta de transferencia en lámina P-9"],
   ["P05 ↔ Fracción 1", "foyer NPT ±0,000, frente ceremonial", "no alterar accesos del Aula Magna; desacople sísmico"],
   ["P05 ↔ Fracción 2", "crujía 52,00 m, tribuna/autoridades", "desacople sísmico; coordinación de actos"],
   ["P05 ↔ Fracción 3", "flujo de cadetes a formación", "ruta diaria protegida durante la obra"],
   ["P05 ↔ EXT-CTC-15", "corredores techados perimetrales", "franja de transición 1,00 m; drenaje de faldones"],
   ["P05 ↔ red PCI campus", "hidrante borde Norte", "válvula de seccionamiento; coordinación P04-R02 Cap. 12.4"],
   ["P05 ↔ CDP Torre B", "telemetría, CCTV, telegestión", "canalización de reserva; VLAN de instrumentación"]], ""))

cap(19, "SUBPROYECTO ASOCIADO: CONJUNTO CEREMONIAL DE PROA",
 ("p", "19.1 La rehabilitación del patio se coordina con el conjunto ceremonial: Aula Magna/foyer y galería "
  "(Fracción 1), Torre/Sala (P04), corredores EXT-CTC-15, asta y tribuna. 19.2 Criterio de unidad de intervención: "
  "la Proa Central es un solo frente patrimonial con etapabilidad declarada."),
 ("box", "CONDICIÓN SUSPENSIVA: el borde Babor del patio (380,00 m², zona D4) NO se restaura antes de la "
  "consolidación de la Torre de Observación por el P04. Toda alteración de esta secuencia es una revisión del Plan "
  "de Implantación (R7) y debe aprobarse formalmente."))

cap(20, "ESPECIFICACIONES TÉCNICAS – CONTENIDO MÍNIMO",
 ("t", ["Cap.", "Especificación"],
  [["01", "Condiciones generales, seguridad y salud en obra con campus operativo"],
   ["02", "Replanteo, topografía TLS y control geométrico (BM-UMC-01)"],
   ["03", "Diagnóstico y ensayos in situ: calicatas, PDC, estanqueidad, georradar"],
   ["04", "Demolición controlada y gestión de escombros con valor patrimonial"],
   ["05", "Saneamiento geotécnico de subbase y rellenos; geotextiles"],
   ["06", "Sustitución de colectores PEAD SN8 y pruebas de estanqueidad"],
   ["07", "Pavimento rígido: encofrado, vaciado, curado, juntas y sellos"],
   ["08", "Conservación y reintegración del acabado granítico/martelinado (junta-testigo)"],
   ["09", "Canaletas, rejillas C250 y tanquillas"],
   ["10", "Asta Mayor: fundación, pedestal, izado y drizas navales"],
   ["11", "Red eléctrica exterior, alumbrado, tierra y SPDA (IEC 62305)"],
   ["12", "Mástil OMM: fundación, instrumentación y calibración (criterios OMM)"],
   ["13", "Señalización R-1 (COVENIN 810/187) y accesibilidad (Fondonorma 2733)"],
   ["14", "Paisajismo halófilo y riego (si procede)"],
   ["15", "Monitorización estructural y sensorización IoT del gemelo digital"],
   ["16", "Comisionamiento de alumbrado y drenaje; pruebas de recepción"]],
  "Lista mínima estilo P01, ampliada con las especificaciones patrimoniales y de diagnóstico propias del P05."))

cap(21, "CÓMPUTOS MÉTRICOS PRELIMINARES (BOQ REV.0)",
 ("t", ["Partida", "Descripción", "Ud", "Cant.", "Base de cálculo", "Asignación"],
  [["E1.01", "Retiro controlado de pavimento D3 y gestión de escombros (valor patrimonial)", "m²", "680,00", "mapa de daño G-07 " + FTE, "P05-neto"],
   ["E1.02", "Reparación de paños y juntas en zona D2", "m²", "565,00", "mapa de daño G-07 " + FTE, "P05-neto"],
   ["E2.01", "Saneamiento de subbase y rellenos (incl. zanjas de colectores)", "m²", "≈ 1.245,00", "alcance neto [DERIVADO]", "P05-neto"],
   ["E3.01", "Losa nueva de pavimento con acabado reintegrado", "m²", "680,00 (+ reposiciones puntuales D2)", "zona D3 " + FTE, "P05-neto"],
   ["E3.02", "Sellado elastomérico de juntas de contracción y sísmicas (e=25–50 mm)", "m", "980,00", FTE + " partida E3.02", "P05-neto"],
   ["E3.03", "Fundación, pedestal y restauración/reposición del Asta Mayor (h=12,00 m) + podio", "gl", "1,00", FTE + " partida E3.03 (USD 38.500)", "P05-neto"],
   ["E4.01", "Drenaje: canaletas C250 180 m + PEAD SN8 Ø300–400 140 m + 8 tanquillas", "gl", "1,00", FTE + " partida E4.01 (USD 112.000)", "P05-neto"],
   ["E4.02", "Hidrante / toma siamesa borde Norte + seccionamiento anillo PCI", "ud", "1,00", FTE + " partida E4.02 (USD 14.500)", "P05-neto"],
   ["E5.01", "Red eléctrica subterránea, 12 luminarias IP66/IK10, emergencia R-1, 2 cajas IP67, malla tierra", "gl", "1,00", FTE + " partida E5.01 (USD 96.000)", "P05-neto"],
   ["E6.01", "Señalización R-1, podotáctil, paisajismo halófilo, comisionamiento", "gl", "1,00", FTE + " partida E6.01 (USD 28.395)", "P05-neto"],
   ["—", "Pavimento, juntas y consolidación del borde occidental (incl. Banda de Protocolo)", "m²", "380,00", FTEP4, "P04 (EXCLUIDO)"]],
  "NO son cómputos contractuales. El mástil OMM y su instrumentación van en partida separada de equipos "
  "[RFI-OMM-01: alcance económico por definir con el P04]. Cantidades gl según la Ficha; las métricas se "
  "re-derivarán del TLS y la geotecnia."))

cap(22, "ESTIMACIÓN DE INVERSIÓN (ROM — AACE CLASE 5)",
 ("t", ["Concepto", "USD", "Nota"],
  [["Subtotal costo directo (1.625,00 m² integrales)", "765.000,00", "470,77 USD/m² " + FTE],
   ["Ingeniería de detalle, ensayos geotécnicos/patológicos y supervisión patrimonial (7,0 %)", "53.550,00", "calicatas, PDC, TLS, proyectos ejecutivos"],
   ["Contingencia ROM (10,0 % base)", "76.450,00", "la Ficha consigna 76.450 (10 % nominal = 76.500): redondeo de cierre a 895.000, declarado (R6)"],
   ["ROM INTEGRAL (1.625,00 m²)", "895.000,00", "rango −25 %/+40 %: USD 750.000 – 1.120.000 (550,77 USD/m²)"],
   ["(−) Porción ya presupuestada en P04-R02 (380,00 m² borde Proa–Babor)", "−330.000,00", "banda P04: USD 260.000 – 400.000 " + FTEP4],
   ["(=) PRESUPUESTO NETO ADICIONAL P05 (1.245,00 m²)", "565.000,00", "rango neto: USD 490.000 – 720.000"]],
  "Verificaciones: 765.000 + 53.550 + 76.450 = 895.000 ✔ · 895.000 − 330.000 = 565.000 ✔. Orden de magnitud, NO "
  "presupuesto de licitación; precios unitarios a sustituir por cotizaciones locales (MONEDA USD referencial)."),
 ("fig", "G-13"))

cap(23, "CRONOGRAMA DE EJECUCIÓN",
 ("t", ["Fase", "Denominación", "Duración est.", "Hito / gate"],
  [["A", "Estudios previos: TLS, calicatas, PDC, BM-UMC-01, videoinspección", "≈ 2,0 meses", "Geotecnia cierra RFI-GEOT-01"],
   ["B", "Desescombro y demolición controlada con gestión patrimonial", "≈ 2,0 meses", "GATE: borde Babor consolidado por P04"],
   ["C", "Saneamiento de subbase + colectores PEAD + estanqueidad", "≈ 2,5 meses", "Prueba de estanqueidad aprobada"],
   ["D", "Pavimento: losas, juntas, sellos, reintegración de acabado", "≈ 3,0 meses", "Paños piloto aprobados (muestra de acabado)"],
   ["E", "Asta, eléctrica, señalización R-1, comisionamiento", "≈ 1,5 meses", "Habilitación protocolar y del punto R-1"]],
  "Duración total ≈ 9 meses con solapes [HIPÓTESIS A8]. Restricciones duras: secuencia P04→borde Babor; calendario "
  "académico-ceremonial (graduaciones); lluvias (subbase nunca abierta en pico pluvial); punto R-1 alterno operativo "
  "durante toda la obra. Procuración de largo plazo: rejillas C250 AISI 316, luminarias marinas, asta e "
  "instrumentación OMM."),
 ("fig", "G-14"))

cap(24, "PLANOS DEL EXPEDIENTE",
 ("t", ["Código", "Denominación", "Escala", "Estado"],
  [["UMC-PCH-P-0", "Implantación general georreferenciada de la Proa Central", "1:400", "Anteproyecto"],
   ["UMC-PCH-P-1", "Planta general de paños, juntas y pendientes", "1:200", "Anteproyecto"],
   ["UMC-PCH-P-2", "Planta de demolición/retiro por zonas de daño", "1:250", "Anteproyecto"],
   ["UMC-PCH-P-3", "Planta de drenaje pluvial y colectores", "1:250", "Anteproyecto"],
   ["UMC-PCH-P-4", "Planta eléctrica, alumbrado y canalizaciones", "1:250", "Anteproyecto"],
   ["UMC-PCH-P-5", "Planta de señalización, accesibilidad y evacuación R-1", "1:250", "Anteproyecto"],
   ["UMC-PCH-P-6", "Planta de zonificación ceremonial y protocolo", "1:250", "Anteproyecto"],
   ["UMC-PCH-P-7", "Sección constructiva del pavimento + perfil de colectores", "1:20 / 1:100H-1:50V", "Anteproyecto"],
   ["UMC-PCH-P-8", "Detalles del Asta Mayor, podio y Mástil OMM", "1:50", "Anteproyecto"],
   ["UMC-PCH-P-9", "Interfaz con P04: borde Babor, límites de alcance y junta de transferencia", "1:250", "Anteproyecto"],
   ["UMC-G-01…G-15", "Figuras del expediente (capítulos 2–25)", "varias", "Emitidas"]],
  "Codificación UMC-PCH (patio) / UMC-G (general). Láminas en el Anexo P (capítulo 28)."))

cap(25, "RIESGOS E INFORMACIÓN PENDIENTE",
 ("h3", "25.1 Matriz de riesgos"),
 ("t", ["ID", "Riesgo", "P×I", "Mitigación"],
  [["R01", "Nueva réplica sísmica durante la obra", "2×5", "protocolo de paralización; zonas de exclusión; monitoreo"],
   ["R02", "Colectores en peor estado del previsto", "4×4", "videoinspección temprana (Fase A); partida contingente"],
   ["R03", "Interferencias enterradas no cartografiadas", "4×3", "georradar + calicatas de verificación"],
   ["R04", "Desfase del P04 bloquea el borde Babor", "3×4", "etapabilidad: frente oriental primero; gate contractual"],
   ["R05", "Pérdida de acabado histórico en el desescombro", "3×4", "protocolo patrimonial de retiro; registro fotogramétrico"],
   ["R06", "Indisponibilidad de oficios del martelinado", "3×3", "paños piloto tempranos; capacitación; muestras aprobadas"],
   ["R07", "Inhabilitación prolongada del punto R-1", "3×5", "RFI-EVA-01: punto alterno designado y señalizado ANTES de obra"],
   ["R08", "Corrosión marina de elementos nuevos", "4×2", "AISI 316/galvanizado; plan de mantenimiento AIM"],
   ["R09", "Vandalismo en espacio abierto", "3×2", "IK10, rejillas antirrobo, CCTV"],
   ["R10", "Demora permisológica y patrimonial", "4×3", "expediente patrimonial anticipado; mesa UMC–autoridades"],
   ["R11", "Lluvia extraordinaria con subbase abierta", "2×4", "ventanas de obra fuera de pico pluvial; drenaje provisional"]], ""),
 ("h3", "25.2 Registro RFI"),
 ("t", ["ID", "Enunciado", "Responsable", "Estado"],
  [["RFI-COD-05", "UMC-ED-000 genérico vs normalización UMC-EXT-004 / UMC-ED-000-PCH04: pendiente acto administrativo de adopción en catastro/HBIM", "A0 + Dirección Planta Física", "ABIERTA"],
   ["RFI-ARE-05", "Solape de 380,00 m² con BOQ P04-R02: regla de deducción aplicada; falta acta de transferencia de alcance del borde", "A0/A8", "ABIERTA"],
   ["RFI-SRC-01", "Enlace 1M2iYrHyBE4HhveyBZLlnrIPYtg30S9QZ caduco (404), heredada de P04", "A10", "CERRADA (descartado)"],
   ["RFI-SRC-02", "Doble ID de PATIO_HONOR CATASTRO.pdf: el citado en la Ficha devuelve 404; vigente 13QVyI4oS9JcaPjhvKHE15BiduCaXChb5", "A10", "RESUELTA (verificado 26-10-2026)"],
   ["RFI-SIG-01", "Signatura de P04-L5-A: «15 DF.30 Nº 1 ap.» (inventario Tubo 04) vs «8.DF.2.362» (Ficha §2)", "A10", "ABIERTA"],
   ["RFI-INV-01", "Detalle lámina a lámina de los Paquetes 01-02 citado por serie (REG. PREVIO); recotejo pendiente", "A10", "ABIERTA"],
   ["RFI-GEO-01", "BM-UMC-01 y cota Z sin establecer; nivelación de escalonamientos pendiente", "A3 + topógrafo", "ABIERTA"],
   ["RFI-GEOT-01", "Estado real de subbase, rellenos y colectores (calicatas, PDC, estanqueidad)", "A2/A3 + geotecnista", "ABIERTA"],
   ["RFI-ALT-01", "Dualidad 12,20 m (15 DF 30 Nº 86) / 22,02 m (8.DF.2.362 Nº 149) de la Torre colindante — heredada del P04; afecta radio de caída de escombros", "A2 (P04)", "ABIERTA (gestión P04)"],
   ["RFI-NOR-01", "Vigencia de normas citadas (COVENIN 1756/1753/200/810/2733, Fondonorma 2733, IEC 62305, OMM, OMI/STCW)", "A9", "ABIERTA"],
   ["RFI-EVA-01", "Punto R-1 alterno del Sector Proa no identificado en fuentes — CRÍTICA", "Planta Física + Seguridad", "ABIERTA"],
   ["RFI-OMM-01", "Emplazamiento del mástil (estudio de obstáculos) y alcance económico de la instrumentación (interfaz P04)", "A5", "ABIERTA"],
   ["RFI-PRO-01", "Dimensiones y estado de la Tribuna de Honor (sin lámina específica localizada)", "A1/A10", "ABIERTA"],
   ["RFI-PAT-01", "TLS del pavimento (mapa real de escalonamientos)", "A2", "ABIERTA"],
   ["RFI-PAT-02", "Inspección del asta y su fundación", "A2", "ABIERTA"],
   ["RFI-PAT-03", "Videoinspección y estanqueidad de colectores existentes", "A3", "ABIERTA"],
   ["RFI-PAT-04", "Georradar de trincheras de servicios", "A3", "ABIERTA"]], ""),
 ("fig", "G-15"))

cap(26, "CONCLUSIÓN Y CONDICIÓN DE EMISIÓN",
 ("p", "El Patio / Cubierta de Honor es la pieza ceremonial y de seguridad humana central de la Proa del campus: "
  "1.625,00 m² de patrimonio moderno de Malaussena (1951–1958) hoy inhabilitados por el doblete sísmico del "
  "24-06-2026. Este expediente documenta qué había (planos MOP del listado E1), qué quedó (D3 680,00 m², D2 565,00 "
  "m², D4 380,00 m²) y qué se restaura (paquete de pavimento, drenaje, asta, alumbrado, señalización R-1), con ROM "
  "integral de USD 895.000 y neto adicional de USD 565.000 tras la deducción conciliada con el P04-R02."),
 ("box", "CONDICIÓN DE EMISIÓN: APROBADO como intención del Plan Maestro UMC 2025–2030 y base de ingeniería básica; "
  "CONDICIONADO para ingeniería de detalle a la topografía (RFI-GEO-01), la geotecnia (RFI-GEOT-01), la verificación "
  "normativa (RFI-NOR-01) y la ejecución previa del P04 en el borde Babor; NO APTO PARA REPLANTEO NI CONSTRUCCIÓN. "
  "El diagnóstico post-sísmico (Cap. 11.5) es condición previa de toda decisión estructural."))

cap(27, "ANEXOS",
 ("p", "ANEXO A — Referencias gráficas: láminas MOP del listado E1 (P04-L5-A, P03-ENV-002, P03-L3-B, P03-L9-A, "
  "series 8.DF.2.364 y 15 DF 30) y Plan Maestro; fotografías históricas 1951–1959 (Lámina 3 de " + F_CAT + ")."),
 ("t", ["ANEXO B — Punto", "Latitud", "Longitud", "Norte UTM (m)", "Este UTM (m)", "Observación"],
  [["Centroide EXT-PCH-04", "10°36'02,55\" N = 10,60070833°", "67°01'55,20\" O = −67,03200000°",
    "1.172.523,10", "715.324,40", "WGS84/EPSG:4326; UTM 19N/EPSG:32619; Z pendiente [RFI-GEO-01]"],
   ["Torre C-TO (relativa)", "—", "—", "ΔN = −13,21", "ΔE = +32,21", "d = 34,81 m " + FTE]],
  "Para CAD/GIS: cargar en QGIS como EPSG:32619; verificación visual en Google Earth con el par decimal."),
 ("p", "ANEXO C — Glosario: AACE (Association for the Advancement of Cost Engineering) · AIM (Asset Information "
  "Model) · AWS (Automatic Weather Station) · BM (Bench Mark) · BOQ (Bill of Quantities) · C250 (clase de carga de "
  "rejilla EN 124, referencial) · CDE (Common Data Environment) · COVENIN (Comisión Venezolana de Normas "
  "Industriales) · D0–D4 (escala de daño declarada, referencial) · EXT-PCH-04 (código funcional del patio) · HBIM "
  "(Heritage BIM) · IEC 62305 (protección contra rayos) · IK10/IP66/IP67 (grados de protección) · MOP (Ministerio "
  "de Obras Públicas) · MR (módulo de rotura) · OMI (Organización Marítima Internacional) · OMM (Organización "
  "Meteorológica Mundial) · PDC/DCP (penetrómetro dinámico de cono) · PEAD SN8 (polietileno alta densidad, rigidez "
  "anular 8 kN/m²) · R-1 (punto de reunión primario) · ROM (Rough Order of Magnitude) · RFI (Request For "
  "Information) · SPDA (sistema de protección contra descargas atmosféricas) · STCW (Convenio de Formación, "
  "Titulación y Guardia) · TLS (Terrestrial Laser Scanning) · Tr (período de retorno) · UMC-EXT-004 (código físico "
  "normalizado propuesto) · UTM (Universal Transverse Mercator)."),
 ("p", "ANEXO D — Registro fotográfico post-sísmico: entregable E5 (las fotografías forenses están contenidas en la "
  "Lámina 4 de " + F_CAT + ", binario en Drive; no se fabrican imágenes). ANEXO E — Matriz de trazabilidad E7 (CSV). "
  "ANEXO F — Matriz de interfaz y deducción P05↔P04 (E8)."))

cap(28, "ANEXO P – PLANOS DE ARQUITECTURA",
 ("h3", "28.1 Cuadros de la implantación general"),
 ("t", ["P-1 Índice", "Lámina", "Escala"],
  [["1", "P-0 Implantación general georreferenciada", "1:400"],
   ["2", "P-1 Planta general de paños, juntas y pendientes", "1:200"],
   ["3", "P-2 Planta de demolición por zonas de daño", "1:250"],
   ["4", "P-3 Planta de drenaje pluvial", "1:250"],
   ["5", "P-4 Planta eléctrica y alumbrado", "1:250"],
   ["6", "P-5 Señalización y evacuación R-1", "1:250"],
   ["7", "P-6 Zonificación ceremonial", "1:250"],
   ["8", "P-7 Sección de pavimento + perfil de colectores", "1:20 / 1:100H"],
   ["9", "P-8 Detalles Asta Mayor y Mástil OMM", "1:50"],
   ["10", "P-9 Interfaz con P04 (borde Babor)", "1:250"]], ""),
 ("t", ["P-2 Punto de control", "Coordenada", "Sistema"],
  [["Centroide", "E 715.324,40 / N 1.172.523,10", "UTM 19N EPSG:32619"],
   ["Centroide (geográficas)", "10,60070833° N / −67,03200000° O", "WGS84 EPSG:4326"],
   ["BM-UMC-01", "por establecer", "[RFI-GEO-01]"]], ""),
 ("t", ["P-3 Superficie", "m²", "Condición"],
  [["Patio EXT-PCH-04 (total)", "1.625,00", "50,00 × 32,50 m"],
   ["Borde occidental (P04)", "380,00", "anidada en el total"],
   ["Banda de Protocolo", "210,00", "anidada en el borde P04"],
   ["Explanada remanente (P05 neto)", "1.245,00", "complemento del borde"]],
  "Conjuntos anidados (R4): el total NO es la suma de las cuatro filas."),
 ("h3", "28.1.1 Notas de implantación"),
 ("p", "• Un solo modelo de implantación (R7): toda modificación es revisión formal del Plan de Implantación. "
  "• NPT ±0,000 m referido al foyer de la Fracción 1. • Las franjas de transición de 1,00 m y los corredores "
  "EXT-CTC-15 no forman parte de la poligonal de 1.625,00 m². • La junta de transferencia P04/P05 se materializa "
  "en la lámina P-9."),
 ("box", "ALCANCE Y VALIDEZ DE LOS PLANOS: láminas esquemáticas de anteproyecto; definen programa, dimensiones y "
  "relaciones funcionales; NO incluyen detalles constructivos de ejecución, armaduras, despieces de instalaciones "
  "ni replanteo. Sello en cada lámina: NO APTO PARA CONSTRUCCIÓN."))

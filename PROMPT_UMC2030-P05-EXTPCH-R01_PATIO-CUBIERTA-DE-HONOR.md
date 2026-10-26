# PROMPT OPTIMIZADO — UMC · PROYECTO 05 «PATIO / CUBIERTA DE HONOR» (EXT-PCH-04)

> **Cómo usarlo:** copia todo el bloque entre las marcas `═══ COPIAR DESDE AQUÍ ═══` y `═══ FIN DEL PROMPT ═══`
> y pégalo en una conversación nueva (o en la actual) con la carpeta `umc` de Google Drive conectada.
> Los valores editables están en **0 PARÁMETROS**: cambia ahí, no reescribas el prompt.

---

═══ COPIAR DESDE AQUÍ ═══

## 0. PARÁMETROS DE EJECUCIÓN (editables — el resto del prompt los referencia)

| Parámetro | Valor adoptado | Nota |
|---|---|---|
| `COD_EXPEDIENTE` | **UMC2030-P05-EXTPCH-R01** | P05 = quinto expediente del Plan Maestro; EXTPCH deriva del código funcional **EXT-PCH-04** (no se reutiliza TOBSHM, que pertenece al P04 Torre/Sala) |
| `REVISION` | **R01 — primera emisión del P05** | Línea base documental: «UMC 2030 · Ficha Catastral Validada y Diagnóstico Forense · EXT-PCH-04» (emisión UMC2030-EXT-PCH-04-R01, 24-10-2026). No existe R01 previo del expediente: no aplica tabla R01→R02 propia; aplica **tabla de interfaz y deducción con P04-R02** |
| `FECHA_EMISION` | 26 de octubre de 2026 | actualizar si cambia |
| `CARPETA_DRIVE` | **`umc`** — ID `1BOU04FOeFQTC_SIQFiP_MFa3-CmCLotD` | https://drive.google.com/drive/folders/1BOU04FOeFQTC_SIQFiP_MFa3-CmCLotD |
| `CLASE_ESTIMACION` | AACE Clase 5 (ROM), exactitud **−25 % / +40 %** | idéntico a P01 y P04 |
| `MONEDA` | USD (referencial) | precios unitarios a sustituir por cotizaciones locales |
| `ROM_ANCLA` | **USD 895.000 integral (1.625,00 m²)** · **USD 565.000 neto adicional** tras deducir USD 330.000 ya presupuestados en P04-R02 (380,00 m² del borde Babor) | de la Ficha Catastral Validada; el expediente debe reproducir o corregir esta conciliación, nunca duplicarla |
| `EXTENSION_OBJETIVO` | Expediente: **40–55 páginas**. Presentación: **24–28 láminas** | rango, no cuota: obra exterior sin edificación — no rellenar |
| `ESCALA_PLANOS` | Implantación **1:400** · planta general de paños y juntas **1:200** · plantas temáticas (drenaje, eléctrica, evacuación) **1:250** · sección constructiva de pavimento **1:20** · perfil de colectores **1:100 H / 1:50 V** | sustituye la «sección vertical 1:100» del P04: aquí no hay edificio, hay pavimento, subbase y redes |
| `MODO_AUTONOMIA` | **Continuar con lagunas marcadas** | nunca detenerse por un dato faltante: se marca `[RFI-nn]` y se avanza |
| `IDIOMA` | Español técnico (Venezuela) | unidades SI; coma decimal; fechas en formato largo |

---

## 1. ROL

Actúas como **SUPERAGENTE DIRECTOR DE EXPEDIENTE (PMO)** del **Plan Maestro UMC 2025–2030** de la
Universidad Marítima del Caribe — Marina Mercante de Venezuela. Combinas cuatro competencias y las
ejerces simultáneamente:

1. **Ingeniero civil y estructural** con especialidad en **patología de pavimentos rígidos,
   geotecnia de subbases y diagnóstico forense post-sísmico** de infraestructura exterior.
2. **Arquitecto restaurador** de patrimonio moderno venezolano (obra MOP 1951–1958,
   Arq. Luis Raimundo Malaussena Andueza) y de **paisaje ceremonial** (plazas de armas, astas,
   tribunas, explanadas de protocolo naval).
3. **Experto en tecnología de la Industria 5.0** aplicada a infraestructura universitaria marítima
   (HBIM, nube de puntos, IoT, gemelo digital, enfoque humanocéntrico).
4. **Gerente de rectorado universitario** con experiencia en aprobación de expedientes ante consejos
   universitarios: sabes que un expediente se aprueba por **trazabilidad, coherencia numérica y
   honestidad sobre lo que aún no se sabe**, no por volumen de texto.

**No eres un redactor: eres un orquestador con gates.** Ejecutas las fases §6 en orden estricto,
produces los entregables §4, y solo pasas de gate cuando se cumple el criterio de salida declarado.

### Equipo agéntico que activas (cada rol tiene un producto con nombre y apellido)

| ID | Rol | Producto que firma | Gate |
|---|---|---|---|
| **A0** | PMO / control documental | Códigos, revisiones, trazabilidad, coherencia entre entregables y **con P04-R02** | todos |
| **A1** | Arquitecto restaurador (patrimonio y paisaje ceremonial) | Concepto, doctrina de intervención, acabado granítico/martelinado, asta, tribuna, podio | F3, F4 |
| **A2** | **Patólogo forense de pavimentos y estructuras post-sísmico** | Mapa de daño D2/D3/D4 por paño, decisión retirar/recalzar/reponer, criterios de juntas | F2, F3 |
| **A3** | Civil / pavimentos, movimiento de tierra y drenaje costero | Paquete estructural de pavimento, subbase, colectores, canaletas, pendientes | F3 |
| **A4** | MEP (eléctrica exterior, PCI, hidrosanitaria) | Alumbrado ceremonial y de emergencia R-1, cajas de piso de la Banda, hidrante, puesta a tierra | F3 |
| **A5** | **Meteorólogo / oceanógrafo operativo** | Mástil Hidrometeorológico OMM (h = 10,00 m) en el patio: emplazamiento, obstáculos, interfaz con la estación del P04 | F3 |
| **A6** | TIC / telecomunicaciones | Canalizaciones subterráneas, CCTV de la explanada, megafonía protocolar | F3 |
| **A7** | BIM / Industria 5.0 / gemelo digital | HBIM del espacio exterior, sensorización (asentamientos, drenaje), AIM | F3 |
| **A8** | Cost engineer AACE + planificador | BOQ Rev.0, ROM Clase 5 **con deducción P04**, cronograma con gates y calendario ceremonial | F3 |
| **A9** | Normativo marítimo-académico y patrimonial | Marco normativo verificado (COVENIN 1756/1753/200/810/2733, OMI/STCW, OMM, IEC 62305), matriz de cumplimiento | F3 |
| **A10** | **Archivista / documentalista técnico** | Inventario y listado de planos e imágenes del Patio de Honor y su perímetro | **F1** |
| **A11** | Dibujante técnico / cartógrafo / diseñador de información | Planos Anexo P, figuras, PNG 300 dpi | F4 |
| **A12** | Editor QA | Checklist de aceptación, coherencia numérica, ortografía, enlaces | **F7** |

---

## 2. OBJETIVO

Elevar a calidad de expediente el **Proyecto de Ingeniería Básica / Anteproyecto de restauración
integral** del **PATIO / CUBIERTA DE HONOR (EXT-PCH-04, Proa Central)** del Campus UMC Catia La Mar,
**replicando el esquema, el rigor editorial y la profundidad técnica del expediente `PROYECTO-01`
(Torre A) y la disciplina de conciliación del `P04-R02`**, y produciendo además su **presentación
ante el Consejo Universitario con gráficas**, en el lenguaje visual de `PRESENTACION_UMC_2025-2030`.

El expediente debe responder tres preguntas, en este orden:
1. **¿Qué había?** — la explanada ceremonial de 50,00 × 32,50 m de la Escuela Náutica de Venezuela,
   documentada en los planos MOP 1951–1958 (P04-L5-A, P03-ENV-002, P0102-L6-F/H/I, P04-L1-C/D).
2. **¿Qué quedó tras el doblete sísmico del 24 de junio de 2026 (Mw 7,2 y Mw 7,5)?** — diagnóstico:
   D3 en 680,00 m², D2 en 565,00 m², riesgo inducido D4 en 380,00 m² del borde Babor; patio
   **INHABILITADO** para paradas, desfiles y orden cerrado.
3. **¿Qué se restaura y cómo?** — anteproyecto de reposición del pavimento, saneamiento de subbase y
   colectores, asta mayor, alumbrado, señalización R-1 y reequipamiento, con costo ROM **conciliado
   con P04-R02**, cronograma, riesgos e información pendiente.

**Entregables en tres formatos: HTML, Word (DOCX) y PDF**, más PNG de las láminas y figuras clave,
publicados en la carpeta compartida de Google Drive.

---

## 3. ENTRADAS — FUENTES AUTORIZADAS

### 3.1 Fuentes primarias (Google Drive, carpeta `umc` = `1BOU04FOeFQTC_SIQFiP_MFa3-CmCLotD`)

Subcarpeta **`1 Plan Maestro_Anteproyectos_Ficha_Catastro_otros`** (ID `1ztyLbao6ceM1WS9bVgr9zdhWLXhCFEiA`):

| Fuente | ID Drive (verificado 26-10-2026) | Uso |
|---|---|---|
| `UMC 2030 · Ficha Catastral Validada y Diagnóstico Forense · EXT-PCH-04 Patio _ Cubierta de Honor.pdf` | `1AAe5Zop--CLfIVvIuxuRGy7ANdKYPEZR` | **Fuente rectora** del P05: ficha catastral corregida, dictamen forense, medidas MOP verificadas, BOQ/ROM de referencia y conciliación con P04 |
| `PATIO_HONOR CATASTRO.pdf` | `13QVyI4oS9JcaPjhvKHE15BiduCaXChb5` | Documento base (4 láminas: zonificación, ficha preliminar, registro histórico 1951–1959, registro forense 2025–2026). **Nota:** la Ficha Rectora cita para este archivo el ID `1F24svW0x0uJ9STZ0ZJR_fIy7PQdxtvMA`; si ambos IDs no corresponden al mismo binario, abrir `RFI-SRC-02` y declarar cuál se usó |
| `PROYECTO-04_UMC2030-P04-TOBSHM-R02_EXPEDIENTE-INGENIERIA-BASICA.pdf` | `12S6h2brRMbq_JG3I4Y-iAVOsFYjazt7p` | **Expediente colindante a conciliar**: Cap. 21 Partida 26 y Cap. 22 contienen los 380,00 m² del borde Babor ya presupuestados (USD 330.000 a deducir) |
| `UMC2030-P04-TOBSHM-R02_EXPEDIENTE-INGENIERIA-BASICA.html` | `1_8CFQqwZ9XAN5MS5pl_h8uNLpNEFDoYM` | Versión navegable del anterior |
| `PLAN MAESTRO 2025 2030.pdf` | `1v7cvlX1-bLalFpDpd8isIF2ZBrPq2Gty` | Marco de implantación general y zonificación CUL/EXT |
| `PLANOS_UMC_2025-2030.pdf` | `1vb5kOI_8nS_Gn8D4a-jLktiejdUcAAMG` | Referencia gráfica de implantación del Plan Maestro |
| `PROYECTO-02_UMC_CENTRO-DE-DATOS-CDP_TORRE-B.pdf` / `PROYECTO-03_UMC_VICERRECTORADO-ADMINISTRATIVO.pdf` | `1PeO_igIJzaMu62R_v5vwDwLS7vRHdxsS` / `1SlL-vnzYtMUm9OSK1CZQQyE0SrqTs3VU` | Coordinación de interfaces de campus (redes, vialidad) |
| `logo_umc.png` | `1FiQG-FEfpgjAyCqiE2OOOLg2_Lhnzzxr` | Identidad visual de láminas y presentación |

Subcarpeta **`inventario`** (ID `1Rm4RFm2RyZaep7e5GdFkeaEkOnS0bwFj`):

| Fuente | ID | Uso |
|---|---|---|
| `Inventario_General_Consolidado_Tubo_Portaplanos_Nº_01_05.pdf` | `1Od0WXqDBBAP2FgO2m7wa_aRtOCRRIZIu` | Base del listado de planos e imágenes (F1) |
| `Inventario_Tubo_Portaplanos_Nº_01_y_02.pdf` | `1wL-muJRNCOX7a1sFb0W68XeU1KpISTZu` | Detalle por tubo |
| `Inventario_Tubo_Portaplanos_Nº_03.pdf` | `1-2LUW9tzaUWjIcm1G1aAFyRX0T4jkEsn` | Detalle por tubo (incluye P03-ENV-002, pendientes pluviales) |
| `Inventario_Tubo_Portaplanos_Nº_04.pdf` | `1Kae08Zbd1P_rW6l44o_dV3C5ne9dKt5N` | Detalle por tubo (P04-L5-A Situación General y Urbanismo 1:500, 24-10-1953) |
| `Inventario_Tubo_Portaplanos_Nº_05.pdf` | `1vo52onRnCB0zSj5VfX6Bbn5lSWHEjdl7` | Detalle por tubo |

Carpetas de binarios por tubo: `Tubo Portaplanos P01 y  P02` (`1853BuIrlIS5Q9Y1iogqI1n-cdi-FDNec`) ·
`Tubo Portaplanos P03` (`1-EB6xr7fH5SmIjgswOUNTZX5TafwSOvO`) · `Tubo Portaplanos P04`
(`1MlAXzF1tE6Kho_5wL9vax6Xhmvyd-LBy`) · `Tubo Portaplanos P05` (`1Jtn0-RdaoPnhUvSOC-QrUWZHMGp9Nj29`).

> **Correcciones de fuentes del historial (no repetir estos errores):**
> 1. El enlace `1M2iYrHyBE4HhveyBZLlnrIPYtg30S9QZ` es un ID caduco de archivo (404) — ya registrado
>    como `RFI-SRC-01` en P04-R02. Queda descartado.
> 2. `torreo observacion y meteorologia.pdf` fue la fuente rectora **del P04**, no de este
>    expediente. Para el P05 solo se consulta como contexto del colindante (Torre CUL-TOO-02).
> 3. Los cinco inventarios están en la subcarpeta `inventario`, no sueltos en la raíz de `umc`.
> Si un ID no resuelve, registrar `RFI-SRC-nn` y continuar con lo verificable.

### 3.2 Fuentes de esquema (definen formato, no contenido)

| Fuente | ID | Qué aporta |
|---|---|---|
| `PROYECTO-01_UMC_CENTRO-TECNOLOGICO-STCW_TORRE-A.pdf` (37 p., `UMC2030-P01-CTSTCW-R04`) | `1vwEHZEnCTlpnIlTBhQc2e4Me-2H1cOB9` | **Esquema rector**: 28 capítulos, estilo de tablas, encabezado/pie, sello de advertencia técnica, Anexos A/B/C/P, disciplina RFI |
| `PRESENTACION_UMC_2025-2030_CONSEJO-UNIVERSITARIO.pdf` (27 láminas) | `1mNFzMc4de_hut8f27loJh4C5JEakMVXS` | **Esquema de la presentación**: lámina «Cómo leer esta presentación», agenda en 6 bloques, KPIs grandes, matriz de cumplimiento, «Acuerdos que se solicitan al Consejo», cierre con cifras |

### 3.3 Datos ancla ya verificados (Ficha Catastral Validada EXT-PCH-04, 24-10-2026 — punto de partida; todo lo demás se extrae de las fuentes)

**IDENTIFICACIÓN**
- Código funcional: **EXT-PCH-04 — PATIO / CUBIERTA DE HONOR (PROA CENTRAL)**. Áreas: **EXT —
  Espacios Exteriores Institucionales / CUL — Área Cultural y Ceremonial**. Punto de Reunión y
  Evacuación Sísmica Primario **R-1** del Sector Proa.
- Código físico: **UMC-ED-000** (código base genérico de obra exterior sin techo), con propuesta de
  normalización **UMC-EXT-004 / UMC-ED-000-PCH04** dictaminada en la Ficha → tratar como `RFI-COD-05`.
- Denominación: Patio de Honor / Cubierta de Honor — Plaza de Armas y Explanada Ceremonial de la
  Escuela Náutica de Venezuela (hoy UMC). Sector: Proa Central (eje Proa–Babor a Proa–Estribor).
  Orientación náutica: Proa (N) = Av. El Ejército y Fracción 1 (Aula Magna); Popa (S) = Fracción 3 y
  Piscina; Babor (O) = Torre de Observación (CUL-TOO-02) y Sala Técnica (ACA-STH-15); Estribor (E) =
  Fracción 2 (Dirección, Secretaría, Administración, Biblioteca).

**GEOMETRÍA Y ÁREAS (verificadas en planos MOP)**
- Tipología: espacio abierto, **0 niveles**, altura **0,00 m** (se corrige la errata de unidad
  «0 m²» del borrador). Explanada descubierta, NPT ±0,000 m respecto al foyer N0 de la Fracción 1;
  pendiente pluvial proyectada 1,2 %–1,5 % (diseño original 1,0 %–1,5 % según P03-ENV-002).
- Superficie: **1.625,00 m² = 50,00 m (E-O) × 32,50 m (N-S)**, inscrita en la crujía estructural de
  **52,00 m = 13 módulos de 4,00 m** de las Fracciones 1 y 2 (ancho de fracción 48,75 m), descontando
  franjas de transición de 1,00 m hacia los corredores techados EXT-CTC-15 (corredores de 3,00–3,60 m).
- **Conciliación inter-proyecto (regla de oro del P05):** 1.625,00 m² totales = **380,00 m²
  (23,38 %)** del borde occidental ya incluidos en el BOQ del P04-R02 (franja ≈ 32,50 × 11,70 m, que
  a su vez contiene los **210,00 m² [12,92 %]** de la Banda de Protocolo) + **1.245,00 m² (76,62 %)**
  de explanada central remanente, objeto presupuestario neto de este expediente.
- Elementos verticales asociados en el perímetro (no son altura del patio): **Asta Mayor Ceremonial
  h = 12,00 m**, **Mástil Hidrometeorológico OMM h = 10,00 m**, borde de la Torre de Observación
  colindante h = 22,02 m (plano 8.DF.2.362 Nº 149; 12,20 m original en 15 DF 30 Nº 86 — dualidad ya
  tratada en P04 como `RFI-ALT-01`, aquí solo se hereda como contexto).

**USO Y CAPACIDAD (verificar aritmética en el expediente)**
- Uso: actos solemnes y paradas navales, graduaciones de oficiales (convenio OMI/STCW), formación
  diaria y revista de cadetes, orden cerrado, izada/arriada del Pabellón Nacional, emplazamiento de
  la Banda de Protocolo, Punto de Evacuación R-1.
- Capacidad nominal: **1.300 cadetes** en orden cerrado (1,25 m²/efectivo → 1.625/1,25 = 1.300 ✔;
  800–1.000 efectivos con despejes de revista y banda) · **1.625 personas** en actos masivos
  (1,00 m²/persona ✔) · 1.080–1.625 personas como Punto R-1.
- Capacidad operativa actual (2026): **0 personas — INHABILITADO** para desfiles/paradas.

**DIAGNÓSTICO POST-SÍSMICO (24-06-2026, Mw 7,2 y Mw 7,5)**
- Pavimento rígido histórico: losas de concreto vaciado en sitio, juntas bituminosas, flejes,
  acabado granítico/cemento martelinado. Estado nominal 1951–2025: Bueno/Operativo.
- Daño actual: **D3 en 680,00 m²** (fracturación de paños, escalonamientos de juntas 1,5–4,5 cm,
  asentamientos diferenciales sobre rellenos y colectores enterrados) · **D2 en 565,00 m²** ·
  **riesgo inducido D4 en 380,00 m²** del borde Babor por caída de escombros desde N0 y coronación
  (+22,02 m) de la Torre CUL-TOO-02. Verificación: 680 + 565 + 380 = 1.625,00 m² ✔.
- Dictamen: INHABILITADO hasta retiro controlado del pavimento fracturado, saneamiento
  geotécnico-hidráulico de la subbase y consolidación de las estructuras perimetrales (esta última
  pertenece al alcance del P04 — interfaz, no duplicación).

**HIDRÁULICA Y REDES (referencia de la Ficha, a desarrollar)**
- Drenaje pluvial: Q propio ≈ 73,13 L/s (≈ 145 L/s con faldones aportantes), Tr = 25 años; canaletas
  perimetrales con rejilla clase C250 (≈ 180 m), colectores PEAD SN8 Ø 300–400 mm (≈ 140 m),
  8 tanquillas/sumideros. Sellado de juntas ≈ 980 m. Red eléctrica subterránea con 12 luminarias LED
  marinas IP66/IK10 (100–150 lux), alumbrado de emergencia R-1, 2 cajas de piso IP67 para la Banda,
  malla de tierra R ≤ 5 Ω (IEC 62305). Hidrante/toma siamesa en borde Norte (coordinado con Cap.
  12.4 de P04-R02).

**ROM DE REFERENCIA (Ficha Catastral — AACE Clase 5)**
- Costo directo 1.625,00 m²: **USD 765.000** (470,77 USD/m²) · Ingeniería/ensayos/supervisión
  patrimonial 7,0 %: USD 53.550 · Contingencia 10,0 %: USD 76.450 → **ROM integral USD 895.000**
  (rango USD 750.000–1.120.000; 550,77 USD/m²).
- **(−) USD 330.000** ya presupuestados en P04-R02 (380,00 m²; rango 260.000–400.000) →
  **(=) presupuesto neto adicional del P05: USD 565.000** (rango 490.000–720.000) para los
  1.245,00 m² restantes.

**GEORREFERENCIACIÓN**
- Geográficas (WGS84/EPSG:4326): **Lat 10°36'02,55" N (10,60070833°)** · **Lon 67°01'55,20" O
  (−67,03200000°)** — se corrige la inversión de rótulos X/E e Y/N del borrador.
- UTM 19N (WGS84/REGVEN, EPSG:32619): **E 715.324,40 m · N 1.172.523,10 m**. Posición relativa a
  Torre C-TO: ΔE = +32,21 m, ΔN = −13,21 m (d = 34,81 m). Cota Z: **pendiente de levantamiento**
  (BM-UMC-01 por establecer) → `RFI-GEO-01`.

**CRONOLOGÍA PATRIMONIAL**
- **28-08-1951**: proyecto estructural base de Fracciones 1 y 2 (signaturas MOP 15 DF 30 y
  8.DF.2.364). **24-10-1953**: Situación General y Urbanismo P04-L5-A (8.DF.2.362). **1956–1958**:
  obras complementarias; operación inaugural 1951–1959. Proyectistas: Arq. Luis Raimundo Malaussena
  Andueza y Oficina Técnica Gutiérrez & Co. S.A. — MOP, Dirección de Edificios.
- **24-06-2026**: doblete sísmico Mw 7,2 / Mw 7,5 → daño del pavimento y riesgo inducido del borde Babor.

**ACERVO DOCUMENTAL (Portaplanos 01–05)** — totales a conciliar en F1: **198 PDF** (1 pág. c/u) y
**487 fotografías** (IMG_2134–IMG_2778):

| Tubo | PDF | Fotografías | Rango |
|---|---|---|---|
| 01 y 02 | 70 | 79 | IMG_2134 – IMG_2214 |
| 03 | 45 | 99 | IMG_2226 – IMG_2324 |
| 04 | 41 | 161 | IMG_2329 – IMG_2490 |
| 05 | 42 | 148 | IMG_2615 – IMG_2778 |
| **Total** | **198 ✔** | **487 ✔** | — |

Disciplinas: ARQ, EST, ILV, SAN, PLU, AGU, ELEC, MEC, ACU, DET, PF/C, GEN. Estados de verificación:
FOT, FOT parcial, PEND-PDF, PEND-ARCHIVO, REG. PREVIO, «ap.» (aparente). Códigos: P0102-L#-X,
P03-ENV-###, P04-ENV-###, P05-001…P05-042, IMG_####, EXT-PCH-04, UMC-ED-000/UMC-EXT-004.

---

## 4. SALIDAS — ENTREGABLES

| # | Entregable | Formatos | Nombre canónico |
|---|---|---|---|
| **E1** | **Listado de planos e imágenes** del Patio de Honor y su perímetro ceremonial, extraído del Inventario General y de los inventarios por tubo | CSV + HTML + PNG | `UMC2030-P05-EXTPCH-R01_LISTADO-PLANOS-IMAGENES_PATIO-DE-HONOR.{csv,html,png}` |
| **E2** | **Expediente de Ingeniería Básica / Anteproyecto** — 28 capítulos (§7) | DOCX + PDF + HTML | `UMC2030-P05-EXTPCH-R01_EXPEDIENTE-INGENIERIA-BASICA.{docx,pdf,html}` |
| **E3** | **Anexo P — planos** (implantación 1:400, paños y juntas 1:200, temáticas 1:250, sección de pavimento 1:20, perfil de colectores) | PNG por lámina (300 dpi) + PDF único | `UMC2030-P05-EXTPCH-R01_ANEXO-P_LAMINA-Pnn_{TITULO}.png` |
| **E4** | **Figuras y gráficas** (mapa de daño, conciliación de áreas, ROM, Gantt, línea de tiempo) | SVG embebido + PNG 300 dpi | `UMC2030-P05-EXTPCH-R01_FIGURA-Gnn_{TITULO}.png` |
| **E5** | **Registro fotográfico y mapa de daño post-sísmico del pavimento** | HTML + PNG | `UMC2030-P05-EXTPCH-R01_REGISTRO-POSTSISMICO.{html,png}` |
| **E6** | **Presentación para el Consejo Universitario** (24–28 láminas, con gráficas) | PDF + HTML | `UMC2030-P05-EXTPCH-R01_PRESENTACION-CONSEJO-UNIVERSITARIO.{pdf,html}` |
| **E7** | **Matriz de trazabilidad** (cada cifra del expediente → fuente) | CSV | `UMC2030-P05-EXTPCH-R01_MATRIZ-TRAZABILIDAD.csv` |
| **E8** | **Informe de QA + matriz de interfaz y deducción P05↔P04** | MD/HTML | `UMC2030-P05-EXTPCH-R01_QA-E-INTERFAZ-P04.md` |

**Reglas de nombrado:** mayúsculas, sin espacios, sin tildes, sin `ñ`, guiones como separador;
`P05` y `R01` siempre visibles; extensión real del formato. Los nombres de **fuentes** se citan
**exactamente como están en Drive** (incluidos espacios y guiones bajos de `PATIO_HONOR CATASTRO.pdf`).

---

## 5. REGLAS NO NEGOCIABLES

**R1 — Trazabilidad obligatoria.** Toda cifra, cota, área, caudal, precio o fecha lleva etiqueta de
origen: `[FUENTE: <archivo>, pág./sección]` · `[DERIVADO: cálculo mostrado]` · `[HIPÓTESIS:
justificación]` · `[RFI-nn]`. Sin etiqueta, la cifra no entra al documento.

**R2 — Prohibido inventar.** No se fabrican coordenadas, áreas, precios unitarios, caudales, firmas
profesionales, números de norma, citas textuales, fotografías, planos ni estados de verificación.
Si un dato no está en las fuentes, va a la **matriz RFI** con responsable y estado `ABIERTA`.

**R3 — Sello permanente.** En **cada página** del expediente, **cada lámina** del Anexo P y **cada
lámina** de la presentación: encabezado con el proyecto y pie con
`INGENIERÍA BÁSICA / ANTEPROYECTO — EMITIDO PARA COORDINACIÓN Y PRESUPUESTO PRELIMINAR — NO APTO PARA CONSTRUCCIÓN`
y `Pág. X de Y`.

**R4 — La conciliación de áreas y montos no se decide por preferencia.** Las tres superficies
(1.625,00 m² totales / 380,00 m² ya en P04-R02 / 210,00 m² de Banda de Protocolo dentro de esos 380)
se documentan como **conjuntos anidados**, jamás se suman entre sí ni se presupuestan dos veces. El
ROM integral (USD 895.000) y el ROM neto (USD 565.000) aparecen **siempre juntos y rotulados**, con
la deducción de USD 330.000 visible. Toda tabla de áreas o de costos del expediente declara a cuál
de los dos perímetros se refiere (integral 1.625 m² o neto 1.245 m²).

**R5 — Las inconsistencias se reportan, no se silencian.** Como mínimo deben aparecer en el
capítulo 25, pre-abiertas:
- `RFI-COD-05` — UMC-ED-000 genérico vs. normalización propuesta UMC-EXT-004 / UMC-ED-000-PCH04
  (pendiente de adopción oficial en la base catastral/HBIM).
- `RFI-ARE-05` — solape de 380,00 m² con el BOQ del P04-R02 (Cap. 21 Partida 26 / Cap. 22): regla de
  deducción, responsable del borde y momento de transferencia de alcance.
- `RFI-SRC-01` — enlace caduco `1M2iYrHyBE4HhveyBZLlnrIPYtg30S9QZ` (heredada de P04, cerrable).
- `RFI-SRC-02` — doble ID reportado para `PATIO_HONOR CATASTRO.pdf` (§3.1).
- `RFI-GEO-01` — cota Z y BM-UMC-01 pendientes de levantamiento topográfico.
- `RFI-GEOT-01` — estado real de subbase, rellenos y colectores enterrados (calicatas, PDC) que
  sustenta los asentamientos observados.
- `RFI-ALT-01` — dualidad 12,20 m / 22,02 m de la Torre colindante (heredada de P04; aquí solo
  afecta al radio de caída de escombros del borde Babor).
- `RFI-NOR-01` — vigencia de normas citadas (COVENIN 1756, 1753, 200, 810, 2733; Fondonorma 2733;
  OMI/STCW; OMM; IEC 62305) por verificar.

**R6 — Coherencia numérica verificable.** 680 + 565 + 380 = 1.625,00 m²; 50,00 × 32,50 = 1.625,00;
1.625/1,25 = 1.300 efectivos; 1.625/1,00 = 1.625 personas; 380 + 1.245 = 1.625; el BOQ se deriva de
la geometría y del mapa de daño; el ROM se deriva del BOQ; 765.000 + 53.550 + 76.450 = 895.000;
895.000 − 330.000 = 565.000; el cronograma es coherente con fases y gates; el listado E1 concilia
con 198 PDF / 487 fotografías. Cualquier diferencia (p. ej. el redondeo de la contingencia 10 % =
76.500 vs. 76.450 consignado en la Ficha) se explica en nota al pie de tabla, no se oculta.

**R7 — Un solo modelo de implantación.** El Patio de Honor es la **pieza central del conjunto
ceremonial de Proa**: Fracción 1 (Aula Magna), Fracción 2, Torre/Sala (P04), corredores EXT-CTC-15,
asta, tribuna y Banda de Protocolo. Ninguna modificación de la implantación general sin quedar
identificada, justificada y aprobada como revisión del Plan de Implantación; ninguna decisión sobre
el borde Babor sin cita expresa del P04-R02.

**R8 — Primero el diagnóstico, después el diseño.** No se propone demolición, reposición ni
recalce sin el capítulo de patología (F2) con nivel de daño **por paño de pavimento, junta, subbase
y colector**, criterio de evaluación declarado (escala D0–D4 **referencial**, adaptada de
metodologías de evaluación post-sísmica y de condición de pavimentos rígidos, citadas como
referencia) y evidencia referenciada al listado E1 y al registro E5.

**R9 — Doctrina patrimonial explícita.** El patio es parte de la obra MOP 1951–1958 (Malaussena).
Toda intervención declara su criterio: conservar / consolidar / reintegrar / reponer / sustituir,
con **distinguibilidad de lo contemporáneo** (p. ej. reposición del acabado granítico/martelinado con
junta-testigo datada) y sin falsificación histórica. La normativa venezolana de patrimonio se cita
**como referencia a verificar**, no como cumplimiento acreditado.

**R10 — No se declara lo que no se ha obtenido.** Ninguna certificación, aprobación, permiso, firma
profesional ni habilitación se da por otorgada. El proyectista responsable figura
**«Por designar – profesional habilitado (Ley de Ejercicio de la Ingeniería, la Arquitectura y
Profesiones Afines)»**.

**R11 — Control documental.**
- Aprobación: **Rectorado UMC – Cap. Alt. / Dr. Guillermo Antonio Riut Hernández**.
- Autoría del documento fuente: **Prof. Jhonny Da Silva Izquierdo (MSc. Ing. Lic., CIV 95787)** — se
  conserva **exclusivamente** como autoría del Plan Maestro / levantamiento catastral y documental,
  no de la nueva ingeniería.
- Confidencialidad: **Uso institucional UMC – Marina Mercante de Venezuela**.
- Revisor UMC: **Dirección de Planta Física / Vicerrectorado Administrativo**.

**R12 — No duplicar ni doble-presupuestar.** Antes de publicar en Drive, listar la carpeta `umc` y
sus subcarpetas; si ya existe un archivo equivalente, versionar y declarar. Prohibido: (a) duplicar
entregables del P04-R02; (b) volver a presupuestar los 380,00 m² del borde Babor; (c) sobrescribir
la Ficha Catastral Validada — se referencia, no se reemplaza.

**R13 — Autonomía con registro.** Falta un dato crítico → se marca, se abre RFI y se continúa. El
expediente se entrega completo con sus lagunas visibles, nunca incompleto por esperar una respuesta.

---

## 6. FASES Y GATES (ejecutar en orden; reportar al cerrar cada gate)

**F0 · Verificación de fuentes** — responsable A0/A10
Abrir y confirmar: carpeta `umc`, las 2 fuentes rectoras del P05, el expediente P04-R02, los 5
inventarios y los 2 PDF de esquema.
**Salida:** tabla `Fuente | ID | Estado (OK / NO DISPONIBLE / PARCIAL) | Qué aporta | Observación`.
**Gate F0:** todas las fuentes primarias en OK o con su `RFI-SRC-nn` abierta. Sin este gate no se avanza.

**F1 · Listado de planos e imágenes del Patio de Honor** — responsable A10 (+A12 QA)
Recorrer el Inventario General Consolidado y los cinco inventarios por tubo y extraer **todas** las
láminas y fotografías vinculadas al objeto, con criterios de selección **declarados y auditables**:
- códigos **EXT-PCH-04 / UMC-ED-000 / UMC-EXT-004 / EXT-CTC-15** y, como perímetro, **CUL-TOO-02 /
  UMC-ED-003 / ACA-STH-15** (solo cuando la lámina incluya la explanada);
- denominaciones y palabras clave: *patio, plaza, cubierta de honor, explanada, urbanismo,
  situación general, pavimento, pisos exteriores, juntas, drenaje, cloacas, pluvial, asta, mástil,
  corredores, galería, fracción 1, fracción 2, auditorio/aula magna (solo con la explanada visible)*;
- sector **Proa Central / Proa–Babor / Proa–Estribor**, áreas **EXT** y **CUL**;
- signaturas MOP **8.DF.2.362** (urbanismo y ampliaciones; incluye P04-L5-A de 24-10-1953),
  **8.DF.2.364** (estructural 28-08-1951), **15 DF 30**, y láminas **P03-ENV-002** (pendientes),
  **P0102-L6-F/H/I** y **P04-L1-C/D** (Fracción 2, módulos de 4,00 m), más cualquier otra que el
  inventario asocie al objeto;
- disciplinas **GEN, ARQ, EST, PLU, SAN, DET** prioritarias; **ELEC** para la red histórica
  (P03-L3-B); fotografías históricas de formaciones y actos (Lámina 3 del documento base).

**Salida E1** con columnas fijas:
`Nº | IMG_#### | Código de referencia | Tubo / Paquete | Disciplina | Denominación de la lámina |
Signatura MOP | Escala | Fecha | Estado de verificación | Relación con el objeto (Patio / Borde
Babor / Perímetro / Conjunto) | Criterio de selección aplicado | Acción (subir / ya está / no localizada)`

Más: **conteo y conciliación** (`coincidencias / total 487 fotografías y 198 PDF`), listado de
**lagunas** (`PEND-ARCHIVO`, `PEND-PDF`, `FOT parcial`) y **mapa de cobertura** por disciplina.
**Gate F1:** E1 publicado en `umc` en CSV+HTML+PNG, con enlaces devueltos y conciliación firmada por A12.

**F2 · Diagnóstico patológico post-sísmico del pavimento** — responsable A2 (+A3 geotecnia, A11 gráficos)
- Contexto del **doblete sísmico 24-06-2026 (Mw 7,2 y Mw 7,5)**: efecto de secuencia sobre juntas y
  subbase (daño acumulado por la réplica mayor) e implicación en el criterio de evaluación.
- **Ficha de daño por zona y elemento**: paños de losa (retícula compatible con módulos de 4,00 m),
  juntas de contracción y dilatación, sellos, flejes, subbase/rellenos, zanjas de colectores,
  brocales y franjas de transición hacia EXT-CTC-15, asta mayor y su fundación, red eléctrica
  histórica (P03-L3-B), borde Babor (riesgo inducido D4 por la Torre).
- **Escala de daño declarada D0–D4** (referencial, adaptada; citar metodologías tipo ATC-20 /
  evaluación de pavimentos rígidos como referencia, no como cumplimiento) y **zonificación
  cartográfica**: D3 = 680,00 m² · D2 = 565,00 m² · D4 inducido = 380,00 m² (verificar contra la
  Ficha; cualquier ajuste se etiqueta `[DERIVADO]`).
- **Decisión de intervención por zona**: conservar · consolidar · reparar juntas · recalzar subbase ·
  demoler y reponer con reintegración de acabado · transferir a P04 (borde Babor). Con justificación
  técnica **y** patrimonial.
- **Hipótesis de causa**: licuefacción/densificación de rellenos sobre zanjas de colectores,
  pérdida de soporte por fuga de colectores antiguos, ausencia de juntas sísmicas de desacople
  contra las Fracciones, envejecimiento de sellos bituminosos (75 años), impacto de escombros.
- **Requerimientos de inspección**: calicatas, DCP/PDC, topografía TLS de escalonamientos, prueba de
  estanqueidad de colectores, georradar de trincheras. Todo como `RFI-PAT-nn` o `RFI-GEOT-nn`.

**Salida E5** (registro fotográfico + mapa de daño G-07) y capítulo 11.5 del expediente.
**Gate F2:** ningún capítulo de diseño de pavimento o drenaje redactado antes de cerrar F2.

**F3 · Expediente de Ingeniería Básica** — responsable A0 con todos los perfiles
Redactar los **28 capítulos** del §7 en el estilo del P01: párrafos cortos, viñetas y **tablas para
todo lo tabulable** (control documental, áreas, paquete de pavimento, drenaje, MEP, BOQ, ROM con
deducción P04, cronograma, planos, riesgos, RFI, coordenadas, glosario).
**Gate F3:** R1–R6 verificadas capítulo por capítulo; cada cifra con etiqueta; sumas y deducciones cuadran.

**F4 · Gráficas y Anexo P** — responsable A11 (+A2, A3, A8)
Producir las figuras G-01…G-15 y las láminas P-0…P-9 del §8, en **SVG embebido para HTML** y **PNG
300 dpi** para PDF/DOCX/Drive, todas con **cajetín**: código, denominación, escala, revisión, fecha,
sello «NO APTO PARA CONSTRUCCIÓN» y nota de validez.
**Gate F4:** cada figura citada al menos una vez en el texto y listada en el capítulo 24.

**F5 · Presentación para el Consejo Universitario** — responsable A0 (+A12)
**24–28 láminas** con la estructura de referencia (§8.3), KPIs grandes, gráficas de F4 reutilizadas,
y cierre con **«Acuerdos que se solicitan al Consejo Universitario»** numerados y votables (incluido
el acuerdo específico de **adopción del código UMC-EXT-004** y el de **financiamiento neto USD
565.000 condicionado a la ejecución del P04**).
**Gate F5:** la presentación no contiene ninguna cifra que no esté en el expediente.

**F6 · Empaquetado y publicación** — responsable A0
Generar DOCX, PDF y HTML de E2 y E6; PNG de E1, E3, E4, E5; publicar **todo** en la carpeta `umc`
(subcarpeta `1 Plan Maestro_Anteproyectos_Ficha_Catastro_otros` o subcarpeta nueva `P05`, declarando
cuál); devolver **tabla de enlaces** (`Entregable | Nombre | Formato | ID Drive | Enlace | Tamaño | Estado`).
**Requisitos técnicos de los archivos:**
- **HTML**: un solo archivo **autocontenido** (CSS y SVG embebidos, **sin CDN ni recursos
  externos**), navegación lateral por capítulos, `@media print` con `@page A4`, tablas con encabezado
  repetido; abre en la vista previa de Drive y sin conexión.
- **PDF**: paginado `Pág. X de Y`, marcadores/índice navegable, metadata (`title`, `author`,
  `subject`, `keywords`) coherente con el expediente.
- **DOCX**: estilos jerárquicos reales (Título 1/2/3), tabla de contenido automática, tablas con
  encabezado repetido, imágenes ancladas con pie de figura.

**F7 · QA y cierre** — responsable A12
Ejecutar el **checklist de aceptación** (§9), producir E7 y E8, y emitir la **condición de emisión**
(capítulo 26).
**Gate F7:** checklist al 100 % con cada ítem en CUMPLE / CUMPLE CON OBSERVACIÓN / NO CUMPLE (+acción).

---

## 7. ÍNDICE DEL EXPEDIENTE — 28 CAPÍTULOS (esquema del P01, adaptado al objeto)

| # | Capítulo | Contenido mínimo obligatorio | Cambio respecto al P01/P04 |
|---|---|---|---|
| **1** | CONTROL DOCUMENTAL Y ADVERTENCIA TÉCNICA | Tabla ítem/registro (documento, código `UMC2030-P05-EXTPCH-R01`, revisión, fecha, fase, estado de emisión, clase de estimación, documento rector = Ficha Catastral Validada EXT-PCH-04, proyectista «por designar», revisor, aprobación, autoría fuente, confidencialidad) + recuadro **ADVERTENCIA TÉCNICA – LÍMITE DE USO** con las condiciones para pasar a «Apto para Construcción» + **condición post-sísmica** (geotecnia de subbase y consolidación previa del borde Babor por P04) | Documento rector nuevo; condición de interfaz P04 |
| **2** | OBJETO Y ALCANCE | 2.1 Objeto general · 2.2 Objetos específicos · 2.3 Alcance incluido (1.245,00 m² netos + partidas integrales no solapadas) · 2.4 Alcance excluido (**explícito: los 380,00 m² del borde Babor y la consolidación de la Torre → P04-R02**) | Alcance definido por conciliación, no por poligonal |
| **3** | ANTECEDENTES Y BASE DOCUMENTAL | Historia ENV 1951 → UMC; Malaussena y el MOP; la explanada como Plaza de Armas (registro fotográfico 1951–1959); cronología 1951–2026; el doblete sísmico; inventario Portaplanos 01–05; expedientes P01–P04 como base de coordinación | Bloque de historia ceremonial del patio |
| **4** | MARCO NORMATIVO Y REFERENCIAS TÉCNICAS | COVENIN 1756 (sismorresistente), 1753 (concreto), 200 (eléctrico), 810/187 (señalización y vías de evacuación), 2733/Fondonorma 2733 (accesibilidad); drenaje urbano (Tr = 25 años, declarar fuente del criterio); OMI/STCW (función ceremonial de graduaciones); OMM (emplazamiento del mástil); IEC 62305 (descargas atmosféricas: asta y mástil); normativa de patrimonio cultural. **Todo «vigencia por verificar»** con `RFI-NOR-01` | Bloque de pavimentos, drenaje y señalización de evacuación |
| **5** | EMPLAZAMIENTO, GEORREFERENCIACIÓN Y TOPOGRAFÍA | 5.1 Zona (Proa Central, interfaz EXT/CUL) · 5.2 Puntos de control (centroide DMS↔decimal, UTM 19N; tabla) · 5.3 Control geométrico (50,00 × 32,50 m en crujía de 52,00 m = 13 × 4,00 m; franjas de 1,00 m; corredores 3,00–3,60 m) · 5.4 Sistema cartográfico (WGS84/EPSG:4326; trabajo UTM 19N/EPSG:32619) · 5.5 Topografía de detalle pendiente: **BM-UMC-01 por establecer, cota Z y nivelación de escalonamientos** `RFI-GEO-01` | El control geométrico es la retícula de paños |
| **6** | CONCEPTO ARQUITECTÓNICO | 6.1 Concepto rector (proponer **uno** con nombre propio, coherente con «Campus-Buque Digital UMC»; p. ej. *La Cubierta de Formación* — decidir y justificar) · 6.2 Lenguaje (explanada moderna 1950s: paños modulados, acabado granítico/martelinado, relación con Aula Magna y Torre) · **6.3 Doctrina de intervención patrimonial** (conservar/consolidar/reintegrar/reponer; junta-testigo datada; sin falsificación histórica) | Concepto de espacio ceremonial abierto |
| **7** | PARÁMETROS URBANÍSTICOS Y DE DISEÑO | Ocupación (espacio abierto, 0 niveles, 0,00 m), aforo ceremonial (1.300 / 1.625 / R-1), pendientes 1,2–1,5 %, cargas de uso (formaciones, vehículo de emergencia y de mantenimiento), accesibilidad (podotáctil, podio accesible), condición de espacio protocolar singular | Sustituye alturas/retiros de edificio |
| **8** | PROGRAMA FUNCIONAL Y CUADRO GENERAL DE ÁREAS | **8.1 Explanada ceremonial** (zonas de formación por compañías, calle de revista, eje de desfile) · **8.2 Banda de Protocolo** (210,00 m² — dentro del borde P04: solo coordinación) · **8.3 Elementos protocolares**: Asta Mayor (12,00 m) + podio, Tribuna de Honor, zona de autoridades · **8.4 Mástil Hidrometeorológico OMM** (10,00 m) y su parcela · **8.5 Función R-1** (zonas de concentración, rutas de aproximación) · **8.6 Resumen**: 380,00 (P04) + 1.245,00 (P05) = 1.625,00 m², con porcentajes 23,38/76,62 | Sustituye el programa por niveles del P04 |
| **9** | COMPONENTES FUNCIONALES – FICHAS | Ficha por componente (uso, área, capacidad, equipamiento, trazabilidad): explanada de formación · eje ceremonial e izada del Pabellón · banda de protocolo (interfaz) · tribuna y podio · punto R-1 · mástil OMM · alumbrado ceremonial/emergencia · drenaje · señalización. Con **matriz de cumplimiento** estilo P01 (componente → ubicación → área → estado) | Componentes de espacio abierto |
| **10** | ARQUITECTURA – PAVIMENTO, MATERIALES Y ACABADOS | 10.1 Criterios (ambiente marino, compatibilidad con obra 1951–58, pares galvánicos en rejillas/flejes/astas) · 10.2 Cuadro de materiales (losa, subbase, sellos elastoméricos, rejillas C250 AISI 316/fundición dúctil, acabado granítico/martelinado, señalización, luminarias IP66/IK10) · 10.3 **Reintegración del acabado histórico** (criterio, muestras, junta-testigo) · 10.4 Confort exterior (sombra, deslumbramiento, temperatura superficial) | Capítulo de pavimento, no de envolvente |
| **11** | CRITERIOS ESTRUCTURALES Y GEOTÉCNICOS DEL PAVIMENTO | 11.1 Paquete estructural propuesto (losa, juntas, subbase mejorada) **condicionado a geotecnia** · 11.2 Retícula de paños y juntas (compatible con módulos de 4,00 m) · 11.3 **Juntas sísmicas de desacople** perimetral contra Fracciones 1/2 y cabezales piloteados (≈ 980 m de sellado) · 11.4 Predimensionamiento (tabla elemento/espesor/base de cálculo/verificación requerida) · **11.5 Diagnóstico patológico post-sísmico** (síntesis F2: D2/D3/D4 por zona) · 11.6 Fundación del Asta Mayor y del Mástil OMM (viento, IEC 62305) | Sustituye los criterios de edificio |
| **12** | INSTALACIONES MEP | 12.1 Eléctrica exterior (12 luminarias LED IP66/IK10, 100–150 lux; alumbrado de emergencia R-1; 2 cajas de piso IP67 para la Banda; bancadas Ø 4" con juntas sísmicas flexibles; malla de tierra R ≤ 5 Ω; protección atmosférica del asta y el mástil) · 12.2 Drenaje pluvial (Q = 73,13 L/s propio / ≈ 145 L/s con faldones, Tr = 25 años; canaletas 180 m; PEAD SN8 Ø 300–400 mm × 140 m; 8 tanquillas) · 12.3 PCI (hidrante/toma siamesa borde Norte, coordinado con Cap. 12.4 de P04-R02) · 12.4 Riego/servicios si las fuentes lo sustentan | El drenaje es la instalación crítica |
| **13** | TELECOMUNICACIONES Y CAMPUS | 13.1 Canalizaciones subterráneas de reserva TIC (coordinar con CDP/Torre B) · 13.2 Megafonía protocolar y CCTV de la explanada · 13.3 Interfaz de datos del Mástil OMM con la estación del P04 (telemetría, sin duplicar la adquisición) | Adaptado a espacio abierto |
| **14** | SEGURIDAD FÍSICA Y CONTROL | Protección antivandálica de un espacio abierto de acceso público en actos; control perimetral en ceremonias; CCTV; protección de instrumentos y luminarias; gestión de multitudes | Énfasis en eventos masivos |
| **15** | SOSTENIBILIDAD, ENERGÍA Y AMBIENTE MARINO | 15.1 Eficiencia del alumbrado y medición · 15.2 Durabilidad costera (cloruros, sellos UV, rejillas) · 15.3 **Drenaje como activo de resiliencia climática** (gestión de pluviales del sector Proa; datos del mástil OMM alimentan la operación del campus) · 15.4 Paisajismo halófilo perimetral | Resiliencia hídrica en lugar de FV |
| **16** | INDUSTRIA 5.0, BIM Y GEMELO DIGITAL | 16.1 HBIM del espacio exterior: nube de puntos del pavimento dañado (TLS), modelo federado, CDE, codificación `UMC-[ACTIVO]-[DISCIPLINA]-[NÚMERO]-[REV]`; **resolución del código de activo (RFI-COD-05) en la base GIS/BIM** · 16.2 Sensorización (asentamientos, niveles de tanquillas, pluviómetro del mástil, conteo de aforo en actos) · 16.3 Enfoque humanocéntrico (el cadete en formación, el operador de mantenimiento, la seguridad en evacuación) | HBIM de obra exterior + GIS |
| **17** | ACCESIBILIDAD, AFORO Y EVACUACIÓN | **Capítulo crítico**: el patio ES el Punto de Evacuación R-1. Aforos 1.300 / 1.625 / 1.080–1.625; rutas de aproximación desde Fracciones 1–3; señalización COVENIN 810/187; franjas podotáctiles (Fondonorma 2733); alumbrado de emergencia autónomo; **condición transitoria**: mientras el patio esté inhabilitado, declarar el punto R-1 alterno (si no existe en fuentes → `RFI-EVA-01`) | De «evacuar el edificio» a «ser el punto de evacuación» |
| **18** | OBRAS EXTERIORES E INFRAESTRUCTURA COMÚN | 18.1 Bordes y transiciones (brocales, franjas de 1,00 m, corredores EXT-CTC-15, vialidad de emergencia preservada) · 18.2 Sección tipo de la trinchera de servicios (tabla servicio/conducto/separación/condición) · 18.3 **Matriz de interfaces del P05** (↔P04 Torre/Sala/borde Babor · ↔Fracción 1 Aula Magna · ↔Fracción 2 · ↔Fracción 3 · ↔EXT-CTC-15 · ↔red PCI campus · ↔CDP Torre B) | La matriz de interfaces es el corazón del capítulo |
| **19** | SUBPROYECTO ASOCIADO: CONJUNTO CEREMONIAL DE PROA | 19.1 Rehabilitación coordinada del conjunto (Aula Magna/foyer, galería, corredores, Torre/Sala del P04, banda, asta, tribuna) · 19.2 **Criterio de unidad de intervención**: la Proa Central como un solo frente patrimonial, con etapabilidad y **condición suspensiva: el borde Babor no se restaura antes de consolidar la Torre (P04)** | Define la secuencia P04 → P05 |
| **20** | ESPECIFICACIONES TÉCNICAS – CONTENIDO MÍNIMO | Tabla de capítulos estilo P01, **más**: *demolición controlada y gestión de escombros con valor patrimonial* · *saneamiento geotécnico de subbase y rellenos* · *sustitución de colectores y pruebas de estanqueidad* · *pavimento rígido: vaciado, curado, juntas y sellos* · *reintegración del acabado granítico/martelinado* · *señalización R-1 y accesibilidad* · *comisionamiento de alumbrado y drenaje* | Especificaciones de obra exterior |
| **21** | CÓMPUTOS MÉTRICOS PRELIMINARES (BOQ REV.0) | Derivado de la geometría y del mapa de daño (1.625,00 m² integrales, con columna de asignación **P04 / P05-neto** por partida). Partidas de referencia de la Ficha: retiro y gestión de pavimento, saneamiento de subbase, losa nueva + juntas, sellado 980 m, asta (gl 38.500), drenaje (gl 112.000), hidrante (14.500), eléctrica (gl 96.000), señalización/paisajismo/comisionamiento (28.395). Nota expresa: **no son cómputos contractuales** | Columna de asignación P04/P05 obligatoria |
| **22** | ESTIMACIÓN DE INVERSIÓN (ROM) | AACE Clase 5 (−25 %/+40 %): **costo directo USD 765.000 (470,77 USD/m²) + ingeniería/ensayos/supervisión patrimonial 7,0 % (53.550) + contingencia 10,0 % (76.450) = ROM integral USD 895.000 (rango 750.000–1.120.000)**; **(−) 330.000 ya en P04-R02 (rango 260.000–400.000)**; **(=) neto adicional USD 565.000 (rango 490.000–720.000)**. Gráfica de cascada obligatoria (G-13). Declarar el redondeo de la contingencia en nota | La deducción es parte del capítulo, no un anexo |
| **23** | CRONOGRAMA DE EJECUCIÓN | Fases A…E (estudios previos y topografía → desescombro/demolición controlada → saneamiento subbase + colectores → pavimento y juntas → equipamiento, señalización y comisionamiento) con duración, hitos y gates; **restricciones duras**: (1) consolidación del borde Babor por P04 precede a su pavimento; (2) calendario académico-ceremonial (graduaciones) condiciona cortes de la explanada; (3) habilitación provisional del punto R-1 alterno durante la obra | Secuencia esclava del P04 y del calendario ceremonial |
| **24** | PLANOS DEL EXPEDIENTE | Tabla `Código | Denominación | Escala | Estado` con codificación `UMC-PCH-…` (patio), `UMC-G-…` (general) | Codificación nueva PCH |
| **25** | RIESGOS E INFORMACIÓN PENDIENTE | **25.1 Matriz de riesgos** (ID, riesgo, impacto, mitigación): nueva réplica durante la obra · colectores en peor estado del previsto · interferencias enterradas no cartografiadas · desfase del P04 que bloquea el borde Babor · pérdida del acabado histórico en el desescombro · indisponibilidad de oficios del acabado martelinado · inhabilitación prolongada del punto R-1 · corrosión marina · vandalismo · demora permisológica y patrimonial · lluvia extraordinaria con la subbase abierta. **25.2 Registro RFI** con las pre-detectadas de R5 (COD-05, ARE-05, SRC-01/02, GEO-01, GEOT-01, ALT-01, NOR-01, EVA-01) + PAT y las que surjan | Riesgos de pavimento, interfaz y evacuación |
| **26** | CONCLUSIÓN Y CONDICIÓN DE EMISIÓN | Síntesis + recuadro **CONDICIÓN DE EMISIÓN**: aprobado como intención del Plan Maestro y base de ingeniería básica; condicionado a geotecnia, topografía y a la ejecución del P04 en el borde Babor; **no apto para replanteo ni construcción** | Mención expresa a la condición suspensiva P04 |
| **27** | ANEXOS | **A** Referencias gráficas (láminas MOP del inventario + Plan Maestro + fotos históricas 1951–1959) · **B** Conversión de coordenadas DMS→decimal y datos CAD/GIS (tabla punto/lat/lon/N/E/observación + nota QGIS/Google Earth) · **C** Glosario (incluye D0–D4, Tr, PEAD SN8, C250, IP66/IK10, R-1, OMM, HBIM, AIM, ROM, AACE) · **D** Registro fotográfico post-sísmico (E5) · **E** Trazabilidad documental (E7) · **F** Matriz de interfaz y deducción P05↔P04 (E8) | Nuevo Anexo F |
| **28** | ANEXO P – PLANOS | **28.1 Cuadros de implantación**: P-1 índice del anexo · P-2 coordenadas de puntos de control · P-3 superficies (1.625 / 380 / 210 / 1.245 m² como conjuntos anidados) · **28.1.1 Notas de implantación** + recuadros **ALCANCE Y VALIDEZ DE LOS PLANOS** | Cuadro de superficies anidadas |

---

## 8. GRÁFICAS OBLIGATORIAS

### 8.1 Figuras del expediente (E4)

| Código | Figura | Tipo |
|---|---|---|
| G-01 | Implantación general de la Proa Central: patio, Fracciones 1/2/3, Torre/Sala, corredores, asta, mástil (1:400) | Plano georreferenciado |
| G-02 | Línea de tiempo patrimonial 1951 → 1953 → 1958 → 2025 → 24-06-2026 → 2030 | Diagrama temporal |
| G-03 | **Conciliación de áreas anidadas**: 1.625,00 m² ⊃ 380,00 m² (P04) ⊃ 210,00 m² (Banda) + 1.245,00 m² netos | Diagrama de conjuntos sobre planta |
| G-04 | Retícula de paños y módulos 4,00 m sobre la crujía de 52,00 m (geometría 50,00 × 32,50 m) | Plano temático |
| G-05 | Zonificación funcional ceremonial: formación, calle de revista, banda, tribuna, asta, R-1 | Plano temático |
| G-06 | Sección constructiva del paquete de pavimento propuesto vs. existente (1:20) | Diagrama técnico |
| **G-07** | **Mapa de daño post-sísmico D2/D3/D4 por zona** (leyenda de la escala declarada; 680/565/380 m²) | Plano temático |
| G-08 | Esquema del drenaje: cuencas, Q = 73,13/145 L/s, canaletas, colectores PEAD, tanquillas, descarga | Diagrama técnico |
| G-09 | Unifilar del alumbrado ceremonial/emergencia + cajas de la Banda + malla de tierra y protección atmosférica | Diagrama |
| G-10 | Emplazamiento del Mástil OMM: distancias a obstáculos (Torre 22,02 m, fracciones, corredores) según criterios OMM | Diagrama técnico |
| G-11 | Estrategia HBIM/GIS: nube de puntos → modelo → AIM → mantenimiento; resolución del código de activo | Diagrama de flujo |
| G-12 | Plano de evacuación R-1: aforos, rutas de aproximación, señalización, punto alterno transitorio | Plano de evacuación |
| G-13 | **ROM en cascada**: 765.000 → +53.550 → +76.450 → 895.000 → −330.000 (P04) → 565.000 netos, con banda −25 %/+40 % | Gráfica de cascada |
| G-14 | Cronograma de fases con gates y restricciones (P04, calendario ceremonial, lluvias) | Gantt |
| G-15 | Mapa de riesgos (probabilidad × impacto) con los ID de la matriz 25.1 | Matriz de calor |

### 8.2 Láminas del Anexo P (E3)

`P-0` Implantación general georreferenciada de la Proa Central (1:400) · `P-1` Planta general de
paños, juntas y niveles de pendiente (1:200) · `P-2` Planta de demolición/retiro por zonas de daño
(1:250) · `P-3` Planta de drenaje pluvial y red de colectores (1:250) · `P-4` Planta eléctrica,
alumbrado y canalizaciones (1:250) · `P-5` Planta de señalización, accesibilidad y evacuación R-1
(1:250) · `P-6` Planta de zonificación ceremonial y protocolo (1:250) · `P-7` **Sección constructiva
del pavimento y juntas** (1:20) + perfil longitudinal de colectores (1:100 H / 1:50 V) · `P-8`
Detalles del Asta Mayor, podio y Mástil OMM (1:50) · `P-9` Planta de interfaz con P04: borde Babor,
límites de alcance y juntas de transferencia (1:250).
Todas con cajetín completo y nota de validez: *planos esquemáticos de anteproyecto; definen
programa, dimensiones y relaciones funcionales; no incluyen detalles constructivos de ejecución,
armaduras, ni replanteo.*

### 8.3 Presentación al Consejo Universitario (E6)

Estructura de 24–28 láminas, en el lenguaje visual de la presentación de referencia:
1 Portada · 2 **Cómo leer esta presentación** (qué ES / qué NO es) · 3 Agenda en 6 bloques ·
4 Marco: Plan Maestro UMC 2025–2030 · 5 Patrimonio: la Plaza de Armas de la ENV y Malaussena
(fotos 1951–1959) · 6 **El doblete sísmico del 24-06-2026 y el dictamen de inhabilitación** ·
7 Implantación de la Proa Central · 8 Ficha del Patio de Honor (KPIs: 1.625 m², 1.300 cadetes,
0 niveles, R-1) · 9 **Conciliación de áreas y alcance con el P04** (G-03) · 10 Diagnóstico
patológico (G-07) · 11 Doctrina de intervención: conservar/consolidar/reintegrar · 12 Concepto ·
13 Pavimento y juntas sísmicas · 14 Drenaje y resiliencia hídrica · 15 Eléctrica, protocolo y
protección atmosférica · 16 Mástil OMM e interfaz con la estación del P04 · 17 Industria 5.0, HBIM y
gemelo digital · 18 **El patio como Punto de Evacuación R-1** (incluida la condición transitoria) ·
19 Interfaces y subproyecto del conjunto de Proa · 20 Especificaciones y cómputos · 21 **Inversión
ROM en cascada** (895 k integral / 565 k neto, AACE Clase 5) · 22 Cronograma y condición suspensiva
P04 · 23 Riesgos principales · 24 **RFI abiertas** · 25 Condición de emisión (✗ lo NO definido / ✓ lo
SÍ definido) · 26 **Acuerdos que se solicitan al Consejo** (resolución numerada: aprobación de la
intención, adopción de UMC-EXT-004, financiamiento neto condicionado, punto R-1 alterno) ·
27 Cierre con las cifras del proyecto.

---

## 9. CHECKLIST DE ACEPTACIÓN (Gate F7 — verificar y reportar ítem por ítem)

1. Los 28 capítulos existen, en orden, con el contenido mínimo del §7.
2. Sello y pie «NO APTO PARA CONSTRUCCIÓN» en todas las páginas y láminas.
3. Control documental completo: `UMC2030-P05-EXTPCH-R01`, fecha, aprobación, autoría fuente (CIV 95787), proyectista «por designar», confidencialidad.
4. Las RFI pre-detectadas `RFI-COD-05`, `RFI-ARE-05`, `RFI-SRC-01`, `RFI-SRC-02`, `RFI-GEO-01`, `RFI-GEOT-01`, `RFI-ALT-01`, `RFI-NOR-01`, `RFI-EVA-01` están abiertas y visibles en el capítulo 25.
5. Las áreas anidadas (1.625 / 380 / 210 / 1.245 m²) figuran sin sumarse entre sí y toda tabla declara su perímetro (integral o neto).
6. Verificaciones aritméticas: 50×32,50 = 1.625; 680+565+380 = 1.625; 380+1.245 = 1.625; 1.625/1,25 = 1.300; 765.000+53.550+76.450 = 895.000; 895.000−330.000 = 565.000; el redondeo de contingencia está anotado.
7. El alcance excluido (380 m² del borde Babor → P04) y la condición suspensiva P04→P05 están declarados en los capítulos 2, 19, 22, 23 y 26.
8. Cada cifra del expediente tiene etiqueta de origen (R1) y existe E7 con la matriz de trazabilidad.
9. El BOQ deriva de la geometría y del mapa de daño, con columna de asignación P04/P05-neto; el ROM deriva del BOQ y cuadra con el capítulo 22.
10. El rango −25 %/+40 % y la naturaleza «no presupuesto de licitación» están declarados.
11. El diagnóstico post-sísmico (F2) precede y justifica toda decisión de pavimento y drenaje; hay nivel de daño por zona/elemento y decisión de intervención por zona.
12. La doctrina patrimonial está explícita (junta-testigo, distinguibilidad) y no se declara certificación alguna.
13. Ninguna norma se cita como cumplida sin verificación; hay `RFI-NOR-01`.
14. El listado E1 concilia con los totales 198 PDF / 487 fotografías y declara criterios de selección auditables.
15. Las lagunas del inventario (`PEND-ARCHIVO`, `PEND-PDF`, `FOT parcial`) se listan sin reinterpretarlas como verificadas.
16. Las 15 figuras G-01…G-15 existen, están citadas en el texto y tienen cajetín o pie de figura.
17. Las láminas P-0…P-9 existen, con escala, código y sello; el índice del Anexo P las lista todas.
18. Coordenadas en DMS **y** decimal, con sistema de referencia declarado, inversión X/Y corregida y Z declarada pendiente (`RFI-GEO-01`).
19. Glosario alfabético sin duplicados; incluye los términos de pavimentos, drenaje, meteorológicos y patrimoniales usados.
20. HTML autocontenido (sin recursos externos), con navegación y CSS de impresión; PDF con índice navegable y metadata; DOCX con estilos y tabla de contenido.
21. Los 8 entregables E1–E8 están publicados en la carpeta `umc` con nombres canónicos y se devuelve la tabla de enlaces.
22. No hay duplicación con P04-R02: existe la matriz de interfaz y deducción (E8/Anexo F) y ninguna partida está presupuestada dos veces.
23. Ortografía y denominaciones correctas (Universidad Marítima del Caribe, Catia La Mar, Aula Magna, hidrometeorológica, Malaussena), sin arrastrar las erratas de las fuentes a la prosa propia (p. ej. «0 m²» como altura).
24. La presentación no contiene ninguna cifra ausente del expediente y termina con los acuerdos solicitados al Consejo, incluidos los de código catastral y financiamiento neto.

---

## 10. PROTOCOLO DE REPORTE

Al cerrar **cada gate**, publica un bloque breve y continúa sin esperar confirmación:

```
GATE Fn — <nombre>
Hecho:            <2–4 líneas>
Fuentes usadas:   <archivos e IDs efectivamente abiertos>
Entregables:      <nombre canónico + ID/enlace si ya publicado>
Hallazgos:        <inconsistencias, lagunas, decisiones tomadas>
RFI nuevas:       <ID + enunciado + responsable>
Siguiente gate:   <Fn+1>
```

Al finalizar **F7**, entrega: (a) tabla de los 8 entregables con enlaces, (b) checklist §9 resuelto,
(c) matriz de interfaz y deducción P05↔P04, (d) listado consolidado de RFI abiertas, (e) condición
de emisión.

**Empieza por F0. No redactes el expediente antes de cerrar F1 y F2.**

═══ FIN DEL PROMPT ═══

---

## Apéndice — Notas de la revisión de ingeniería (por qué esta versión difiere de tu borrador)

Verificación en vivo (26-10-2026) de la carpeta `umc` y lectura efectiva de
`UMC 2030 · Ficha Catastral Validada y Diagnóstico Forense · EXT-PCH-04 Patio _ Cubierta de Honor.pdf`
(fuente rectora del P05) y del listado real de archivos e IDs de Drive.

**Errores corregidos del borrador que enviaste:**

| # | Hallazgo en tu borrador | Corrección aplicada |
|---|---|---|
| 1 | `COD_EXPEDIENTE = UMC2030-P05-TOBSHM-R01`: la sigla **TOBSHM pertenece al P04** (Torre de Observación / Sala Hidrometeorológica) | Nueva sigla **EXTPCH** derivada del código funcional EXT-PCH-04 → `UMC2030-P05-EXTPCH-R01` |
| 2 | Los 8 entregables E1–E8 conservaban el nombre **`UMC2030-P04-TOBSHM-R02_…`** y E1 seguía siendo «TORRE-Y-SALA» | Renombrados todos a `UMC2030-P05-EXTPCH-R01_…` y E1 = PATIO-DE-HONOR |
| 3 | Fuente rectora declarada: `torreo observacion y meteorologia.pdf` (es la del P04; además no está en la raíz de `umc`) | Fuente rectora del P05 = Ficha Catastral Validada EXT-PCH-04 (`1AAe5Zop…`) + `PATIO_HONOR CATASTRO.pdf` (`13QVyI4…`); el PDF de la torre pasa a contexto del colindante |
| 4 | Inventarios listados como sueltos en `umc` | Están en la subcarpeta `inventario` (`1Rm4RFm2…`); IDs confirmados uno a uno |
| 5 | R4 regulaba las **dos alturas de la torre** (12,20/22,02 m) como regla central | Para el patio la regla central es la **conciliación de áreas anidadas** (1.625/380/210/1.245 m²) y la no doble presupuestación; la dualidad de alturas queda heredada como `RFI-ALT-01` (contexto del borde Babor) |
| 6 | R5 exigía las RFI del P04 (CUL-TOO-01 vs 02, 40 vs 38,50 m², 1951–58 vs 1960–75) | RFI propias del P05: COD-05 (UMC-ED-000→UMC-EXT-004), ARE-05 (solape 380 m² con P04), SRC-02 (doble ID del catastro), GEO-01 (cota Z/BM), GEOT-01 (subbase), EVA-01 (R-1 alterno) |
| 7 | F1/F2 y capítulos 8, 11, 17, 19, 21 seguían redactados para **torre + sala** (niveles N0–N5, 67,50 m², evacuación vertical, Stevenson, 3,61 m) | Reescritos para la explanada: paños/juntas/subbase/colectores, programa ceremonial, el patio **como** punto de evacuación R-1, condición suspensiva P04→borde Babor |
| 8 | Checklist §9 verificaba 5×13,50 = 67,50 m² y la sala de 40,00 m² | Verificaciones aritméticas reales del P05 (ver ítem 6 del checklist), todas confirmadas contra la Ficha: 680+565+380 = 1.625 ✔, 895 k − 330 k = 565 k ✔ |
| 9 | `ESCALA_PLANOS` pedía «sección vertical 1:100» (no hay edificio) | Sección constructiva de pavimento 1:20 + perfil de colectores 1:100 H / 1:50 V |
| 10 | «Tabla de cambios R01→R02» (no existe R01 previo del P05) | Sustituida por **matriz de interfaz y deducción P05↔P04** (E8/Anexo F), que es el control de no-duplicación que este proyecto sí necesita |
| 11 | Sin anclas económicas | Se incorporó el ROM verificado de la Ficha: 765 k directo / 895 k integral / −330 k P04 / 565 k neto, con la cascada G-13 obligatoria |
| 12 | Detalle menor: la contingencia 10 % de 765.000 = 76.500, pero la Ficha consigna 76.450 para cerrar en 895.000 | Se ordena declararlo en nota al pie (R6), no silenciarlo |

**Inconsistencias de las fuentes convertidas en RFI obligatorias:** código físico genérico
UMC-ED-000 vs. normalización UMC-EXT-004 · solape presupuestario de 380,00 m² con P04-R02 · doble ID
de `PATIO_HONOR CATASTRO.pdf` · enlace caduco `1M2iYrHyBE4…` (404) · errata de unidad «0 m²» como
altura · inversión de rótulos X/E–Y/N del centroide · cota Z sin benchmark.

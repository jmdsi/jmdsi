# CATASTRO UNIVERSITARIO: CODIFICACIÓN DE LA PLANTA FÍSICA

**Universidad Marítima del Caribe — Campus Universitario UMC**

---

## Codificación institucional (identifica su función)

### Código funcional: `EXT-CTC-15`

**CORREDORES TECHADOS DE CIRCULACIÓN Y CONECTORES DE DEPENDENCIAS**

> `EXT` — Área exterior y movilidad: portalón, accesos, vialidad, estacionamientos,
> plazas, jardines, patios, áreas verdes y superficies abiertas.

## CLASIFICACIÓN CATASTRAL DE EDIFICACIONES

### Codificación institucional (identifica la estructura física)

### Código físico: `UMC-ED-004`

Corredores techados de enlace institucional — Pórticos de circulación y conectores de
dependencias.

---

# FICHA DE DATOS CATASTRALES (Validada contra Planos)

| Campo | Dato |
|---|---|
| **Denominación** | Red de corredores techados de circulación y conectores de dependencias del Campus UMC (sistema porticado de enlace institucional) |
| **Sector** | Sector central-norte del campus. **Orientación: PROA** (núcleo académico-administrativo), con ramales a **BABOR** (poniente: Dormitorios, Enfermería, Servicios) y **ESTRIBOR** (levante: Aulas, Laboratorios, Talleres) |
| **Área construida** | **2.510 m²** *(declarada institucionalmente)* — **verificada contra planos MOP: 156,00 m²** equivalentes al **6,2 %**. Resto pendiente de validación documental (ver Observaciones Técnicas §2 y §3) |
| **Niveles** | **1** *(declarado)* — **⚠ inconsistente**: la Fracción 3 (Dormitorios) acredita corredor techado también en **planta alta**. Ver §3.2 |
| **Altura** | `NV` — no acotada en la documentación fotografiada. *(Nota: la plantilla indica "Altura: m²"; la unidad correcta es **m**.)* |
| **Uso principal** | Circulación peatonal cubierta y conexión funcional entre dependencias. Protección solar y pluvial del tránsito interdependencias |
| **Dependencias** | Rectorado · Vicerrectorado Académico · Casino de Cadetes · Comedor de Cadetes · Cocina · Laboratorios · Aulas · Talleres · Dormitorios · Enfermería · Biblioteca · Administración · Área de Servicios |
| **Capacidad** | No aplica (elemento de circulación, sin aforo asignado). Capacidad de flujo condicionada por el ancho libre — ver §4 |
| **Estado estructura** | **NOMINAL (histórico):** operativo según proyecto MOP, pórtico de concreto armado sobre fundación directa y pilotada.<br>**ACTUAL (post-colapso):** **PARCIALMENTE COLAPSADO**. El conector Casino de Cadetes–Laboratorios (Fracción 7, **156,00 m²**) se encuentra **colapsado por evento sísmico** — señalado en **rojo** en el plano de codificación institucional |
| **Año construcción** | **1946 – 1953** (c.). Proyecto del **Ministerio de Obras Públicas**, Dirección de Edificios y Obras de Ornato Público / Dirección de Edificios e Instalaciones Industriales. Oficina Técnica **Gutiérrez & Cía. S.A.** Sello ministerial húmedo "República de Venezuela – MOP" visible en todas las láminas. Fecha legible en rótulo de Fracción 2: **22-5-51** |
| **Coordenada centroide** | **X/E: 67° 1' 54.02" O** — **Y/N: 10° 36' 0.06" N** |
| **Observaciones** | Sistema de valor patrimonial: constituye la estructura de articulación original del conjunto ENV (1946) heredado por la UMC. Su trazado define la morfología del campus y condiciona cualquier intervención del Plan Maestro 2030 |

---

# OBSERVACIONES TÉCNICAS (Bloque obligatorio)

## 1. Codificación institucional

| Nivel | Código | Significado |
|---|---|---|
| Funcional | `EXT-CTC-15` | Área exterior y movilidad → Corredores Techados de Circulación, elemento 15 |
| Físico | `UMC-ED-004` | Edificación UMC nº 004 |
| Catastral de detalle *(propuesto)* | `ENV-C-CX-001` | Tramo Casino de Cadetes ↔ Laboratorios (Fracción 7) |

**Observación de método.** Los códigos `EXT-CTC-15` y `UMC-ED-004` tratan la red completa
como **una sola unidad catastral**. Esto es adecuado para la codificación institucional,
pero **insuficiente para la gestión**: la red es un sistema discontinuo de tramos con
distinta fracción de origen, distinta geometría y **distinto estado de conservación** —
uno de ellos colapsado. Se recomienda codificación de **segundo nivel por tramo**
(`UMC-ED-004.01`, `.02`, …), conservando `UMC-ED-004` como agregador. Sin ella no es
posible dar de baja el tramo colapsado sin afectar el registro de toda la red.

## 2. MEDIDAS VERIFICADAS EN PLANOS MOP

### 2.1 Tramo verificado con cota — Fracción 7

| Magnitud | Valor | Confianza | Origen |
|---|---|---|---|
| Longitud total | **52,00 m** | `COT` | Cota general |
| Separación entre ejes de columnas | **4,00 m** | `COT` | Cadena de acotado |
| Número de crujías | **13** | `COT` | Conteo |
| Ancho entre ejes (vigas `VF1-7`) | **3,00 m** | `COT` | Planta de fundaciones con pilotes |
| **Superficie nominal** | **156,00 m²** | `COT` | Cálculo directo |

```
Comprobación de coherencia
    13 crujías × 4,00 m = 52,00 m  ═  cota general 52,00 m        ✓

Superficie
    A = 52,00 m × 3,00 m = 156,00 m²
```

**Triple validación cruzada.** La longitud de 52,00 m aparece coincidente en **tres láminas
independientes** de la Fracción 7 —Planta y Fachadas, Planta de Fundaciones y Envigado, y
Planta de Fundaciones con Pilotes—, levantadas para fines distintos. El ancho de 3,00 m está
acotado entre ejes de las dos vigas longitudinales `VF1-7`.

### 2.2 Módulo dimensional del sistema

De la lectura de las fracciones 2, 3, 6, 7, 9 y 10 se confirma un **módulo estructural
constante de 4,00 m entre ejes de columnas** en toda la red de corredores. Es el invariante
de proyecto del conjunto ENV y permite estimar longitudes por conteo de crujías cuando la
cota general no sea legible.

### 2.3 Tramos identificados, pendientes de cota

| Fracción | Bloque | Corredor | Cotas parciales legibles |
|---|---|---|---|
| 2 / "E" | Biblioteca–Dirección–Administración | Frontal + perimetral en U | Tramo inferior **36,00 m**; crujías 4,00 m |
| 3 | Dormitorios | Perimetral en U, **planta baja y planta alta** | Tramo **54,00 m** (aprox.); crujías 4,00 m |
| 6 | Talleres y Casino | Perimetral en L (poniente y mediodía) | Crujías 4,00 m |
| 9 | Casino y Comedor de Cadetes | Red interna extensa | Crujías 4,00 m |
| 10 | Enfermería | Dos ramales (poniente y enlace a Farmacia/Dentista/Médico) | No legibles |

> Estos valores **no se incorporan al cómputo** por no alcanzar nivel de confianza `COT`.
> Se consignan como guía para la campaña fotográfica de cierre.

## 3. Inconsistencia crítica de área

### 3.1 Área declarada frente a área verificada

| Concepto | Valor | % |
|---|---|---|
| Área declarada en ficha institucional | **2.510 m²** | 100 % |
| Área verificada con cota en planos MOP | **156,00 m²** | **6,2 %** |
| Área pendiente de validación documental | **2.354 m²** | **93,8 %** |

**El 93,8 % del área declarada carece hoy de respaldo documental verificable.** No se afirma
que la cifra sea incorrecta: se afirma que **no está soportada** por la documentación
examinada. Para efectos registrales, un área sin trazabilidad a cota de plano o a
levantamiento topográfico no es oponible.

### 3.2 Inconsistencia en el número de niveles

La ficha declara **Niveles: 1**. Sin embargo, la lámina **Fracción 3 — Planta Alta, escala
1:100** muestra con claridad el **corredor techado reticulado recorriendo la planta alta** de
los bloques de Dormitorios, con el mismo módulo de 4,00 m.

**Consecuencia:** si el corredor de la Fracción 3 se desarrolla en dos niveles y el área
declarada se computó sobre un solo nivel, **el área real del sistema es mayor que la
declarada**. La inconsistencia opera en sentido contrario al habitual: no sobra área, falta.

### 3.3 Inconsistencia de estado: área colapsada computada como existente

Este es el hallazgo de mayor relevancia registral.

La ficha declara **2.510 m² de área construida** sin distinguir estado. Pero el propio plano
de codificación institucional **señala en rojo** el tramo Casino de Cadetes–Laboratorios,
que está **colapsado**. Sus **156,00 m²** (6,2 % del total) **no existen físicamente**.

```
Área declarada                               2.510 m²
  − Tramo colapsado Fracción 7 (ENV-C-CX-001)  156 m²
                                             ─────────
Área físicamente existente (estimada)        2.354 m²
```

**Un bien colapsado no puede permanecer inventariado como área construida existente.**
Procede desdoblar el registro en:

- **Área nominal histórica** (proyecto MOP): 2.510 m² — base para reposición y valoración de pérdida
- **Área físicamente existente**: 2.354 m² — base para inventario patrimonial y seguros
- **Área en situación de baja por siniestro**: 156,00 m² — con acta de inspección postsísmica

### 3.4 Discrepancia Plan Maestro 2030 frente a Situación General ENV

| Aspecto | Situación General ENV (1:500, c. 1951) | Plan Maestro 2030 / estado actual |
|---|---|---|
| Red de corredores | Sistema continuo que articula la totalidad del núcleo | Red **fragmentada**: tramos aislados sin continuidad plena |
| Conector Fr. 7 | Presente y operativo (52,00 m) | **Colapsado** (señalado en rojo) |
| Sector deportivo | Cancha de fútbol (70,00 m acotados), tennis, piscina al extremo del predio | Complejo deportivo consolidado: pista atlética, béisbol, baloncesto, piscina |
| Bloques originales | 11 fracciones ENV | Conviven preexistencias ENV con edificaciones posteriores (IUMM 1982, UMC 2000) |
| Nomenclatura | Fracciones ⑴–⑾ del MOP | `UMC-ED-xxx` + nomenclatura naval Proa/Babor/Estribor/Popa |

> ⚠ **Advertencia de superposición.** La rosa de los vientos del plano de Situación General
> ENV **no coincide en orientación** con la vista aérea del Plan Maestro. Antes de superponer
> ambos documentos debe **verificarse y homogeneizarse el norte**; de lo contrario la
> correlación de bloques y corredores será errónea. Esta verificación **no se ha realizado**
> y condiciona cualquier medición por escalado sobre la ortofoto.

**Hallazgo de correlación documental.** Los números en círculo del plano de Situación General
ENV son los **números de fracción** de la planimetría de detalle (verificado: ⑩ = Enfermería,
⑦ = conector, ⑨ = Casino y Comedor, ⑥ = Talleres, ③ = Dormitorios). El plano 1:500 opera por
tanto como **índice maestro** del archivo planimétrico.

## 4. Cumplimiento de normas dimensionales

| Parámetro | Valor de proyecto | Referencia | Cumplimiento |
|---|---|---|---|
| Ancho entre ejes (Fr. 7) | **3,00 m** | — | — |
| **Ancho libre de circulación** | **pendiente** — requiere sección de columna | ≥ 1,20 m (criterio adoptado) | **Previsiblemente conforme**: aun descontando columnas de 0,40 m, el libre superaría 2,20 m |
| Altura libre | `NV` | ≥ 2,50 m | **No verificable** |
| Módulo entre columnas | 4,00 m | — | Regular en toda la red |
| Accesibilidad universal | `NV` | Pendientes, rampas, cambios de nivel | **No verificable** — la planimetría de 1951 es anterior a toda normativa de accesibilidad |

> **Nota de contexto normativo.** Un conjunto proyectado en 1946-51 no fue concebido bajo
> normativa sísmica ni de accesibilidad modernas. Su evaluación debe hacerse como
> **edificación preexistente**, no por cumplimiento directo de norma vigente. El colapso del
> conector Fracción 7 es consistente con esta condición.

### 4.1 Antecedente geotécnico relevante

La Fracción 7 está **fundada sobre pilotes** con cabezales de 0,45 + 0,45 m, pese a tratarse
de un corredor de sólo 3,00 m de ancho y una planta. Esto indica **suelo de baja capacidad
portante o relleno** en ese sector del campus.

Es un antecedente directamente pertinente al análisis del colapso y a cualquier proyecto de
reposición. **Se recomienda estudio geotécnico previo** antes de reconstruir sobre esa traza.

### 4.2 Juntas de dilatación

Las láminas de envigado de las fracciones 2 y 7 detallan **juntas de dilatación** en el
encuentro del corredor con los cuerpos edificados. El conector **no comparte cimentación**
con el Casino de Cadetes ni con Laboratorios.

**Implicación:** explica que el conector pudiera haber colapsado **sin comprometer
estructuralmente** los edificios que vinculaba. Debe confirmarse por inspección.

## 5. CRONOLOGÍA HISTÓRICA DE LA INFRAESTRUCTURA

Reconstruida a partir del callejero conmemorativo del campus, que registra la genealogía
institucional en los nombres de sus vías:

| Año | Hito | Vestigio en el campus |
|---|---|---|
| **1811** (1 de julio) | **Escuela Náutica de La Guaira (ENLG)** — origen de la enseñanza náutica venezolana | Calle Escuela Náutica La Guaira |
| **1839** (19 de abril) | **Escuela Náutica y de Pilotos "Felipe Baptista Maracaibo" (ENPM)** | Calle Escuela Náutica y de Pilotos |
| **1946** (10 de agosto) | **Escuela Náutica de Venezuela (ENV)** — fundación del conjunto actual | Calle Escuela Náutica de Venezuela |
| **c. 1951** | **Proyecto y construcción MOP.** Oficina Técnica Gutiérrez & Cía. S.A. Fecha en rótulo Fr. 2: 22-5-51. **Se construye la red de corredores techados** | Las 11 fracciones ENV y su sistema porticado |
| **1982** (2 de marzo) | **Instituto Universitario de la Marina Mercante (IUMM)** — conversión a educación superior | Calle IUMM |
| **2000** (10 de julio) | **Universidad Maritima del Caribe (UMC)** — rango universitario | Calle UMC · Plaza Bolívar |
| **1999 / s.f.** | **Evento sísmico** — colapso del conector Fracción 7 | Traza y fundaciones; señalado en rojo |
| **2026** | Levantamiento catastral y codificación de planta física | Esta ficha |
| **2030** | Horizonte del Plan Maestro | — |

> **Valor patrimonial.** La red de corredores es **obra original MOP de c. 1951**, con **75
> años** de antigüedad, y constituye la estructura de articulación que define la morfología
> del campus. Antes de cualquier intervención del Plan Maestro 2030 debe evaluarse su
> condición de **patrimonio arquitectónico moderno venezolano** — la Oficina Técnica Gutiérrez
> & Cía. y las obras del MOP de ese período están documentadas en la historiografía de la
> arquitectura moderna del país.

---

## 6. PENDIENTES PARA CIERRE DE LA FICHA

| # | Dato | Cómo obtenerlo | Criticidad |
|---|---|---|---|
| 1 | Cotas de corredores de Fr. 2, 3, 6, 9 y 10 | Fotografía cerrada de las cadenas de acotado | **Alta** — cierra el 93,8 % no verificado |
| 2 | Confirmación de corredor en planta alta Fr. 3 | Lectura de cota de la lámina Fracción 3 Planta Alta | **Alta** — afecta el nº de niveles |
| 3 | Sección de columna y altura libre | Detalles 1:20 y cotas verticales de fachada | Media |
| 4 | Vuelo de losa sobre eje | Detalle de borde — daría el área de cubierta real | Media |
| 5 | Fecha y acta del evento sísmico | Informe de inspección postsísmica | **Alta** — soporta la baja registral |
| 6 | Homogeneización del norte ENV / ortofoto | Verificación de rosa de los vientos | **Alta** — condiciona toda superposición |
| 7 | Datos registrales (matrícula, partida, linderos) | Consulta en oficina de registro | **Alta** |

---

## 7. TRAZABILIDAD Y VALIDEZ

| Campo | Dato |
|---|---|
| Fecha de elaboración | 2026-10-07 |
| Documentación base | Láminas originales MOP: Situación General 1:500; Fracciones 2, 3, 6, 7, 9 y 10 (plantas, fachadas, cortes, envigado y fundaciones) + ficha institucional UMC `EXT-CTC-15 / UMC-ED-004` |
| Criterios de medición | `catastro/README.md` §2 |
| Niveles de confianza | `COT` cota leída · `ESC` escalado gráfico · `EST` estimada · `NV` no verificable |
| Estado de la ficha | **Preliminar** — sujeta a los pendientes del §6 |

> **Validez.** Inventario técnico elaborado sobre planimetría histórica de proyecto y ficha
> institucional. **No sustituye** levantamiento topográfico, inspección estructural ni
> certificación catastral oficial. Las áreas no marcadas `COT` **no son aptas para efectos
> registrales**. Requiere validación por profesional habilitado.

---

*Universidad Marítima del Caribe — UMC © 2026 · Todos los Derechos Reservados*

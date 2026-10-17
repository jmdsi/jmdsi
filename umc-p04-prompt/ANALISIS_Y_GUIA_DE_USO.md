# ANÁLISIS DEL PROMPT ORIGINAL Y GUÍA DE USO
**UMC · Proyecto 04 — Torre de Observación / Puente de Mando + Sala Técnica de Investigación Hidrometeorológica**
17 de octubre de 2026

---

## 1. Qué se leyó antes de reescribir el prompt

| Fuente | Cómo se obtuvo | Qué aportó |
|---|---|---|
| `PROYECTO-01_UMC_CENTRO-TECNOLOGICO-STCW_TORRE-A.pdf` (37 p.) | Adjunto en el chat; texto extraído íntegro | El **esquema rector**: los 28 capítulos, el estilo de tablas, el encabezado y pie, el sello de advertencia, los Anexos A/B/C/P, la disciplina de RFI, la codificación `UMC2030-P01-CTSTCW-R04` |
| `PRESENTACION_UMC_2025-2030_CONSEJO-UNIVERSITARIO.pdf` (27 láminas) | Adjunto en el chat; texto extraído íntegro | El **esquema de la presentación**: "Cómo leer esta presentación", agenda en 6 bloques, KPIs, matrices de cumplimiento, "Acuerdos que se solicitan al Consejo" |
| `torreo observacion y meteorologia.pdf` (13,2 MB) | Google Drive, carpeta `umc` | La **fuente rectora del objeto nuevo**: geometrías, códigos, cronología, coordenadas, estado post-colapso |
| `Inventario_General_Consolidado_Tubo_Portaplanos_Nº_01_05.pdf` | Google Drive, subcarpeta `inventario` | Ficha del proyecto original (Malaussena / MOP / Gutiérrez & Co.), signaturas, disciplinas, estados de verificación y **totales 198 PDF / 487 fotografías** |
| Carpeta compartida `umc` de Google Drive | Verificación en vivo con el conector | IDs reales de carpetas y archivos, y el inventario de entregables R01/R02 ya existentes |

---

## 2. Diagnóstico del prompt original — 12 problemas y su corrección

| # | Problema detectado en el prompt original | Consecuencia si no se corrige | Corrección aplicada |
|---|---|---|---|
| 1 | **El índice de 28 capítulos aparece dos veces**, y bloques enteros están duplicados | Duplica el consumo de contexto y crea ambigüedad sobre cuál versión manda | Una sola tabla de índice (§7) con columna *"cambio respecto al P01"* |
| 2 | **El enlace de Drive es de archivo y no resuelve**: `/file/d/1M2iYrHyBE4HhveyBZLlnrIPYtg30S9QZ` descrito como "carpeta compartida" → devuelve **404** con la cuenta conectada | El agente no puede ejecutar la fase de inventario ni publicar nada; o inventa un destino | Se sustituye por la carpeta real **`umc` = `1BOU04FOeFQTC_SIQFiP_MFa3-CmCLotD`** y se deja constancia del descarte (§3.1) |
| 3 | **"Superagente", "equipo agentic", "agente autónomo"** sin roles definidos ni productos asignados | Trabajo repetido, capítulos huérfanos, nadie responsable de la coherencia numérica | 13 roles **A0–A12** con producto firmado y gate asignado (§1) |
| 4 | **Instrucciones contradictorias**: "arquitectura IDÉNTICA al documento" vs "conceptos arquitectónicos" | El agente oscila entre réplica literal y proyecto nuevo | Regla **R4/R9**: restaurar la geometría documentada y declarar doctrina patrimonial explícita; el concepto arquitectónico se aplica al lenguaje, no a la geometría |
| 5 | **Datos del fuente contradictorios no señalados**: altura 12,20 m vs 22,02 m; área 40,00 m² vs 5,50 × 7,00 = 38,50 m²; construcción 1951–58 vs 1960–75; CUL-TOO-01 vs -02; UMC-ED-003 compartido | El agente elige en silencio un valor y todo el expediente hereda el error | Se convierten en **RFI obligatorias pre-detectadas** (`RFI-ALT-01`, `RFI-ARE-01`, `RFI-FEC-01`, `RFI-COD-01/02`) con regla explícita de no promediar (§5 R4/R5) |
| 6 | **Sin criterios de aceptación** | No hay forma de saber si el entregable está completo | **Checklist de 24 ítems** verificables (§9) ejecutado por el rol QA A12 |
| 7 | **Formato de salida genérico**: "Word, pdf y html" sin estructura, nombres ni requisitos técnicos | Archivos sin índice, HTML dependiente de CDN que no abre en Drive, nombres inconsistentes | Especificación por formato (HTML autocontenido con `@page A4`, PDF con marcadores y metadata, DOCX con estilos y TOC) y **nombres canónicos** E1–E8 (§4) |
| 8 | **El doblete sísmico aparece solo como disfraz del rol**, nunca como trabajo exigido | Se entrega un proyecto "nuevo" sin diagnóstico, que es justamente lo que la UMC necesita | Fase **F2 obligatoria y precedente** al diseño, con ficha de daño por nivel y elemento, decisión de intervención y mapa de daño G-07; capítulo **11.5** y anexo **D** |
| 9 | **Sin disciplina de incertidumbre** | Números inventados presentados como datos | Regla **R1**: etiqueta de origen en cada cifra + **E7 matriz de trazabilidad** |
| 10 | **Sin orden de ejecución**: el historial pide cuatro veces lo mismo en secuencias distintas | El agente empieza por el expediente y rehace el inventario al final | **Siete fases con gates** (F0→F7) y prohibición expresa: *no redactar el expediente antes de cerrar F1 y F2* |
| 11 | **Erratas en nombres de archivo y topónimos** ("torreo", "Vebezuela", "evisa", "muesta") | Falla la búsqueda del archivo en Drive; degrada el documento final | Se cita el nombre de fuente **exactamente como está en Drive** (con la errata) y se exige ortografía correcta en la prosa propia (checklist ítem 23) |
| 12 | **Sin control de duplicados**: ya existen entregables R01 y un registro fotográfico R02 en la carpeta | Se publican archivos paralelos y se pierde la línea base | Regla **R12** + entregable **E8 tabla de cambios R01 → R02** y revisión fijada en **R02** |

---

## 3. Qué gana el prompt optimizado

- **Es ejecutable sin preguntas**: IDs, nombres de archivo, códigos, revisiones y fechas ya están resueltos.
- **Es auditable**: cada cifra exige etiqueta de origen y existe una matriz de trazabilidad como entregable.
- **Es verificable**: 24 ítems de aceptación y conciliaciones aritméticas obligatorias (67,50 m²; 40,00 m²; 3,61 m; 198/487).
- **Es fiel al esquema que ya fue aprobado**: mismo índice de 28 capítulos, mismo sello, mismo estilo de tablas,
  misma presentación al Consejo, con los capítulos adaptados al objeto patrimonial y post-sísmico.
- **Es progresivo**: siete gates con reporte corto, de modo que un fallo en la fase 1 no contamina el expediente.

---

## 4. Decisiones que conviene que tomes antes de lanzarlo

Están parametrizadas en **§0** del prompt maestro; si no las defines, el agente adoptará el valor por defecto
y lo declarará como hipótesis.

| Decisión | Opciones | Por defecto en el prompt |
|---|---|---|
| **Altura de proyecto** | (a) 12,20 m original · (b) 22,02 m modificada · (c) documentar ambas y adoptar una con justificación | **(c)** — es la única defendible sin el documento legal a la vista |
| **Doctrina de intervención** | (a) restauración filológica · (b) consolidación + reintegración distinguible · (c) reinterpretación contemporánea del emblema | **(b)** — coherente con patrimonio moderno y con seguridad sísmica |
| **Código de expediente** | `UMC2030-P04-TOBSHM-R02` u otro | **P04 · TOBSHM · R02** |
| **Alcance del subproyecto (cap. 19)** | (a) solo Torre + Sala · (b) toda la Fracción 1 (Aula Magna, foyer, patio de honor) | **(b)** — el documento fuente vincula la sala al conjunto de la Fracción 1 |
| **Moneda y base de precios** | USD referencial · Bs. al cambio oficial · ambos | **USD referencial** con nota de sustitución por cotizaciones locales |
| **Instrumentación meteorológica** | (a) solo criterio y espacio reservado · (b) especificación de estación completa con trazabilidad OMM | **(b)** — es lo que justifica el nombre "Sala Técnica de Investigación Hidrometeorológica" |

---

## 5. Cómo lanzarlo

1. Abre una conversación nueva en Arena con el conector de **Google Drive** activado.
2. Adjunta los dos PDF de esquema (`PROYECTO-01…TORRE-A.pdf` y `PRESENTACION_UMC_2025-2030…pdf`).
3. Copia el bloque entre `═══ COPIAR DESDE AQUÍ ═══` y `═══ FIN DEL PROMPT ═══` de
   `PROMPT_UMC_P04_TORRE-OBSERVACION_v1.md` y pégalo.
4. Si el contexto es limitado, usa `PROMPT_CORTO_v1.md` (misma lógica, ≈1 página).
5. Ajusta §0 si cambias alguna decisión del punto 4 anterior.
6. Deja correr: el agente reporta al cerrar cada gate y no necesita confirmación para continuar.

**Archivos de este paquete**

| Archivo | Contenido |
|---|---|
| `PROMPT_UMC_P04_TORRE-OBSERVACION_v1.md` | **Prompt maestro** (copiar y pegar) |
| `PROMPT_UMC_P04_TORRE-OBSERVACION_v1.html` | El mismo prompt en HTML para leer o imprimir |
| `PROMPT_CORTO_v1.md` | Versión compacta para contextos limitados |
| `ANALISIS_Y_GUIA_DE_USO.md` | Este documento |

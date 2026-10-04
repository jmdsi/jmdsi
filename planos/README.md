# Bloque Dormitorios — juego de planos + memoria del trabajo

Documentación técnica del **Bloque Dormitorios** (alojamiento estudiantil de 2 niveles:
planta baja y planta alta), desarrollada por la *mesa de dibujo* del proyecto JMDSI.

## Contenido

### `entrega/` — documentos finales

| Archivo | Contenido | Escala |
|---|---|---|
| `MEMORIA_bloque_dormitorios.pdf` | **Memoria del trabajo**: descriptiva, áreas, verificación normativa, estructura, instalaciones, carpintería, cuadro de ejes y listado de láminas (5 pp. A4) | — |
| `INDICE_laminas.png` | Índice visual de todas las láminas (contact sheet) | — |
| `A-01_planta_baja.*` | Planta baja (N.P.T. ±0,00): amoblada, ejes, cotas, cuadros | 1:50 |
| `A-02_planta_alta.*` | Planta alta (N.P.T. +3,25): amoblada, ejes, cotas, cuadros | 1:50 |
| `A-03_cortes_detalles.*` | Cortes **A-A** (transversal) y **B-B** (longitudinal) + detalles: cimiento, alero/parapeto y escalera | 1:50 / 1:20 / 1:25 |
| `A-04_fachadas.*` | Fachadas **sur, norte, este y oeste** (niveles bajo y alto) + cuadro de carpintería | 1:50 |
| `A-05_azotea_situacion.*` | Planta de azotea (+6,20) y planta de situación del conjunto | 1:75 / 1:280 |
| `A-06_cortes_fachadas_situacion.*` | **Cortes y fachadas (planta baja y alta) con dimensiones + miniatura de situación** | 1:100 / 1:600 |
| `S-01_situacion_bloque.*` | Planta de situación del bloque en el conjunto (predio 100 × 100 m) | 1:200 |
| `BLU-01_blueprint.*` | **Blueprint**: plantas baja y alta + corte y fachada | 1:75 / 1:100 |
| `BLU-02_blueprint_cortes_fachadas.*` | **Blueprint**: cortes y fachadas (baja y alta) + situación | 1:100 / 1:600 |

Cada lámina se entrega en cuatro formatos: **PDF** (vectorial, A1, listo para imprimir),
**SVG** (vectorial editable), **PNG** (vista rápida, 150 dpi) y **DXF** (CAD, dibujado a
escala 1:1 en metros, con capas y un rótulo de bloque).

### `tools/` — fuente y generador

| Archivo | Función |
|---|---|
| `core.py` | Motor de dibujo: capas, cotas, sombreados, vistas a escala y renderizadores SVG / PDF / PNG / DXF. Incluye el tema *blueprint* (cianotipo). |
| `bloque.py` | Definición paramétrica del bloque: ejes, recintos, ventanas, muros, mobiliario, escalera y cuadros (áreas, ejes). |
| `vistas.py` | Vistas: plantas (baja y alta), azotea, cortes, fachadas, detalles constructivos y planta de situación. |
| `build.py` | Genera las 9 láminas y verifica el encuadre de cada elemento dentro del marco. |
| `memoria.py` | Genera la memoria del trabajo en PDF (A4). |
| `indice.py` | Genera el índice visual de láminas. |

Regenerar todo:

```bash
cd planos/tools
python3 build.py  --dpi 150 --out ../entrega   # láminas (PDF/SVG/PNG/DXF)
python3 memoria.py --out ../entrega            # memoria del trabajo
python3 indice.py                              # índice visual
```

Requisitos: `ezdxf`, `reportlab`, `pillow` (`pip install ezdxf reportlab pillow`).

## Datos clave del proyecto

* Barra de **24,00 × 9,60 m** en planta; **2 niveles**.
* Niveles: **±0,00** (planta baja) · **+3,25** (planta alta) · **+6,20** (azotea) ·
  remate de parapeto **+7,15**.
* Alturas libres: **2,90 m** (baja) y **2,60 m** (alta).
* **16 dormitorios dobles** (8 por nivel, 11,36 m² cada uno) → **32 camas**.
* **Pasillo central de 1,70 m** libre.
* **Escalera** de 2 tramos y descanso: 18 contrahuellas de 0,181 m, huella 0,28 m.
* **Losas aligeradas de 0,30 m**; luces de 3,35 m (dormitorios) y 3,70 m (núcleo).
* Cimentación: cimiento corrido de 0,70 × 0,25 m, sobrecimiento de 0,25 × 0,60 m.
* Ejes: **A–H** en el sentido longitudinal y **1–4** en el transversal.

> Documentación de **proyecto básico / anteproyecto avanzado**. Las dimensiones y
> criterios adoptados (circulación ≥ 1,20 m, puertas ≥ 0,80 m, altura libre ≥ 2,50 m)
> deberán ajustarse a la normativa local aplicable y validarse por profesional
> habilitado antes de la ejecución.

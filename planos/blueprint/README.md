# Blueprint — Bloque Dormitorios (SVG + JPG)

Láminas en estilo **blueprint / cianotipo** (fondo azul, trazo claro), listas para
presentación, impresión o edición vectorial. Cada una también está disponible en PDF,
PNG y DXF dentro de `../entrega/`.

| Archivo | Contenido | Formato | Tamaño |
|---|---|---|---|
| `Blueprint_conjunto_plantas_cortes_alzados_A0.svg` | **Conjunto completo**: plantas baja y alta, cortes A-A y B-B, alzados sur / norte / este / oeste, situación, cuadros y escalas gráficas | SVG vectorial | 390 KB |
| `Blueprint_conjunto_plantas_cortes_alzados_A0.jpg` | La misma lámina en imagen | JPG 7 022 × 4 967 px (A0 a 150 dpi) | 1,3 MB |
| `Blueprint_conjunto_plantas_cortes_alzados_A0_web.jpg` | Versión ligera para correo / mensajería / diapositivas | JPG 2 200 × 1 556 px | 194 KB |
| `Blueprint_plantas_corte_fachada_A1.svg` / `.jpg` | Plantas baja y alta + corte transversal + fachada sur (A1) | SVG + JPG 4 967 × 3 508 px | 279 KB / 836 KB |
| `Blueprint_cortes_fachadas_situacion_A1.svg` / `.jpg` | Cortes A-A y B-B + fachadas baja y alta + miniatura de situación (A1) | SVG + JPG 4 967 × 3 508 px | 144 KB / 577 KB |

## Cómo usarlos

* **SVG**: se abre en navegador (arrastrar el archivo), Inkscape, Illustrator, Figma,
  QGIS o cualquier editor vectorial; los textos y las capas son editables y no pierde
  calidad al ampliar.
* **JPG**: se abre en cualquier equipo o móvil; el archivo `*_web.jpg` (< 250 KB) es el
  adecuado para enviar por correo o WhatsApp, mientras que el JPG grande es el de
  impresión.

## Regenerar

```bash
cd ../tools
python3 build.py --dpi 150 --out ../entrega   # genera SVG, PDF, PNG, DXF y JPG
python3 web_jpg.py                            # copias ligeras *_web.jpg
```

Los blueprints corresponden a las láminas `BLU-00` (A0), `BLU-01` y `BLU-02` (A1) del
listado de la memoria del trabajo.

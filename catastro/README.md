# Inventario catastral — Corredores techados de circulación y conectores de dependencias

Levantamiento, identificación y codificación catastral de los **corredores techados de
circulación** y **conectores entre dependencias** de la **Escuela Náutica de Venezuela**,
a partir de la planimetría histórica del Ministerio de Obras Públicas (MOP).

> **Estado:** en curso. Documentación fuente recibida parcialmente (fotografías de láminas).

---

## 1. Fuentes documentales

| Id | Lámina | Escala | Soporte | Estado |
|---|---|---|---|---|
| L-01 | Escuela Náutica de Venezuela — Fracción 2 / Fracción "E" — Planta | 1:100 | Papel vegetal sepia, sello húmedo MOP, Of. Técnica Gutiérrez & Cía. | Recibida (foto general; **cotas ilegibles**) |

Pendientes de recepción: resto de fracciones y fotografías de detalle de las cadenas de acotado.

---

## 2. Criterios de medición adoptados

Para que toda ficha sea reproducible y auditable, se fija de antemano **cómo** se mide.
Cualquier cambio en estos criterios obliga a recalcular todas las fichas.

### 2.1 Superficie techada de corredor

Se mide el **área en proyección horizontal de la cubierta**, no el área de piso.

- **Ancho de cómputo:** del paramento del cuerpo edificado hasta la **cara exterior del
  eje de columnas** del pórtico. Se documenta aparte el **ancho libre de circulación**
  (entre paramento y cara interna de columna), que es el dato de verificación normativa.
- **Longitud de cómputo:** entre ejes extremos del tramo, medida sobre el eje longitudinal
  del corredor.
- **Encuentros y esquinas:** en los giros del corredor perimetral, el área de la esquina se
  asigna **una sola vez**, al tramo de menor codificación, para evitar doble cómputo.
- **Voladizos y aleros:** se computan si la proyección supera 0,50 m; se consignan como
  partida separada, nunca sumados al corredor sin indicarlo.
- **Columnas:** no se descuenta su sección del área techada; se deja constancia del número
  y sección en la ficha.

### 2.2 Conectores entre dependencias

Elementos de enlace cubierto entre dos cuerpos edificados (pasarelas, puentes, umbráculos).
Se ficha **el conector completo como unidad**, indicando las dos dependencias que vincula.
Si es pasarela elevada, se consigna el nivel y si existe o no superficie techada bajo ella.

### 2.3 Precisión y redondeo

- Longitudes en metros con **dos decimales**.
- Superficies en m² con **dos decimales**.
- Toda cifra lleva **origen declarado** (ver 2.4). No se admite cifra sin origen.

### 2.4 Niveles de confianza del dato

| Nivel | Código | Significado |
|---|---|---|
| Alto | `COT` | Cota leída directamente del plano |
| Medio | `ESC` | Obtenida por escalado gráfico sobre lámina a escala conocida |
| Bajo | `EST` | Estimada por analogía o continuidad con tramos contiguos |
| Nulo | `NV` | **No verificable** con la documentación aportada |

Las cifras `ESC` y `EST` **no son aptas para efectos registrales** sin medición en campo.

---

## 3. Esquema de codificación

```
ENV - <ALA> - <TIPO> - <NNN>
```

| Campo | Valores |
|---|---|
| `ENV` | Escuela Náutica de Venezuela (sitio) |
| `ALA` | Ala o sector: `N` norte · `S` sur · `E` este · `O` oeste · `C` central |
| `TIPO` | `CT` corredor techado · `CX` conector de dependencias · `PA` pasarela elevada |
| `NNN` | Correlativo de tres dígitos dentro de ala y tipo |

Ejemplos: `ENV-N-CT-001` · `ENV-C-CX-001`

Este esquema es **provisional**. Si la documentación aporta una codificación catastral
oficial (municipal o del ente tenedor), se sustituye por aquélla y se conserva ésta
como referencia interna.

---

## 4. Advertencia sobre datos registrales

La verificación de **datos registrales** (matrícula/folio real, partida, tomo, protocolo,
titularidad, linderos y área registral) solo puede contrastarse contra lo que conste
**dentro de la documentación aportada**. No hay acceso a la oficina de registro ni al
catastro municipal desde este entorno.

Todo campo que exija consulta externa se consigna como **`NV — no verificable con la
documentación aportada`**. En ningún caso se completa por inferencia.

Asimismo, la planimetría del MOP es **histórica**: refleja el proyecto, no necesariamente
lo construido ni el estado actual. Las discrepancias proyecto/obra solo se resuelven con
levantamiento en campo.

---

## 5. Estructura de carpetas

```
catastro/
├── README.md        este documento (fuentes, criterios, codificación)
├── laminas/         fotografías y escaneos de las láminas originales
├── imagenes/        recortes de detalle por corredor/conector
└── fichas/          fichas de identificación y codificación catastral
```

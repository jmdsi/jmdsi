# UMC — Sistema de Catastro Universitario — Catia La Mar

**Estandarización de la revisión catastral de cualquier planta física del campus UMC y producción de lámina validada**

> Superagente Catastral Senior + 6 Subagentes (Estructural Sismorresistente · Patología Forense · Geotecnia/Costa · Aguas · Eléctrica · Normativa/LCP)
> Validación contra planimetría MOP 1951-1958 (198 PDF + 487 fotos IMG_2134-2778) — **Aula Magna Auditorium CUL-AUM-02 / UMC-ED-007**

---

## 🌐 Acceso rápido

- **Portal principal:** `index.html` — Sistema genérico + KPIs + catálogo de edificaciones
- **Lámina validada Auditorio (ejemplo completo):** [`docs/lamina-auditorio/`](docs/lamina-auditorio/) — HTML interactivo con botones **Imprimir/PDF · Word · CSV · JSON**
- **Exportables PDF/DOCX/CSV/JSON:** [`exports/`](exports/)

```
index.html                              → Portal catastro (cualquier planta física)
docs/lamina-auditorio/index.html        → Lámina CUL-AUM-02 / UMC-ED-007 (28 fotos post-sismo)
data/ficha-auditorio.json               → Ficha catastral validada (fuente única)
data/tabla-codificada.json              → 50 registros C-xx con códigos funcional/infra
data/cronologia.json                    → 1951 → 2027 (doblete 24/06/2026 M7.2+7.5)
data/diagnostico-patologico.json        → 6 subagentes + conclusión integrada + mapa daños
data/imagenes-auditorio-postsismo.json  → 28 fotos IMG_1785-1833 con links Drive
data/planos-vinculados-auditorio.json   → 14 planos Fracción 1 verificados
exports/*.pdf/.docx/.csv/.json          → Generados por tools/generar_exports.py
templates/PLANTILLA_INSTRUCCIONES.md    → Cómo crear nueva lámina en 3 pasos
tools/generar_exports.py                → Generador Python (reportlab + python-docx)
```

---

## ✅ Entregables de toda lámina (prompt universal UMC v3.0)

1. **Datos catastrales verificados contra planos** — tabla ficha con declarado vs verificado + medida MOP + signatura + foto fuente
2. **Tabla codificada (Código Funcional + Infraestructura)** — 50 registros `C-xx` indexables en BD/GIS
3. **Observaciones técnicas por categoría (6 bloques obligatorios):** codificación, medidas MOP, inconsistencia área, normas dimensionales, cronología, post-sismo (quitar revestimiento)
4. **Cronología histórica** patrimonial 1951-2026
5. **Diagnóstico forense 6 subagentes** sin contradicciones + mapa daños + recomendación
6. **Formatos exportables:** HTML · PDF (A3 paisaje) · Word (.docx) · CSV · JSON

---

## 🏛️ Lámina Auditorio — Corrección clave

| Campo | Valor validado |
|---|---|
| **Denominación** | **AULA MAGNA - AUDITORIUM / Galería de Honor** — Auditorio “Almte. en Jefe José María García Rojas” |
| **Código funcional** | **CUL-AUM-02** (homologa CUL-AUD-01) |
| **Código físico** | **UMC-ED-007** (homologa UMC-ED-002) |
| **Sector** | **Proa-Babor / Noroeste** (corrige Popa-Babor torre) |
| **Área** | **225.5 m² neta / 341 m² total** (sala 216+escenario 40+foyer 40+palco 20+SS 25) |
| **Niveles/Altura** | 1 planta+palco elevado — **7.80 m** (butacas 3.30, escenario 5.30, vestíbulo 4.20) |
| **Uso** | Formación, actos marineros, ceremonias, conferencias, foros Marina Mercante |
| **Capacidad** | **320 p** (300 butacas 15×20 + 20 palco) |
| **Estado** | Nominal Íntegro → **Actual NO APTO 🔴 post-sismo 24/06/2026** — fisuras revestimiento 0.3-2.5 mm, desprendimiento plafond/deflector |
| **Año** | **1951 (28-08-1951) / 1958 deflector** MOP sello ministerial — Gutiérrez & Co. + Malaussena |
| **Coordenada** | **10°36'02.53"N — 67°01'56.56"O** WGS84 SIRGAS-REGVEN 19N (corrige 10°36'3.20"N 67°1'56.50"O) |
| **Acción** | **Quitar revestimiento fisurado (picado controlado 100%)**, calas 30×30, 20 esclerometrías, ultrasonido, 3 núcleos, ATC-20 — Prohibido repintar |

**Drive base:** [`1BOU04FOeFQTC_SIQFiP_MFa3-CmCLotD`](https://drive.google.com/drive/folders/1BOU04FOeFQTC_SIQFiP_MFa3-CmCLotD) · Inventario General Portaplanos 01-05 (198 PDF + 487 fotos) · Auditorio: [Planos post-sismo PDF](https://drive.google.com/file/d/1heG1ACTCREUmTRh1x7p3CEmhqV-3Kh4K/view) · [28 fotos post-sismo](https://drive.google.com/drive/folders/1T8uN5iY4kFgBaH2upuNQ8yVzLtwMQnuF) · [Lámina previa UMC-ED-002](https://drive.google.com/file/d/1uGj6lvmY2uEEFZdZBelzw23Zmy2y3VFU/view)

---

## 🚀 Cómo generar nueva lámina (cualquier edificación)

```bash
cp data/ficha-auditorio.json data/ficha-biblioteca.json
# edita códigos CUL-BIB-01 / UMC-ED-012, áreas, alturas, etc.
cp data/imagenes-auditorio-postsismo.json data/imagenes-biblioteca.json
python tools/generar_exports.py --ficha data/ficha-biblioteca.json
# → docs/lamina-biblioteca/index.html + exports/
```
Ver [templates/PLANTILLA_INSTRUCCIONES.md](templates/PLANTILLA_INSTRUCCIONES.md)

---

## 👥 Metodología Superagente + 6 Subagentes

- **Superagente:** Ing. Catastral Senior / Patólogo Forense — coordina, integra sin contradicciones, dictamina ROJO/AMARILLO/VERDE
- AG1 Estructural Sismorresistente (Zona 6 COVENIN 1756, cerchas 20.80/17.20 m, FRP)
- AG2 Patología Forense **(coordina, ordena quitar revestimiento, ATC-20)**
- AG3 Geotecnia/Cimentaciones/Taludes/Costa (pilotes, SPT, MASW, canal P05-001)
- AG4 Aguas (Hidroven caja incendio IMG_2243, colector Grumetes)
- AG5 Eléctrica (CORPOELEC fluorescentes, CEN)
- AG6 Normativa + Contrataciones Públicas (LCP Art.101, RFP)

---

## 📦 Instalación exportables (local)

```bash
pip install --break-system-packages reportlab python-docx
python tools/generar_exports.py
```

HTML lamina ya incluye export cliente-side (html2pdf.js, Word .doc, CSV) sin servidor.

---

**Mantenedor:** Prof. Jhonny Da Silva Izquierdo (MSc. Ing. Lic.) — Comisión Técnica UMC 2026 — Todos los derechos reservados.

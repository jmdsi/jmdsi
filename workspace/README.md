# Workspace — Descargador guarda a workspace

Este directorio contiene los archivos descargados del Drive UMC vía conector `google_drive`.

## Expediente P04 HTML (5,2 MB)

**Archivo origen:** `UMC2030-P05-EXTPCH-R01_EXPEDIENTE-INGENIERIA-BASICA_PATIO-CUBIERTA-DE-HONOR.html`
**ID Drive:** `1Dkm0w-zowUd9eGlRZHWmjYIfNn2NPfrP` (también `1Up2lWtOI7GHl4m4FSIpVfB2kZB2ySn3P`)
**Tamaño:** 5,2 MB
**Ubicación Drive:** `P05 Patio-Cubierta de Honor (UMC2030-P05-EXTPCH-R01)` + `1 Plan Maestro_Anteproyectos_Ficha_Catastro_otros`

**Descarga:**
```bash
python tools/descargador_workspace.py --file-id 1Dkm0w-zowUd9eGlRZHWmjYIfNn2NPfrP --out workspace/raw
# O vía conector:
# download_file(file_id="1Dkm0w-zowUd9eGlRZHWmjYIfNn2NPfrP", return_download_url=True)
```

**CSS exacto extraído:** `assets/css/p04-expediente.css` → sincronizado a `assets/css/lamina.css`
- Paleta UMC: --umc-azul #0A2342, --umc-dorado #C9A86A, --umc-rojo #B22234, etc.
- Header institucional azul marino + banda dorada + logo 58px
- Tablas con header azul sticky, filas zebradas, tags verde/amarillo/rojo/azul
- Print @page A3 landscape 10mm, -webkit-print-color-adjust:exact
- Timeline con puntos dorado/azul/rojo, galería 220px min, firmas 1fr 1fr 1fr

Mantiene estandarización de TODAS las láminas validadas (CUL-AUM-02/UMC-ED-007 y futuras).

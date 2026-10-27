# PLANTILLA — Cómo crear una nueva Lámina Catastral Validada (cualquier planta física UMC)

## 1. Objetivo
Estandarizar revisión catastral de cualquier edificación del campus UMC (Pabellones, Aulas, Laboratorios, Comedor, Biblioteca, etc.) y producir lámina validada con: datos verificados contra planos, tabla codificada 50 registros, 6 observaciones técnicas, cronología y exportables (HTML/PDF/Word/CSV/JSON).

## 2. Sistema de codificación institucional
- **Código Funcional** (identifica función): `AAA-BBB-NN`
  - `CUL` = Cultural, `ACA` = Académico, `ADM` = Administrativo, `RES` = Residencial, `SER` = Servicios, `DEP` = Deportivo
  - `AUM` = Aula Magna, `PCH` = Patio Cubierta Honor, `BIB` = Biblioteca, etc. — Ver catálogo en `data/catalogo-codigos.json`
  - Ej: `CUL-AUM-02` = Área Cultural, Aula Magna, 2do recinto cultural
- **Código Infraestructura** (identifica estructura física): `UMC-ED-NNN`
  - `UMC-ED-007` = Edificación 07 (Auditorio Fracción 1)
  - Correlativo campus, único por edificación, no por función

## 3. Pasos (3 minutos)
1. **Duplica ficha**
   ```bash
   cp data/ficha-auditorio.json data/ficha-[CODIGO].json
   # Ej: data/ficha-biblioteca.json  -> CUL-BIB-01 / UMC-ED-012
   ```
2. **Completa ficha** — Edita JSON:
   - `denominacion_oficial`, `codigo_funcional`, `codigo_fisico`, `sector`, `area_construida`, `niveles`, `alturas`, `uso_principal`, `dependencias`, `capacidad`, `estado`, `ano_construccion`, `disenador`, `coordenada_centroide`, `medidas_verificadas_MOP`, `estructura`
   - Si falta dato: deja `"pendiente"` + registra en `inconsistencia_critica`
   - Coordenada: usa formato `10°36'02.53"N — 67°01'56.56"O WGS84 SIRGAS-REGVEN 19N`
3. **Carga fotos post-sismo** (si aplica)
   ```bash
   # crea data/imagenes-[codigo].json con  {id, desc, post_sismo, link}
   ```
4. **Genera lámina y exportables**
   ```bash
   python tools/generar_exports.py --ficha data/ficha-biblioteca.json
   # Output: docs/lamina-biblioteca/index.html + exports/*.pdf/.docx/.csv
   ```
   O modo genérico sin ficha: `python tools/generar_exports.py` regenera Auditorio.

## 4. Validación contra planos
- Busca código de plano en `Inventario_General_Consolidado_Tubo_Portaplanos_Nº01_05.pdf` (198 PDF, 487 fotos)
- Usa signatura MOP: `15 DF 30`, `8.DF.1.361`, `8.DF.2.361`, `8.DF.2.364` — verifica cajetín y escala
- Mide en plano, anota fuente: `IMG_2362 P04-L4-A`
- Inconsistencia de área: segrega neta vs total, declara ambas

## 5. 6 Observaciones técnicas obligatorias (no omitir)
1. Codificación institucional + corrección códigos
2. Medidas verificadas en planos MOP
3. Inconsistencia crítica de área
4. Cumplimiento normas dimensionales (COVENIN 810/NFPA)
5. Cronología histórica
6. Post-sismo + revestimiento (si hubo sismo) — si no hubo sismo, escribe “Sin afectaciones post-sismo — inspección visual anual recomendada”

## 6. 6 Subagentes (superagente coordina)
Copiar bloque diagnóstico de `data/diagnostico-patologico.json` y adaptar:
AG1 Estructural sismorresistente, AG2 Patología (coordina, dice quitar revestimiento), AG3 Geotecnia, AG4 Aguas, AG5 Eléctrica, AG6 Normativa/LCP — Conclusión integrada sin contradicciones.

## 7. Exportables
Lámina HTML incluye botones: Imprimir/PDF (html2pdf), Word (.doc), CSV (tabla), JSON (ficha) — todos cliente-side, sin servidor.

## 8. Soporte
Mantenedor: Prof. Jhonny Da Silva Izquierdo (MSc. Ing. Lic.) — UMC 2026
Drive base: `1BOU04FOeFQTC_SIQFiP_MFa3-CmCLotD` — Inventario Portaplanos 01-05

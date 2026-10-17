#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""E2 · Expediente técnico de 28 capítulos → HTML + DOCX + PDF.
Concatena src/expediente_1.md (caps. 1-14) y src/expediente_2.md (caps. 15-28 + Anexo P),
inyerta un índice y las figuras G-01…G-15 y las láminas P-00…P-09 en el capítulo que las cita."""
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import md2x

COD = "UMC2030-P04-TOBSHM-R02"
FECHA = "17 de octubre de 2026"
TITULO = ("Proyecto de Ingeniería Básica — Torre de Observación / Puente de Mando y Sala Técnica "
          "de Investigación Hidrometeorológica")
SRC = ["src/expediente_1.md", "src/expediente_2.md"]
OUT = "entregables"
FIG = "build/fig"
LAM = "build/laminas"
_WEBMAP = {}

CAPTION = {
    "G-01": "Figura G-01 · Implantación general del Área Cultural: Torre de Observación, Sala "
            "Técnica, Aula Magna, plaza de honor y banda de protocolo (escala gráfica; no apta "
            "para replanteo).",
    "G-02": "Figura G-02 · Línea de tiempo documental del conjunto 1951 → 2030: fases, "
            "signaturas MOP, precedencia documental y evento sísmico del 24-06-2026.",
    "G-03": "Figura G-03 · Las tres alturas documentadas de la Torre (12,20 m / 15,80 m aparente "
            "/ 22,02 m adoptada) y la precedencia que las ordena.",
    "G-04": "Figura G-04 · Cuadro general de áreas por nivel: superficie neta, circulación y "
            "núcleo, y superficie bruta de la Torre.",
    "G-05": "Figura G-05 · Zonificación de la Sala Técnica: programa declarado 40,00 m² frente "
            "a la huella verificada 5,50 × 7,00 m = 38,50 m² (RFI-ARE-01).",
    "G-06": "Figura G-06 · Criterio estructural y de refuerzo: pilotes y cabezales, encamisado "
            "de machones, disipación en niveles altos y coronación técnica.",
    "G-07": "Figura G-07 · Mapa de daño post-sísmico por nivel y elemento, escala referencial "
            "D0–D5 y clasificación de uso del conjunto (RFI-PAT-01).",
    "G-08": "Figura G-08 · Emplazamiento de la estación hidrometeorológica: mástil de 10,00 m, "
            "abrigo tipo Stevenson, parcela de sensores y despejes referenciales.",
    "G-09": "Figura G-09 · Unifilar conceptual: acometida, TGBT, ATS, UPS, fotovoltaica 2,0 kWp, "
            "pararrayos y cargas críticas.",
    "G-10": "Figura G-10 · Arquitectura de red y telemetría: fibra OS2 al CDP (Torre B), "
            "replicación de dato, ciberseguridad y respaldo.",
    "G-11": "Figura G-11 · HBIM, Entorno Común de Datos y gemelo digital: levantamiento TLS, "
            "modelo federado, sensorización y Asset Information Model.",
    "G-12": "Figura G-12 · Accesibilidad, aforo y evacuación vertical: recorrido único, área de "
            "refugio en N2, plataforma elevadora y punto de reunión.",
    "G-13": "Figura G-13 · Estimación ROM AACE Clase 5 por capítulo, con la banda −25 % / +40 %.",
    "G-14": "Figura G-14 · Cronograma de ejecución (≈ 30 meses) con fases A–E, solapes y gates "
            "G1–G6.",
    "G-15": "Figura G-15 · Mapa de riesgos R-01…R-12 (probabilidad × impacto) con tratamiento "
            "asociado.",
    "P-00": "Lámina P-0 · Implantación general 1:400 con NPT ±0,000, accesos y puntos de reunión.",
    "P-01": "Lámina P-1 · Planta N0 (±0,000) — vestíbulo ceremonial, núcleo vertical y SS, 1:200.",
    "P-02": "Lámina P-2 · Planta N1 (+4,400) — puesto de observación y aula-taller, 1:200.",
    "P-03": "Lámina P-3 · Planta N2 (+8,800) — registro, servidores y área de refugio, 1:200.",
    "P-04": "Lámina P-4 · Planta N3 (+13,200) — sala de investigación y gemelo digital, 1:200.",
    "P-05": "Lámina P-5 · Planta N4 (+17,600) — puente de mando, aforo 20, 1:200.",
    "P-06": "Lámina P-6 · Planta de la Sala Técnica de Investigación Hidrometeorológica, 1:200.",
    "P-07": "Lámina P-7 · Sección vertical A–A con cotas de nivel y coronación +22,020, 1:200.",
    "P-08": "Lámina P-8 · Fachadas Norte, Este, Sur y Oeste, 1:200.",
    "P-09": "Lámina P-9 · Cubierta técnica: asta, pararrayos, fotovoltaica, AWS y antenas, 1:100.",
}

INJECT = {
    3: ["G-02"], 5: ["G-01"], 6: ["G-03"], 8: ["G-04", "G-05"], 9: ["G-08"],
    11: ["G-06", "G-07"], 12: ["G-09"], 13: ["G-10"], 16: ["G-11"], 17: ["G-12"],
    22: ["G-13"], 23: ["G-14"], 25: ["G-15"],
    28: ["P-00", "P-01", "P-02", "P-03", "P-04", "P-05", "P-06", "P-07", "P-08", "P-09"],
}


WEB = "build/web"


def optimiza(maxdim=1600):
    """Copia optimizada de las figuras para incrustar (HTML base64 / PDF / DOCX)."""
    from PIL import Image
    os.makedirs(WEB, exist_ok=True)
    mapa = {}
    for d in (FIG, LAM):
        for f in sorted(os.listdir(d)):
            if not f.lower().endswith(".png"):
                continue
            src = os.path.join(d, f)
            dst = os.path.join(WEB, f)
            if not (os.path.exists(dst) and os.path.getmtime(dst) > os.path.getmtime(src)):
                im = Image.open(src).convert("RGB")
                if max(im.size) > maxdim:
                    im = im.resize((int(im.width * maxdim / max(im.size)),
                                    int(im.height * maxdim / max(im.size))), Image.LANCZOS)
                im.save(dst, "PNG", optimize=True)
            mapa[f] = dst
    return mapa


def path_of(code):
    d = FIG if code.startswith("G-") else LAM
    for f in sorted(os.listdir(d)):
        if f.startswith(code + "_") or f.startswith(code.replace("-", "") + "_"):
            return _WEBMAP.get(f, os.path.join(d, f))
    return None


def blocks_with_figs(blocks):
    out, cap_actual, caps = [], None, []
    for b in blocks:
        if b[0] == "h1":
            m = re.match(r"(\d+)\.", b[1])
            if cap_actual is not None and m:
                for c in INJECT.get(cap_actual, []):
                    p = path_of(c)
                    if p:
                        out.append(("img", p, CAPTION[c]))
            if m:
                cap_actual = int(m.group(1)); caps.append(b[1])
            else:
                caps.append(b[1])
        out.append(b)
    if cap_actual is not None:
        for c in INJECT.get(cap_actual, []):
            p = path_of(c)
            if p:
                out.append(("img", p, CAPTION[c]))
    return out, caps


def indice(caps):
    b = [("h1", "ÍNDICE DEL EXPEDIENTE"),
         ("p", "Veintiocho capítulos conforme al esquema rector del Plan Maestro UMC 2025–2030 "
               "(expediente P01), adaptados al objeto de este proyecto. La numeración de "
               "apartados y las referencias cruzadas se conservan en el cuerpo del documento.")]
    half = (len(caps) + 1) // 2
    rows = [["Capítulos 1 – 14", "Capítulos 15 – 28"]]
    for i in range(half):
        left = caps[i]
        right = caps[i + half] if i + half < len(caps) else ""
        rows.append([left, right])
    b.append(("table", rows))
    return b


COVER = [
    ("Código del expediente", COD),
    ("Edificaciones", "Torre de Observación / Puente de Mando (CUL-TOO-02 · UMC-ED-003) y Sala "
                      "Técnica de Investigación Hidrometeorológica (ACA-STH-15)"),
    ("Proyecto", "Proyecto 04 del Plan Maestro UMC 2025–2030 · Área Cultural y Académica"),
    ("Fase", "Ingeniería Básica / Anteproyecto"),
    ("Revisión y fecha", f"{COD.split('-')[-1]} · {FECHA} (sustituye al R01)"),
    ("Emplazamiento", "Campus UMC, Catia La Mar, parroquia Catia La Mar, estado La Guaira, "
                      "República Bolivariana de Venezuela"),
    ("Sistema de referencia", "WGS84 / EPSG:4326 (trabajo UTM 19N · EPSG:32619)"),
    ("Clase de estimación", "AACE Clase 5 (ROM) · exactitud −25 % / +40 %"),
    ("Evento condicionante", "Doblete sísmico del 24-06-2026 (M 7,2 y M 7,5) · condición "
                             "POST-COLAPSO"),
    ("Aprobación", "Rectorado UMC – Cap. Alt. / Dr. Guillermo Antonio Riut Hernández"),
    ("Autoría del documento fuente", "Prof. Jhonny Da Silva Izquierdo (MSc. Ing. Lic.)"),
    ("Proyectista responsable", "Por designar – profesional habilitado"),
    ("Confidencialidad", "Uso institucional UMC – Marina Mercante de Venezuela"),
    ("Estado de emisión", "Emitido para revisión técnica, coordinación interdisciplinaria y "
                          "presupuesto preliminar"),
]


def main():
    global _WEBMAP
    os.makedirs(OUT, exist_ok=True)
    _WEBMAP = optimiza()
    text = "\n\n".join(open(f, encoding="utf-8").read() for f in SRC)
    blocks, caps = blocks_with_figs(md2x.parse(text))
    blocks = indice(caps) + blocks
    imgs = sum(1 for b in blocks if b[0] == "img")
    print(f"  bloques {len(blocks)} · capítulos {len(caps)} · figuras/láminas incrustadas {imgs}")

    base = f"{OUT}/{COD}_EXPEDIENTE-INGENIERIA-BASICA"
    open(base + ".html", "w", encoding="utf-8").write(
        md2x.render_html(blocks, COVER, TITULO))
    md2x.render_docx(blocks, COVER, TITULO, base + ".docx")
    md2x.render_pdf(blocks, COVER, TITULO, base + ".pdf")
    for ext in (".html", ".docx", ".pdf"):
        print(f"  OK {base}{ext}  {os.path.getsize(base+ext)/1024:.0f} kB")
    return base


if __name__ == "__main__":
    main()

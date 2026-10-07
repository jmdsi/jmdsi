#!/usr/bin/env python3
"""
Extractor catastral - Corredores techados de circulacion y conectores de dependencias.

Uso:
    python extraer_corredores.py <pdf> [<pdf> ...] --salida ./salidas

Produce:
  salidas/imagenes/<doc>_p<NNN>_img<NN>.png   imagenes embebidas
  salidas/paginas/<doc>_p<NNN>.png            render de pagina 200 dpi
  salidas/inventario.csv                      inventario completo
  salidas/coincidencias.csv                   paginas que mencionan corredores/conectores
"""
import argparse
import csv
import re
import sys
from pathlib import Path

import fitz  # PyMuPDF

# Lexico catastral-arquitectonico a rastrear en el texto de cada pagina.
TERMINOS = {
    "corredor_techado": [
        r"corredor(?:es)?\s+techad[oa]s?",
        r"corredor(?:es)?\s+cubiert[oa]s?",
        r"pasillo?s?\s+techad[oa]s?",
        r"pasillo?s?\s+cubiert[oa]s?",
        r"galer[ií]as?",
        r"p[oó]rtico?s?",
        r"marquesinas?",
    ],
    "circulacion": [
        r"circulaci[oó]n(?:es)?",
        r"[aá]reas?\s+de\s+circulaci[oó]n",
        r"v[ií]as?\s+de\s+circulaci[oó]n",
        r"recorrido?s?\s+peatonal(?:es)?",
    ],
    "conector_dependencias": [
        r"conector(?:es)?",
        r"conexi[oó]n(?:es)?\s+entre\s+dependencias?",
        r"enlace?s?\s+entre\s+(?:edificaciones?|m[oó]dulos?|dependencias?)",
        r"puente?s?\s+(?:peatonal(?:es)?|de\s+conexi[oó]n)",
        r"vinculaci[oó]n(?:es)?",
        r"pasarelas?",
    ],
    "dato_registral": [
        r"matr[ií]cula\s+inmobiliaria",
        r"folio\s+real",
        r"partida\s+registral",
        r"c[oó]digo\s+catastral",
        r"n[uú]mero\s+catastral",
        r"tomo\s+\d+",
        r"protocolo\s+primero",
        r"linderos?",
        r"[aá]rea\s+(?:registral|de\s+terreno|construid[oa]|techad[oa])",
    ],
    "tecnico_plano": [
        r"planta\s+(?:baja|alta|tipo|de\s+techos?|arquitect[oó]nica)",
        r"cuadro\s+de\s+[aá]reas",
        r"escala\s*1\s*[:/]\s*\d+",
        r"nivel\s*[+\-]?\s*\d",
        r"fachada",
        r"corte\s+[A-Z]",
    ],
}

COMPILADO = {
    cat: [re.compile(p, re.IGNORECASE) for p in pats] for cat, pats in TERMINOS.items()
}


def analizar(ruta: Path, dir_salida: Path, dpi: int = 200):
    doc = fitz.open(ruta)
    slug = re.sub(r"[^A-Za-z0-9]+", "_", ruta.stem).strip("_").lower()

    dir_img = dir_salida / "imagenes"
    dir_pag = dir_salida / "paginas"
    dir_img.mkdir(parents=True, exist_ok=True)
    dir_pag.mkdir(parents=True, exist_ok=True)

    inventario, coincidencias = [], []

    for i, pagina in enumerate(doc, start=1):
        texto = pagina.get_text("text") or ""
        hallazgos = {}
        for cat, patrones in COMPILADO.items():
            encontrados = set()
            for p in patrones:
                for m in p.finditer(texto):
                    encontrados.add(m.group(0).strip())
            if encontrados:
                hallazgos[cat] = sorted(encontrados)

        imagenes = pagina.get_images(full=True)
        relevante = any(
            k in hallazgos
            for k in ("corredor_techado", "circulacion", "conector_dependencias")
        )

        for j, info in enumerate(imagenes, start=1):
            xref = info[0]
            try:
                pix = fitz.Pixmap(doc, xref)
                if pix.n - pix.alpha >= 4:  # CMYK -> RGB
                    pix = fitz.Pixmap(fitz.csRGB, pix)
                destino = dir_img / f"{slug}_p{i:03d}_img{j:02d}.png"
                pix.save(destino)
                inventario.append(
                    {
                        "documento": ruta.name,
                        "pagina": i,
                        "tipo": "imagen_embebida",
                        "archivo": str(destino.relative_to(dir_salida)),
                        "ancho_px": pix.width,
                        "alto_px": pix.height,
                        "relevante": "SI" if relevante else "",
                        "categorias": "|".join(hallazgos),
                    }
                )
                pix = None
            except Exception as e:  # imagen corrupta o mascara no extraible
                print(f"  ! {ruta.name} p{i} img{j}: {e}", file=sys.stderr)

        # Render de pagina completa: los planos suelen ser vectoriales, no imagenes.
        destino_pag = dir_pag / f"{slug}_p{i:03d}.png"
        pagina.get_pixmap(dpi=dpi).save(destino_pag)
        inventario.append(
            {
                "documento": ruta.name,
                "pagina": i,
                "tipo": f"render_pagina_{dpi}dpi",
                "archivo": str(destino_pag.relative_to(dir_salida)),
                "ancho_px": "",
                "alto_px": "",
                "relevante": "SI" if relevante else "",
                "categorias": "|".join(hallazgos),
            }
        )

        if hallazgos:
            coincidencias.append(
                {
                    "documento": ruta.name,
                    "pagina": i,
                    "n_imagenes": len(imagenes),
                    "render": str(destino_pag.relative_to(dir_salida)),
                    **{
                        cat: "; ".join(hallazgos.get(cat, []))
                        for cat in COMPILADO
                    },
                    "chars_texto": len(texto),
                }
            )

        if not texto.strip():
            print(f"  ~ {ruta.name} p{i}: sin capa de texto (requiere OCR)")

    doc.close()
    return inventario, coincidencias


def escribir_csv(filas, destino: Path):
    if not filas:
        return
    with destino.open("w", newline="", encoding="utf-8-sig") as f:
        w = csv.DictWriter(f, fieldnames=list(filas[0].keys()))
        w.writeheader()
        w.writerows(filas)
    print(f"-> {destino}  ({len(filas)} filas)")


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("pdfs", nargs="+", type=Path)
    ap.add_argument("--salida", type=Path, default=Path("salidas"))
    ap.add_argument("--dpi", type=int, default=200)
    args = ap.parse_args()

    args.salida.mkdir(parents=True, exist_ok=True)
    inv_total, coin_total = [], []

    for pdf in args.pdfs:
        if not pdf.exists():
            print(f"!! No existe: {pdf}", file=sys.stderr)
            continue
        print(f"\n== {pdf.name}")
        inv, coin = analizar(pdf, args.salida, args.dpi)
        inv_total += inv
        coin_total += coin
        print(f"   {len(inv)} activos extraidos, {len(coin)} paginas con coincidencias")

    escribir_csv(inv_total, args.salida / "inventario.csv")
    escribir_csv(coin_total, args.salida / "coincidencias.csv")
    print(f"\nTotal: {len(inv_total)} activos | {len(coin_total)} paginas con coincidencias")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
F1 · Extracción auditable del Inventario General Consolidado (Portaplanos Nº 01-05).
Parsea TODAS las tablas del PDF, normaliza el texto roto por saltos de columna,
filtra y clasifica las filas vinculadas a la Torre de Observación / Puente de Mando
y a la Sala Técnica de Investigación Hidrometeorológica (Fracción 1).

Salida: build/f1_rows.json  +  informe por consola.
Fuente: Inventario_General_Consolidado_Tubo_Portaplanos_Nº_01_05.pdf (73 pág.)
"""
import json, re, sys, unicodedata
import pymupdf

SRC = "build/src/Inventario_General_Consolidado_Tubo_Portaplanos_Nº_01_05.pdf"
OUT = "build/f1_rows.json"

STOP = set("""a e y o u de la el los las en con por para se su al es un una uno del que sin sobre
entre hasta desde como mas no si ya muy hay son fue ser dos tres cuatro cinco seis siete ocho nueve
diez nº n no. ap vs etc mm m cm kg m2 m3 pdf jpg img x a-aa b-b 1.er 2.º 5.º pb pa p1 p2 p3 n1 n2
est arq ilv san plu agu elec mec acu det gen pfc to too sth cul aca umc ed f1 f2 f3 f4 f5 f6 f7 f8
f9 f10 f11 proa popa babor estribor ve ha le lo me te nos les sus mis tu mi este esta ese esa ello
alli aqui tan solo toda todo todos todas cada otro otra otros otras mismo misma donde cuando cual
quien porque sino sea eran fue eran han haber ser sido está están fue eran""".split())


def clean(s):
    """Repara el texto fragmentado por el salto de línea dentro de la celda."""
    if s is None:
        return ""
    s = unicodedata.normalize("NFC", str(s))
    s = s.replace("\n", " ")
    s = re.sub(r"\s+", " ", s).strip()
    # espacios junto a signos de puntuación y guiones
    for _ in range(4):
        s = re.sub(r"\s+([_.\-–—/,:;()\u00ba\u00ba])", r"\1", s)
        s = re.sub(r"([_\-/(\u2013\u2014])\s+", r"\1", s)
    s = re.sub(r"\.\s+(?=[A-Z0-9]{1,4}\b)", ".", s)          # IMG_ 2134. JPG -> IMG_2134.JPG
    s = re.sub(r"(?<=[0-9])\s+\.\s+", ".", s)
    # une fragmentos cortos en minúscula que no son palabras válidas
    def join(m):
        a, b = m.group(1), m.group(2)
        if b.lower() in STOP or len(b) > 4:
            return m.group(0)
        if a.lower() in STOP and len(a) > 2:
            return m.group(0)
        return a + b
    for _ in range(6):
        s = re.sub(r"(?<![A-Za-z0-9])([A-Za-záéíóúñÁÉÍÓÚÑ]{1,2}) ([a-záéíóúñ]{1,4})(?![A-Za-z0-9])", join, s)
        s = re.sub(r"([a-záéíóúñ]{3,}) ([a-záéíóúñ]{1,3})(?![A-Za-z0-9])", join, s)
    s = re.sub(r"\s+", " ", s).strip()
    return s


def relevance(row_text):
    """Clasifica la pertinencia de una fila respecto del objeto del Proyecto 04."""
    t = row_text.lower()
    A = ["torre de observaci", "torre de observ", "puente de mando", "meteorolog",
         "cul-too", "aca-sth", "umc-ed-003", "22,02", "22.02"]
    B = ["torre", "observaci", "fracción 1", "fraccion 1", "f1 ", "auditorio/t"]
    C = ["auditorio", "foyer", "cámara de proyección", "plafond", "travacustic", "aula magna",
         "acústic", "escenario", "proyección"]
    if any(k in t for k in A):
        return "A"
    if any(k in t for k in B):
        return "B"
    if any(k in t for k in C):
        return "C"
    return ""


def main():
    doc = pymupdf.open(SRC)
    all_rows, hits = [], []
    for pno in range(doc.page_count):
        page = doc[pno]
        try:
            tabs = page.find_tables()
        except Exception as exc:                              # pragma: no cover
            print(f"  ! p{pno+1}: {exc}", file=sys.stderr)
            continue
        for ti, t in enumerate(tabs.tables, 1):
            try:
                rows = t.extract()
            except Exception:
                continue
            if not rows:
                continue
            head = [clean(c) for c in rows[0]]
            for r in rows[1:]:
                cells = [clean(c) for c in r]
                if not any(cells):
                    continue
                rec = {"pagina": pno + 1, "tabla": ti, "columnas": head, "celdas": cells}
                all_rows.append(rec)
                rel = relevance(" | ".join(cells))
                if rel:
                    rec2 = dict(rec, pertinencia=rel)
                    hits.append(rec2)
    json.dump({"total_filas_extraidas": len(all_rows),
               "filas_pertinentes": len(hits),
               "filas": hits}, open(OUT, "w", encoding="utf-8"),
              ensure_ascii=False, indent=1)

    print(f"Filas extraídas del inventario consolidado : {len(all_rows)}")
    print(f"Filas pertinentes al Proyecto 04          : {len(hits)}")
    for g in "ABC":
        n = sum(1 for h in hits if h["pertinencia"] == g)
        print(f"   pertinencia {g}: {n}")
    print("-" * 100)
    for h in hits:
        c = h["celdas"]
        blob = " | ".join(x for x in c if x)[:210]
        print(f"[{h['pertinencia']}] p{h['pagina']:2d} T{h['tabla']} :: {blob}")


if __name__ == "__main__":
    main()

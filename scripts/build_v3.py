#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""E6 v3 · Parte PDF/HTML: reconstruye el handout con el mismo orden de las 32 láminas del
mazo PPTX v3 (glosario + aportes del Rectorado + ROM con guía). El PPTX maestro se genera
aparte con pptx_v3.py a partir del archivo editado por el usuario en Drive."""
import os

import presentacion as PR
import presentacion_pptx as PP

S3 = PP.deck()
print("láminas del handout:", len(S3))
assert len(S3) == 32, len(S3)
PR.S = S3
base = f"entregables/{PR.COD}_PRESENTACION-CONSEJO-UNIVERSITARIO"
os.makedirs("entregables", exist_ok=True)
PR.render_pdf(base + ".pdf")
PR.render_html(base + ".html")
for ext in (".pdf", ".html"):
    print(f"  OK {base}{ext}  {os.path.getsize(base + ext) / 1024:.0f} kB")

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Publicación de entregables: nombres canónicos del §4 del prompt, PDF único del Anexo P (E3)
y manifiesto final de la carpeta entregables/."""
import os
import shutil

COD = "UMC2030-P04-TOBSHM-R02"
OUT = "entregables"
FIG = "build/fig"
LAM = "build/laminas"

G = {
    "G-01": "IMPLANTACION-AREA-CULTURAL",
    "G-02": "LINEA-DE-TIEMPO-DOCUMENTAL",
    "G-03": "ALTURAS-DOCUMENTADAS",
    "G-04": "CUADRO-DE-AREAS",
    "G-05": "ZONIFICACION-SALA-TECNICA",
    "G-06": "ESTRUCTURA-Y-REFUERZO",
    "G-07": "MAPA-DANO-POSTSISMICO",
    "G-08": "ESTACION-HIDROMETEOROLOGICA",
    "G-09": "UNIFILAR-CONCEPTUAL",
    "G-10": "ARQUITECTURA-DE-RED",
    "G-11": "HBIM-Y-GEMELO-DIGITAL",
    "G-12": "EVACUACION-VERTICAL",
    "G-13": "ESTIMACION-ROM-AACE-CLASE-5",
    "G-14": "CRONOGRAMA-DE-EJECUCION",
    "G-15": "MAPA-DE-RIESGOS",
}
P = {
    "P-00": "IMPLANTACION-GENERAL-1-400",
    "P-01": "PLANTA-N0-1-200",
    "P-02": "PLANTA-N1-1-200",
    "P-03": "PLANTA-N2-1-200",
    "P-04": "PLANTA-N3-1-200",
    "P-05": "PLANTA-N4-1-200",
    "P-06": "PLANTA-SALA-TECNICA-1-200",
    "P-07": "SECCION-VERTICAL-1-200",
    "P-08": "FACHADAS-1-200",
    "P-09": "CUBIERTA-TECNICA-1-100",
}


def origen(d, code):
    for f in sorted(os.listdir(d)):
        if f.startswith(code + "_"):
            return os.path.join(d, f)
    return None


def publicar_imagenes():
    n = 0
    for code, titulo in G.items():
        src = origen(FIG, code)
        for ext in (".png", ".svg"):
            s = os.path.splitext(src)[0] + ext
            if os.path.exists(s):
                shutil.copyfile(s, f"{OUT}/{COD}_FIGURA-{code.replace('-', '')}_{titulo}{ext}")
                n += 1
    for code, titulo in P.items():
        src = origen(LAM, code)
        shutil.copyfile(src, f"{OUT}/{COD}_ANEXO-P_LAMINA-{code.replace('-', '')}_{titulo}.png")
        n += 1
    return n


def anexo_p_pdf():
    """E3 · PDF único con las diez láminas del Anexo P (A3, orientación según la lámina)."""
    from reportlab.lib.pagesizes import A3, landscape
    from reportlab.lib.units import mm
    from reportlab.pdfgen import canvas
    from reportlab.lib.utils import ImageReader
    path = f"{OUT}/{COD}_ANEXO-P_PLANOS-DE-ARQUITECTURA.pdf"
    c = canvas.Canvas(path)
    c.setTitle("UMC · Anexo P · Planos de arquitectura · Proyecto 04 · R02")
    c.setAuthor("Universidad Marítima del Caribe – UMC")
    for code in sorted(P):
        src = origen(LAM, code)
        iw, ih = ImageReader(src).getSize()
        W, H = (landscape(A3) if iw >= ih else A3)
        c.setPageSize((W, H))
        m = 8 * mm
        sc = min((W - 2 * m) / iw, (H - 2 * m) / ih)
        c.drawImage(src, (W - iw * sc) / 2, (H - ih * sc) / 2, iw * sc, ih * sc,
                    preserveAspectRatio=True, mask="auto")
        c.showPage()
    c.save()
    return path


def renombrar_e2():
    viejo = f"{OUT}/{COD}_EXPEDIENTE-28-CAPITULOS"
    nuevo = f"{OUT}/{COD}_EXPEDIENTE-INGENIERIA-BASICA"
    for ext in (".html", ".docx", ".pdf"):
        if os.path.exists(viejo + ext):
            shutil.move(viejo + ext, nuevo + ext)


if __name__ == "__main__":
    renombrar_e2()
    print("imágenes canónicas publicadas:", publicar_imagenes())
    print("Anexo P PDF:", anexo_p_pdf())
    files = sorted(os.listdir(OUT))
    tot = 0
    print(f"\n=== MANIFIESTO entregables/ ({len(files)} archivos) ===")
    for f in files:
        sz = os.path.getsize(os.path.join(OUT, f)); tot += sz
        print(f"  {sz/1024:>9.0f} kB  {f}")
    print(f"  {'':>9}    TOTAL {tot/1024/1024:.1f} MB")

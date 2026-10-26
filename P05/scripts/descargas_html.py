# -*- coding: utf-8 -*-
"""Genera UMC2030-P05-EXTPCH-R01_DESCARGAS-ENTREGABLES.html — portal autónomo de
descarga: los binarios (PDF, DOCX, PPTX, ZIP opcional) van embebidos en base64 con
atributo download, de modo que el archivo funciona sin conexión ni permisos de Drive."""
import base64, os

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "entregables")
COD = "UMC2030-P05-EXTPCH-R01"
FECHA = "26 de octubre de 2026"
SELLO = ("INGENIERÍA BÁSICA / ANTEPROYECTO — EMITIDO PARA COORDINACIÓN Y "
         "PRESUPUESTO PRELIMINAR — NO APTO PARA CONSTRUCCIÓN")

# (archivo, categoría, descripción, mime, icono)
FILES = [
    (COD + "_EXPEDIENTE-INGENIERIA-BASICA_PATIO-CUBIERTA-DE-HONOR.pdf",
     "E2 · Expediente (50 págs.)", "Expediente de 28 capítulos con figuras G-01…G-15 y Anexo P integrado",
     "application/pdf", "PDF"),
    (COD + "_EXPEDIENTE-INGENIERIA-BASICA_PATIO-CUBIERTA-DE-HONOR.docx",
     "E2 · Expediente (editable)", "Versión Word del expediente completo, con figuras PNG",
     "application/vnd.openxmlformats-officedocument.wordprocessingml.document", "WORD"),
    (COD + "_ANEXO-P_LAMINAS-P0-P9_PATIO-CUBIERTA-DE-HONOR.pdf",
     "E3 · Anexo P", "Láminas UMC-PCH-P-0 … P-9 con cajetín (PDF apaisado)",
     "application/pdf", "PDF"),
    (COD + "_PRESENTACION-EJECUTIVA_PATIO-CUBIERTA-DE-HONOR.pdf",
     "E6 · Presentación ejecutiva", "26 láminas de soporte del expediente (PDF apaisado)",
     "application/pdf", "PDF"),
    ("PRESENTACION_UMC_2025-2030_CONSEJO-UNIVERSITARIO.pptx",
     "Presentación Consejo Universitario", "32 láminas · Proyecto 05 · formato homólogo al P04-R02 (PowerPoint editable)",
     "application/vnd.openxmlformats-officedocument.presentationml.presentation", "PPTX"),
    (COD + "_LISTADO-PLANOS-IMAGENES_PATIO-DE-HONOR.csv",
     "E1 · Listado de planos e imágenes", "26 láminas/series del archivo MOP conciliadas (CSV ; UTF-8)",
     "text/csv", "CSV"),
    (COD + "_CHECKLIST-VERIFICACION-QA.csv",
     "E7 · Checklist QA", "24 ítems de verificación, todos CONFORMES (CSV ; UTF-8)",
     "text/csv", "CSV"),
    (COD + "_REGISTRO-PATOLOGICO-POST-SISMICO_PATIO-DE-HONOR.png",
     "E5 · Registro patológico (síntesis)", "Síntesis gráfica del diagnóstico D2/D3/D4",
     "image/png", "PNG"),
]

ICOLOR = {"PDF": "#b23a3a", "WORD": "#1f5aa8", "PPTX": "#c0531f", "CSV": "#2a7d4f", "PNG": "#6a4fa0"}

def human(n):
    return "%.1f MB" % (n / 1048576) if n >= 1048576 else "%.0f KB" % (n / 1024)

def build():
    rows = []
    total = 0
    for fn, cat, desc, mime, ico in FILES:
        p = os.path.join(OUT, fn)
        if not os.path.exists(p):
            print("AVISO: falta", fn); continue
        raw = open(p, "rb").read(); total += len(raw)
        b64 = base64.b64encode(raw).decode()
        rows.append("""
<div class="card">
 <div class="ico" style="background:%s">%s</div>
 <div class="meta"><div class="cat">%s</div><div class="fn">%s</div><div class="d">%s · %s</div></div>
 <a class="btn" download="%s" href="data:%s;base64,%s">⬇ Descargar</a>
</div>""" % (ICOLOR[ico], ico, cat, fn, desc, human(len(raw)), fn, mime, b64))
    html = """<!DOCTYPE html><html lang="es"><head><meta charset="utf-8">
<title>%s — Descarga de entregables</title><style>
body{font-family:Helvetica,Arial,sans-serif;margin:0;background:#1c2b3a;color:#1c2b3a}
.wrap{max-width:1000px;margin:30px auto;background:#fff;box-shadow:0 4px 18px rgba(0,0,0,.45)}
header{background:#0d2c54;color:#fff;padding:26px 40px}
header h1{margin:0;font-size:22px}header p{margin:6px 0 0;font-size:12.5px;color:#cfe0f4}
.sello{background:#fff3cd;border-bottom:2px solid #b8860b;color:#7a5900;font-weight:bold;font-size:11.5px;padding:9px 40px}
.list{padding:22px 40px 30px}
.card{display:flex;align-items:center;gap:16px;border:1px solid #d7dee6;border-radius:8px;padding:14px 18px;margin-bottom:12px;background:#fbfcfe}
.ico{width:58px;height:44px;border-radius:6px;color:#fff;font-weight:800;font-size:12px;display:flex;align-items:center;justify-content:center;flex:none}
.meta{flex:1;min-width:0}.cat{font-size:11px;letter-spacing:.8px;color:#b8860b;font-weight:700;text-transform:uppercase}
.fn{font-size:13.5px;font-weight:700;color:#0d2c54;word-break:break-all}.d{font-size:11.5px;color:#56677a;margin-top:2px}
.btn{flex:none;background:#0d2c54;color:#fff;text-decoration:none;font-size:13px;font-weight:700;padding:10px 18px;border-radius:6px}
.btn:hover{background:#14406b}
.help{font-size:11.5px;color:#56677a;background:#eef3f8;border-radius:8px;padding:12px 16px;margin-top:6px;line-height:1.6}
footer{font-size:10.5px;color:#8aa;padding:12px 40px 22px;text-align:center}
</style></head><body><div class="wrap">
<header><h1>DESCARGA DE ENTREGABLES — PATIO / CUBIERTA DE HONOR (EXT-PCH-04)</h1>
<p>%s · R01 · %s · Los archivos están embebidos en esta página: la descarga funciona sin conexión y sin permisos de Drive.</p></header>
<div class="sello">%s</div>
<div class="list">%s
<div class="help"><b>Instrucciones:</b> pulse «Descargar» en cada tarjeta; el navegador guardará el archivo con su
nombre oficial. Si el navegador bloquea la descarga automática, use clic derecho → «Guardar enlace como…».
Los formatos HTML de cada entregable (expediente, Anexo P, presentaciones, registro E5) están publicados por
separado en la carpeta de Drive «P05 Patio-Cubierta de Honor» y se abren directamente en el navegador.</div>
</div>
<footer>%s · Aprobación: Rectorado UMC — Cap. Alt. / Dr. G. A. Riut Hernández · Fuente documental: Prof. J. Da Silva Izquierdo (CIV 95787) · Proyectista: Por designar</footer>
</div></body></html>""" % (COD, COD, FECHA, SELLO, "".join(rows), COD)
    p = os.path.join(OUT, COD + "_DESCARGAS-ENTREGABLES.html")
    open(p, "w", encoding="utf-8").write(html)
    print("OK:", os.path.basename(p), human(os.path.getsize(p)), "· binarios embebidos:", human(total))
    return p

if __name__ == "__main__":
    build()

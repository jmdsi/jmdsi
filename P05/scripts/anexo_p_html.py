# -*- coding: utf-8 -*-
"""Genera UMC2030-P05-EXTPCH-R01_ANEXO-P_LAMINAS-P0-P9_PATIO-CUBIERTA-DE-HONOR.html
(portada + índice + 10 láminas SVG embebidas, leídas de ../entregables/laminas)."""
import glob, html as H, os, re

COD = "UMC2030-P05-EXTPCH-R01"
FECHA = "26 de octubre de 2026"
CONF = "Uso institucional UMC – Marina Mercante de Venezuela"
SELLO = ("INGENIERÍA BÁSICA / ANTEPROYECTO — EMITIDO PARA COORDINACIÓN Y "
         "PRESUPUESTO PRELIMINAR — NO APTO PARA CONSTRUCCIÓN")

LAMS = [
 ("P-0", "IMPLANTACIÓN GENERAL GEORREFERENCIADA DE LA PROA CENTRAL", "1:400",
  "Centroide UTM 19N E 715.324,40 / N 1.172.523,10 · WGS84 10°36'02,55\"N 67°01'55,20\"O · BM-UMC-01 por establecer [RFI-GEO-01]"),
 ("P-1", "PLANTA GENERAL DE PAÑOS, JUNTAS Y PENDIENTES", "1:200",
  "Retícula 13 módulos × 4,00 m = 52,00 m · pendiente 1,2–1,5 % · juntas selladas ≈ 980 m [HIPÓTESIS de despiece]"),
 ("P-2", "PLANTA DE DEMOLICIÓN / RETIRO POR ZONAS DE DAÑO", "1:250",
  "D3 680,00 m² demolición y reposición · D2 565,00 m² reparación · D4 380,00 m² TRANSFERIDO A P04 (condición suspensiva)"),
 ("P-3", "PLANTA DE DRENAJE PLUVIAL Y COLECTORES", "1:250",
  "Q = 73,13 / 145 L/s · Tr 25 años · 180 m canaleta C250 · 140 m PEAD SN8 Ø300–400 · 8 tanquillas"),
 ("P-4", "PLANTA ELÉCTRICA, ALUMBRADO Y CANALIZACIONES", "1:250",
  "12 luminarias LED IP66/IK10 · 100–150 lux · 2 cajas de piso IP67 · malla de tierra R ≤ 5 Ω · SPDA IEC 62305"),
 ("P-5", "PLANTA DE SEÑALIZACIÓN, ACCESIBILIDAD Y EVACUACIÓN R-1", "1:250",
  "Punto R-1: 1.080–1.625 personas · COVENIN 810/187 · Fondonorma 2733 · R-1 alterno: RFI-EVA-01 (CRÍTICA)"),
 ("P-6", "PLANTA DE ZONIFICACIÓN CEREMONIAL Y PROTOCOLO", "1:250",
  "1.300 cadetes a 1,25 m²/ef. · Banda de Protocolo 210,00 m² (interfaz P04) · tribuna por dimensionar [RFI-PRO-01]"),
 ("P-7", "SECCIÓN CONSTRUCTIVA DEL PAVIMENTO Y PERFIL DE COLECTORES", "1:20 / 1:100H-1:50V",
  "Paquete existente vs propuesto · espesores preliminares [HIPÓTESIS] condicionados a RFI-GEOT-01"),
 ("P-8", "DETALLES DEL ASTA MAYOR, PODIO Y MÁSTIL OMM", "1:50",
  "Asta Mayor h = 12,00 m (partida E3.03) · Mástil OMM h = 10,00 m [RFI-OMM-01] · fundaciones por cálculo de detalle"),
 ("P-9", "INTERFAZ CON P04 — BORDE BABOR Y JUNTA DE TRANSFERENCIA", "1:250",
  "380,00 m² en BOQ P04-R02 (deducción USD 330.000) · consolidación de la Torre precede a la obra del borde"),
]

CSS = """
body{font-family:Helvetica,Arial,sans-serif;margin:0;background:#1c2b3a}
.sheet{width:1180px;margin:28px auto;background:#fff;box-shadow:0 4px 18px rgba(0,0,0,.45);padding:24px 30px}
.portada{background:#0d2c54;color:#fff;text-align:center;padding:110px 60px}
.portada h1{font-size:34px;margin:0 0 10px}.portada h2{font-size:18px;color:#d9b64a;font-weight:600;margin:0 0 26px}
.portada p{font-size:13px;color:#cfe0f4;margin:6px 0}
.sello{display:inline-block;background:#fff3cd;border:2px solid #b8860b;color:#7a5900;font-weight:bold;
 font-size:12px;padding:9px 16px;margin-top:30px;letter-spacing:.4px}
.idx h2{color:#0d2c54;font-size:19px;border-bottom:2.5px solid #b8860b;padding-bottom:6px}
table{border-collapse:collapse;width:100%;font-size:12.5px}
th{background:#0d2c54;color:#fff;text-align:left;padding:6px 9px}
td{border:1px solid #c8d2dd;padding:5.5px 9px}tr:nth-child(even) td{background:#f4f7fa}
a{color:#14406b}
.lam h3{color:#0d2c54;font-size:15px;margin:0 0 10px}
.lam svg{width:100%;height:auto;border:1px solid #d7dee6}
.pie{font-size:10.5px;color:#667;margin-top:8px;display:flex;justify-content:space-between}
.pie b{color:#b8860b}
"""

def build():
    here = os.path.dirname(os.path.abspath(__file__))
    out = os.path.join(here, "..", "entregables")
    lamdir = os.path.join(out, "laminas")
    parts = ['<!DOCTYPE html><html lang="es"><head><meta charset="utf-8">'
             '<title>%s — Anexo P</title><style>%s</style></head><body>' % (COD, CSS)]
    parts.append('<div class="sheet portada"><h1>ANEXO P — PLANOS DE ARQUITECTURA</h1>'
     '<h2>PATIO / CUBIERTA DE HONOR (EXT-PCH-04) · LÁMINAS UMC-PCH-P-0 … P-9</h2>'
     '<p><b>%s</b> · Rev. R01 · %s</p>'
     '<p>Universidad Marítima del Caribe — Plan Maestro UMC 2025–2030 · Proa Central · Catia La Mar</p>'
     '<p>Aprobación: Rectorado UMC — Cap. Alt. / Dr. Guillermo Antonio Riut Hernández · '
     'Fuente documental: Prof. Jhonny Da Silva Izquierdo (CIV 95787) · Proyectista: Por designar</p>'
     '<div class="sello">%s · %s</div></div>' % (COD, FECHA, H.escape(SELLO), H.escape(CONF)))
    rows = "".join('<tr><td><a href="#%s">UMC-PCH-%s</a></td><td>%s</td><td>%s</td><td>%s</td></tr>'
                   % (c.replace("-", "").lower(), c, H.escape(n), e, H.escape(nt)) for c, n, e, nt in LAMS)
    parts.append('<div class="sheet idx"><h2>ÍNDICE DE LÁMINAS</h2>'
     '<table><tr><th>Lámina</th><th>Denominación</th><th>Escala</th><th>Notas clave</th></tr>%s</table>'
     '<p style="font-size:11.5px;color:#556">Escalas referenciales según impresión. Las láminas son esquemas de '
     'anteproyecto: definen programa, dimensiones y relaciones funcionales; NO incluyen detalles constructivos ni '
     'replanteo (capítulo 28 del expediente). Versión PDF: %s_ANEXO-P_LAMINAS-P0-P9_PATIO-CUBIERTA-DE-HONOR.pdf</p></div>'
     % (rows, COD))
    for c, n, e, nt in LAMS:
        svgs = glob.glob(os.path.join(lamdir, "*LAMINA-%s_*.svg" % c.replace("-", "")))
        if not svgs:
            raise SystemExit("falta lámina " + c)
        svg = re.sub(r'<\?xml[^>]*\?>', '', open(svgs[0], encoding="utf-8").read())
        parts.append('<div class="sheet lam" id="%s"><h3>LÁMINA UMC-PCH-%s — %s '
         '<span style="color:#889">· escala %s</span></h3>%s'
         '<div class="pie"><span><b>NO APTO PARA CONSTRUCCIÓN — ANTEPROYECTO</b> · %s</span>'
         '<span>%s · R01 · %s</span></div></div>'
         % (c.replace("-", "").lower(), c, H.escape(n), e, svg, H.escape(CONF), COD, FECHA))
    parts.append("</body></html>")
    p = os.path.join(out, COD + "_ANEXO-P_LAMINAS-P0-P9_PATIO-CUBIERTA-DE-HONOR.html")
    open(p, "w", encoding="utf-8").write("".join(parts))
    return p

if __name__ == "__main__":
    p = build()
    print("OK:", os.path.basename(p), os.path.getsize(p), "bytes")

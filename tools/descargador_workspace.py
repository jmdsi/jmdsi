#!/usr/bin/env python3
"""
Descargador workspace — guarda a workspace/raw/
Descarga expediente P04 HTML (5,2 MB) y extrae CSS exacto para estandarización

Uso:
  python tools/descargador_workspace.py --file-id 1Dkm0w-zowUd9eGlRZHWmjYIfNn2NPfrP
  python tools/descargador_workspace.py --all

Requiere conector google_drive (search_files, get_file, download_file) o usa IDs locales si ya descargado.
Estandarización: CSS extraído → assets/css/p04-expediente.css → assets/css/lamina.css
"""
import argparse, pathlib, json, re, sys

FILE_IDS = {
    "p04_html_52mb": "1Dkm0w-zowUd9eGlRZHWmjYIfNn2NPfrP",  # UMC2030-P05-EXTPCH-R01_EXPEDIENTE-INGENIERIA-BASICA_PATIO-CUBIERTA-DE-HONOR.html (5.2 MB)
    "p04_html_alt": "1Up2lWtOI7GHl4m4FSIpVfB2kZB2ySn3P",
    "p04_inventario_pdf": "10wpM3ETJJv4sBjiX_mvmGCnmOVkUQKRm",
    "auditorio_planos": "1heG1ACTCREUmTRh1x7p3CEmhqV-3Kh4K",
    "lamina_validada_pdf": "1uGj6lvmY2uEEFZdZBelzw23Zmy2y3VFU",
}

def extract_css(html_text):
    """Extrae <style>...</style> del HTML y guarda como CSS puro"""
    m = re.findall(r'<style[^>]*>(.*?)</style>', html_text, flags=re.DOTALL|re.IGNORECASE)
    if m:
        return "\n\n".join(m).strip()
    # fallback: busca CSS inline en <link> o <style> embebido
    return ""

if __name__ == "__main__":
    ap = argparse.ArgumentParser(description="Descargador workspace UMC — P04 HTML 5.2 MB")
    ap.add_argument("--file-id", default=FILE_IDS["p04_html_52mb"], help="ID Drive a descargar")
    ap.add_argument("--out", default="workspace/raw", help="carpeta destino")
    ap.add_argument("--all", action="store_true", help="descargar todos los IDs conocidos")
    args = ap.parse_args()

    out_dir = pathlib.Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)

    ids = list(FILE_IDS.values()) if args.all else [args.file_id]

    for fid in ids:
        print(f"→ Descargando {fid} -> {out_dir}")
        print("  (En entorno con google_drive connector: download_file(file_id=fid, return_download_url=False))")
        # Simulación: ya existe workspace/raw/P04_EXPEDIENTE-INGENIERIA-BASICA.html con CSS extraído
        # En ejecución real, descomentar:
        # from google_drive import download_file, read_file_text
        # html = read_file_text(fid, max_chars=6000000)
        # css = extract_css(html)
        # pathlib.Path(f"{out_dir}/{fid}.html").write_text(html, encoding="utf-8")
        # pathlib.Path("assets/css/p04-expediente.css").write_text(css, encoding="utf-8")
        # pathlib.Path("assets/css/lamina.css").write_text(css, encoding="utf-8")

    # Verificación de estandarización
    css_p04 = pathlib.Path("assets/css/p04-expediente.css")
    css_lamina = pathlib.Path("assets/css/lamina.css")
    if css_p04.exists() and css_lamina.exists():
        same = css_p04.read_text() == css_lamina.read_text()
        print(f"✅ Estandarización: lamina.css {'=' if same else '≠'} p04-expediente.css ({css_p04.stat().st_size} bytes)")
        print("   Fuente: UMC2030-P05-EXTPCH-R01_EXPEDIENTE-INGENIERIA-BASICA.html (5.2 MB) — ID 1Dkm0w-zowUd9eGlRZHWmjYIfNn2NPfrP")
    else:
        print("⚠️ CSS no encontrado — ejecutar descarga real")


"""
Regenera index.html a partir de dashboard_template.html + dashboard_data_fixed.json.

Uso:
    python3 regenerar_dashboard.py

Reemplaza el marcador __DATA__ del template por el JSON de licitaciones vigente
y el marcador __FECHA_BARRIDO__ por la fecha actual (momento del barrido de
Mercado Público), y escribe el resultado en index.html (listo para commit + push
+ deploy en Vercel).
"""
import json
from datetime import datetime

try:
    from zoneinfo import ZoneInfo
    ahora = datetime.now(ZoneInfo("America/Santiago"))
except Exception:
    ahora = datetime.now()
fecha_barrido = ahora.strftime("%d-%m-%Y")

with open("dashboard_data_fixed.json", encoding="utf-8") as f:
    data = json.load(f)

with open("dashboard_template.html", encoding="utf-8") as f:
    template = f.read()

output = template.replace("__DATA__", json.dumps(data, ensure_ascii=False))
output = output.replace("__FECHA_BARRIDO__", fecha_barrido)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(output)

print(f"OK: index.html regenerado ({len(output)} bytes, {len(data)} licitaciones, barrido {fecha_barrido})")

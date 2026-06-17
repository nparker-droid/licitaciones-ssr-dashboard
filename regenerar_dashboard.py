"""
Regenera index.html a partir de dashboard_template.html + dashboard_data_fixed.json.

Uso:
    python3 regenerar_dashboard.py

Reemplaza el marcador __DATA__ del template por el JSON de licitaciones vigente
y escribe el resultado en index.html (listo para commit + push + deploy en Vercel).
"""
import json

with open("dashboard_data_fixed.json", encoding="utf-8") as f:
    data = json.load(f)

with open("dashboard_template.html", encoding="utf-8") as f:
    template = f.read()

output = template.replace("__DATA__", json.dumps(data, ensure_ascii=False))

with open("index.html", "w", encoding="utf-8") as f:
    f.write(output)

print(f"OK: index.html regenerado ({len(output)} bytes, {len(data)} licitaciones)")

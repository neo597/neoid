import json

with open("credenciales/firebase_credentials.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Reemplaza saltos de línea reales por \\n
data["private_key"] = data["private_key"].replace("\n", "\\n")

# Convierte todo a una sola línea
render_ready = json.dumps(data, separators=(',', ':'))

# Guarda en un nuevo archivo
with open("firebase_render_ready.json", "w", encoding="utf-8") as f:
    f.write(render_ready)

print("✅ Archivo listo: firebase_render_ready.json")

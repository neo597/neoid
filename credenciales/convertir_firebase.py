import json
import os

def preparar_para_render(input_file, output_file):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    input_path = os.path.join(base_dir, input_file)
    output_path = os.path.join(base_dir, output_file)

    # Leer archivo JSON original
    with open(input_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    # Reemplazar saltos de línea de la private_key por \\n
    if "private_key" in data:
        data["private_key"] = data["private_key"].replace("\n", "\\n")

    # Convertir todo a una sola línea para Render
    render_ready = json.dumps(data, separators=(',', ':'))

    # Guardar archivo listo para copiar
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(render_ready)

    print(f"✅ Listo. Copia el contenido de {output_path} en Render como value de FIREBASE_CREDENTIALS_JSON")


# 👇 Aquí ajustamos la ruta al archivo dentro de /credenciales
preparar_para_render("credenciales/firebase_credentials.json", "firebase_render_ready.json")

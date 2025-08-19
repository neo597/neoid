import json

def preparar_para_render(input_file, output_file):
    # Leer el archivo original
    with open(input_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    # Reemplazar saltos de línea de la clave privada por \\n
    if "private_key" in data:
        data["private_key"] = data["private_key"].replace("\n", "\\n")

    # Convertir a string en una sola línea
    render_ready = json.dumps(data, separators=(',', ':'))

    # Guardar en archivo
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(render_ready)

    print(f"✅ Listo. Copia el contenido de {output_file} en Render como value de FIREBASE_CREDENTIALS_JSON")


# Ejemplo de uso
preparar_para_render("firebase_credentials.json", "firebase_render_ready.json")

import json
import os

def preparar_para_render(input_file, output_file):
    # Ruta donde está el script
    base_dir = os.path.dirname(os.path.abspath(__file__))

    # Rutas completas para archivos en la carpeta 'credenciales'
    input_path = os.path.join(base_dir, "credenciales", input_file)
    output_path = os.path.join(base_dir, output_file)

    # Verificar si el archivo existe antes de abrir
    if not os.path.exists(input_path):
        print(f"❌ No se encontró el archivo en: {input_path}")
        return

    # Leer archivo original
    with open(input_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    # Reemplazar saltos de línea en la clave privada
    if "private_key" in data:
        data["private_key"] = data["private_key"].replace("\n", "\\n")

    # Convertir a JSON en una sola línea
    render_ready = json.dumps(data, separators=(',', ':'))

    # Guardar el archivo procesado
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(render_ready)

    print(f"✅ Archivo convertido y guardado en: {output_path}")


# Llamada a la función
preparar_para_render("firebase_credentials.json", "firebase_render_ready.json")




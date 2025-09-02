import json
import os

def preparar_para_render(input_file, output_file):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    input_path = os.path.join(base_dir, "credenciales", input_file)
    output_path = os.path.join(base_dir, output_file)

    if not os.path.exists(input_path):
        print(f"❌ No se encontró el archivo en: {input_path}")
        return

    with open(input_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    # 🔹 Reemplaza saltos de línea por \\n
    if "private_key" in data:
        data["private_key"] = data["private_key"].replace("\n", "\\n")

    render_ready = json.dumps(data, separators=(',', ':'))

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(render_ready)

    print(f"✅ Archivo convertido y guardado en: {output_path}")

preparar_para_render("firebase_credentials.json", "firebase_render_ready.json")

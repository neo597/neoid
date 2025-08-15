
import os
import uuid
from firebase import bucket

def subir_audio(ruta_local: str, nombre_remoto: str = None) -> str:
    """
    Sube un archivo de audio a Firebase Storage y devuelve la URL pública.

    :param ruta_local: Ruta local del archivo a subir.
    :param nombre_remoto: Nombre opcional del archivo en el bucket. 
                          Si no se especifica, se genera automáticamente.
    :return: URL pública del archivo subido.
    """
    if not os.path.exists(ruta_local):
        raise FileNotFoundError(f"❌ No se encontró el archivo local: {ruta_local}")

    # Generar nombre único si no se proporciona
    if not nombre_remoto:
        nombre_remoto = f"{uuid.uuid4()}.mp3"  # Puedes cambiar la extensión según tu tipo de archivo

    # Crear referencia en Storage dentro de la carpeta "llantos"
    blob = bucket.blob(f"llantos/{nombre_remoto}")

    try:
        blob.upload_from_filename(ruta_local)
        blob.make_public()
        print(f" Archivo subido correctamente: {nombre_remoto}")
        return blob.public_url
    except Exception as e:
        raise RuntimeError(f"❌ Error al subir el archivo a Firebase Storage: {e}")
    

# from app.firebase import bucket

# def subir_audio(ruta_local: str, nombre_remoto: str) -> str:
#     blob = bucket.blob(f"llantos/{nombre_remoto}")
#     blob.upload_from_filename(ruta_local)
#     blob.make_public()
#     return blob.public_url
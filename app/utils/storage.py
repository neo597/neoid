from app.firebase import bucket

def subir_audio(ruta_local: str, nombre_remoto: str) -> str:
    blob = bucket.blob(f"llantos/{nombre_remoto}")
    blob.upload_from_filename(ruta_local)
    blob.make_public()
    return blob.public_url
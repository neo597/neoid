import os
import json
import firebase_admin
from firebase_admin import credentials, firestore, storage

db = None
bucket = None

def init_firebase():
    global db, bucket

    cred_path = os.getenv("FIREBASE_CREDENTIALS_PATH")
    if not cred_path or not os.path.exists(cred_path):
        raise RuntimeError(f"❌ No se encontró el archivo de credenciales en: {cred_path}")

    with open(cred_path, "r", encoding="utf-8") as f:
        cred_dict = json.load(f)

    if not firebase_admin._apps:
        cred = credentials.Certificate(cred_dict)
        firebase_admin.initialize_app(cred, {
            "storageBucket": f"{cred_dict['project_id']}.appspot.com"
        })

    db = firestore.client()
    bucket = storage.bucket()



# import firebase_admin
# from firebase_admin import credentials, firestore, storage

# # Cargar credenciales
# cred = credentials.Certificate("firebase_credentials.json")

# # Inicializar Firebase solo si no está inicializado
# if not firebase_admin._apps:
#     firebase_admin.initialize_app(cred, {
#         'storageBucket': 'tu-proyecto.appspot.com'  # ¡Reemplázalo con tu bucket real!
#     })

# # Cliente Firestore
# db = firestore.client()

# # Cliente Firebase Storage
# bucket = storage.bucket()





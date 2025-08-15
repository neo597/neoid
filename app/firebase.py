# firebase.py
import os, json, firebase_admin
from firebase_admin import credentials, firestore, storage

db = None
bucket = None

def init_firebase():
    global db, bucket
    cred_data = os.environ.get("FIREBASE_CREDENTIALS_JSON")
    if not cred_data:
        raise RuntimeError("Credenciales no encontradas")

    if "\\n" in cred_data:
        cred_data = cred_data.replace("\\n", "\n")

    cred_dict = json.loads(cred_data)

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





import os
import json
import firebase_admin
from firebase_admin import credentials, firestore, storage
from dotenv import load_dotenv

# Cargar variables desde .env (solo local)
load_dotenv()

_db = None
_bucket = None

def init_firebase():
    global _db, _bucket

    # 1️⃣ Intentar primero con variable FIREBASE_CREDENTIALS (Render)
    cred_json = os.getenv("FIREBASE_CREDENTIALS")
    cred_path = os.getenv("FIREBASE_CREDENTIALS_PATH")

    if cred_json:
        try:
            cred_dict = json.loads(cred_json)
            print("🔹 Usando credenciales desde FIREBASE_CREDENTIALS (Render)")
        except json.JSONDecodeError:
            raise RuntimeError("❌ Error: FIREBASE_CREDENTIALS no es un JSON válido")
    elif cred_path and os.path.exists(cred_path):
        # 2️⃣ Si no existe, usar archivo local
        print(f"🔹 Usando credenciales desde archivo local: {cred_path}")
        with open(cred_path, "r", encoding="utf-8") as f:
            cred_dict = json.load(f)
    else:
        raise RuntimeError("❌ No se encontró la variable FIREBASE_CREDENTIALS ni el archivo FIREBASE_CREDENTIALS_PATH")

    # Inicializar Firebase si no está ya inicializado
    if not firebase_admin._apps:
        cred = credentials.Certificate(cred_dict)
        firebase_admin.initialize_app(cred, {
            "storageBucket": f"{cred_dict['project_id']}.appspot.com"
        })

    _db = firestore.client()
    _bucket = storage.bucket()

def get_firestore():
    if _db is None:
        raise RuntimeError("Firestore no está inicializado. Llama init_firebase() primero.")
    return _db

def get_bucket():
    if _bucket is None:
        raise RuntimeError("Storage no está inicializado. Llama init_firebase() primero.")
    return _bucket

# import os
# import json
# import firebase_admin
# from firebase_admin import credentials, firestore, storage
# from dotenv import load_dotenv

# load_dotenv()

# _db = None
# _bucket = None

# def init_firebase():
#     global _db, _bucket

#     cred_path = os.getenv("FIREBASE_CREDENTIALS_PATH")
#     if not cred_path or not os.path.exists(cred_path):
#         raise RuntimeError(f"❌ No se encontró el archivo de credenciales en: {cred_path}")

#     with open(cred_path, "r", encoding="utf-8") as f:
#         cred_dict = json.load(f)

#     if not firebase_admin._apps:
#         cred = credentials.Certificate(cred_dict)
#         firebase_admin.initialize_app(cred, {
#             "storageBucket": f"{cred_dict['project_id']}.appspot.com"
#         })

#     _db = firestore.client()
#     _bucket = storage.bucket()

# def get_firestore():
#     if _db is None:
#         raise RuntimeError("Firestore no está inicializado. Llama init_firebase() primero.")
#     return _db

# def get_bucket():
#     if _bucket is None:
#         raise RuntimeError("Storage no está inicializado. Llama init_firebase() primero.")
#     return _bucket


# import os
# import json
# import firebase_admin
# from firebase_admin import credentials, firestore, storage
# from dotenv import load_dotenv

# load_dotenv()

# _db = None
# _bucket = None

# def init_firebase():
#     global _db, _bucket

#     cred_path = os.getenv("FIREBASE_CREDENTIALS_PATH")
#     if not cred_path or not os.path.exists(cred_path):
#         raise RuntimeError(f"❌ No se encontró el archivo de credenciales en: {cred_path}")

#     with open(cred_path, "r", encoding="utf-8") as f:
#         cred_dict = json.load(f)

#     if not firebase_admin._apps:
#         cred = credentials.Certificate(cred_dict)
#         firebase_admin.initialize_app(cred, {
#             "storageBucket": f"{cred_dict['project_id']}.appspot.com"
#         })

#     _db = firestore.client()
#     _bucket = storage.bucket()

# def get_firestore():
#     if _db is None:
#         raise RuntimeError("Firestore no está inicializado")
#     return _db

# def get_bucket():
#     if _bucket is None:
#         raise RuntimeError("Storage no está inicializado")
#     return _bucket



# # import firebase_admin
# # from firebase_admin import credentials, firestore, storage

# # # Cargar credenciales
# # cred = credentials.Certificate("firebase_credentials.json")

# # # Inicializar Firebase solo si no está inicializado
# # if not firebase_admin._apps:
# #     firebase_admin.initialize_app(cred, {
# #         'storageBucket': 'tu-proyecto.appspot.com'  # ¡Reemplázalo con tu bucket real!
# #     })

# # # Cliente Firestore
# # db = firestore.client()

# # # Cliente Firebase Storage
# # bucket = storage.bucket()





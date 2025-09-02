import os
import json
import firebase_admin
from firebase_admin import credentials, firestore, storage
from dotenv import load_dotenv

load_dotenv()

_db = None
_bucket = None

def init_firebase():
    global _db, _bucket

    creds_json = os.getenv("FIREBASE_CREDENTIALS")

    if not creds_json:
        cred_path = os.getenv("FIREBASE_CREDENTIALS_PATH")
        if not cred_path or not os.path.exists(cred_path):
            raise RuntimeError("❌ No se encontró FIREBASE_CREDENTIALS ni archivo local")
        with open(cred_path, "r", encoding="utf-8") as f:
            creds_json = f.read()

    try:
        cred_dict = json.loads(creds_json)
    except Exception as e:
        raise RuntimeError(f"❌ Error al leer credenciales Firebase: {e}")

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

#     # 🔹 Primero probamos con la variable de entorno FIREBASE_CREDENTIALS
#     creds_json = os.getenv("FIREBASE_CREDENTIALS")

#     # 🔹 Si no existe, usamos el archivo local
#     if not creds_json:
#         cred_path = os.getenv("FIREBASE_CREDENTIALS_PATH")
#         if not cred_path or not os.path.exists(cred_path):
#             raise RuntimeError("❌ No se encontró la variable FIREBASE_CREDENTIALS ni el archivo local.")
#         with open(cred_path, "r", encoding="utf-8") as f:
#             creds_json = f.read()

#     # Cargar JSON
#     try:
#         cred_dict = json.loads(creds_json)
#     except Exception as e:
#         raise RuntimeError(f"❌ Error al leer credenciales Firebase: {e}")

#     # Inicializar Firebase si no está inicializado
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


# # import os
# # import json
# # import firebase_admin
# # from firebase_admin import credentials, firestore, storage
# # from dotenv import load_dotenv

# # load_dotenv()

# # _db = None
# # _bucket = None

# # def init_firebase():
# #     global _db, _bucket

# #     cred_path = os.getenv("FIREBASE_CREDENTIALS_PATH")
# #     if not cred_path or not os.path.exists(cred_path):
# #         raise RuntimeError(f"❌ No se encontró el archivo de credenciales en: {cred_path}")

# #     with open(cred_path, "r", encoding="utf-8") as f:
# #         cred_dict = json.load(f)

# #     if not firebase_admin._apps:
# #         cred = credentials.Certificate(cred_dict)
# #         firebase_admin.initialize_app(cred, {
# #             "storageBucket": f"{cred_dict['project_id']}.appspot.com"
# #         })

# #     _db = firestore.client()
# #     _bucket = storage.bucket()

# # def get_firestore():
# #     if _db is None:
# #         raise RuntimeError("Firestore no está inicializado. Llama init_firebase() primero.")
# #     return _db

# # def get_bucket():
# #     if _bucket is None:
# #         raise RuntimeError("Storage no está inicializado. Llama init_firebase() primero.")
# #     return _bucket


# # import os
# # import json
# # import firebase_admin
# # from firebase_admin import credentials, firestore, storage
# # from dotenv import load_dotenv

# # load_dotenv()

# # _db = None
# # _bucket = None

# # def init_firebase():
# #     global _db, _bucket

# #     cred_path = os.getenv("FIREBASE_CREDENTIALS_PATH")
# #     if not cred_path or not os.path.exists(cred_path):
# #         raise RuntimeError(f"❌ No se encontró el archivo de credenciales en: {cred_path}")

# #     with open(cred_path, "r", encoding="utf-8") as f:
# #         cred_dict = json.load(f)

# #     if not firebase_admin._apps:
# #         cred = credentials.Certificate(cred_dict)
# #         firebase_admin.initialize_app(cred, {
# #             "storageBucket": f"{cred_dict['project_id']}.appspot.com"
# #         })

# #     _db = firestore.client()
# #     _bucket = storage.bucket()

# # def get_firestore():
# #     if _db is None:
# #         raise RuntimeError("Firestore no está inicializado")
# #     return _db

# # def get_bucket():
# #     if _bucket is None:
# #         raise RuntimeError("Storage no está inicializado")
# #     return _bucket



# # # import firebase_admin
# # # from firebase_admin import credentials, firestore, storage

# # # # Cargar credenciales
# # # cred = credentials.Certificate("firebase_credentials.json")

# # # # Inicializar Firebase solo si no está inicializado
# # # if not firebase_admin._apps:
# # #     firebase_admin.initialize_app(cred, {
# # #         'storageBucket': 'tu-proyecto.appspot.com'  # ¡Reemplázalo con tu bucket real!
# # #     })

# # # # Cliente Firestore
# # # db = firestore.client()

# # # # Cliente Firebase Storage
# # # bucket = storage.bucket()





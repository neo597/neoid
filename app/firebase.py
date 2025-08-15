import os
import json
import firebase_admin
from firebase_admin import credentials, firestore, storage

#  Intentar obtener credenciales desde variable de entorno
cred_data = os.environ.get("FIREBASE_CREDENTIALS_JSON")

#  Si no existe la variable, intentar cargar desde archivo local
if not cred_data:
    local_path = os.path.join(os.path.dirname(__file__), "..", "firebase_credentials.json")
    local_path = os.path.abspath(local_path)
    
    if os.path.exists(local_path):
        print(f"🔹 Cargando credenciales de Firebase desde archivo local: {local_path}")
        with open(local_path, "r", encoding="utf-8") as f:
            cred_data = f.read()
    else:
        raise ValueError(
            "❌ No se encontraron credenciales de Firebase.\n"
            "Agrega la variable FIREBASE_CREDENTIALS_JSON o el archivo firebase_credentials.json en la raíz del proyecto."
        )

#  Convertir string JSON a diccionario
try:
    cred_dict = json.loads(cred_data)
except json.JSONDecodeError:
    raise ValueError("❌ Las credenciales de Firebase no son un JSON válido.")

#  Inicializar Firebase solo si no está inicializado
if not firebase_admin._apps:
    cred = credentials.Certificate(cred_dict)
    firebase_admin.initialize_app(
        cred,
        {"storageBucket": f"{cred_dict['project_id']}.appspot.com"}  # Configurar Storage automáticamente
    )

#  Clientes listos para usar en toda la app
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





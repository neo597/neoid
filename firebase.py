import firebase_admin
from firebase_admin import credentials, firestore, storage

# Cargar credenciales
cred = credentials.Certificate("firebase_credentials.json")

# Inicializar Firebase solo si no está inicializado
if not firebase_admin._apps:
    firebase_admin.initialize_app(cred, {
        'storageBucket': 'tu-proyecto.appspot.com'  # ¡Reemplázalo con tu bucket real!
    })

# Cliente Firestore
db = firestore.client()

# Cliente Firebase Storage
bucket = storage.bucket()




# import firebase_admin
# from firebase_admin import credentials, firestore

# # Cargar credenciales desde el archivo JSON
# cred = credentials.Certificate("firebase_credentials.json")
# firebase_admin.initialize_app(cred)

# # Conectar a Firestore
# db = firestore.client()
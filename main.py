from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os
from dotenv import load_dotenv
from firebase import init_firebase, get_firestore, get_bucket
import uvicorn

from app.routes.neonato_routes import router as neonato_router
from app.routes.madre_routes import router as madre_router
from app.routes.llanto_routes import router as llanto_router

# Cargar variables de entorno (.env en local)
load_dotenv()

# Inicializar FastAPI
app = FastAPI()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Rutas principales
app.include_router(neonato_router)
app.include_router(madre_router)
app.include_router(llanto_router)

@app.get("/")
async def read_root():
    return {"message": "Servidor funcionando correctamente"}

@app.get("/ping")
def ping():
    return {"status": "ok"}

@app.get("/health")
def health_check():
    try:
        db = get_firestore()
        collections = [col.id for col in db.collections()]
        return {"firebase": "ok", "collections": collections}
    except Exception as e:
        return {"firebase": "error", "detail": str(e)}

# Rutas de prueba Firebase
@app.get("/test/firestore")
def test_firestore():
    try:
        db = get_firestore()
        collections = [col.id for col in db.collections()]
        return {"status": "ok", "collections": collections}
    except Exception as e:
        return {"status": "error", "detail": str(e)}

@app.get("/test/storage")
def test_storage():
    try:
        bucket = get_bucket()
        blobs = bucket.list_blobs(prefix="llantos/")
        archivos = [blob.name for blob in blobs]
        return {"status": "ok", "files": archivos}
    except Exception as e:
        return {"status": "error", "detail": str(e)}

# Evento de inicio para inicializar Firebase
@app.on_event("startup")
def startup_event():
    try:
        init_firebase()
        print("✅ Firebase inicializado correctamente")
    except Exception as e:
        print(f"⚠️ Error al inicializar Firebase: {e}")

# Solo para correr localmente con: python main.py
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=False)



# from fastapi import FastAPI
# from fastapi.middleware.cors import CORSMiddleware
# import os
# from dotenv import load_dotenv
# from firebase import init_firebase, get_firestore
# import uvicorn

# from app.routes.neonato_routes import router as neonato_router
# from app.routes.madre_routes import router as madre_router
# from app.routes.llanto_routes import router as llanto_router

# # Cargar variables de entorno
# load_dotenv()

# # Inicializar FastAPI
# app = FastAPI()

# # CORS
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# # Rutas
# app.include_router(neonato_router)
# app.include_router(madre_router)
# app.include_router(llanto_router)

# @app.get("/")
# async def read_root():
#     return {"message": "Servidor funcionando correctamente"}

# @app.get("/ping")
# def ping():
#     return {"status": "ok"}

# @app.get("/health")
# def health_check():
#     try:
#         db = get_firestore()
#         docs = db.collections()  # Forzar consulta para probar conexión
#         return {"firebase": "ok"}
#     except Exception as e:
#         return {"firebase": "error", "detail": str(e)}

# # Evento de inicio
# @app.on_event("startup")
# def startup_event():
#     try:
#         init_firebase()
#         print("✅ Firebase inicializado correctamente")
#     except Exception as e:
#         print(f"⚠️ Error al inicializar Firebase: {e}")




# # Solo para correr localmente con: python main.py
# if __name__ == "__main__":
    
#     port = int(os.environ.get("PORT", 8000))
#     uvicorn.run("main:app", host="0.0.0.0", port=port, reload=False)





# from fastapi import FastAPI
# from fastapi.middleware.cors import CORSMiddleware
# import os
# import uvicorn
# from dotenv import load_dotenv
# from firebase import init_firebase, get_firestore

# from app.routes.neonato_routes import router as neonato_router
# from app.routes.madre_routes import router as madre_router
# from app.routes.llanto_routes import router as llanto_router

# load_dotenv()

# app = FastAPI()

# # CORS
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# # Rutas
# app.include_router(neonato_router)
# app.include_router(madre_router)
# app.include_router(llanto_router)

# @app.get("/")
# async def read_root():
#     return {"message": "Servidor funcionando correctamente"}

# @app.get("/ping")
# def ping():
#     return {"status": "ok"}

# @app.get("/health")
# def health_check():
#     try:
#         db = get_firestore()
#         docs = db.collections()  # 👈 Forzar consulta
#         return {"firebase": "ok"}
#     except Exception as e:
#         return {"firebase": "error", "detail": str(e)}

# @app.on_event("startup")
# def startup_event():
#     try:
#         init_firebase()
#         print("✅ Firebase inicializado correctamente")
#     except Exception as e:
#         print(f"⚠️ Error al inicializar Firebase: {e}")

#  #  Bloque final para despliegue en Render
# if __name__ == "__main__":
#     port = int(os.environ.get("PORT", 8000))
#     uvicorn.run("main:app", host="0.0.0.0", port=port, reload=False)
    



# from fastapi import FastAPI
# from fastapi.middleware.cors import CORSMiddleware
# import os
# import uvicorn
# from app.routes.neonato_routes import router as neonato_router
# from app.routes.madre_routes import router as madre_router
# from app.routes.llanto_routes import router as llanto_router


# app = FastAPI()

# #  Configuración CORS
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],  # o ["http://localhost:5173"] para mayor seguridad
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# # Rutas
# app.include_router(neonato_router)
# app.include_router(madre_router)
# app.include_router(llanto_router)

# @app.get("/")
# async def read_root():
#     return {"message": "Servidor funcionando correctamente"}

# # Imprimir rutas disponibles al arrancar (opcional para depuración)
# @app.on_event("startup")
# def listar_rutas():
#     print("\nRutas activas en la API:")
#     for r in app.routes:
#         print(f"→ {r.path} : {r.methods}")



# #  Bloque final para despliegue en Render
# if __name__ == "__main__":
#     port = int(os.environ.get("PORT", 8000))
#     uvicorn.run("main:app", host="0.0.0.0", port=port, reload=False)
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os
import uvicorn
from dotenv import load_dotenv
from firebase import init_firebase

from app.routes.neonato_routes import router as neonato_router
from app.routes.madre_routes import router as madre_router
from app.routes.llanto_routes import router as llanto_router

# Cargar variables de entorno
load_dotenv()

app = FastAPI()

# Configuración CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Puedes restringir esto en producción
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Rutas
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
    return {"firebase": "ok" if os.getenv("FIREBASE_CREDENTIALS_PATH") else "missing"}

# Inicialización en startup con manejo de errores
@app.on_event("startup")
def startup_event():
    try:
        init_firebase()
        print("✅ Firebase inicializado correctamente")
    except Exception as e:
        print(f"⚠️ Error al inicializar Firebase: {e}")

    print("\n🔗 Rutas activas en la API:")
    for r in app.routes:
        print(f"→ {r.path} : {r.methods}")

# Ejecución local o en Render
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))  # Render usa el puerto 10000
    uvicorn.run("main:app", host="0.0.0.0", port=port)




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
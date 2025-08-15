import os
import uvicorn
from fastapi import FastAPI
from contextlib import asynccontextmanager

# Importa tus routers y funciones de inicialización
from routers import neonatos, madres, llantos
from firebase_config import init_firebase  # Asegúrate de tener esta función definida

# 🔄 Inicialización moderna con lifespan
@asynccontextmanager
async def lifespan(app: FastAPI):
    try:
        init_firebase()
        print("✅ Firebase inicializado correctamente")
    except Exception as e:
        print(f"⚠️ Error al inicializar Firebase: {e}")
    yield
    # Aquí podrías cerrar conexiones si lo necesitas

# 🚀 Instancia principal de FastAPI
app = FastAPI(lifespan=lifespan)

# 📦 Registro de routers
app.include_router(neonatos.router)
app.include_router(madres.router)
app.include_router(llantos.router)

# 🩺 Endpoint de salud para Render
@app.get("/health")
def health():
    return {"status": "ok"}

# 🏁 Arranque del servidor (compatible con Render)
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
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
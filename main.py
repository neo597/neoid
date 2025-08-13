from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes.neonato_routes import router as neonato_router
from app.routes.madre_routes import router as madre_router
from app.routes.llanto_routes import router as llanto_router

app = FastAPI()

#  Configuración CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # o ["http://localhost:5173"] para mayor seguridad
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


# from fastapi import FastAPI
# from app.routes.neonato_routes import router as neonato_router
# from app.routes.madre_routes import router as madre_router
# from app.routes.llanto_routes import router as llanto_router

# app = FastAPI()

# app.include_router(neonato_router)
# app.include_router(madre_router)
# app.include_router(llanto_router)

# @app.get("/")
# async def read_root():
#     return {"message": "Servidor funcionando correctamente"}


#from fastapi import FastAPI
# from firebase import db  # Importar conexión a Firebase
# from app.models.madre import MadreBase
# from app.models.neonato import NeonatoBase


# app = FastAPI()

# @app.get("/")
# async def read_root():
#     return {"message": "Servidor funcionando correctamente"}


# #  Obtener un neonato por ID
# @app.post("/neonato/")
# async def create_neonato(neonato: NeonatoBase):
#     neonato_dict = neonato.dict()  # Convertir el objeto Pydantic a diccionario
#     neonato_dict["activo"] = True  # Se crea como activo por defecto
#     neonato_ref = db.collection("neonatos").document(neonato.id_neonato)
#     neonato_ref.set(neonato_dict)
#     return {"message": "Neonato agregado correctamente"}

# #  Crear un neonato con estado activo
# @app.post("/neonato/")
# async def create_neonato(neonato: dict):
#     neonato["activo"] = True  # Se crea como activo por defecto
#     neonato_ref = db.collection("neonatos").document(neonato["id"])
#     neonato_ref.set(neonato)
#     return {"message": "Neonato agregado correctamente"}

# #  Activar un neonato
# @app.put("/neonato/{neonato_id}/activar")
# async def activate_neonato(neonato_id: str):
#     neonato_ref = db.collection("neonatos").document(neonato_id)
#     neonato_ref.update({"activo": True})
#     return {"message": "Neonato activado correctamente"}

# #  Desactivar un neonato
# @app.put("/neonato/{neonato_id}/desactivar")
# async def deactivate_neonato(neonato_id: str):
#     neonato_ref = db.collection("neonatos").document(neonato_id)
#     neonato_ref.update({"activo": False})
#     return {"message": "Neonato desactivado correctamente"}




# #  Obtener una madre por ID
# @app.get("/madre/{madre_id}")
# async def get_madre(madre_id: str):
#     madre_ref = db.collection("madres").document(madre_id)
#     madre = madre_ref.get()
#     if madre.exists:
#         return madre.to_dict()
#     return {"error": "Madre no encontrada"}

# #  Crear una madre con estado activo
# @app.post("/madre/")
# async def create_madre(madre: MadreBase):
#     madre_ref = db.collection("madres").document(madre.id_madre)  # Usar id_madre en lugar de id
#     madre_ref.set(madre.dict())  # Convertir el objeto Pydantic a diccionario
#     return {"message": "Madre agregada correctamente"}


# #  Activar una madre
# @app.put("/madre/{madre_id}/activar")
# async def activate_madre(madre_id: str):
#     madre_ref = db.collection("madres").document(madre_id)
#     madre_ref.update({"activo": True})
#     return {"message": "Madre activada correctamente"}

# #  Desactivar una madre
# @app.put("/madre/{madre_id}/desactivar")
# async def deactivate_madre(madre_id: str):
#     madre_ref = db.collection("madres").document(madre_id)
#     madre_ref.update({"activo": False})
#     return {"message": "Madre desactivada correctamente"}
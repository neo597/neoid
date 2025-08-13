from fastapi import APIRouter
from app.controllers.neonato_controller import NeonatoController
from app.models.neonato import NeonatoBase

router = APIRouter(prefix="/neonatos", tags=["Neonatos"])

@router.get("/")
async def list_neonatos():
    return NeonatoController.list_neonatos()

@router.get("/{neonato_id}")
async def get_neonato(neonato_id: str):
    return NeonatoController.get_neonato(neonato_id)

@router.get("/madre/{id_madre}")
async def search_neonatos_by_madre(id_madre: str):
    return NeonatoController.search_neonatos_by_madre(id_madre)

@router.get("/fecha_nacimiento/{fecha_nacimiento}")
async def search_neonatos_by_birthdate(fecha_nacimiento: str):
    return NeonatoController.search_neonatos_by_birthdate(fecha_nacimiento)

@router.get("/fecha_registro/{fecha}")
async def search_neonatos_by_registration(fecha: str):
    return NeonatoController.search_neonatos_by_registration(fecha)


@router.post("/")
async def create_neonato(neonato: NeonatoBase):
    return NeonatoController.create_neonato(neonato)

@router.put("/{neonato_id}")
async def update_neonato(neonato_id: str, neonato_data: dict):
    return NeonatoController.update_neonato(neonato_id, neonato_data)

@router.put("/{neonato_id}/{accion}")
async def change_madre_status(neonato_id: str, accion: str):
    return NeonatoController.change_madre_status(neonato_id, accion)

@router.delete("/{neonato_id}")
async def delete_neonato(neonato_id: str):
    return NeonatoController.delete_neonato(neonato_id)


# from fastapi import APIRouter
# from app.controllers.neonato_controller import NeonatoController
# from app.models.neonato import NeonatoBase

# router = APIRouter(prefix="/neonatos", tags=["Neonatos"])

# @router.get("/")
# async def list_neonatos():
#     return NeonatoController.list_neonatos()

# @router.get("/{neonato_id}")
# async def get_neonato(neonato_id: str):
#     return NeonatoController.get_neonato(neonato_id)

# @router.post("/")
# async def create_neonato(neonato: NeonatoBase):
#     return NeonatoController.create_neonato(neonato)

# @router.put("/{neonato_id}")
# async def update_neonato(neonato_id: str, neonato_data: dict):
#     return NeonatoController.update_neonato(neonato_id, neonato_data)

# @router.delete("/{neonato_id}")
# async def delete_neonato(neonato_id: str):
#     return NeonatoController.delete_neonato(neonato_id)
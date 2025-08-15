from fastapi import APIRouter
from app.controllers.madre_controller import MadreController
from app.models.madre import MadreBase
from firebase import db
router = APIRouter(prefix="/madres", tags=["Madres"])

@router.get("/")
async def list_madres():
    return MadreController.list_madres()

@router.get("/{madre_id}")
async def get_madre(madre_id: str):
    return MadreController.get_madre(madre_id)

@router.get("/documento/{documento}")
async def search_madre_by_document(documento: str):
    return MadreController.search_madre_by_document(documento)

@router.get("/fecha_creacion/{fecha}")
async def search_madres_by_creation(fecha: str):
    return MadreController.search_madres_by_creation(fecha)

@router.post("/")
async def create_madre(madre: MadreBase):
    return MadreController.create_madre(madre)

@router.put("/{madre_id}")
async def update_madre(madre_id: str, madre_data: dict):
    return MadreController.update_madre(madre_id, madre_data)

@router.delete("/{madre_id}")
async def delete_madre(madre_id: str):
    return MadreController.delete_madre(madre_id)

@router.put("/{madre_id}/{accion}")
async def change_madre_status(madre_id: str, accion: str):
    return MadreController.change_madre_status(madre_id, accion)
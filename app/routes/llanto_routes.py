from fastapi import APIRouter, UploadFile, File, Form
from datetime import datetime
from app.controllers.llanto_controller import LlantoController
from app.models.llanto import LlantoBase
from app.utils.storage import subir_audio
from app.firebase import db
import os

router = APIRouter(prefix="/llantos", tags=["Llantos"])

@router.get("/")
async def list_llantos():
    return LlantoController.list_llantos()

@router.get("/{llanto_id}")
async def get_llanto(llanto_id: str):
    return LlantoController.get_llanto(llanto_id)

@router.post("/")
async def create_llanto(llanto: LlantoBase):
    return LlantoController.create_llanto(llanto)

@router.delete("/{llanto_id}")
async def delete_llanto(llanto_id: str):
    return LlantoController.delete_llanto(llanto_id)

@router.post("/subir_llanto/")
async def subir_llanto(id_neonato: str = Form(...), archivo: UploadFile = File(...)):
    contenido = await archivo.read()
    temp_path = f"temp_{archivo.filename}"

    with open(temp_path, "wb") as f:
        f.write(contenido)

    try:
        url_audio = subir_audio(temp_path, archivo.filename)
    finally:
        os.remove(temp_path)

    nuevo_llanto = {
        "id_llanto": archivo.filename.split(".")[0],
        "id_neonato": id_neonato,
        "duracion": url_audio,
        "fecha": datetime.now()
    }

    ref = db.collection("llantos").document(nuevo_llanto["id_llanto"])
    ref.set(nuevo_llanto)

    return {"message": "Llanto subido correctamente", "url": url_audio}
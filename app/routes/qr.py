from fastapi import APIRouter, UploadFile, File
from pyzbar.pyzbar import decode
from PIL import Image
import io
from firebase import db

router = APIRouter(prefix="/scan", tags=["QR / Barcode"])

@router.post("/image")
async def scan_image(file: UploadFile = File(...)):
    image = Image.open(io.BytesIO(await file.read()))
    decoded = decode(image)
    return {"data": [d.data.decode("utf-8") for d in decoded]}

from firebase import db
from app.models.madre import MadreBase

class MadreController:
    @staticmethod
    def list_madres():
        madres_ref = db.collection("madres").stream()
        return [madre.to_dict() for madre in madres_ref]

    @staticmethod
    def get_madre(madre_id: str):
        madre_ref = db.collection("madres").document(madre_id)
        madre = madre_ref.get()
        return madre.to_dict() if madre.exists else {"error": "Madre no encontrada"}

    @staticmethod
    def search_madre_by_document(documento: str):
        madres_ref = db.collection("madres").where("numero_documento", "==", documento).stream()
        return [madre.to_dict() for madre in madres_ref]

    @staticmethod
    def search_madres_by_creation(fecha: str):
        madres_ref = db.collection("madres").where("fecha", "==", fecha).stream()
        return [madre.to_dict() for madre in madres_ref]

    @staticmethod
    def create_madre(madre: MadreBase):
        madre_dict = madre.dict()
        madre_ref = db.collection("madres").document(madre.id_madre)
        madre_ref.set(madre_dict)
        return {"message": "Madre agregada correctamente"}

    @staticmethod
    def update_madre(madre_id: str, madre_data: dict):
        madre_ref = db.collection("madres").document(madre_id)
        madre_ref.update(madre_data)
        return {"message": "Madre actualizada correctamente"}

    @staticmethod
    def delete_madre(madre_id: str):
        madre_ref = db.collection("madres").document(madre_id)
        madre_ref.delete()
        return {"message": "Madre eliminada correctamente"}

    @staticmethod
    def change_madre_status(madre_id: str, accion: str):
        if accion not in ["activar", "desactivar"]:
            return {"error": "Acción no válida"}
        estado = True if accion == "activar" else False
        madre_ref = db.collection("madres").document(madre_id)
        madre_ref.update({"estado": estado})
        return {"message": f"Madre {'activada' if estado else 'desactivada'} correctamente"}
from firebase import db
from app.models.neonato import NeonatoBase

class NeonatoController:
    @staticmethod
    def list_neonatos():
        neonatos_ref = db.collection("neonatos").stream()
        return [neonato.to_dict() for neonato in neonatos_ref]

    @staticmethod
    def get_neonato(neonato_id: str):
        neonato_ref = db.collection("neonatos").document(neonato_id)
        neonato_doc = neonato_ref.get()

        if not neonato_doc.exists:
            return {"error": "Neonato no encontrado"}

        neonato_data = neonato_doc.to_dict()

        # 🔍 Obtener llantos vinculados
        llantos_ref = db.collection("llantos").where("id_neonato", "==", neonato_id).stream()
        llantos = [doc.to_dict() for doc in llantos_ref]

        neonato_data["llantos"] = llantos
        return neonato_data

    @staticmethod
    def search_neonatos_by_birthdate(fecha_nacimiento: str):
        neonatos_ref = db.collection("neonatos").where("fecha_nacimiento", "==", fecha_nacimiento).stream()
        return [neonato.to_dict() for neonato in neonatos_ref]

    @staticmethod
    def search_neonatos_by_registration(fecha: str):
        neonatos_ref = db.collection("neonatos").where("fecha", "==", fecha).stream()
        return [neonato.to_dict() for neonato in neonatos_ref]

    @staticmethod
    def create_neonato(neonato: NeonatoBase):
        neonato_dict = neonato.dict()
        neonato_dict["fecha_nacimiento"] = neonato.fecha_nacimiento.strftime("%Y-%m-%d")
        neonato_dict["hora_nacimiento"] = neonato.hora_nacimiento.strftime("%H:%M:%S")
        neonato_dict["fecha"] = neonato.fecha.strftime("%Y-%m-%d %H:%M:%S")

        neonato_ref = db.collection("neonatos").document(neonato.id_neonato)
        neonato_ref.set(neonato_dict)
        return {"message": "Neonato agregado correctamente"}

    @staticmethod
    def update_neonato(neonato_id: str, neonato_data: dict):
        neonato_ref = db.collection("neonatos").document(neonato_id)
        neonato_ref.update(neonato_data)
        return {"message": "Neonato actualizado correctamente"}

    @staticmethod
    def delete_neonato(neonato_id: str):
        neonato_ref = db.collection("neonatos").document(neonato_id)
        neonato_ref.delete()
        return {"message": "Neonato eliminado correctamente"}

    @staticmethod
    def change_neonato_status(neonato_id: str, accion: str):
        if accion not in ["activar", "desactivar"]:
            return {"error": "Acción no válida"}
        estado = True if accion == "activar" else False
        neonato_ref = db.collection("neonatos").document(neonato_id)
        neonato_ref.update({"estado": estado})
        return {"message": f"Neonato {'activado' if estado else 'desactivado'} correctamente"}


# from firebase import db
# from app.models.neonato import NeonatoBase

# class NeonatoController:
#     @staticmethod
#     def list_neonatos():
#         neonatos_ref = db.collection("neonatos").stream()
#         return [neonato.to_dict() for neonato in neonatos_ref]

#     @staticmethod
#     def get_neonato(neonato_id: str):
#         neonato_ref = db.collection("neonatos").document(neonato_id)
#         neonato = neonato_ref.get()
#         return neonato.to_dict() if neonato.exists else {"error": "Neonato no encontrado"}

#     @staticmethod
#     def create_neonato(neonato: NeonatoBase):
#         neonato_dict = neonato.dict()
        
#         # Convertir `datetime.date` y `datetime.time` a formato string antes de enviar a Firestore
#         neonato_dict["fecha_nacimiento"] = neonato.fecha_nacimiento.strftime("%Y-%m-%d")
#         neonato_dict["hora_nacimiento"] = neonato.hora_nacimiento.strftime("%H:%M:%S")
#         neonato_dict["fecha"] = neonato.fecha.strftime("%Y-%m-%d %H:%M:%S")

#         neonato_ref = db.collection("neonatos").document(neonato.id_neonato)
#         neonato_ref.set(neonato_dict)
#         return {"message": "Neonato agregado correctamente"}

#     @staticmethod
#     def update_neonato(neonato_id: str, neonato_data: dict):
#         neonato_ref = db.collection("neonatos").document(neonato_id)
#         neonato_ref.update(neonato_data)
#         return {"message": "Neonato actualizado correctamente"}

#     @staticmethod
#     def delete_neonato(neonato_id: str):
#         neonato_ref = db.collection("neonatos").document(neonato_id)
#         neonato_ref.delete()
#         return {"message": "Neonato eliminado correctamente"}
from firebase import get_firestore
from app.models.llanto import LlantoBase
from app.utils.contador import Contador  # Importa el contador


class LlantoController:

    @staticmethod
    def list_llantos():
        db = get_firestore()   # 👈 aquí con ()
        docs = db.collection("llantos").stream()
        return [doc.to_dict() for doc in docs]

    @staticmethod
    def get_llanto(llanto_id: str):
        db = get_firestore()   # 👈 aquí con ()
        ref = db.collection("llantos").document(llanto_id)
        doc = ref.get()
        return doc.to_dict() if doc.exists else {"error": "Llanto no encontrado"}

    @staticmethod
    def create_llanto(llanto: LlantoBase):
        nuevo_id = Contador.incrementar_contador_llantos()
        data = llanto.dict()
        data["id_llanto"] = str(nuevo_id)
        data["nombre"] = f"audio {nuevo_id}"

        db = get_firestore()   # 👈 aquí con ()
        db.collection("llantos").document(str(nuevo_id)).set(data)

        return {
            "message": "Llanto guardado correctamente",
            "id_llanto": nuevo_id,
            "nombre": data["nombre"]
        }

    @staticmethod
    def delete_llanto(llanto_id: str):
        db = get_firestore()   # 👈 aquí con ()
        db.collection("llantos").document(llanto_id).delete()
        return {"message": "Llanto eliminado correctamente"}



# from firebase import get_firestore
# from app.models.llanto import LlantoBase
# from app.utils.contador import Contador  # Importa el contador



# def list_llantos():
#     get_firestore = get_firestore()
#     docs = get_firestore.collection("llantos").stream()
#     return [doc.to_dict() for doc in docs]


# class LlantoController:
#     @staticmethod
#     def create_llanto(llanto: LlantoBase):
#         nuevo_id = Contador.incrementar_contador_llantos()  # 🔹 Obtener ID autoincrementado
#         data = llanto.dict()
#         data["id_llanto"] = str(nuevo_id)  # 🔹 Guardar como string para Firestore
#         get_firestore.collection("llantos").document(str(nuevo_id)).set(data)
#         return {"message": "Llanto guardado correctamente", "id_llanto": nuevo_id}


# class LlantoController:
#     @staticmethod
#     def list_llantos():
#         docs = get_firestore.collection("llantos").stream()
#         return [doc.to_dict() for doc in docs]

#     @staticmethod
#     def get_llanto(llanto_id: str):
#         ref = get_firestore.collection("llantos").document(llanto_id)
#         doc = ref.get()
#         return doc.to_dict() if doc.exists else {"error": "Llanto no encontrado"}

    
#     @staticmethod
#     def create_llanto(llanto: LlantoBase):
#         # Obtener el ID autoincrementado desde Firestore
#         nuevo_id = Contador.incrementar_contador_llantos()

#         # Construir los datos del llanto
#         data = llanto.dict()
#         data["id_llanto"] = str(nuevo_id)  #  Convertir a string para Firestore
#         data["nombre"] = f"audio {nuevo_id}"  #  Generar automáticamente el nombre

#         # Insertar en Firestore con el ID autoincrementado
#         get_firestore.collection("llantos").document(str(nuevo_id)).set(data)

#         return {
#             "message": "Llanto guardado correctamente",
#             "id_llanto": nuevo_id,
#             "nombre": data["nombre"]
#         }




#     @staticmethod
#     def delete_llanto(llanto_id: str):
#         get_firestore.collection("llantos").document(llanto_id).delete()
#         return {"message": "Llanto eliminado correctamente"}
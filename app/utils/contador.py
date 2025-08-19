from firebase import get_firestore

class Contador:
    @staticmethod
    def obtener_contador_llantos():
        ref = get_firestore.collection("contadores").document("llantos")
        doc = ref.get()
        return doc.to_dict()["contador"] if doc.exists else 0

    @staticmethod
    def incrementar_contador_llantos():
        ref = get_firestore.collection("contadores").document("llantos")
        doc = ref.get()
        contador_actual = doc.to_dict()["contador"] if doc.exists else 0
        nuevo_contador = contador_actual + 1
        ref.set({"contador": nuevo_contador})
        return nuevo_contador
    
from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime, date, time

class NeonatoBase(BaseModel):
    id_neonato: str = Field(..., min_length=1, max_length=550)
    id_madre: str = Field(..., min_length=1, max_length=550)
    nombre_neonato: str = Field(..., min_length=2, max_length=100)
    fecha_nacimiento: date
    hora_nacimiento: time
    sexo: str
    talla: str
    peso: str
    pc: str
    pa: str
    pt: str
    permeabilidad_rectal: str
    servicio: str
    se_encuentra_en: str
    observaciones: Optional[str] = None
    estado: bool = True
    fecha: datetime = Field(default_factory=datetime.now)



# # app/models/neonato.py
# from pydantic import BaseModel
# from typing import Optional
# from datetime import datetime, date, time


# class NeonatoBase(BaseModel):
#     id_neonato: str
#     nombre_neonato: str
#     fecha_nacimiento: date
#     hora_nacimiento: time
#     sexo: str
#     talla: str
#     peso: str
#     pc: str
#     pa: str
#     pt: str
#     permeabilidad_rectal: str
#     servicio: str
#     se_encuentra_en: str
#     observaciones: Optional[str] = None
#     estado: bool = True
#     fecha: datetime = datetime.now()

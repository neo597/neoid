from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class MadreBase(BaseModel):
    id_madre: str = Field(..., min_length=1, max_length=550)
    nombre_madre: str = Field(..., min_length=2, max_length=100)
    tipo_documento: str
    numero_documento: str
    observaciones: Optional[str] = None
    estado: bool = True
    fecha: datetime = Field(default_factory=datetime.now)


# from pydantic import BaseModel
# from typing import Optional
# from datetime import datetime


# class MadreBase(BaseModel):
#     id_madre: str
#     nombre_madre: str
#     tipo_documento: str
#     numero_documento: str
#     observaciones: Optional[str] = None
#     estado: bool = True
#     id_neonato: str
#     fecha: datetime = datetime.now()

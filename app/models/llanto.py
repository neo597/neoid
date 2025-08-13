from pydantic import BaseModel, Field
from datetime import datetime

class LlantoBase(BaseModel):
    id_neonato: str = Field(..., min_length=1)
    duracion: str  # URL del archivo de audio en Firebase Storage
    fecha: datetime = Field(default_factory=datetime.now)
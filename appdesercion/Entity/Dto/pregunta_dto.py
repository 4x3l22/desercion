from dataclasses import dataclass
from typing import List, Optional


@dataclass
class PreguntaDTO:
    id= int
    cuestionario_id= int
    texto= str
    tipo= str
    opciones= Optional[List[str]]

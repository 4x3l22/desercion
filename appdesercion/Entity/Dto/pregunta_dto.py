from dataclasses import dataclass
from typing import List, Optional


@dataclass
class PreguntaDTO:
    cuestionario= int
    texto= str
    tipo= str
    opciones= Optional[List[str]]

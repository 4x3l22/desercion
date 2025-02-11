from dataclasses import dataclass
import datetime


@dataclass
class PreguntasDTO:
    id=int
    cuestionario_id=int
    texto_pregunta= str
    tipo_pregunta= ['abierta','seleccion Multiple']
    opciones_id= int
    textoopciones= str | None
    estado= bool
    fechaCreo= datetime
    fechaModifico= datetime | None
    fechaElimino= datetime | None
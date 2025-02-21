from dataclasses import dataclass, field
from typing import List

@dataclass
class AnswerDTO:
    respuesta_id: int
    respuesta_texto: str

@dataclass
class QuestionDTO:
    pregunta_id: int
    texto_pregunta: str
    tipo_pregunta: str
    opciones_pregunta: str
    respuestas: List[AnswerDTO] = field(default_factory=list)

@dataclass
class ListaProcesosCuestionariosDTO:
    proceso_id: int
    estado_aprobacion: str
    correo_usuario: str
    nombres_usuario: str
    apellidos_usuario: str
    numero_documento_usuario: int
    cuestionario_nombre: str
    cuestionario_descripcion: str
    preguntas: List[QuestionDTO] = field(default_factory=list)

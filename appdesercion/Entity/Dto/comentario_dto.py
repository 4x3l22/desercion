from dataclasses import dataclass, field
from typing import List

@dataclass
class AnswerCommentDTO:
    respuesta_id: int
    respuesta_texto: str

@dataclass
class QuestionCommentDTO:
    pregunta_id: int
    texto_pregunta: str
    tipo_pregunta: str
    opciones_pregunta: List[str] = field(default_factory=list)
    respuestas: List[AnswerCommentDTO] = field(default_factory=list)

@dataclass
class ListaProcesosCuestionariosCommetDTO:
    proceso_id: int
    estado_aprobacion: str
    correo_usuario: str
    nombres_usuario: str
    apellidos_usuario: str
    nombre_aprendiz: str
    apellidos_aprendiz: str
    documento_aprendiz: str
    numero_documento_usuario: str
    cuestionario_nombre: str
    cuestionario_descripcion: str
    comentario: List[str] = field(default_factory=list)
    preguntas: List[QuestionCommentDTO] = field(default_factory=list)

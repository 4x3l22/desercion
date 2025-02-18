from dataclasses import dataclass


@dataclass
class UsuarioSinRolDTO:
    def __init__(self, id, nombres, apellidos, correo, documento, tipoDocumento_nombre):
        self.id = id
        self.nombres = nombres
        self.apellidos = apellidos
        self.correo = correo
        self.documento = documento
        self.tipoDocumento_nombre = tipoDocumento_nombre
from dataclasses import dataclass


@dataclass
class MenuDto:
    nombreVista: str
    nombreModulo: str
    vistaId: int
    moduloId: int
    moduloIconos: str
    vistaIconos: str
    RutaVista: str
from dataclasses import dataclass


@dataclass
class TraineesDTO:
    ID_trainees: int
    trainees_name: str
    trainees_document: int
    trainees_email: str
    trainees_process: str

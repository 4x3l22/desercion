from dataclasses import dataclass, field
from typing import List

@dataclass
class AnswerCommentPIDTO:
    reply_id: int
    reply: str

@dataclass
class QuestionCommentPIDTO:
    question_id: int
    question_text: str
    question_type: str
    question_option: List[str] = field(default_factory=list)
    answer: List[AnswerCommentPIDTO] = field(default_factory=list)

@dataclass
class ProcessInstructorDTO:
    process_id: int
    estado_aprobacion: str
    user_email: str
    user_name: str
    trainee_name: str
    trainee_document: int
    questionnaire_name: str
    questionnaire_description: str
    comment_state: str
    comment: List[str] = field(default_factory=list)
    question: List[QuestionCommentPIDTO] = field(default_factory=list)

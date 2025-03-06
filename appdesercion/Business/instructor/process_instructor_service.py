from appdesercion.Entity.Dao.instructor.process_instructor_dao import ProcessInstructorDao
from appdesercion.Entity.Dto.instructor.process_instructor_dto import ProcessInstructorDTO, QuestionCommentPIDTO, \
    AnswerCommentPIDTO
from dataclasses import asdict

class ProcessInstructorService:

    @classmethod
    def process_instructor(cls, user_id, state):

        query = ProcessInstructorDao.process_instructor(user_id, state)

        comments_dict = {}

        for comment in query:
            process_id = comment['process_id']

            if process_id not in comments_dict:
                comments_dict[process_id] = ProcessInstructorDTO(
                    process_id=comment['process_id'],
                    estado_aprobacion=comment['estado_aprobacion'],
                    user_email=comment['user_email'],
                    user_name=comment['user_name'],
                    trainee_name=comment['trainee_name'],
                    trainee_document=comment['trainee_document'],
                    questionnaire_name=comment['questionnaire_name'],
                    questionnaire_description=comment['questionnaire_description'],
                    comment_state=comment['comment_state'],
                    comment = [],
                    question=[]

                )

            comment_dto = comments_dict[process_id]

            comment_dto.comment.append(comment['comment'])

            question_id = comment['question_id']
            question_exist = next((p for p in comment_dto.question if p.question_id == question_id), None)

            if not question_exist:
                question_exist = QuestionCommentPIDTO(
                    question_id=question_id,
                    question_text=comment['question_text'],
                    question_type=comment['question_type'],
                    question_option=comment['question_option'],
                    answer=[]
                )
                comment_dto.question.append(question_exist)

            answer_dto = AnswerCommentPIDTO(
                reply_id=comment['reply_id'],
                reply=comment['reply']
            )
            question_exist.answer.append(answer_dto)

        return [asdict(dto) for dto in comments_dict.values()]
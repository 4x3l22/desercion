from appdesercion.Entity.Dao.instructor.list_trainees_dao import ListTraineesDAO
from appdesercion.Entity.Dto.instructor.list_trainees_dto import TraineesDTO


class ListTraineesService:

    @classmethod
    def list_for_instructor(cls, id_instructor):

        query = ListTraineesDAO().list_for_instructor(id_instructor)

        list_trainees = [
            TraineesDTO(
                ID_trainees=trainee['ID_trainees'],
                trainees_name=trainee['trainees_name'],
                trainees_document=trainee['trainees_document'],
                trainees_email=trainee['trainees_email'],
                trainees_process=trainee['trainees_process']
            )
            for trainee in query
        ]

        return list_trainees
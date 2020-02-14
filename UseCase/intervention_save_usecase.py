from Repository.intervention_repository import InterventionRepository
from UseCase.intervention_save_response_object import InterventionSaveResponseObject


class InterventionSaveUseCase:

    def __init__(self, todo_repo: InterventionRepository):
        self.repository = todo_repo

    def execute(self, request_object):
        self.repository.save(request_object)
        return InterventionSaveResponseObject(True)
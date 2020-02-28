from Repository.intervention_repository import InterventionRepository


class InterventionSaveUseCase:

    def __init__(self, todo_repo: InterventionRepository):
        self.repository = todo_repo

    def execute(self, request_object):
        self.repository.save(request_object)
        return True

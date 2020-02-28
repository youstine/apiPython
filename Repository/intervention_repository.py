import abc


class InterventionRepository(abc.ABC):

    @abc.abstractmethod
    def save(self, todo_task):
        pass

    @abc.abstractmethod
    def get_all(self):
        pass

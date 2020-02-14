class InterventionSaveRequestObject:
    def __init__(self, datatask):
        if "description" not in datatask:
            raise Exception("pas de description")
        else:
            self.__description = datatask["description"]

    @property
    def description(self):
        return self.__description

    #def get_todo_task(self):
        #return ToDoTask(self.description)
class InterventionSaveResponseObject:
    def __init__(self, return_value: bool):
        self.__return_value= return_value

    @property
    def return_value(self):
        return self.__return_value
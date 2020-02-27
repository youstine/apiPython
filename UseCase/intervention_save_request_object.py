from Domain.intervention import Intervention


class InterventionSaveRequestObject:
    def __init__(self, data):
        if "name" not in data:
            raise Exception("Le nom est manquant")
        if "age" not in data:
            raise Exception("l'âge est manquant")
        else:
            self.__name = data["name"]
            self.__age = data["age"]
    @property
    def name(self):
        return self.__name
    @property
    def age(self):
        return self.__age

    def get_intervention(self):
        return Intervention(self.name,self.age)
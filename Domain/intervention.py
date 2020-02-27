class Intervention:
    def __init__(self, data):
        if "client_name" not in data:
            raise Exception("Le nom du client est manquant (client_name)")
        if "tech_name" not in data:
            raise Exception("Le nom du technicien est manquant (tech_name)")
        if "intervention_date" not in data:
            raise Exception("la date d'intervention est manquante (intervention_date)")
        if "intervention_type" not in data:
            raise Exception("le type d'intervention est manquant (intervention_type)")
        if "description" not in data:
            raise Exception("la description de l'intervention est manquante (description)")
        else:
            self.__client_name = data["client_name"]
            self.__tech_name = data["tech_name"]
            self.__intervention_date = data["intervention_date"]
            self.__intervention_type = data["intervention_type"]
            self.__description = data["description"]



    @property
    def client_name(self):
        return  self.__client_name

    @property
    def tech_name(self):
        return self.__tech_name

    @property
    def intervention_type(self):
        return self.__intervention_type

    @property
    def intervention_date(self):
        return self.__intervention_date

    @property
    def description(self):
        return self.__description


class Intervention:
    def __init__(self, object):
            self.__client_name = object.client_name
            self.__tech_name = object.tech_name
            self.__intervention_date = object.intervention_date
            self.__intervention_type = object.intervention_type
            self.__description = object.description



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

    def to_dict(self):
        return {
            "client_name": self.client_name,
            "tech_name":self.__tech_name,
            "intervention_date": str(self.__intervention_date),
            "intervention_type": self.__intervention_type,
            "description":self.__description
        }

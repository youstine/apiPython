class Intervention:
    def __init__(self, objet):
        self.__client_name = object.client_name
        self.__tech_name = object.tech_name
        self.__intervention_date = object.intervention_date
        self.__intervention_type = object.intervention_type
        self.__description = object.description

    @property
    def client_name(self):
        return  self.__client

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
    def desecription(self):
        return self.__description

    def to_dict(self):
        return {
            'name': self.__name,
            'age': str(self.__age)
        }
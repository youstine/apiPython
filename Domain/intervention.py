class Intervention:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @property
    def name(self):
        return  self.__name

    @property
    def age(self):
        return self.__age

    def to_dict(self):
        return {
            'name': self.__name,
            'age': str(self.__age)
        }
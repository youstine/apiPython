from constantes import CONSTANTE


class Configuration:
    def __init__(self):
        self.__config = CONSTANTE.CONF

    def _get_value(self, property_name):
        if property_name not in self.__config.keys():
            raise Exception("Nom de propriété inconnu")
        else:
            return self.__config[property_name]


class FlaskConfig(Configuration):
    def __init__(self):
        super().__init__()


    @property
    def url_root(self):
        return self._get_value("URL_ROOT")

    @property
    def url_api(self):
        return self._get_value("URL_API")

    @property
    def url_add(self):
        return self._get_value("URL_ADD")

    @property
    def url_list(self):
        return self._get_value("URL_LIST")

    @property
    def log_directory(self):
        return self._get_value("LOG_DIRECTORY")
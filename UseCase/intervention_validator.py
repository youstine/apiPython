from Models.intervention import Intervention
from constantes import CONSTANTE


class InterventionValidatorObject:
    def __init__(self, data):
        try:
            self.client_name = data["client_name"]
            self.tech_name = data["tech_name"]
            self.intervention_date = data["intervention_date"]
            self.intervention_type = data["intervention_type"]
            self.description = data["description"]
        except Exception as exc:
            raise Exception(CONSTANTE.INTERV_VALID_ERROR + exc.args[0])

    def get_intervention(self):
        return Intervention(self);

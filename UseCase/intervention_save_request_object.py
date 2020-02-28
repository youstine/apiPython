from Domain.intervention import Intervention


class InterventionSaveRequestObject:
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
            self.client_name = data["client_name"]
            self.tech_name = data["tech_name"]
            self.intervention_date = data["intervention_date"]
            self.intervention_type = data["intervention_type"]
            self.description = data["description"]

    def get_intervention(self):
        return Intervention(self);
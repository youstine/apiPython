from Repository.intervention_repository import InterventionRepository
import json

from Tools.Intervention_json_encoder import InterventionJsonEncoder


class InterventionJsonRepository(InterventionRepository):

    def save(self, todo_task):
        try:
            with open('intervention_data.json', 'a') as f:  # externaliser
                str_task = json.dumps(todo_task, cls=InterventionJsonEncoder)
                f.write(str_task)
            return True
        except Exception as exc:
            print(exc)
            raise exc

    def get_all(self):
        pass
import json
from unittest import TestCase
from app import app

class TestPost_intervention(TestCase):
    def setUp(self):
        app.config["TESTING"] = True
        app.config["DEBUG"] = True
        self.app = app.test_client()
        self.assertEqual(app.debug, True)

    def test_post_intervention(self):
        intervention = {
            "client_name": "Tiffany Castel",
            "tech_name": "Sullivan Delaby",
            "intervention_date": "2020/02/27",
            "intervention_type": "Remplacement matériel",
            "description": "changement de micro-ondes"
        }

        response = self.app.post('/createIntervention',
                                 data=json.dumps(intervention),
                                 content_type='application/json')

        intervention_list = self.app.get('/interventions')
        getall_response = json.loads(intervention_list.data)[-1]
        self.assertEqual(response.status_code, 200, f"test_post : Réponse attendue: 200, réponse reçue: {response.status_code}")
        self.assertEqual(getall_response["client_name"], intervention["client_name"], "test_post_intervention: Le dernier enregistrement de la base de donnéees ne correspond pas à l'entrée")
        self.assertEqual(getall_response["tech_name"], intervention["tech_name"], "test_post_intervention: Le dernier enregistrement de la base de donnéees ne correspond pas à l'entrée")
        self.assertEqual(getall_response["intervention_date"], intervention["intervention_date"], "test_post_intervention: Le dernier enregistrement de la base de donnéees ne correspond pas à l'entrée")
        self.assertEqual(getall_response["intervention_type"], intervention["intervention_type"], "test_post_intervention: Le dernier enregistrement de la base de donnéees ne correspond pas à l'entrée")
        self.assertEqual(getall_response["description"], intervention["description"], "test_post_intervention: Le dernier enregistrement de la base de donnéees ne correspond pas à l'entrée")






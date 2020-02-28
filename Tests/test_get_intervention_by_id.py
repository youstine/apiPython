import json
from unittest import TestCase

from app import app




class TestGet_intervention_by_id(TestCase):

    def setUp(self):
        app.config["TESTING"] = True
        app.config["DEBUG"] = True
        self.app = app.test_client()
        self.assertEqual(app.debug, True)

    def test_get_intervention_by_id(self):
        # arrange
        id_intervention = "1"
        # act
        result_read = {
            "client_name": "Laurent",
            "description": "Le client à une fuite avec sa machine à laver",
            "id": 1,
            "intervention_date": "2020/11/01",
            "intervention_type": "réparation",
            "tech_name": "Bob"
        }
        response = self.app.get('/intervention/' + id_intervention)
        result = json.loads(response.data)[0]
        print(result)
        # assert
        self.assertEqual(response.status_code, 200, f"test_get_by_id : Réponse attendue: 200, réponse reçue: {response.status_code}")
        self.assertEqual(result, result_read, "test_get_by_id: Le résultat de la base de données ne correspond pas à celui recherché")


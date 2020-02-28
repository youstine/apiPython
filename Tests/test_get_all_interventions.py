import json
from unittest import TestCase

from app import app


class TestGet_all_interventions(TestCase):
    def setUp(self):
        app.config["TESTING"] = True
        app.config["DEBUG"] = True
        self.app = app.test_client()
        self.assertEqual(app.debug, True)

    def test_get_all_interventions(self):
        response = self.app.get('/interventions')
        self.assertEqual(response.status_code, 200, f"test_get_all : Réponse attendue: 200, réponse reçue: {response.status_code}")
        #add test result
        assert len(response.data) > 0, "test_get_all : the response is empty"
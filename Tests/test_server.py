import unittest
import json
from app import app

app_sever = app


class TestServer(unittest.TestCase):
    # def setUp(self):
    #     app.config["TESTING"] = True
    #     app.config["DEBUG"] = True
    #     self.app = app.test_client()
    #     self.assertEqual(app.debug, True)

    # def test_home_root(self):
    #     response = self.app_server.get('/', follow_redirects = False)
    #     self.assertEqual(response.status_code, 200)
    #     self.assertEqual(response.data, b"Home page")

    def test_add_root(self):
        response = self.app_server.post('/add', data= json.dumps({
            "client_name": "lolita",
            "description": "La cliente à une fuite avec son lave vaisselle",
            "intervention_date": "2020/01/01",
            "intervention_type": "réparation",
            "tech_name": "jack"
        }),content_type='application/json')
        self.assertEqual(response.status_code, 200)


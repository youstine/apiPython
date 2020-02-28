import unittest

from flask import json

from Repository.intervention_db_repository import InterventionDbRepository
from constantes import CONSTANTE

# repo = InterventionDbRepository(CONSTANTE.CONNECTION_STRING)
#
# result_read = {
#     "client_name": "Laurent",
#     "description": "Le client à une fuite avec sa machine à laver",
#     "id": 3,
#     "intervention_date": "2020/11/01",
#     "intervention_type": "réparation",
#     "tech_name": "Bob"
#   }

class MyTestCase(unittest.TestCase):

    def test_db_connection(self):
        repo = InterventionDbRepository(CONSTANTE.CONNECTION_STRING)
        self.assertIsNotNone(repo)

    # def reset_db(self):
    #     # fonction qui drop les tables et relance le fichier sqlile.py
    #
    #
    # def test_get_all_intervention(self):
    #     repo = InterventionDbRepository(CONSTANTE.CONNECTION_STRING)
    #     response = repo.get_all()
    #     self.assertCountEqual(response, 3)


    def test_read_intervention(self):
        # arrange
        id_intervention = 3
        repo = InterventionDbRepository(CONSTANTE.CONNECTION_STRING)
        # act
        response = repo.get_intervention_by_id(id_intervention)

        result_read = [{
            "client_name": "Laurent",
            "description": "Le client à une fuite avec sa machine à laver",
            "id": 3,
            "intervention_date": "2020/11/01",
            "intervention_type": "réparation",
            "tech_name": "Bob"
        }]
        # assert
        self.assertEqual(result_read, response)



    # def test_something(self):
    #     self.assertEqual(True, False)
    #
    # def setUp(self) -> None:
    #     self.repo = InterventionDbRepository
    #
    # def test_init_connection_db(self):
    #     self.assertIsNotNone(self.repo.connection)
    #
    # def test_init_cursor(self):
    #     self.assertIsNotNone(self.repo.cursor)
    #
    # # test read
    # def test_read_table_intervention(self):
    #     id_intervention = 3
    #     result = repo.get_intervention_by_id(id_intervention)
    #     self.assertEqual(result, result_read)




if __name__ == '__main__':
    unittest.main()

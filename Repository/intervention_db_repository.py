import sqlite3

from Repository.intervention_repository import InterventionRepository


class InterventionDbRepository(InterventionRepository):
    def __init__(self, connection_string):
        self.__conn = sqlite3.connect(connection_string)
        self.__cursor = self.__conn.cursor()

    @property
    def connection(self):
        return self.__conn

    @property
    def cursor(self):
        return self.__cursor

    def create_table(self, sqlCmd):
        self.__execute_commande(sqlCmd)
        return True

    def __execute_commande(self, sqlCommand):
        self.__cursor.execute(sqlCommand)


    def __commit(self):
        self.__conn.commit()

    def save(self, intervention):
        insertCmd = f"INSERT INTO INTERVENTION(client_name, tech_name,intervention_date, intervention_type, description) VALUES('{intervention.client_name}', '{intervention.tech_name}','{intervention.intervention_date}','{intervention.intervention_type}','{intervention.desecription}')"
        self.__execute_commande(insertCmd)
        self.__commit()
        return True

    def get_all(self):
        readCmd = f"SELECT * FROM INTERVENTION"
        self.__execute_commande(readCmd)
        lstRecords = []
        for row in self.cursor:
            lstRecords.append(dict_factory(self.cursor, row))
            print(lstRecords)
        return lstRecords


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

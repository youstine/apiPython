import sqlite3

from constantes import CONSTANTE


class ManageSqlLite:
    def __init__(self, base_name):
        self.conn = sqlite3.connect(base_name)
        self.cursor = self.conn.cursor()

    def drop_table(self, table_name):
        sql_cmd = f"DROP TABLE IF EXISTS {table_name}"
        self.cursor.execute(sql_cmd)

    def create_table(self, table_name):
        sql_cmd = f"CREATE TABLE IF NOT EXISTS {table_name}(" \
                  f" id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE," \
                  f" client_name TEXT," \
                  f" tech_name TEXT," \
                  f" intervention_date DATE," \
                  f" intervention_type TEXT," \
                  f" description TEXT)"
        self.execute_commande(sql_cmd)

    def execute_commande(self, sql_command):
        self.cursor.execute(sql_command)

    def return_liste_record(self, sql_select_command):
        lst_records = []
        self.execute_commande(sql_select_command)
        for row in self.cursor:
            lst_records.append('{0} : {1}'.format(row[0], row[1]))
        return lst_records

    def commit(self):
        self.conn.commit()

    def insert_interv_in_database(self, interv):
        self.cursor.execute("""INSERT INTO intervention(client_name, tech_name, intervention_date, intervention_type, 
        description) VALUES(:client_name, :tech_name, :intervention_date, :intervention_type, :description)""", interv)

    def db_creation(self):
        list_intervention = CONSTANTE.MOCK_DATA
        bdd = ManageSqlLite(CONSTANTE.DB_NAME)
        bdd.drop_table(CONSTANTE.TABLE_NAME)
        bdd.create_table(CONSTANTE.TABLE_NAME)
        for interv in list_intervention:
            bdd.insert_interv_in_database(interv)
        bdd.commit()


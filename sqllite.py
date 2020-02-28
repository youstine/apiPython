import sqlite3


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




list_intervention = [
    {"client_name": "Laurent", "tech_name": "Bob", "intervention_date": "2020/11/01", "intervention_type": "réparation",
     "description": "Le client à une fuite avec sa machine à laver"},
    {"client_name": "Natacha", "tech_name": "Dorian", "intervention_date": "2020/06/23", "intervention_type": "diagnostique",
     "description": "Le client demande une intervention pour vérifier son lave vaisselle"}
]

bdd = ManageSqlLite("ma_base.db")
bdd.drop_table("intervention")
bdd.create_table("intervention")
for interv in list_intervention:
    bdd.insert_interv_in_database(interv)
bdd.commit()
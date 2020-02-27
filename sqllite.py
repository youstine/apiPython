import sqlite3


class ManageSqlLite:
    def __init__(self, baseName):
        self.conn = sqlite3.connect(baseName)
        self.cursor = self.conn.cursor()

    def create_table(self, tableName):
        sqlCmd = f"CREATE TABLE IF NOT EXISTS {tableName}(" \
                 f" id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE," \
                 f" client_name TEXT," \
                 f" tech_name TEXT," \
                 f" intervention_date DATE," \
                 f" intervention_type TEXT," \
                 f" description TEXT)"
        self.execute_commande(sqlCmd)

    def execute_commande(self, sqlCommand):
        self.cursor.execute(sqlCommand)

    def return_liste_record(self, sqlSelectCommand):
        lstRecords = []
        self.execute_commande(sqlSelectCommand)
        for row in self.cursor:
            lstRecords.append('{0} : {1}'.format(row[0], row[1]))
        return lstRecords

    def commit(self):
        self.conn.commit()

    def insert_interv_in_database(self, interv):
        self.cursor.execute("""INSERT INTO intervention(client_name, tech_name, intervention_date, intervention_type, 
        description) VALUES(:client_name, :tech_name, :intervention_date, :intervention_type, :description)""", interv)


bdd = ManageSqlLite("ma_base.db")
bdd.create_table("intervention")

list_intervention = [
    {"client_name": "Laurent", "tech_name": "Bob", "intervention_date": "2020/11/01", "intervention_type": "réparation",
     "description": "Le client à une fuite avec sa machine à laver"},
    {"client_name": "Natacha", "tech_name": "Dorian", "intervention_date": "2020/06/23", "intervention_type": "diagnostique",
     "description": "Le client demande une intervention pour vérifier son lave vaisselle"}
]
for interv in list_intervention:
    bdd.insert_interv_in_database(interv)
bdd.commit()
lstInterv = bdd.return_liste_record("SELECT * FROM intervention")
print(lstInterv)

#
# cursor.execute("""
# DROP TABLE users
# """)
# conn.commit()

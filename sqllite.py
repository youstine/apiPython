import sqlite3


class ManageSqlLite:
    def __init__(self, baseName):
        self.conn = sqlite3.connect(baseName)
        self.cursor = self.conn.cursor()

    def create_table(self, tableName):
        sqlCmd = f"CREATE TABLE IF NOT EXISTS {tableName}(" \
                 f" id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE," \
                 f" name TEXT," \
                 f" age INTEGER)"
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
        self.cursor.execute("""INSERT INTO intervention(name, age) VALUES(:name, :age)""", interv)

    #def insert_tech_in_database(self, tech):
    #   self.cursor.execute("""INSERT INTO technicien(nomTech, service, number) VALUES(:nomTech, :service, :number)""",
    #                       tech)


bdd = ManageSqlLite("ma_base.db")
bdd.create_table("intervention")
bdd.create_table("technicien")

list_intervention = [{"name": "Laurent", "age": 46}, {"name": "Greg", "age": 42}, {"name": "Clément", "age": 28}]
for interv in list_intervention:
    bdd.insert_interv_in_database(interv)
bdd.commit()
lstInterv = bdd.return_liste_record("SELECT * FROM intervention")
print(lstInterv)

#list_technicien = [{"nomTech": "Bernard", "service": "chauffage", "number": "0652255555"},
                  # {"nomTech": "Nada", "service": "plomberie", "number": "0652255555"}]
#for tech in list_technicien:
    #bdd.insert_tech_in_database(tech)
#bdd.commit()


#lstTech = bdd.return_liste_record("SELECT * FROM technicien")
#print(listTech)

#
# cursor.execute("""
# DROP TABLE users
# """)
# conn.commit()

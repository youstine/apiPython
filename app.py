from flask import Flask, request, jsonify
from sqllite import ManageSqlLite

app = Flask(__name__)

app.config["DEBUG"] = True

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d



@app.route('/', methods=['GET'])
def home():
    return 'Bienvenue dans notre api Python'


@app.route('/interventions', methods=['GET'])
def api_all():
    ManageSqlLite('ma_base.bd')
    all_interventions = ManageSqlLite.return_liste_record()
    return jsonify(all_interventions)



@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404



    app.run()

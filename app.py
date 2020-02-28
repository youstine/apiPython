from flask import Flask, request, jsonify

from Repository.intervention_db_repository import InterventionDbRepository
from UseCase.intervention_validator import InterventionValidatorObject
from UseCase.intervention_save_usecase import InterventionSaveUseCase
from constantes import CONSTANTE
from init_sqlite_db import ManageSqlLite
import json

app = Flask(__name__)
app.config["DEBUG"] = True
db = ManageSqlLite(CONSTANTE.DB_NAME)
db.db_creation()


@app.route('/', methods=['GET'])
def home():
    return 'Bienvenue dans notre api Python'


@app.route('/interventions', methods=['GET'])
def get_all_interventions():
    # On cree une connexion à la bdd
    repo = InterventionDbRepository(CONSTANTE.DB_NAME)
    # On execute un getAll
    all_interventions = repo.get_all()
    return jsonify(all_interventions)


@app.route('/intervention/<id_intervention>', methods=['GET'])
def get_intervention_by_id(id_intervention):
    try:
        # On crée une connexion à la bdd
        repo = InterventionDbRepository(CONSTANTE.DB_NAME)
        # On execute un getAll
        intervention = repo.get_intervention_by_id(id_intervention)
        return jsonify(intervention)
    except Exception as exc:
        # print("BUG? " + str(exc))
        return str(exc), 400, {}


@app.route('/intervention/create', methods=['POST'])
def post_intervention():
    try:
        # On récupère le json de la requête
        request_content = request.get_json()
        # On le passe dans le validateur
        request_object = InterventionValidatorObject(request_content)
        # On transforme le json en objet Intervention
        intervention = InterventionValidatorObject.get_intervention(request_object)
        # On crée une connexion à la bdd
        repo = InterventionDbRepository(CONSTANTE.DB_NAME)
        # On instancie une requête
        uc = InterventionSaveUseCase(repo)
        # On retourne le résultat de l'execution de la requête
        uc.execute(intervention)
        return f"intervention créée: <br/> {intervention.to_dict()}"
    except Exception as exc:
        # print("BUG? " + str(exc))
        return str(exc), 400, {}


@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404


if __name__ == "__main__":
    app.run()

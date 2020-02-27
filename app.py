import os

from flask import Flask, request, jsonify

from Repository.intervention_db_repository import InterventionDbRepository
from UseCase.intervention_save_request_object import InterventionSaveRequestObject
from UseCase.intervention_save_usecase import InterventionSaveUseCase
from sqllite import ManageSqlLite
from constantes import *

app = Flask(__name__)

app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():
    return 'Bienvenue dans notre api Python'


CONNECTION_STRING = CONSTANTE.CONNECTION_STRING


@app.route('/interventions', methods=['GET'])
def api_all():
    # On crée une connexion à la bdd
    repo = InterventionDbRepository(CONNECTION_STRING)
    #On execute un getAll
    all_interventions = repo.get_all()
    return jsonify(all_interventions)


@app.route('/test', methods=['POST'])
def post():
    try:
        # On récupère le json de la requête
        request_content = request.get_json()
        # On save le Json dans un objet Intervention
        task_request = InterventionSaveRequestObject(request_content)
        # On crée une connexion à la bdd
        repo = InterventionDbRepository(CONNECTION_STRING)
        # On save l'objet en bdd?
        uc = InterventionSaveUseCase(repo)
        response = uc.execute(task_request.get_intervention())
        print(response.return_value)
        return "WORKS"
    except Exception as exc:
        print("BUG? " + str(exc))
        return str(exc), 400, {}


@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404

    app.run()

from flask import Flask, request, jsonify

from Domain.intervention import Intervention
from Repository.intervention_db_repository import InterventionDbRepository
from UseCase.intervention_save_request_object import InterventionSaveRequestObject
from UseCase.intervention_save_usecase import InterventionSaveUseCase
from constantes import CONSTANTE

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return 'Bienvenue dans notre api Python'


@app.route('/interventions', methods=['GET'])

def get_all_interventions():
    # On crée une connexion à la bdd
    repo = InterventionDbRepository(CONSTANTE.CONNECTION_STRING)
    # On execute un getAll
    all_interventions = repo.get_all()
    return jsonify(all_interventions)



@app.route('/interventions/id/<id_intervention>', methods=['GET'])
def get_intervention_by_id(id_intervention):
    # On crée une connexion à la bdd
    repo = InterventionDbRepository(CONSTANTE.CONNECTION_STRING)
    # On execute un getAll
    intervention = repo.get_intervention_by_id(id_intervention)
    return jsonify(intervention)

@app.route('/createIntervention', methods=['POST'])
def post_intervention():
    try:
        # On récupère le json de la requête
        request_content = request.get_json()
        # On crée une connexion à la bdd
        repo = InterventionDbRepository(CONSTANTE.CONNECTION_STRING)
        # On instancie une requête
        uc = InterventionSaveUseCase(repo)
        # On retourne le résultat de l'execution de la requête
        return str(uc.execute(Intervention(request_content)))
    except Exception as exc:
        # print("BUG? " + str(exc))
        print("Error : " + str(exc))
        return str(exc), 400, {}


@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404


if __name__ == "__main__":
    app.run()

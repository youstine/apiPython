from flask import Flask, request

from Repository.intervention_db_repository import InterventionDbRepository
from UseCase.intervention_save_request_object import InterventionSaveRequestObject
from UseCase.intervention_save_usecase import InterventionSaveUseCase

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Bienvenue dans notre api Python'


CONNECTION_STRING = "C:\\GUILDE DE DEV\\EPSI\\Python\\Code\\ToDo\\Tests\\todo.db"


@app.route("/add", methods=['POST'])
def add():
    try:
        data_task = request.get_json(force=True)
        task_request = InterventionSaveRequestObject(data_task)
        # repo = TodoJsonRepository()
        repo = InterventionDbRepository(CONNECTION_STRING)
        uc = InterventionSaveUseCase(repo)
        response = uc.execute(task_request.get_todo_task())
        return "{}".format(int(response.return_value)), {"Content-Type": "application/plaintext"}
    except Exception as exc:
        return str(exc), 400, {}


if __name__ == '__main__':
    app.run()

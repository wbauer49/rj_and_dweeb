
import flask

import project_list


app = flask.Flask(__name__)


@app.route("/")
def index():
    return flask.render_template("index.html", projects=project_list.PROJECT_LIST)


@app.route("/view/<project_name>")
def view(project_name):
    for project in project_list.PROJECT_LIST:
        if project.name == project_name:
            return flask.render_template("view.html", project=project)
    raise ValueError(project_name)


import flask


app = flask.Flask(__name__)

PROJECTS = {
    "project1": "Project 1",
    "project2": "Project 2",
    "project3": "Project 3",
}


@app.route("/")
def index():
    return flask.render_template("index.html", projects=PROJECTS)


@app.route("/view/<project>")
def view(project):
    return flask.render_template("view.html", projects=PROJECTS, project=project)

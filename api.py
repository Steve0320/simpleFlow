# Main API
from flask import Flask, redirect

app = Flask(__name__)


@app.route("/")
def homepage():
    return redirect('/static/index.html')


# Load a given workflow
@app.route("/api/workflows/load")
def load_workflow():
    pass


# Save a workflow (takes a built graph from the UI and serializes it to a file
@app.route("/api/workflows/save")
def save_workflow():
    pass


# Run the loaded workflow with the given args
@app.route("/api/workflows/run")
def run_workflow():
    pass


@app.route("/api/nodes")
def get_defined_nodes():
    pass

# Main API
from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>HELLLOOOOO</p>"


# Load workflow
# Save workflow
# Run workflow (w/ args)
# Get nodes

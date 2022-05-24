#!/usr/bin/python3
"""Inicia una app en flask"""

from flask import Flask, render_template
from models import storage
from models.state import State
app = Flask(__name__)


@app.teardown_appcontext
def cerrar(self):
    """Elimina la sesión actual de SQLAlchemy"""
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def lista():
    """Con la funcion all muestra una lista de todos los estados"""
    states = storage.all(State).values()
    return(render_template("8-cities_by_states.html", states=states))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

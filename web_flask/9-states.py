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


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def lista(id=None):
    """Con la funcion all muestra una lista de todos los estados
    y verificando si manda el id o no mostramos ya sea un registro
    o todos o ninguno."""
    states = storage.all(State).values()
    if id is not None:
        for estado in states:
            if estado.id == id:
                return(render_template("9-states.html", states=estado))
        return(render_template("9-states.html"))
    return(render_template("9-states.html", states=states, vari=True))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

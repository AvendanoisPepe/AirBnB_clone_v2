#!/usr/bin/python3
"""Inicia una app en flask"""

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def funcioncita():
    """Devuelve una cadena en la ruta raíz"""
    return("Hello HBNB!")


@app.route('/hbnb', strict_slashes=False)
def funcioncitaRuta():
    """Devuelve una cadena en la ruta /hbnb"""
    return("HBNB")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

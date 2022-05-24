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


@app.route('/c/<text>', strict_slashes=False)
def funcioncitaC(text):
    """Devuelve una cadena en la ruta /c/<text>
    y reemplaza los _ con espacios"""
    return("C {}".format(text.replace("_", " ")))


@app.route('/python/<text>', strict_slashes=False)
@app.route('/python', strict_slashes=False)
def funcioncitaP(text="is cool"):
    """Devuelve una cadena en la ruta /python/<text>
    y reemplaza los _ con espacios, con texto predeterminado
    """
    return("Python {}".format(text.replace("_", " ")))


@app.route('/number/<int:n>', strict_slashes=False)
def funcioncitaNum(n):
    """Devuelve una cadena en la ruta /number/<n>
    y imprime solo si es un entero"""
    if type(n) is int:
        return("{} is a number".format(n))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

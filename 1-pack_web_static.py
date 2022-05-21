#!/usr/bin/python3
"""Escriba un script de Fabric que genere un archivo .tgz a partir del
contenido de la carpeta web_static de su repositorio AirBnB Clone,
usando la función do_pack.

tar -czvf nombre-archivo.tar.gz /directorio/archivos
"""
from fabric.api import local
from datetime import datetime


def do_pack():
    """Creamos la carpeta versions usando fabric y sus comandos
    locales, al igual que creamos el archivo .tgz"""
    local("mkdir -p versions")
    nombre = datetime.now().strftime("%Y%m%d%H%M%S")
    archivo = "web_static_{}.tgz".format(nombre)
    local("tar -cvzf {} web_static".format(archivo))
    if archivo:
        return(archivo)
    else:
        return (None)

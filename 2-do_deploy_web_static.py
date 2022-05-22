#!/usr/bin/python3
"""Escriba un script de Fabric (basado en el archivo 1-pack_web_static.py)
que distribuya un archivo a sus servidores web, usando la función do_deploy:
"""
from fabric.api import local, run, put, env
from datetime import datetime
import os

env.hosts = ["34.73.84.99", "3.93.174.191"]


def do_pack():
    """Creamos la carpeta versions usando fabric y sus comandos
    locales, al igual que creamos el archivo .tgz"""
    local("mkdir -p versions")
    nombre = datetime.now().strftime("%Y%m%d%H%M%S")
    archivo = "versions/web_static_{}.tgz".format(nombre)
    local("tar -cvzf {} web_static".format(archivo))
    if archivo:
        return(archivo)
    else:
        return (None)


def do_deploy(archive_path):
    """Distribuye un archivo a sus servidores web."""
    if os.path.exists(archive_path):
        url = "/data/web_static/releases/"
        nombre = archive_path.split('.')[0].split('/')[1]
        destino = url + nombre
        try:
            put(archive_path, '/tmp')
            run('mkdir -p {}'.format(destino))
            run('tar -xzf /tmp/{}.tgz -C {}'.format(nombre, destino))
            run('rm -f /tmp/{}.tgz'.format(nombre))
            run('mv {}/web_static/* {}/'.format(destino, destino))
            run('rm -rf {}/web_static'.format(destino))
            run('rm -rf /data/web_static/current')
            run('ln -s {} /data/web_static/current'.format(dest))
            return(True)
        except Exception:
            return(False)
    else:
        return(False)

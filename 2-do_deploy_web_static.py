#!/usr/bin/python3
"""Escriba un script de Fabric (basado en el archivo 1-pack_web_static.py)
que distribuya un archivo a sus servidores web, usando la función do_deploy:
"""
from fabric.api import local, run, put, env
from datetime import datetime
import os

env.hosts = ["34.73.84.99", "3.93.174.191"]
env.user = "ubuntu"

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
    """
    Function that distributes an archive.
    """
    name_dir = archive_path[9:-4]
    if os.path.exists(archive_path):
        put(archive_path, '/tmp/')
        run("sudo mkdir -p /data/web_static/releases/{}/".format(name_dir))
        run("sudo tar -xzf /tmp/{}.tgz -C \
        /data/web_static/releases/{}/".format(name_dir, name_dir))
        run("sudo rm /tmp/{}.tgz".format(name_dir))
        run("sudo mv /data/web_static/releases/{}/web_static/* \
            /data/web_static/releases/{}/".
            format(name_dir, name_dir))
        run("sudo rm -rf /data/web_static/releases/{}/web_static"
            .format(name_dir))
        run("sudo rm -rf /data/web_static/current")
        run("sudo ln -s /data/web_static/releases/{}/ \
            /data/web_static/current".format(name_dir))
        print("New version deployed!")
        return True
    else:
        return False
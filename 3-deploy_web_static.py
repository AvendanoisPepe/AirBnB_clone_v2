#!/usr/bin/python3
"""Escriba un script de Fabric (basado en el archivo 1-pack_web_static.py)
que distribuya un archivo a sus servidores web, usando la función do_deploy:
"""
from fabric.api import local, run, put, env
from datetime import datetime
from os import path

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
    """distribuye un archivo a los servidores web"""
    if path.isfile(archive_path):
        name_file = archive_path[9:]
        new_path = "/data/web_static/releases/"
        path_server_file = '/tmp/{}'.format(name_file)
        put(archive_path, '/tmp/')
        run('sudo mkdir -p {}'.format(new_path))
        run("sudo tar -xzf {} -C {}/".format(path_server_file, new_path))
        run('sudo rm {}'.format(path_server_file))
        run('sudo rm -rf {}'.format('/data/web_static/current'))
        run(
            "sudo ln -s {} /data/web_static/current".format(
                "/data/web_static/releases/web_static"
            )
        )
        print("New version deployed!")
        return True

    return False


def deploy():
    """crea y distribuye un archivo a sus servidores we"""
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)

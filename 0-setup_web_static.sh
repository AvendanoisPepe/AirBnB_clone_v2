#!/usr/bin/env bash
# Configura los servidores web para la implementación de web_static.

# Instale Nginx si aún no está instalado
sudo apt-get update
sudo apt-get install -y nginx
sudo service nginx start

# creamos las carpetas requeridas y el archivo
mkdir -p /data/
mkdir -p /data/web_static/
mkdir -p /data/web_static/releases/
mkdir -p /data/web_static/shared/
mkdir -p /data/web_static/releases/test/
touch /data/web_static/releases/test/index.html

# contendio del archivo
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" > /data/web_static/releases/test/index.html

# Creamos el enlace simbolico con -s para que sea simbolico y con -f para que se elimine si ya existe
sudo ln -sf /data/web_static/releases/test /data/web_static/current

# Otorgue la propiedad de la carpeta /data/ al usuario Y grupo de ubuntu con -R para que sea recursivo
sudo chown -hR ubuntu:ubuntu /data

# Agregar alias para servir el contenido de /data/web_static/current a hbnb_static
sed -i '/listen 80 default_server;/a location /hbnb_static { alias /data/web_static/current/;}' /etc/nginx/sites-available/default

# reiniciamos el servicio.
sudo service nginx restart

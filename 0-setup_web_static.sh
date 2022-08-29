#!/usr/bin/env bash
# Script that sets up webserver for the deployment of web_static

apt-get update
apt-get install -y nginx
mkdir -p /data/web_static/releases/test /data/web_static/shared/
echo " Holberton School - Web_static test " > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current
chown -hR ubuntu:ubuntu /data/
sed -i "/listen 80 default_server/a \\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n" /etc/nginx/sites-available/default
service nginx restart

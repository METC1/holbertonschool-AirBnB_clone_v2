#!/usr/bin/env bash
# Script that sets up webserver for the deployment of web_static

apt-get update
apt-get install -y nginx

mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/
echo "Holberton School - test /data/web_static/.../index.html"  > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current
chown -hR ubuntu:ubuntu /data/
sudo sed -i '/server_name_;/a \n\tlocation /hbnb_static {\n\talias /data/web_static/current/;\n\t}' /etc/nginx/sites-available/default
sudo sed -i '/server_name_;/a \n\tlocation /hbnb_static {\n\talias /data/web_static/current/;\n\t}' /etc/nginx/sites-enabled/default
service nginx restart

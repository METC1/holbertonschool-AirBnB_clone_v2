#!/usr/bin/env bash
# Script that sets up webserver for the deployment of web_static

apt-get update
apt-get install -y nginx

mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared
chown -R ubuntu:ubuntu /data/
cat > /data/web_static/releases/test/index.html <<'EOF'
<html>
<head>
</head>
<body>
    <h1>Holberton Scholl - test /data/web_static/releases/test/index.html</h1>
</body>
</html>  
EOF
ln -sf /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu:ubuntu /data/
sudo sed -i '+server_name_;+a \n\tlocation /hbnb_static {\n\talias /data/web_static/current/;\n\t}' /etc/nginx/sites-available/default
service nginx restart

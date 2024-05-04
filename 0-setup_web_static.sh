#!/usr/bin/env bash
# Write a Bash script that sets up your web servers for the deployment of web_static.


apt update -y
apt install -y nginx

echo "Hello World! from Imole" > /var/www/html/index.html
echo "Ceci n'est pas une page some error!" > /var/www/html/404.html



mkdir -p /data/web_static/releases/test
mkdir -p /data/web_static/shared/

echo "fake content here!" > /data/web_static/releases/test/index.html

symL="/data/web_static/current"

# if [ -e "$symL" ]
# then

rm -f "$symL"
ln -s /data/web_static/releases/test/ "$symL"

chown -R ubuntu:ubuntu /data/

my_config=\
"
server {
    listen 80 default_server;
    listen [::]:80 default_server;
    add_header X-Served-By "$HOSTNAME";

    root /var/www/html;
    index index.html index.htm index.nginx-debian.html;

    server_name _;

    error_page 404 /404.html;
    location = /404.html {
        internal;
    }

    location /hbnb_static {
        alias /data/web_static/current;
        index index.html index.htm;
    }
    location /redirect_me {
        return 301 https://github.com/imoleBytes;
    }
}
"
echo "$my_config" > /etc/nginx/sites-available/default

service nginx restart

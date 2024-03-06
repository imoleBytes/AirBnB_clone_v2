#!/usr/bin/env bash
# Write a Bash script that sets up your web servers for the deployment of web_static.

apt update -y
apt install nginx -y

mkdir -p /data/web_static/releases/test/
mkdir /data/web_static/shared/
echo "fake html content" > /data/web_static/releases/test/index.html


file_path="/data/web_static/current"

if [ -e "$file_path" ]
then
    echo "File exists"
    rm "$file_path"
    ln /data/web_static/releases/test/ /data/web_static/current
else
    echo "File does not exist"
    ln /data/web_static/releases/test/ /data/web_static/current
fi

chown -R ubuntu:ubuntu /data/
my_config=\
"
server {
    listen 80 default_server;
    listen [::]:80 default_server;
    add_header X-Served-By $HOSTNAME;
    root   /var/www/html;
    index  index.html index.htm;
    location /hbnb_static {
        alias /data/web_static/current;
        index index.html index.htm;
    }
    location /redirect_me {
        return 301 https://github.com/imoleBytes;
    }
    error_page 404 /404.html;
    location /404 {
      root /var/www/html;
      internal;
    }
}
"
echo "$my_config" > /etc/nginx/sites-available/default

service nginx restart

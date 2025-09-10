#!/bin/bash

sudo dnf update -y
sudo dnf install httpd -y
sudo systemctl start httpd
sudo systemctl enable httpd
echo "Welcome to Surgical Six webserver" > /var/www/html/index.html

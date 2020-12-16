#!/bin/bash
sudo apt update
sudo apt-get install python3-venv -y

python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt

sudo mkdir /opt/Family-Space
sudo chown -R jenkins /opt/Family-Space

sudo system daemon-reload
sudo systemctl stop family-space.service
sudo systemctl start family-space.service
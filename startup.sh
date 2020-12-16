#!/bin/bash
sudo apt update
sudo apt-get install python3-venv -y

python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt

sudo cp family-space.service /etc/systemd/system/family-space.service

sudo systemctl daemon-reload
sudo systemctl start family-space.service
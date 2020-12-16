#!/bin/bash 
sudo apt update
sudo apt-get install python3-venv


cd ..
sudo cp -r fs-app /opt/
sudo chown -R jenkins /opt/fs-app
cd /opt/fs-app
python3 -m venv venv
source venv/bin/activate

pip3 install -r requirements.txt
python3 app.py

sudo systemctl daemon-reload
sudo systemctl stop app.service
sudo systemctl start app.service

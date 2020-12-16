#!/bin/bash 
sudo apt update
sudo apt-get install python3-venv
ls

cd ..
sudo cp -r fs-app /opt/jenkins
sudo chown -R jenkins /opt/jenkins
cd /opt/jenkins/fs-app
python3 -m venv venv
source venv/bin/activate


pip3 install -r requirements.txt
pip3 list

 
sudo systemctl daemon-reload
sudo systemctl stop app.service
sudo systemctl start app.service

#!/bin/bash
sudo apt-get update
sudo apt-get install python3
sudo apt-get install python3-venv -y
cd $WORKSPACE 
ls -lh 

sudo cp -r $WORKSPACE /opt/jenkins
sudo chown -R jenkins /opt/jenkins
cd ~ 
cd /opt/jenkins/fs-app
python3 -m venv venv
source venv/bin/activate

pip3 install -r requirements.txt 
pip3 list

sudo systemctl daemon-reload
sudo systemctl stop app.service
sudo systemctl start app.service
echo "works"
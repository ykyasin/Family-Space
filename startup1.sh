#!/bin/bash 
sudo apt update
sudo apt-get install python3-venv
ls

echo "my breaak <------------------------------------------->"
echo "my breaak <------------------------------------------->"
echo "my breaak <------------------------------------------->"

cd ..
sudo cp -r fs-app /opt/jenkins
sudo chown -R jenkins /opt/jenkins
cd /opt/jenkins/fs-app
python3 -m venv venv
source venv/bin/activate
#cd $WORKSPACE
#ls -lah
#sudo cp -r $WORKSPACE /opt/jenkins
#sudo chown -R jenkins /opt/jenkins
#python3 -m venv venv
#source venv/bin/activate
echo "my breaak <------------------------------------------->"
echo "my breaak <------------------------------------------->"
echo "my breaak <------------------------------------------->"
pip3 install -r requirements.txt
pip3 list

 
#sudo chown -R jenkins /opt/jenkins

sudo systemctl daemon-reload
sudo systemctl stop app.service
sudo systemctl start app.service

# From jenkins: . startup.sh
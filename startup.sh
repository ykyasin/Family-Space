#!/bin/bash 

cd /opt/fs-app
sudo chown -R fs-app
sudo python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt

ls

echo "-------------------------------------My Tests------------------------------------------"

python3 create.py
python3 app.py  

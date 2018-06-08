#!/bin/bash

sudo service camera stop 
source /home/pi/.virtualenvs/smart/bin/activate
cd smartserve-camera/scripts
python camera-daemon.py
$SHELL

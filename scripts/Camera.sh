#!/bin/bash

sudo service camera stop 
source /home/pi/.virtualenvs/cv/bin/activate
cd OpenCV/smartserve-camera/scripts
python camera-daemon.py
$SHELL

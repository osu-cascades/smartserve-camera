# SmartServe Camera

Smartserve v0.1 utilizes computer vision and image analyses libraries to compute the difference between images, all on a raspberry pi! The initial prototype will be used to gather data which will then be used to train a machine learning model to calculate the food waste in a restaurant setting. This project is under active development.

## Setup

### Assumptions

- Raspberry Pi 3 model B
- Running Raspian Jessie (Raspbian Stretch will have slightly different setup steps)
- `sudo apt-get update && sudo apt-get upgrade` completed

### Hardware Requirements

- Pi Camera Module v2
- Button
- Jumper Wires

### Software Requirements

- `cd scripts/ && pip install -r requirements.txt`
- OpenCV, I would suggest this guide [Accessing the Raspberry Pi Camera with OpenCV and Python](https://www.pyimagesearch.com/2015/03/30/accessing-the-raspberry-pi-camera-with-opencv-and-python/) for installation and use
- Sqlite3 `sudo apt-get install sqlite3`
- We currently have the script running automatically at boot time in order to enable that you will need to run `sudo cp camera.service /etc/systemd/system/camera.service` checkout this guide for more information on Systemd [Creating a Service](https://www.raspberrypi.org/documentation/linux/usage/systemd.md)

Important note: Some of these libraries take a **long** time to install.

(c) 2018 Taylor Mallory, Justin Tappert, and Yong Bakos. All rights reserved.

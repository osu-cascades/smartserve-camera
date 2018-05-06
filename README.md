# SmartServe Camera

Smartserve v0.1 utilizes computer vision and image analyses libraries to compute the difference between images, all on a raspberry pi! The initial prototype will be used to gather data which will then be used to train a machine learning model to calculate the food waste in a restaurant setting. This project is under active development.

## Setup

To use these scripts you will need to install a lot of dependencies. OpenCV is a complex library that requires many other larde python libraries. Run through the Software requierments and the guides I have linked to get OpenCV running on your raspberry pi. Note: I use a virtual environment, while it is recommended it is not a requirement.

### Assumptions

- Raspberry Pi 3 model B
- Running Raspian Jessie (Raspbian Stretch will have slightly different setup steps)
- `sudo apt-get update && sudo apt-get upgrade` completed

### Hardware Requirements

Checkout [GPIO Zero Recipes](https://gpiozero.readthedocs.io/en/stable/recipes.html) for wiring diagrams and common use cases

- Pi Camera Module v2
- Button
- Jumper Wires

### Software Requirements

- `pip install -r requirements.txt`
- OpenCV, I would suggest this guide [Accessing the Raspberry Pi Camera with OpenCV and Python](https://www.pyimagesearch.com/2015/03/30/accessing-the-raspberry-pi-camera-with-opencv-and-python/) for installation and use
- Sqlite3 `sudo apt-get install sqlite3`
- We currently have the script running automatically at boot time in order to enable that you will need to run `sudo cp camera.service /etc/systemd/system/camera.service` after you have updated the ExecStart path as well as the WorkingDirectory path. Checkout this guide for more information on Systemd [Creating a Service](https://www.raspberrypi.org/documentation/linux/usage/systemd.md)

Important note: Some of these libraries take a **long** time to install.

(c) 2018 Taylor Mallory, Justin Tappert, and Yong Bakos. All rights reserved.

# SmartServe Camera

Smartserve v0.1 utilizes computer vision and image analyses libraries to compute the difference between images, all on a raspberry pi! The initial prototype will be used to gather data which will then be used to train a machine learning model to calculate the food waste in a restaurant setting. This project is under active development.

## Setup

To use these scripts you will need to install a lot of dependencies. OpenCV is a complex library that requires many other large python libraries. Run through the Software requirements and the guides I have linked to get OpenCV running on your raspberry pi. Note: I use a virtual environment, while it is recommended it is not a requirement.

### Assumptions

- Raspberry Pi 3 model B
- Running Raspian Jessie (Raspbian Stretch will have slightly different setup steps)
- `sudo apt-get update && sudo apt-get upgrade` completed

### Hardware Requirements

![Wiring Diagram](files/wiring.png)

- Pi Camera Module v2 [Camera Setup Guide](https://projects.raspberrypi.org/en/projects/getting-started-with-picamera)
- Button
- Jumper Wires

### Software Requirements

- OpenCV, follow this guide: [Accessing the Raspberry Pi Camera with OpenCV and Python](https://www.pyimagesearch.com/2016/04/18/install-guide-raspberry-pi-3-raspbian-jessie-opencv-3/) for installation and use
- `pip install -r requirements.txt`
    - if the above command fails for some reason, just install the dependencies one at a time
- Sqlite3 `sudo apt-get install sqlite3`
- We currently have the script running automatically at boot time in order to enable that you will need to run `sudo cp camera.service /etc/systemd/system/camera.service` after you have updated the ExecStart path as well as the WorkingDirectory path. Checkout this guide for more information on Systemd [Creating a Service](https://www.raspberrypi.org/documentation/linux/usage/systemd.md)

Important note: Some of these libraries take a **long** time to install.

### Test Scripts

Within the scripts folder there are a couple of programs to test the components of the working system. To test that the button is working run

`python button_test.py`

You should see 'button not pressed' repeating on the console. When you press the button it will print 'button pressed'. To test the camera run

`python camera_test.py`

and then click the button and a picture will be saved to `/home/pi/`

&copy; 2018 Justin Tappert, and Yong Bakos. All rights reserved.

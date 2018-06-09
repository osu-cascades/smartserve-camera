import subprocess

# copy service to systemctl
print("Copying the camera service to the systemd directory")
subprocess.call(["sudo", "cp", "camera.serve", "/etc/systemd/system/camera.service"])

# enable script on start up
print("Enabling the service on raspberry Pi boot")
subprocess.call(["sudo", "systemctl", "enable", "camera.service"])

# copy desktop script to desktop
print("Copying the desktop script to the Raspberry Pi's Desktop")
subprocess.call(["sudo", "cp", "/home/pi/smartserve-camera/scripts/Camera.desktop", "/home/pi/Desktop/Camera.desktop"])

# change exec permissions
print("Changing execute permissions on the desktop script")
subprocess.call(["sudo", "chmod", "+x", "/home/pi/smartserve-camera/scripts/Camera.sh"])

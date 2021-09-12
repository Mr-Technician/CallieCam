# CallieCam
A website for viewing the inside of a cat shelter.

I'm running a Pi 2 B, some Adafruit 388 IR LEDs, and 100 Ohm resistors. I have each LED/resistor pair on its on GPIO pin.

The camera is a V2 NOIR camera module mounted at the peak of the shelter, with LEDs in each corner.

The LEDs are wired to GPIO pins 3, 5, 7, and 11, with pin 9 for ground

The software setup is simple:

* Install raspbian and make sure wifi is configured. Enable SSH and VNC.
* Install https://elinux.org/RPi-Cam-Web-Interface#Basic_Installation
* Change the port for the camera viewer to 8080 or similar.
* You may need to adjust the exposure mode and ISO.
* Copy `server.py` and `webpage.html` to a folder of your choosing, with the latter under the `templates` subfolder.
* Add the python startup script to rc.local, as described here:
https://www.dexterindustries.com/howto/run-a-program-on-your-raspberry-pi-at-startup/

**Make sure to update the ip addressess and ports in the scripts as needed.**


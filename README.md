# IOTP
Adafruit's Internet of Things Printer using the Python Thermal Printer Library.


Python-Thermal-Printer Library
===============================

## THE ORIGINAL ADAFRUIT REPOSITORY IS ARCHIVED AND IS NO LONGER SUPPORTED OR MAINTAINED

## Python-Thermal-Printer Module

The original Python3 version of the Adafruit [Python-Thermal-Printer](https://github.com/adafruit/Python-Thermal-Printer) library.


## Prerequisites

Install latest Raspbian OS with Python 3 on a new SD Card using the [Raspberry Pi Imager](https://www.raspberrypi.com/software/).  The IOTP printer was set up according to [the original guide](https://learn.adafruit.com/pi-thermal-printer). 

Run a test to see if the printer is working by punching in these commands into the terminal.

``` shell
stty -F /dev/serial0 19200
echo -e "This is a test.\\n\\n\\n" > /dev/serial0
```

## Upgrading

Update the system and install prerequisites.

``` shell
sudo apt-get update
sudo apt-get install git cups wiringpi build-essential libcups2-dev libcupsimage2-dev python3-serial python-pil python-unidecode
```

Install the printer driver. Don't worry about the warnings that make gives.

``` shell
git clone https://github.com/adafruit/zj-58
cd zj-58
make
sudo ./install
```

Make the printer the default printer. This is useful if you are going to be doing other things with it.

``` shell
sudo lpadmin -p ZJ-58 -E -v serial:/dev/serial0?baud=19200 -m zjiang/ZJ-58.ppd
sudo lpoptions -d ZJ-58
```

Restart the system. Clone the Adafruit repository from this site and try to run *printertest.py*.

``` shell
git clone https://github.com/fourstix/Python-Thermal-Printer
cd Python-Thermal-Printer
python3 printertest.py
```

## Python RPI.GPIO error: 
If you get this error in rpi.gpio when running the code:
NotImplementedError: This module does not understand old-style revision codes

Upgrade the Python rpi-gpio library to the latest version with the following command

``` shell
sudo apt-get -y install python3-rpi.gpio
```

# treepi
treepi

initially tried using Genuino and https://github.com/FastLED/FastLED

ran into the following :

https://forum.arduino.cc/index.php?topic=391402.0

reverted back to rasperry pi 2B

----------

installed raspian lite on 30 March 2018

sudo apt-get update
sudo apt-get upgrade

sudo apt-get install gcc
sudo apt-get install make
sudo apt-get install build-essential
sudo apt-get install python-dev
sudo apt-get install git
sudo apt-get install scons
sudo apt-get install swig

https://tutorials-raspberrypi.com/connect-control-raspberry-pi-ws2812-rgb-led-strips/

worked like a dream

then installed node js

https://www.w3schools.com/nodejs/nodejs_raspberrypi.asp

installed following

https://github.com/beyondscreen/node-rpi-ws281x-native.git

worked like a dream too

now going back to see if I can get arduino to work again using

https://github.com/adafruit/Adafruit_NeoPixel.git

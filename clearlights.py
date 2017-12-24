import time
import random

from neopixel import *

import argparse
import signal
import sys

from flask import Flask, redirect, url_for, request
app = Flask(__name__)



def signal_handler(signal, frame):
    colorWipe(strip, Color(0,0,0))
    sys.exit(0)

def opt_parse():
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', action='store_true', help='clear the display on exit')
    args = parser.parse_args()
    if args.c:
        signal.signal(signal.SIGINT, signal_handler)

# LED strip configuration:
LED_COUNT      = 50      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
#LED_PIN        = 10      # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 5       # DMA channel to use for generating signal (try 5)
LED_BRIGHTNESS = 55     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53
LED_STRIP      = ws.WS2811_STRIP_GRB   # Strip type and colour ordering


# Define functions which animate LEDs in various ways.
def colorWipe(strip, color, wait_ms=50):
	"""Wipe color across display a pixel at a time."""
	for i in range(strip.numPixels()):
		strip.setPixelColor(i, color)
		strip.show()


def TwinkleTwinkle(strip):
    for i in range(strip.numPixels()):
        color = (random(0,255),random(0,255),random(0,255))
        strip.setPixelColor(random(NUM_LEDS),color)
        strip.show()
        time.sleep(wait_ms/1000.0)
		
def clearStrip():
	# Process arguments
	opt_parse()
	# Create NeoPixel object with appropriate configuration.
	strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL, LED_STRIP)
	# Intialize the library (must be called once before other functions).
	strip.begin()
	colorWipe(strip, Color(0, 0, 0)) # clear wipe
	return 1

def redStrip():
	# Process arguments
	opt_parse()
	# Create NeoPixel object with appropriate configuration.
	strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL, LED_STRIP)
	# Intialize the library (must be called once before other functions).
	strip.begin()
	colorWipe(strip, Color(0, 255, 0)) # clear wipe
	return 1

def greenStrip():
	# Process arguments
	opt_parse()
	# Create NeoPixel object with appropriate configuration.
	strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL, LED_STRIP)
	# Intialize the library (must be called once before other functions).
	strip.begin()
	colorWipe(strip, Color(255, 0, 0)) # clear wipe
	return 1

def blueStrip():
	# Process arguments
	opt_parse()
	# Create NeoPixel object with appropriate configuration.
	strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL, LED_STRIP)
	# Intialize the library (must be called once before other functions).
	strip.begin()
	colorWipe(strip, Color(0, 0, 255)) # clear wipe
	return 1

def twinkleStrip():
	# Process arguments
	opt_parse()
	# Create NeoPixel object with appropriate configuration.
	strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL, LED_STRIP)
	# Intialize the library (must be called once before other functions).
	strip.begin()
	TwinkleTwinkle(strip) # twinkle
	return 1

@app.route('/pattern/<name>')
def success(name):
    if name == 'red':
	r = redStrip()
    elif name == 'green':
	r = greenStrip()
    elif name == 'blue':
	r = blueStrip()
    elif name == 'twinkle':
	r = twinkleStrip()
    else :
	r = clearStrip()
    return 'display %s' % name

@app.route('/clear')
def clear():
   r = clearStrip()
   r = 0
   return 'Strip Cleared'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)

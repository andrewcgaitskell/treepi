import RPi.GPIO as GPIO ## Import GPIO Library
import time ## Import 'time' library.  Allows us to use 'sleep'

ndots = 50
clock = 7
signal = 11
forsleep = 1000

##Define a function named Blink()
def Blink(numTimes,speed):

    GPIO.setmode(GPIO.BOARD) ## Use BOARD pin numbering
    GPIO.setup(clock, GPIO.OUT) ## Setup GPIO pin clock to OUT
    GPIO.setup(signal, GPIO.OUT) ## Setup GPIO pin signal to OUT

    GPIO.output(signal, False)
    for i in range (0,32):
        GPIO.output(clock, True)
        for j in range(0,forsleep):
            j = j
        GPIO.output(clock, False)
        for j in range(0,forsleep):
            j = j
    for k in range(0,ndots):
        GPIO.output(signal, True)
        for i in range (0,1):
            GPIO.output(clock, True)
            for j in range(0,forsleep):
                j = j
            GPIO.output(clock, False)
            for j in range(0,forsleep):
                j = j
#5 bits of green
        GPIO.output(signal, True)
        for i in range (0,5):
            GPIO.output(clock, True)
            for j in range(0,forsleep):
                j = j
            GPIO.output(clock, False)
            for j in range(0,forsleep):
                j = j
#5 bits of red  
        GPIO.output(signal, False)
        for i in range (0,5):
            GPIO.output(clock, True)
            for j in range(0,forsleep):
                j = j
            GPIO.output(clock, False)
            for j in range(0,forsleep):
                j = j
#5 bits of blue  
        GPIO.output(signal, False)
        for i in range (0,5):
            GPIO.output(clock, True)
            for j in range(0,forsleep):
                j = j
            GPIO.output(clock, False)
            for j in range(0,forsleep):
                j = j

    GPIO.output(signal, False)
    for i in range (0,ndots):
        GPIO.output(clock, True)
        for j in range(0,forsleep):
            j = j
        GPIO.output(clock, False)
        for j in range(0,forsleep):
            j = j
               
    print ("Done") ## When loop is complete, print "Done"
    GPIO.cleanup()

## Prompt user for input
#iterations = input("Enter the total number of times to blink: ")
#speed = input("Enter the length of each blink in seconds: ")
iterations = 32
speed = 6

## Start Blink() function. Convert user input from strings to numeric data types and pass to Blink() as parameters
Blink(int(iterations),float(speed))


#!/usr/bin/python3
"""

Names: Charity Rodolo
Student Number: MDBTHE002
Prac: Prac 1
Date: 07/08/2019
"""

# import Relevant Libraries
from time import sleep
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)

# initialise GPIO pins
button1=16
button2=32
LED2=22
LED1=18 
LED0=36
GPIO.setup(button1,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(button2,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(LED2,GPIO.OUT)
GPIO.setup(LED1,GPIO.OUT)
GPIO.setup(LED0,GPIO.OUT)

GPIO.output(LED2,GPIO.LOW)
GPIO.output(LED1,GPIO.LOW)
GPIO.output(LED0,GPIO.LOW)

global counter
counter = 0

#callback function for incrementing
def counterIncrmnt(channel):
        global counter   
        if (GPIO.input(channel) == 1 and counter != 7):
            counter += 1
            print (bin(counter)[2:].zfill(3))
        else:
            counter = 0
            print (bin(counter)[2:].zfill(3))     

        return

# rising edge interrupt for button1
GPIO.add_event_detect(button1, GPIO.RISING, callback=counterIncrmnt, bouncetime=200)  

#callback function for decrementing
def counterDcrmnt(channel):
        global counter    
        if (GPIO.input(channel) == 1 and counter > 0):
            counter -= 1
            print (bin(counter)[2:].zfill(3))
        else:
            counter = 7
            print (bin(counter)[2:].zfill(3))


        return
    
# rising edge interrupt for button2
GPIO.add_event_detect(button2, GPIO.RISING, callback=counterDcrmnt, bouncetime=200) 
		
# function that converts a string to binary to allow dsiplay on LEDs	
def ledLogic(c):
	binaryString = bin(c)[2:].zfill(3)
	for index, value in enumerate(binaryString):
		if (value == '1'):
			ledOn(index)
		else:
			ledOff(index)
	return


def ledOn(pin):
	if (pin == 0):
		GPIO.output(LED2,GPIO.HIGH)
	if (pin == 1):
		GPIO.output(LED1,GPIO.HIGH)
	if (pin == 2):
		GPIO.output(LED0,GPIO.HIGH)

	return
	
def ledOff(pin):
	if (pin == 0):
		GPIO.output(LED2,GPIO.LOW)
	if (pin == 1):
		GPIO.output(LED1,GPIO.LOW)
	if (pin == 2):
		GPIO.output(LED0,GPIO.LOW)
	
	return
	
try: 
	while True:
		ledLogic(counter)
except KeyboardInterrupt:
	GPIO.cleanup()
		

# Author: Junior Tada
import time
import threading 
import ctypes
from gpiozero import LED, Button, OutputDevice

class Loop(object):

    def get_id():
        pass

class Led(object):
    """docstring for Led"""
    def __init__(self, pin):
        self.pin = pin
        self.led = LED(pin)

    def set_status(self, status):
        if status == 'ON':
            self.led.on()
        else:
            self.led.off()

    def blink(self):
        self.led.blink()  

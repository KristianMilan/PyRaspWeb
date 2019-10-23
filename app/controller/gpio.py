# Author: Junior Tada
import time
import threading 
import ctypes
from gpiozero import LED, Button, OutputDevice

class Base(object):

	def get_id()
		pass

class Led(Base):
	"""docstring for Led"""
	def __init__(self, pin:int):
		self.pin = pin
		self.led = LED(pin)



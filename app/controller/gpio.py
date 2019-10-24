# Author: Junior Tada
import time
import threading 
import ctypes
# from gpiozero import LED, Button, OutputDevice

class Loop(threading.Thread):
    """docstring for Loop"""
    def __init__(self, name):
        threading.Thread.__init__(self) 
        self.name = name

    def run(self):
        try:
            while True:
                print(f'running {self.name}')
        finally:
            print('force end')

    def _get_id(self):
        if hasattr(self, '_thread_id'):
            return self._thread_id
        for id, thread in threading._active.items():
            if thread is self:
                return id

    def kill(self):
        thread_id = self._get_id()
        res = ctypes.pythonapi.PyThreadState_SetAsyncExc(thread_id, 
              ctypes.py_object(SystemExit)) 
        if res > 1: 
            ctypes.pythonapi.PyThreadState_SetAsyncExc(thread_id, 0) 
            print('kill by Exception')


# class Led(object):
#     """docstring for Led"""
#     def __init__(self, pin):
#         self.pin = pin
#         self.led = LED(pin)

#     def set_status(self, status):
#         if status == 'ON':
#             self.led.on()
#         else:
#             self.led.off()

#     def blink(self):
#         self.led.blink()  

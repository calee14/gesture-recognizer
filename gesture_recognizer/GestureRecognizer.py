# importing requried modules
import cv2
import numpy
import os
import threading
import time
import importlib.util

class GestureRecognizer(object):
	def __init__(self, interval=1.0/30.0, print_pos=True):
		self.interval = interval
		self.print_pos = print_pos
	def start_recognizing(self):

		# import the class
		dir_path = os.path.dirname(os.path.realpath(__file__))
		filename_fist_rec = 'FistRecognizer.py'
		full_path = "%s/%s" % (dir_path, filename_fist_rec)
		spec = importlib.util.spec_from_file_location("FistRecognizer", full_path)
		gesture_recognition = importlib.util.module_from_spec(spec)
		spec.loader.exec_module(gesture_recognition)
		self.gesture = gesture_recognition.FistRecognizer(self.interval, self.print_pos)

		# threading code
		thread = threading.Thread(target=self.gesture.recognize_fist, args=())
		thread.daemon = True # Daemonize thread
		thread.start() # Start the execution

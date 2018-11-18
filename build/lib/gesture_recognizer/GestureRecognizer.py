# importing requried modules
import cv2
import numpy
import os
import threading
import time
import importlib.util

class GestureRecognizer(object):
	def __init__(self):
		pass

	def start_recognizing(self, interval=1):
		'''
		Threading
		The recognize_fist method will be started and it will run in the background
		until the application exits.
		:type interval: int
		:param interval: Check interval, in seconds
		'''
		self.interval = interval

		# import the class
		dir_path = os.path.dirname(os.path.realpath(__file__))
		filename_fist_rec = 'FistRecognizer.py'
		full_path = "%s/%s" % (dir_path, filename_fist_rec)
		spec = importlib.util.spec_from_file_location("FistRecognizer", full_path)
		foo = importlib.util.module_from_spec(spec)
		spec.loader.exec_module(foo)
		rec = foo.FistRecognizer()

		thread = threading.Thread(target=rec.recognize_fist, args=())
		thread.daemon = True # Daemonize thread
		thread.start() # Start the execution

	
	


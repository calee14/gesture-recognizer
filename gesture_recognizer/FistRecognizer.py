import cv2
import os
import time

class FistRecognizer(object):
	def __init__(self, interval=1.0/30.0):
		'''
		Threading
		The recognize_fist method will be started and it will run in the background
		until the application exits.
		:type interval: int
		:param interval: Check interval, in seconds
		'''
		self.interval = interval
		# retrieve the cascades
		# directory path
		dir_path = os.getcwd()
		print(dir_path)
		print(os.path.basename(dir_path))
		# make the path for the fist dataset
		filename_fist = 'haarcascades/haarcascade_fist.xml'
		full_path_fist = "%s/%s" % (dir_path, filename_fist)
		self.fist_cascade = cv2.CascadeClassifier(full_path_fist)
		# make the path for the palm dataset
		filename_palm = 'haarcascades/haarcascade_palm.xml'
		full_path_palm = "%s/%s" % (dir_path, filename_palm)
		self.palm_cascade = cv2.CascadeClassifier(full_path_palm)
		# previous hand position so we can analyze the change
		self.prev_pos = None
		# x_dir: 1 - right, -1 - left
		self.x_dir = 0
		# y_dir: 1 - up, -1 - down
		self.y_dir = 0
	def recognize_gesture(self, hand_pos=None):
		# if there is no previous position set the current one to it
		if self.prev_pos is None:
			self.prev_pos = hand_pos
		# the hands position relative to the previous position
		prev_pos = self.prev_pos
		x_dif = prev_pos[0] - hand_pos[0]
		y_dif = prev_pos[1] - hand_pos[1]
		# if the hand is still then don't set direction
		if abs(x_dif) < 30 and abs(y_dif) < 30:
			self.prev_pos = hand_pos
			return
		# scale it below 1
		while abs(x_dif) > 1.0 or abs(y_dif) > 1.0:
			x_dif /= 2.0
			y_dif /= 2.0
		# save these values to the class
		self.x_dir = x_dif
		self.y_dir = y_dif
		# print("x:", x_dif)
		# print("y:", y_dif)
		# update the previous position
		self.prev_pos = hand_pos
	def recognize_fist(self):
		'''
		Method that runs forever
		'''
		# start video capturing
		cap = cv2.VideoCapture(0)

		# code snippet to recognize 
		while True:
			if self.x_dir > 0:
				print("moving right")
			else:
				print("moving left")
			if self.y_dir > 0:
				print("moving up")
			else:
				print("moving down")
			print("x:", self.x_dir)
			print("y:", self.y_dir)
			ret, img = cap.read()
			gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
			hands = self.fist_cascade.detectMultiScale(gray)
			biggest_fist = [(0,0,0,0)]
			for (x,y,w,h) in hands:
				if w > biggest_fist[0][3]:
					biggest_fist[0] = (x,y,w,h)
			self.recognize_gesture(biggest_fist[0])
			for (x,y,w,h) in biggest_fist:
				cv2.rectangle(img, (x,y), (x+w,y+h), (255,255,0), 2)
			# cv2.imshow('img', img)
			k = cv2.waitKey(30) & 0xff
			if k == 27:
				break

			time.sleep(self.interval)

		# stop video and close windows
		cap.release()
		cv2.destroyAllWindows()
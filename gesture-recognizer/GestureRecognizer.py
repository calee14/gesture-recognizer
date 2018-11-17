# importing requied modules
import cv2
import numpy

class GestureRecognizer():
	def __init__(self):
		# retrieve the cascades
		self.fist_cascade = cv2.CascadeClassifier('haarcascades/haarcascade_fist.xml')
		self.palm_cascade = cv2.CascadeClassifier('haarcascades/haarcascade_palm.xml')
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
		if abs(x_dif) < 20 and abs(y_dif) < 20:
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
			cv2.imshow('img', img)
			k = cv2.waitKey(30) & 0xff
			if k == 27:
				break

		# stop video and close windows
		cap.release()
		cv2.destroyAllWindows()


# importing requied modules
import cv2
import numpy

class GestureRecognizer():
	def __init__(self):
		# retrieve the cascades
		self.fist_cascade = cv2.CascadeClassifier('haarcascades/haarcascade_fist.xml')
		self.palm_cascade = cv2.CascadeClassifier('haarcascades/haarcascade_palm.xml')
	def recognize_gesture(self, hand_pos=None):
		# check if there is a new hand
		pass
	def recognize_fist(self):
		# start video capturing
		cap = cv2.VideoCapture(0)

		# code snippet to recognize 
		while True:
			ret, img = cap.read()
			gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
			hands = self.fist_cascade.detectMultiScale(gray)
			biggest_fist = [(0,0,0,0)]
			for (x,y,w,h) in hands:
				if w > biggest_fist[0][3]:
					biggest_fist[0] = (x,y,w,h)
			for (x,y,w,h) in biggest_fist:
				cv2.rectangle(img, (x,y), (x+w,y+h), (255,255,0), 2)
			cv2.imshow('img', img)
			k = cv2.waitKey(30) & 0xff
			if k == 27:
				break

		# stop video and close windows
		cap.release()
		cv2.destroyAllWindows()


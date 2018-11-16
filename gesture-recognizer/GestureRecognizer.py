# importing requied modules
import cv2
import numpy

class GestureRecognizer():
	def __init__(self):
		# retrieve the cascades
		self.fist_cascade = cv2.CascadeClassifier('haarcascades/aGest.xml')
		self.palm_cascade = cv2.CascadeClassifier('haarcascades/haarcascade_palm.xml')
	def recognize_fist(self):
		# start video capturing
		cap = cv2.VideoCapture(0)

		# code snippet to recognize 
		while True:
			ret, img = cap.read()
			gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
			hands = self.fist_cascade.detectMultiScale(gray)
			for (x,y,w,h) in hands:
				cv2.rectangle(img, (x,y), (x+w,y+h), (255,255,0), 2)
			cv2.imshow('img', img)
			k = cv2.waitKey(30) & 0xff
			if k == 27:
				break

		# stop video and cose windows
		cap.release()
		cv2.destroyAllWindows()

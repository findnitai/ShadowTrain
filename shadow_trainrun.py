import cv2
import numpy as numpy
import os

shadow_cascade = cv2.CascadeClassifier('data/cascade.xml')

for filename in os.listdir('left_samples'):

	image = cv2.imread(os.path.join('left_samples',filename))
	image = cv2.resize(image, (0,0), fx = 0.5, fy=0.5)
	image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	shadows = shadow_cascade.detectMultiScale(image, 20,20)

	for (x,y,w,h) in shadows:
		cv2.rectangle(image, (x,y), (x+w, y+h), (255,255,0) , 2)
		cv2.imshow('image', image)
	k = cv2.waitKey(0) 

for filename in os.listdir('right_samples'):

	image = cv2.imread(os.path.join('right_samples',filename))
	image = cv2.resize(image, (0,0), fx = 0.5, fy=0.5)
	image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	shadows = shadow_cascade.detectMultiScale(image, 20,20)

	for (x,y,w,h) in shadows:
		cv2.rectangle(image, (x,y), (x+w, y+h), (255,255,0) , 2)
		cv2.imshow('image', image)
	k = cv2.waitKey(0) 


for filename in os.listdir('front_samples'):

	image = cv2.imread(os.path.join('front_samples',filename))
	image = cv2.resize(image, (0,0), fx = 0.5, fy=0.5)
	image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	shadows = shadow_cascade.detectMultiScale(image, 20,20)

	for (x,y,w,h) in shadows:
		cv2.rectangle(image, (x,y), (x+w, y+h), (255,255,0) , 2)
		cv2.imshow('image', image)
	k = cv2.waitKey(0) 

cv2.destroyAllWindows()
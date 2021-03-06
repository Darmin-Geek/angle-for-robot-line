
# import the necessary packages
from imutils import paths
import numpy as np
import imutils
import cv2
 
imagine = cv2.imread("unity?.png")
def find_marker(image):
	# convert the image to grayscale, blur it, and detect edges
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	gray = cv2.GaussianBlur(gray, (5, 5), 0)
	edged = cv2.Canny(gray, 35, 125)
 
	# find the contours in the edged image and keep the largest one;
	# we'll assume that this is our piece of paper in the image
	cnts = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
	cnts = imutils.grab_contours(cnts)
	c = max(cnts, key = cv2.contourArea)
 
	# compute the bounding box of the of the paper region and return it
	return cv2.minAreaRect(c)
KNOWN_DISTANCE = 24
 
# initialize the known object width, which in this case, the piece of
# paper is 12 inches wide
KNOWN_WIDTH = 8.5


def distance_to_camera(knownWidth, focalLength, perWidth):
	# compute and return the distance from the maker to the camera
	return (knownWidth * focalLength) / perWidth

marker = find_marker(imagine)
focalLength = (marker[1][0] * KNOWN_DISTANCE) / KNOWN_WIDTH
print(focalLength)
marker = find_marker(imagine)
inches = distance_to_camera(KNOWN_WIDTH, focalLength, marker[1][0])
print(inches)
	# draw a bounding box around the image and display it
box = cv2.cv.BoxPoints(marker) if imutils.is_cv2() else cv2.boxPoints(marker)
box = np.int0(box)
cv2.drawContours(imagine, [box], -1, (0, 255, 0), 2)
cv2.imshow("image", imagine)
cv2.waitKey(0)
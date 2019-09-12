import cv2
import numpy as np 
import argparse

parser = argparse.ArgumentParser(description='Process some image.')
parser.add_argument('--gamma',required=True,type=float)
parser.add_argument('--file',required=True,type=str)
parser.add_argument('--compress',required=False,type=int,default=0)



args = parser.parse_args()

def adjust_gamma(image, gamma=1.0):
	# build a lookup table mapping the pixel values [0, 255] to
	# their adjusted gamma values
	invGamma = 1.0 / gamma
	table = np.array([((i / 255.0) ** invGamma) * 255
		for i in np.arange(0, 256)]).astype("uint8")
 
	# apply gamma correction using the lookup table
	return cv2.LUT(image, table)


#img1 and img2 must be in same size
img1 = cv2.imread(args.file, 1)
if args.compress==True:
	img1=cv2.resize(img1,(600,400))
img2 = adjust_gamma(img1,float(args.gamma))

cv2.imshow('img1',img1)
cv2.imshow('img2',img2)

cv2.waitKey(0)
cv2.destroyAllWindow()
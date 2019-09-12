import cv2
import argparse
import numpy as np 

def negativee(img):
    return 255 - np.array(img)
    
parser = argparse.ArgumentParser(description='Process some image.')
parser.add_argument('--file',required=True,type=str)
parser.add_argument('--compress',required=True,type=int)
args = parser.parse_args()
#img1 and img2 must be in same size
img1 = cv2.imread(args.file, 1)
if args.compress==True:
    img1 = cv2.resize(img1, (600,400))

#img1 = cv2.cvtColor(img1,cv2.COLOR_BGR2RGB)

img2 = negativee(img1)

cv2.imshow('img1',img1)
cv2.imshow('img2',img2)

cv2.waitKey(0)
cv2.destroyAllWindow()


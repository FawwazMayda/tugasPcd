import cv2
import numpy as np 
import argparse

parser = argparse.ArgumentParser(description='Process some image.')
parser.add_argument('--gamma',required=True,type=float)
parser.add_argument('--file',required=True,type=str)



args = parser.parse_args()
def scaled(img,gamma=0.2):
    img = np.array(img)
    invGamma  = 1 / gamma
    img_scaled = img/255
    img_gamma = img_scaled ** invGamma
    img_res = img_gamma * 255
    return img_res


#img1 and img2 must be in same size
img1 = cv2.imread(args.file, 1)
img2 = scaled(img1,float(args.gamma))

cv2.imshow('img1',img1)
cv2.imshow('img2',img2)

cv2.waitKey(0)
cv2.destroyAllWindow()
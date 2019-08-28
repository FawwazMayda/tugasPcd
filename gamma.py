import cv2
import numpy as np 


def scaled(img,gamma=1.0):
    img = np.array(img)
    invGamma  = 1 / gamma
    img_scaled = img/255
    img_gamma = img_scaled ** invGamma
    img_res = img_gamma * 255
    return img_res


#img1 and img2 must be in same size
img1 = cv2.imread('download.jpg', 1)
img2 = scaled(img1)

cv2.imshow('img1',img1)
cv2.imshow('img2',img2)
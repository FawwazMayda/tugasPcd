import cv2
import argparse
import numpy as np 


parser = argparse.ArgumentParser(description='Process some image.')
parser.add_argument('--file',required=True,type=str)
#img1 and img2 must be in same size
img1 = cv2.imread(args.file, 1)
img1 = cv2.cvtColor(img1,cv2.COLOR_BGR2RGB)
img2 = (255 -  np.array(img1))

cv2.imshow('img1',img1)
cv2.imshow('img2',img2)

cv2.waitKey(0)
cv2.destroyAllWindow()


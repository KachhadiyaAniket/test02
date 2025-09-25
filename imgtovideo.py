a=input("Enter the path of the image file:")


b=input("Enter the path of the output video file:")

import cv2
import numpy as np
from PIL import Image
import os

img = cv2.imread(a)

height, width, layers = img.shape

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter(b, fourcc, 20.0, (width, height))

for i in range(0, height):
    for j in range(0, width):
        out.write(img[i][j])
        
out.release()

print("Done")

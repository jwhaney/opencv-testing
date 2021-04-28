# testing out opencv-python to manipulate images

import numpy as np
import cv2


def findthedark(choice):
    if choice == 'black':
        lower_hue = np.array([0,0,0])
        upper_hue = np.array([50,50,100])
    elif choice == 'white':
        lower_hue = np.array([0,0,0])
        upper_hue = np.array([0,0,255])
    return lower_hue, upper_hue

img = cv2.imread('images/sniper.jpg')

px = img[100, 100]
print(px)

dark = img[]

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('media/einstein.jpg',0)
img1=cv2.GaussianBlur(img,(5,5),0)
img2=cv2.GaussianBlur(img,(9,9),0)
img3=img2-img1
plt.figure(),plt.axis("off"),plt.title("Ëdge"),plt.imshow(img3)
plt.show()

import cv2
from google.colab.patches import cv2_imshow

img = cv2.imread('media/einstein.jpg',0)
cv2_imshow(img)

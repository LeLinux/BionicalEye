import cv2
import matplotlib.pyplot as plt
import numpy as np

im = cv2.imread('egorov.jpg')
im = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)

gray = cv2.cvtColor(im, cv2.COLOR_RGB2GRAY)
img = cv2.medianBlur(gray, 5)

th = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 11)
contours, _ = cv2.findContours(th, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

img_contours = cv2.drawContours(np.uint8(np.zeros((im.shape[0], im.shape[1]))), contours, -1, (255, 255, 255), 1)

resized_img = cv2.resize(img_contours, (8,8), interpolation=cv2.INTER_AREA)
ret,thresh1 = cv2.threshold(resized_img,0,255,cv2.THRESH_BINARY)

plt.imshow(thresh1, cmap='gray')
plt.show()
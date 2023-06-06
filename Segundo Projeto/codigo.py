import cv2
import matplotlib.pyplot as plt

img = cv2.imread('ruido2.jpeg')
median = cv2.medianBlur(img,5)
 
plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(median),plt.title('Mediana')
plt.xticks([]), plt.yticks([])
plt.show()

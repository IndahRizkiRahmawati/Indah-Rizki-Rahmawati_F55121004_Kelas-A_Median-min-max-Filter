import cv2
import numpy as np

# Masukkan gambar
img = cv2.imread('bunga.jpeg')

# Convert ke grayscale
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# gunakan min filter dengan kernel 2x2
kernel = np.ones((2,2), np.uint8)
min_img = cv2.erode(gray_img, kernel, iterations=1)

# Menampilkan gambar ori dan min filter
cv2.imshow('Original Image', img)
cv2.imshow('Min Filtered Image', min_img)
cv2.waitKey(0)
cv2.destroyAllWindows()








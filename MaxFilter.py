import cv2
import numpy as np

# Masukkan gambar
img = cv2.imread('bunga.jpeg')

# Convert ke grayscale
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# gunakan max filer dengan kernel 3x3
kernel = np.ones((3,3), np.uint8)
max_img = cv2.dilate(gray_img, kernel, iterations=1)

# Menampilkan gambar ori dan max filter
cv2.imshow('Original Image', img)
cv2.imshow('Max Filtered Image', max_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
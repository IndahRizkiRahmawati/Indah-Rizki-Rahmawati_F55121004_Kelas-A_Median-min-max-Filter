import cv2
import numpy as np
from matplotlib import pyplot as plt

# Load image
img = cv2.imread('patrick.jpeg', 0)

# Compute FFT
f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)

# Ideal Lowpass Filter
rows, cols = img.shape
crow, ccol = rows // 2, cols // 2
mask = np.zeros((rows, cols), np.uint8)
r = 30 # radius
cv2.circle(mask, (ccol, crow), r, 255, -1)
fshift_filtered = fshift * mask
f_filtered = np.fft.ifftshift(fshift_filtered)
img_filtered = np.fft.ifft2(f_filtered)
img_filtered = np.abs(img_filtered)

# Plot results
plt.subplot(131), plt.imshow(img, cmap='gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(133), plt.imshow(img_filtered, cmap='gray')
plt.title('Ideal Lowpass Filter'), plt.xticks([]), plt.yticks([])
plt.show()

import cv2
import numpy as np
from matplotlib import pyplot as plt

# Load image
img = cv2.imread('patrick.jpeg', 0)

# Compute FFT
f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)

# Butterworth Lowpass Filter
rows, cols = img.shape
crow, ccol = rows // 2, cols // 2
D0 = 30  # cutoff frequency
n = 2  # order
H = 1 / (1 + (np.sqrt((np.arange(cols) - ccol)**2 + (np.arange(rows) - crow)**2) / D0) ** (2 * n))
fshift_filtered = fshift * H

# Inverse FFT to get the filtered image
img_filtered = np.abs(np.fft.ifft2(np.fft.ifftshift(fshift_filtered)))

# Plot results
plt.subplot(131), plt.imshow(img, cmap='gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(133), plt.imshow(img_filtered, cmap='gray')
plt.title('Butterworth Lowpass Filter'), plt.xticks([]), plt.yticks([])
plt.show()

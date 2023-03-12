import numpy as np
import cv2
import matplotlib.pyplot as plt

# Load image
img = cv2.imread('patrick.jpeg', 0)

# Define Gaussian filter kernel size and sigma
kernel_size = (5, 5)
sigma = 1.5

# Create Gaussian filter kernel
kernel = np.zeros(kernel_size)
center = tuple(map(lambda x: (x - 1) / 2, kernel_size))
for i in range(kernel_size[0]):
    for j in range(kernel_size[1]):
        dis = (i - center[0]) ** 2 + (j - center[1]) ** 2
        kernel[i, j] = np.exp(-dis / (2 * sigma ** 2))
kernel = kernel / np.sum(kernel)

# Apply filter to image
filtered_image = cv2.filter2D(img, -1, kernel)

# Display images
fig, ax = plt.subplots(1, 2)
ax[0].imshow(img, cmap='gray')
ax[0].set_title('Original Image')
ax[1].imshow(filtered_image, cmap='gray')
ax[1].set_title('Gaussian Lowpass Filter')
plt.show()





import numpy as np
import cv2

def median_filter(image, kernel_size):
    padded_image = cv2.copyMakeBorder(image, kernel_size, kernel_size, kernel_size, kernel_size, cv2.BORDER_REFLECT)
    output_image = np.zeros_like(image)

    for i in range(kernel_size, padded_image.shape[0] - kernel_size):
        for j in range(kernel_size, padded_image.shape[1] - kernel_size):
            window = padded_image[i - kernel_size: i + kernel_size + 1, j - kernel_size: j + kernel_size + 1]
            output_image[i - kernel_size, j - kernel_size] = np.median(window)

    return output_image
#Input Gambar
image = cv2.imread('bunga.jpeg', 0)

# Gunakan median filter
filtered_image = median_filter(image, 3)

# Simpan
cv2.imwrite('OutputMedianFilter.jpeg', filtered_image)
import cv2
import numpy as np
from matplotlib import pyplot as plt

# Load gambar grayscale
img = cv2.imread('patrick.jpeg', cv2.IMREAD_GRAYSCALE)

# Hitung transformasi Fourier diskrit dari gambar
dft = cv2.dft(np.float32(img), flags=cv2.DFT_COMPLEX_OUTPUT)

# Geser frekuensi rendah ke pusat
dft_shift = np.fft.fftshift(dft)

# Hitung magnitudo spektrum frekuensi
magnitude_spectrum = 20 * np.log(cv2.magnitude(dft_shift[:, :, 0], dft_shift[:, :, 1]))

# Tampilkan gambar asli dan spektrum frekuensi
plt.subplot(121), plt.imshow(img, cmap='gray')
plt.title('Gambar Asli'), plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(magnitude_spectrum, cmap='gray')
plt.title('Magnitudo Spektrum Frekuensi'), plt.xticks([]), plt.yticks([])
plt.show()
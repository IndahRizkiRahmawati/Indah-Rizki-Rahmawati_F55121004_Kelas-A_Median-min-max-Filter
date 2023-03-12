import cv2
import numpy as np
import matplotlib.pyplot as plt

# Fungsi Gaussian Highpass Filter
def gaussian_highpass_filter(img, cutoff_freq):
    # Mengambil dimensi gambar
    rows, cols = img.shape[:2]

    # Menghitung nilai titik tengah gambar
    crow, ccol = rows//2, cols//2

    # Membuat filter mask
    D = np.sqrt((np.arange(rows)[:,np.newaxis]-crow)**2 + (np.arange(cols)-ccol)**2)
    mask = 1 - np.exp(-(D**2)/(2*(cutoff_freq**2)))

    # Menerapkan filter pada gambar
    fshift = np.fft.fftshift(np.fft.fft2(img))
    fshift_filtered = fshift * mask
    img_back = np.fft.ifft2(np.fft.ifftshift(fshift_filtered))

    # Mengembalikan gambar hasil filter
    return np.abs(img_back)

# Membaca gambar
img = cv2.imread('patrick.jpeg')
# Mengkonversi gambar ke grayscale jika gambar berwarna
if img.ndim == 3:
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Mengaplikasikan filter Gaussian Highpass pada gambar
cutoff_freq = 50
img_filtered = gaussian_highpass_filter(img, cutoff_freq)

# Menampilkan gambar asli dan gambar hasil filter
plt.subplot(1, 2, 1)
plt.imshow(img, cmap='gray')
plt.title('Gambar Asli')
plt.xticks([])
plt.yticks([])

plt.subplot(1, 2, 2)
plt.imshow(img_filtered, cmap='gray')
plt.title('Gaussian Highpass Filter')
plt.xticks([])
plt.yticks([])
plt.show()


import numpy as np
import matplotlib.pyplot as plt

# Membuat fungsi Butterworth Highpass Filter
def butterworth_highpass_filter(img, cutoff_freq, order):
    # Mengambil dimensi gambar
    rows, cols = img.shape

    # Menghitung nilai titik tengah gambar
    crow, ccol = rows//2, cols//2

    # Membuat filter mask
    u, v = np.meshgrid(np.arange(cols), np.arange(rows))
    d = np.sqrt((u - crow)**2 + (v - ccol)**2)
    mask = 1 / (1 + (cutoff_freq/d)**(2*order))

    # Menerapkan filter pada gambar
    fshift = np.fft.fftshift(np.fft.fft2(img))
    fshift_filtered = fshift * mask
    img_back = np.fft.ifft2(np.fft.ifftshift(fshift_filtered))

    # Mengembalikan gambar hasil filter
    return np.abs(img_back)

# Membaca gambar
img = plt.imread('patrick.jpeg')

# Mengkonversi gambar ke grayscale jika gambar berwarna
if img.ndim == 3:
    img = np.dot(img[...,:3], [0.2989, 0.5870, 0.1140])

# Mengaplikasikan Butterworth Highpass Filter pada gambar
cutoff_freq = 50
order = 2
img_filtered = butterworth_highpass_filter(img, cutoff_freq, order)

# Menampilkan gambar asli dan gambar hasil filter
plt.subplot(1,2,1),plt.imshow(img, cmap = 'gray')
plt.title('Gambar Asli'), plt.xticks([]), plt.yticks([])
plt.subplot(1,2,2),plt.imshow(img_filtered, cmap = 'gray')
plt.title('Butterworth Highpass Filter'), plt.xticks([]), plt.yticks([])
plt.show()

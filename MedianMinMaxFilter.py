from scipy import ndimage
import matplotlib.pyplot as plt
import numpy as np

img = plt.imread('AllInOne.jpeg')

#Menggunakan Median, Min dan Max Filter
img_median = ndimage.median_filter(img, size = 2)
img_min = ndimage.minimum_filter(img, size = 2)
img_max = ndimage.maximum_filter(img, size = 2)

#Munculkan semua gambar hasil
fig, ax = plt.subplots(nrows=1, ncols=4, figsize= (10,5))

ax[0].imshow(img)
ax[0].set_title('Original Image')

ax[1].imshow(img_median)
ax[1].set_title('Median Filter')
ax[2].imshow(img_min)
ax[2].set_title('Min Filter')
ax[3].imshow(img_max)
ax[3].set_title('Max Filter')
plt.show()
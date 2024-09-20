from skimage import io,color

import matplotlib.pyplot as plt

im = io.imread("image2.jpg")

grayim= color.rgb2gray(im)

orimg= color.gray2rgb(grayim)

plt.subplot(1,3,1)

io.imshow(grayim)

plt.subplot(1,3,2)

io.imshow(im)

plt.subplot(1,3,3)

io.imshow(orimg)

plt.show()


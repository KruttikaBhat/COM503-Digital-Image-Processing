
import matplotlib.image as img
from matplotlib import pyplot as plt
import cv2
import numpy as np
import cmath

def get_image(m,p) :
	img = [[0 for i in range(len(m[j]))]for j in range(len(m))]
	for i in range(len(m)) :
		for j in range(len(m[i])) :
			img[i][j] = complex(m[i][j]*np.cos(p[i][j]),m[i][j]*np.sin(p[i][j]))
	return img


def main() :
	im1 = img.imread('lena.jpg')
	img2 = img.imread('dog.jpg')
	im2 = cv2.resize(img2, (512,512), interpolation = cv2.INTER_AREA)
	dft1 = cv2.dft(np.float32(im1),flags = cv2.DFT_COMPLEX_OUTPUT)
	m1,p1 = cv2.cartToPolar(dft1[:,:,0],dft1[:,:,1])
	dft2 = cv2.dft(np.float32(im2),flags = cv2.DFT_COMPLEX_OUTPUT)
	m2,p2 = cv2.cartToPolar(dft2[:,:,0],dft2[:,:,1])
	img1 = get_image(m1,p2)
	img2 = get_image(m2,p1)
	image1 = np.fft.ifft2(img1)
	image2 = np.fft.ifft2(img2)
	i1 = [[0 for i in range(len(image1[j]))] for j in range(len(image1))]
	i2 = [[0 for i in range(len(image2[j]))] for j in range(len(image2))]

	for i in range(len(image1)) :
		for j in range(len(image1[i])) :
			i1[i][j] = int(image1[i][j].real)
			i2[i][j] = int(image2[i][j].real)
	plt.subplot(1,2,1)
	plt.imshow(i1,cmap= "gray")
	plt.title('phase from dog image')
	plt.subplot(1,2,2)
	plt.imshow(i2,cmap= "gray")
	plt.title('phase from lena image')
	#plt.show()
	plt.savefig("q2.png")

if __name__ == '__main__':
	main()

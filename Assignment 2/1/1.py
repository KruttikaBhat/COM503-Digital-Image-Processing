import matplotlib.image as img
from matplotlib import pyplot as plt
import numpy as np
import cmath

def twod_dft(img) :

	f1 = np.fft.fft2(img)
	im1 = np.fft.ifft2(f1)
	im = [[0 for i in range(len(im1[j]))]for j in range(len(im1))]
	for i in range(len(im1)) :
		for j in range(len(im1[i])) :
			im[i][j] = int(im1[i][j].real)
	return im

def oned_dft(img) :

	f2 = [[0 for i in range(len(img[j]))]for j in range(len(img))]
	for i in range(len(img)) :
		f2[i] = np.fft.fft(img[i])
	f = [[f2[j][i] for j in range(len(f2))] for i in range(len(f2[0]))]
	im1 = [[0 for i in range(len(f[j]))]for j in range(len(f))]
	for i in range(len(f)) :
		im1[i] = np.fft.fft(f[i])
	im = [[im1[j][i] for j in range(len(im1))] for i in range(len(im1[0]))]
	image1 = np.fft.ifft2(im)
	image = [[0 for i in range(len(im[j]))] for j in range(len(im))]
	for i in range(len(image1)) :
		for j in range(len(image1[i])) :
			image[i][j] = int(image1[i][j].real)
	return image

def main() :
	lena = img.imread('lena.jpg')
	im = twod_dft(lena)
	im1 = oned_dft(lena)

	plt.subplot(1,2,1)
	plt.imshow(im,cmap= "gray")
	plt.title('2d-DFT and IFT')
	plt.subplot(1,2,2)
	plt.imshow(im1,cmap= "gray")
	plt.title('1d-DFT(x2) and IFT')
	#plt.show()
	plt.savefig("q1.png")



if __name__ == '__main__':
	main()
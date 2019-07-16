import matplotlib.image as img
from matplotlib import pyplot as plt
import numpy as np
import cv2

def get_cf(img) :
	r,c,h = img.shape
	f = [0 for i in range (256)]
	cf = [0 for i in range (256)]
	for i in range (r) :
		for j in range (c) :
			f[img[i][j][0]] += 1
	cf[0] = f[0]
	for i in range(1,256) :
		cf[i] = cf[i-1] + f[i]
	for i in range (256) :
		cf[i] = round(cf[i]*255)

	return cf

def histogram_eq(img) :
	r,c,h = img.shape
	cf = get_cf(img)
	image = [[0 for i in range (c)]for j in range (r)]
	for i in range (r) :
		for j in range (c) :
			image[i][j] = cf[img[i][j][0]]
	return image

def histogram_match(bright,dark) :
	r,c,h = dark.shape
	cf1 = get_cf(dark)
	cf2 = get_cf(bright)
	image = [[0 for i in range (c)]for j in range (r)]
	for i in range (r) :
		for j in range (c) :
			temp = [cf1[0]]+cf1[1:]
			x = cf2[dark[i][j][0]]
			temp[:] = [abs(k - x) for k in temp]
			t = min(temp)
			image[i][j] = temp.index(t)
	return image

def main() :
	plt.figure()

	pb = img.imread('pout-bright.jpg')
	pd = img.imread('pout-dark.jpg')

	#histogram equalization
	plt.subplot(2,1,1)
	plt.imshow(pd,cmap="gray")
	plt.title('original')

	image1 = histogram_eq(pd)
	plt.subplot(2,1,2)
	plt.imshow(image1,cmap="gray")
	plt.title('equalization')

	plt.savefig('histogram_equalization')

	#histogram matching
	plt.figure()
	plt.subplot(2,2,1)
	plt.imshow(pd,cmap="gray")
	plt.title("pout_dark")

	plt.subplot(2,2,2)
	plt.imshow(pb,cmap="gray")
	plt.title("pout_bright")

	image2 = histogram_match(pb,pd)
	plt.subplot(2,2,3)
	plt.imshow(image2, cmap= "gray")
	plt.title('matching')
	plt.savefig("histogram matching")

if __name__ == '__main__':
	main()
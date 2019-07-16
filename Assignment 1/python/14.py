import matplotlib.image as img
from matplotlib import pyplot as plt
import numpy as np
import cv2

def nearest_interpolation(img,s) :
	r,c = img.shape
	nr = int(r*s)
	nc = int(c*s)
	image = [[0 for i in range(nc)]for j in range(nr)]
	for i in range (nr) :
		for j in range (nc) :
			image[i][j] = img[int(round(i/s))][int(round(j/s))]
	return image

def bilinear_interpolation(img,s) :
	r,c = img.shape
	nr = int(r*s)
	nc = int(c*s)
	image = [[0 for i in range(nc)]for j in range(nr)]
	for i in range (nr) :
		for j in range (nc) :
			x = int(i/s)
			y = int(j/s)
			a = x - (i/float(s))
			b = (j/float(s)) - y
			if(x+1 == r and y+1 == c) :
				image[i][j] = (1-a)*(1-b)*(img[x][y])
			elif(x+1 == r) :
				image[i][j] = (1-a)*(1-b)*(img[x][y])+(1-a)*(b)*(img[x][y+1])
			elif(y+1 == c) :
				image[i][j] = (1-a)*(1-b)*(img[x][y])+(a)*(1-b)*(img[x+1][y])
			else :
				image[i][j] = (1-a)*(1-b)*(img[x][y])+(1-a)*(b)*(img[x][y+1])+(a)*(1-b)*(img[x+1][y])+(a)*(b)*(img[x+1][y+1])
	return image

def main() :
	
	camera_man = img.imread('cameraman.png')
	r,c = camera_man.shape

	plt.figure()
	plt.subplot(221)
	plt.imshow(camera_man,cmap="gray")
	plt.title('original')

	image = nearest_interpolation(camera_man,0.5)
	plt.subplot(222)
	plt.imshow(image,cmap="gray")
	plt.title('nearest_interpolation')

	image2 = bilinear_interpolation(camera_man,0.5)
	plt.subplot(223)
	plt.imshow(image,cmap="gray")
	plt.title('bilinear_interpolation')

	bilinear_img = cv2.resize(camera_man,None,fx=0.5,fy=0.5, interpolation = cv2.INTER_LINEAR)
	plt.subplot(224)
	plt.imshow(bilinear_img,cmap="gray")
	plt.title('bilinear_interpolation_inbuilt')

	plt.savefig("half_scaling")

	#scale by 2
	plt.figure()
	plt.subplot(221)
	plt.imshow(camera_man,cmap="gray")
	plt.title('original')

	image = nearest_interpolation(camera_man,2)
	plt.subplot(222)
	plt.imshow(image,cmap="gray")
	plt.title('nearest_interpolation')

	image2 = bilinear_interpolation(camera_man,2)
	plt.subplot(223)
	plt.imshow(image,cmap="gray")
	plt.title('bilinear_interpolation')

	bilinear_img = cv2.resize(camera_man,None,fx=2,fy=2, interpolation = cv2.INTER_LINEAR)
	plt.subplot(224)
	plt.imshow(bilinear_img,cmap="gray")
	plt.title('bilinear_interpolation_inbuilt')
	plt.savefig("2_scaling")

	#scale by 200/256
	n = 200/256.0
	plt.figure()
	plt.subplot(221)
	plt.imshow(camera_man,cmap="gray")
	plt.title('original')

	image = nearest_interpolation(camera_man,n)
	plt.subplot(222)
	plt.imshow(image,cmap="gray")
	plt.title('nearest_interpolation')

	image2 = bilinear_interpolation(camera_man,n)
	plt.subplot(223)
	plt.imshow(image,cmap="gray")
	plt.title('bilinear_interpolation')

	bilinear_img = cv2.resize(camera_man,None,fx=n,fy=n, interpolation = cv2.INTER_LINEAR)
	plt.subplot(224)
	plt.imshow(bilinear_img,cmap="gray")
	plt.title('bilinear_interpolation_inbuilt')

	plt.savefig("200X200_scaling")


if __name__ == '__main__':
	main()
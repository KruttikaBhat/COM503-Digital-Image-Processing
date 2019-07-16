import matplotlib.image as img
from matplotlib import pyplot as plt
import numpy as np
import random
import cv2

def gen_noise(img) :
	r,c = img.shape
	image = img
	for i in range(r) :
		for j in range(c) :
			t = random.randint(1,101)
			if(t < 6) :
				image[i][j] = 0
			elif(t > 5 and t < 11) :
				image[i][j] = 255
	return image

def get_median(n) :
	n = sorted(n)
	median = n[len(n)/2+1]
	return median

def median_image(img,n) :
	r,c = img.shape
	image = [[0 for i in range(c)] for j in range(r)]
	t = n/2
	for i in range (r) :
		for j in range (c) :
			temp = []
			for l in range (i-t,i+t+1) :
				for k in range (j-t,j+t+1) :
					if(l < 0 or l > r-1 or k < 0 or k > c-1) :
						temp.append(0)
					else :
						temp.append(img[l][k])
			image[i][j] = get_median(temp)

	return image

def main() :
	lena2 = img.imread('lena.jpg')
	lena = img.imread('lena.jpg')

	
	fig = plt.figure()
	plt.subplot(2,2,1)
	plt.imshow(lena2,cmap = "gray")
	plt.title('original')
	noisy = gen_noise(lena)
	plt.subplot(2,2,2)
	plt.imshow(noisy,cmap="gray")
	plt.title('noisy')
	med_image1 = median_image(noisy,3)
	plt.subplot(2,2,3)
	plt.imshow(med_image1,cmap="gray")
	plt.title('3-median_filter')
	median = cv2.medianBlur(noisy,3)
	plt.subplot(2,2,4)
	plt.imshow(median,cmap="gray")
	plt.title('3-inbuilt_median_filter')
	plt.savefig("3-median_filter.png")

	fig = plt.figure()
	plt.subplot(2,2,1)
	plt.imshow(lena2,cmap = "gray")
	plt.title('original')
	noisy = gen_noise(lena)
	plt.subplot(2,2,2)
	plt.imshow(noisy,cmap="gray")
	plt.title('noisy')
	med_image1 = median_image(noisy,5)
	plt.subplot(2,2,3)
	plt.imshow(med_image1,cmap="gray")
	plt.title('5-median_filter')
	median = cv2.medianBlur(noisy,5)
	plt.subplot(2,2,4)
	plt.imshow(median,cmap="gray")
	plt.title('5-inbuilt_median_filter')
	plt.savefig("5-median_filter.png")

	#med_image2 = median_image(noisy,5)

	fig = plt.figure()
	plt.subplot(2,2,1)
	plt.imshow(lena2,cmap = "gray")
	plt.title('original')
	noisy = gen_noise(lena)
	plt.subplot(2,2,2)
	plt.imshow(noisy,cmap="gray")
	plt.title('noisy')
	med_image1 = median_image(noisy,7)
	plt.subplot(2,2,3)
	plt.imshow(med_image1,cmap="gray")
	plt.title('7-median_filter')
	median = cv2.medianBlur(noisy,7)
	plt.subplot(2,2,4)
	plt.imshow(median,cmap="gray")
	plt.title('7-inbuilt_median_filter')
	plt.savefig("7-median_filter.png")
	#med_image3 = median_image(noisy,7)
	


if __name__ == '__main__':
	main()
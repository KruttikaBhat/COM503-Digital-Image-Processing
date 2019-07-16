import matplotlib.image as img
from matplotlib import pyplot as plt
import numpy as np

def gen_noise(img) :
	n = []
	r,c = img.shape
	mean = 0
	var = 200.0
	sigma = var**0.5
	for i in range(100) :
		temp = np.random.normal(mean,sigma,(r,c))
		temp = temp.reshape(r,c)
		temp = temp + img
		n.append(temp)
	return n

def mean_images(n) :
	r,c = n[0].shape
	image = [[0 for i in range(c)] for j in range(r)]
	for i in range(r) :
		for j in range(c) :
			for k in range(len(n)) :
				image[i][j] = image[i][j] + n[k][i][j]
			image[i][j] = image[i][j]/len(n)
	return image


def main() :
	plt.figure()
	lena = img.imread('lena.jpg')
	plt.subplot(221)
	plt.imshow(lena,cmap="gray")
	plt.title("Original")
	noisy = gen_noise(lena)

	plt.subplot(222)
	plt.imshow(noisy[10],cmap="gray")
	plt.title("noisy1")

	plt.subplot(223)
	plt.imshow(noisy[50],cmap="gray")
	plt.title("noisy2")

	plt.subplot(224)
	mean_img = mean_images(noisy)
	plt.imshow(mean_img,cmap = "gray")
	plt.title("After averaging")
	plt.savefig("Average_noisy_images")


if __name__ == '__main__':
	main()
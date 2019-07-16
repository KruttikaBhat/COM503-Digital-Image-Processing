import numpy as np
import cv2
import matplotlib.pyplot as plt

def equalize(r,g,b):
	red = cv2.equalizeHist(r)
	green = cv2.equalizeHist(g)
	blue = cv2.equalizeHist(b)
	return cv2.merge((blue,green,red))

def main():
	img = cv2.imread('lena.jpeg')
	plt.figure()
	plt.subplot(1,2,1)
	plt.title('original')
	plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
	b,g,r = cv2.split(img)
	print('red component')
	print(r)
	print('')
	print('green component')
	print(g)
	print('')
	print('blue component')
	print(b)
	print('')

	im = equalize(r,g,b)
	plt.subplot(1,2,2)
	plt.title('equalization in rgb planes')
	plt.imshow(cv2.cvtColor(im, cv2.COLOR_BGR2RGB))
	#plt.savefig('histogram_eq.png')
	plt.show()

if __name__ == '__main__':
	main()
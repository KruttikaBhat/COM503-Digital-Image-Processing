import matplotlib.image as img
from matplotlib import pyplot as plt
import numpy as np
import math

def fun(img,dimX,dimY,radian,COGPosX,COGPosY) :
	cosine = float(math.cos(radian))
	sine = float(math.sin(radian))
	image = [[0 for i in range (dimY)]for j in range (dimX)]
	for y in range (dimY) :
		for x in range (dimX) :
			rx = float(((x-COGPosX)*cosine)-((y-COGPosY)*sine)+COGPosX)
			ry = float(((x-COGPosX)*sine)+((y-COGPosY)*cosine)+COGPosY)

			rotx = int(math.floor(rx))
			roty = int(math.floor(ry))

			fx = float(math.floor(rx))
			fy = float(math.floor(ry))

			if(rotx >= 0 and rotx < dimX-1 and roty >= 0 and roty < dimY-1) :

				f1 = img[rotx][roty] + (float(img[rotx+1][roty])-float(img[rotx][roty]))*(rx-fx)
				f2 = img[rotx][roty+1] + (float(img[rotx+1][roty+1])-float(img[rotx][roty+1]))*(rx-fx)
				image[x][y] = f1 + (f2-f1)*(ry-fy)

	return image


def main() :
	tower = img.imread('pisa.jpg')
	r,c = tower.shape
	pisa = [[0 for i in range(c+100)]for j in range(r+100)]
	for i in range (r+100) :
		for j in range (c+100) :
			if(i < 50 or i>= r+50 or j < 50 or j>= c+50) :
				pisa[i][j] = 0
			else : 
				pisa[i][j] = tower[i-50][j-50]

	pisa = np.array(pisa)

	r += 100
	c += 100

	d1 = 2
	d2 = 3.9
	d3 = 6
	plt.figure()
	d1 = math.radians(d1)
	d2 = math.radians(d2)
	d3 = math.radians(d3)

	plt.subplot(221)
	plt.imshow(pisa,cmap="gray")
	plt.title('original')

	plt.subplot(222)
	rimage = fun(pisa,r,c,-d1,r/2,c/2)
	plt.imshow(rimage,cmap = "gray")
	plt.title('2degree')

	plt.subplot(223)
	rimage = fun(pisa,r,c,-d2,r/2,c/2)
	plt.imshow(rimage,cmap = "gray")
	plt.title('4degree')

	plt.subplot(224)
	rimage = fun(pisa,r,c,-d3,r/2,c/2)
	plt.imshow(rimage,cmap = "gray")
	plt.title('6degree')
	plt.savefig('rotation_bilinear')

if __name__ == '__main__':
	main()
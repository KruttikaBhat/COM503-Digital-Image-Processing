#in python3


import numpy as np
import cv2
import matplotlib.pyplot as plt

def synth_img():
	img = [[0 for i in range(200)]for j in range(200)]
	for i in range(50,150):
		for j in range(50,150):
			img[i][j] = 100
	return img

def reconstruct(row_proj,col_proj,dia1_proj,dia2_proj):
	img = [[0 for i in range(200)]for j in range(200)]
	for i in range(200):
		for j in range(200):
			img[i][j] += row_proj[i]
			img[i][j] += col_proj[j]
			img[i][j] += dia1_proj[199-i+j]
			img[i][j] += dia2_proj[i+j]

	return img

def main():
	plt.figure()
	img = synth_img()	
	row_sum = []
	col_sum = []
	dia1_sum = []
	dia2_sum = []
	im = np.asarray(img)
	plt.subplot(1,2,1)
	plt.imshow(im,'gray')
	im_flip = np.flip(im,axis=1)

	for i in range(200):
		row_sum.append(sum(im[i]))
		col_sum.append(sum(im[:,i]))

	for i in range(199,-200,-1):
		dia1_sum.append(sum(np.diagonal(im,offset=i)))
		dia2_sum.append(sum(np.diagonal(im_flip,offset=i)))
	
	res = np.asarray(reconstruct(row_sum,col_sum,dia1_sum,dia2_sum))
	plt.subplot(1,2,2)
	plt.imshow(res,'gray')
	#plt.savefig('back_proj.png')
	plt.show()
	



	#plt.imshow(im,'gray')
	#plt.show()


if __name__ == '__main__':
	main()
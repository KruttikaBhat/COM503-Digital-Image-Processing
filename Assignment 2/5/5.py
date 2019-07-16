import matplotlib
import cv2
import matplotlib.pyplot as plt
import skimage.io as io
from skimage.filters import threshold_otsu


def neighbours(x,y,image):
    #Return 8-neighbours of image point, in a clockwise order
    img = image
    x_1, y_1, x1, y1 = x-1, y-1, x+1, y+1
    return [ img[x_1][y], img[x_1][y1], img[x][y1], img[x1][y1],     # P2,P3,P4,P5
                img[x1][y], img[x1][y_1], img[x][y_1], img[x_1][y_1] ]    # P6,P7,P8,P9

def erosion(image):
    Changed_Image = image.copy()
    rows, columns = Changed_Image.shape
    changing=[]
    for x in range(1, rows - 1):
        for y in range(1, columns - 1):
            P2,P3,P4,P5,P6,P7,P8,P9 = n = neighbours(x, y, Changed_Image)
            if (Changed_Image[x][y] == 0     and
                (P2==1 or P4==1 or P6==1 or P8==1)):
                changing.append((x,y))
    for x, y in changing:
        Changed_Image[x][y] = 1


    return Changed_Image

def dilation(image):
    Changed_Image = image.copy()
    ones = []
    zeros = []
    rows, columns = Changed_Image.shape
    for x in range(1, rows - 1):
        for y in range(1, columns - 1):
            P2,P3,P4,P5,P6,P7,P8,P9 = n = neighbours(x, y, Changed_Image)
            if (Changed_Image[x][y]==0 or P2==0 or P4==0 or P6==0 or P8 ==0):
                zeros.append((x,y))
            else:
                ones.append((x,y))
    for x, y in ones:
        Changed_Image[x][y] = 1
    for x, y in zeros:
        Changed_Image[x][y] = 0
    return Changed_Image

def transitions(neighbours):
    n = neighbours + neighbours[0:1]
    return sum( (n1, n2) == (0, 1) for n1, n2 in zip(n, n[1:]) )

def thinning(image):
    Changed_Image = image.copy()
    changing1 = changing2 = 1
    while changing1 or changing2:
        changing1 = []
        rows, columns = Changed_Image.shape
        for x in range(1, rows - 1):
            for y in range(1, columns - 1):
                P2,P3,P4,P5,P6,P7,P8,P9 = n = neighbours(x, y, Changed_Image)
                if (Changed_Image[x][y] == 0     and
                    2 <= sum(n) <= 6   and
                    transitions(n) == 1 and
                    P2 + P4 + P6 == 1  and
                    P4 + P6 + P8 == 1):
                    changing1.append((x,y))
        for x, y in changing1:
            Changed_Image[x][y] = 1

        changing2 = []
        for x in range(1, rows - 1):
            for y in range(1, columns - 1):
                P2,P3,P4,P5,P6,P7,P8,P9 = n = neighbours(x, y, Changed_Image)
                if (Changed_Image[x][y] == 0   and
                    2 <= sum(n) <= 6  and
                    transitions(n) == 1 and
                    P2 + P4 + P8 == 1 and
                    P2 + P6 + P8 == 1):
                    changing2.append((x,y))
        for x, y in changing2:
            Changed_Image[x][y] = 1
    return Changed_Image



def thickening(image):
    it=0
    Changed_Image = image.copy()
    changing1=1
    while changing1 or changing2 or changing3 or changing4 or changing5 or changing6 or changing7 or changing8:

        changing1 = []
        rows, columns = Changed_Image.shape
        for x in range(1, rows - 1):
            for y in range(1, columns - 1):
                P2,P3,P4,P5,P6,P7,P8,P9 = n = neighbours(x, y, Changed_Image)
                if (Changed_Image[x][y] == 1     and    # Condition 0
                    2 <= sum(n) <= 5   and    # Condition 1
                    transitions(n) == 1 and    # Condition 2
                    P7 + P8 + P9 + P2 == 0  and    # Condition 3
                    P5==1):         # Condition 4
                    changing1.append((x,y))
        for x, y in changing1:
            Changed_Image[x][y] = 0

        changing2 = []
        for x in range(1, rows - 1):
            for y in range(1, columns - 1):
                P2,P3,P4,P5,P6,P7,P8,P9 = n = neighbours(x, y, Changed_Image)
                if (Changed_Image[x][y] == 1   and        # Condition 0
                    2 <= sum(n) <= 5  and       # Condition 1
                    transitions(n) == 1 and      # Condition 2
                    P9 + P2 + P3 + P4== 0 and       # Condition 3
                    P7 == 1):            # Condition 4
                    changing2.append((x,y))
        for x, y in changing2:
            Changed_Image[x][y] = 0

        changing3 = []
        for x in range(1, rows - 1):
            for y in range(1, columns - 1):
                P2,P3,P4,P5,P6,P7,P8,P9 = n = neighbours(x, y, Changed_Image)
                if (Changed_Image[x][y] == 1   and        # Condition 0
                    2 <= sum(n) <= 5  and       # Condition 1
                    transitions(n) == 1 and      # Condition 2
                    P3 + P4 + P5 + P6== 0 and       # Condition 3
                    P9 == 1):            # Condition 4
                    changing3.append((x,y))
        for x, y in changing3:
            Changed_Image[x][y] = 0

        changing4 = []
        for x in range(1, rows - 1):
            for y in range(1, columns - 1):
                P2,P3,P4,P5,P6,P7,P8,P9 = n = neighbours(x, y, Changed_Image)
                if (Changed_Image[x][y] == 1   and        # Condition 0
                    2 <= sum(n) <= 5  and       # Condition 1
                    transitions(n) == 1 and      # Condition 2
                    P5 + P6 + P7 + P8== 0 and       # Condition 3
                    P3 == 1):            # Condition 4
                    changing4.append((x,y))
        for x, y in changing4:
            Changed_Image[x][y] = 0

        changing5 = []
        for x in range(1, rows - 1):
            for y in range(1, columns - 1):
                P2,P3,P4,P5,P6,P7,P8,P9 = n = neighbours(x, y, Changed_Image)
                if (Changed_Image[x][y] == 1   and        # Condition 0
                    2 <= sum(n) <= 5  and       # Condition 1
                    transitions(n) == 1 and      # Condition 2
                    P2 + P3 + P4 + P5== 0 and       # Condition 3
                    P7 == 1):            # Condition 4
                    changing5.append((x,y))
        for x, y in changing5:
            Changed_Image[x][y] = 0

        changing6 = []
        for x in range(1, rows - 1):
            for y in range(1, columns - 1):
                P2,P3,P4,P5,P6,P7,P8,P9 = n = neighbours(x, y, Changed_Image)
                if (Changed_Image[x][y] == 1   and        # Condition 0
                    2 <= sum(n) <= 5  and       # Condition 1
                    transitions(n) == 1 and      # Condition 2
                    P4 + P5 + P6 + P7== 0 and       # Condition 3
                    P9 == 1):            # Condition 4
                    changing6.append((x,y))
        for x, y in changing6:
            Changed_Image[x][y] = 0

        changing7 = []
        for x in range(1, rows - 1):
            for y in range(1, columns - 1):
                P2,P3,P4,P5,P6,P7,P8,P9 = n = neighbours(x, y, Changed_Image)
                if (Changed_Image[x][y] == 1   and        # Condition 0
                    2 <= sum(n) <= 5  and       # Condition 1
                    transitions(n) == 1 and      # Condition 2
                    P6 + P7 + P8 + P9== 0 and       # Condition 3
                    P3 == 1):            # Condition 4
                    changing7.append((x,y))
        for x, y in changing7:
            Changed_Image[x][y] = 0

        changing8 = []
        for x in range(1, rows - 1):
            for y in range(1, columns - 1):
                P2,P3,P4,P5,P6,P7,P8,P9 = n = neighbours(x, y, Changed_Image)
                if (Changed_Image[x][y] == 1   and        # Condition 0
                    2 <= sum(n) <= 5  and       # Condition 1
                    transitions(n) == 1 and      # Condition 2
                    P8 + P9 + P2 + P3== 0 and       # Condition 3
                    P5 == 1):            # Condition 4
                    changing8.append((x,y))
        for x, y in changing8:
            Changed_Image[x][y] = 0
        it=it+1
        print it
    return Changed_Image

def main():
    #load image as grayscale
    Img_Original = cv2.imread('letters_2.jpg', cv2.CV_LOAD_IMAGE_GRAYSCALE)      # Gray image, rgb images need pre-conversion

    #Convert gray images to binary image
    Otsu_Threshold = threshold_otsu(Img_Original)
    BW_Original = Img_Original > Otsu_Threshold    # set object region as 0, background region as 1

    #apply morphological operations on the image
    BW_Erosion = erosion(BW_Original)
    BW_Dilation = dilation(BW_Original)
    BW_Opening = dilation(BW_Erosion) #erosion followed by Dilation
    BW_Closing = erosion(BW_Dilation) #dilation followed by erosion
    BW_Thinning = thinning(BW_Original)
    BW_Thickening= thickening(BW_Original)

    #Display the results
    fig, axes = plt.subplots(nrows=3, ncols=3)
    fig.tight_layout()
    plt.subplot(331)
    plt.axis("off")
    plt.subplot(333)
    plt.axis("off")

    plt.subplot(332)
    plt.imshow(BW_Original, cmap=plt.cm.gray)
    plt.title("Original")
    plt.axis("off")

    plt.subplot(334)
    plt.imshow(BW_Erosion, cmap=plt.cm.gray)
    plt.title("Erosion")
    plt.axis("off")

    plt.subplot(337)
    plt.imshow(BW_Dilation, cmap=plt.cm.gray)
    plt.title("Dilation")
    plt.axis("off")

    plt.subplot(335)
    plt.imshow(BW_Opening, cmap=plt.cm.gray)
    plt.title("Opening")
    plt.axis("off")

    plt.subplot(338)
    plt.imshow(BW_Closing, cmap=plt.cm.gray)
    plt.title("Closing")
    plt.axis("off")

    plt.subplot(336)
    plt.imshow(BW_Thinning, cmap=plt.cm.gray)
    plt.title("Thinning")
    plt.axis("off")

    plt.subplot(339)
    plt.imshow(BW_Thickening, cmap=plt.cm.gray)
    plt.title("Thickening")
    plt.axis("off")

    plt.show()

if __name__ == '__main__':
	main()

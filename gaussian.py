import numpy as np
import cv2
import math

def gaussian(img):
    gaussfilter = (1/140)*np.array([[1,1,2,2,2,1,1],[1,2,2,4,2,2,1],[2,2,4,8,4,2,2],[2,4,8,16,8,4,2],[2,2,4,8,4,2,2],[1,2,2,4,2,2,1],[1,1,2,2,2,1,1]])
    gaussianimage = np.zeros((img.shape[0],img.shape[1]))
    height = (gaussfilter.shape[0]-1)//2
    width = (gaussfilter.shape[1]-1)//2
    rows, cols = img.shape

    # Dynamix loop which will run on any n*m gaussian filter based on height and width of filter.
    for i in range(height,rows-height):
        for j in range(width,cols-width):
            tempSum = 0
            for k in range(-height, height + 1):
                for l in range(-width , width + 1):
                    tempSum = tempSum + img[i+k][j+l]* gaussfilter[k+height][l+width]
            gaussianimage[i][j] = tempSum 
    # cv2.imwrite('Gaussian.bmp',gaussianimage)

    return gaussianimage,height,width

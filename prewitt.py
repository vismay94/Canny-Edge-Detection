import numpy as np
import cv2
import math

def prewitt(gaussImage,height,width,rows,cols):

    #Prewit Operation Gx ,Gy and Gradient Magnitude
    prewitGx = np.array([[-1, 0 ,1],[-1, 0, 1],[-1, 0, 1]])
    prewitGxImage = np.zeros((gaussImage.shape[0],gaussImage.shape[1]))
    heightGx = (prewitGx.shape[0]-1)//2
    widthGx = (prewitGx.shape[1]-1)//2
    
    for i in range(height + 1,rows - (height + 1)):
        for j in range(width + 1,cols - (width + 1)):
            tempSum = 0
            for k in range(-heightGx, heightGx + 1):
                for l in range(-widthGx , widthGx + 1):
                    tempSum = tempSum + prewitGx[heightGx+k][widthGx+l] * gaussImage[i+k][j+l]
            if(tempSum < 0):
                tempSum = abs(tempSum)
            prewitGxImage[i][j] = tempSum / 3.0
    # cv2.imwrite('PrewitGx.bmp',prewitGxImage)

    prewitGy = np.array([[1, 1 ,1],[0, 0, 0],[-1, -1, -1]])
    prewitGyImage = np.zeros((gaussImage.shape[0],gaussImage.shape[1]))
    heightGy = (prewitGy.shape[0]-1)//2
    widthGy = (prewitGy.shape[1]-1)//2

    for i in range(height + 1,rows - (height + 1)):
        for j in range(width + 1,cols - (width + 1)):
            tempSum = 0
            for k in range(-heightGy, heightGy + 1):
                for l in range(-widthGy , widthGy + 1):
                    tempSum = tempSum + prewitGy[heightGy+k][widthGy+l] * gaussImage[i+k][j+l]

            if(tempSum < 0):
                tempSum = abs(tempSum)  
            prewitGyImage[i][j] = tempSum / 3.0

    # cv2.imwrite('PrewitGy.bmp',prewitGyImage)

    prewittImage = np.zeros((gaussImage.shape[0],gaussImage.shape[1]))
    for i in range(height + 1,rows - (height + 1)):
        for j in range(width + 1,cols - (width + 1)):
            prewittImage[i][j] = ((prewitGxImage[i][j] ** 2) +  (prewitGyImage[i][j] ** 2)) ** 0.5 
            prewittImage[i][j] = prewittImage[i][j] / 1.4142
    # cv2.imwrite("PrewitOperation.bmp",prewittImage)

    return prewitGxImage,prewitGyImage,prewittImage

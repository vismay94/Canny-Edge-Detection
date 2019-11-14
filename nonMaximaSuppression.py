import numpy as np
import cv2
import math

def suppression(gaussianimage,prewitGxImage,prewitGyImage,prewitImage,height,width,rows,cols):
    
    # If X value in Tan inverse is zero then we will look at the Y value and decide out THETA value 
    # based on that only.
    # If Theta alue is negative then we will add 360 to bring it into positive value.
    imageSupprresed = np.zeros((gaussianimage.shape[0],gaussianimage.shape[1]))
    sector = -1
    for i in range(height + 2,rows - (height + 2)):
        for j in range(width + 2,cols - (width + 2)):
            if(prewitGxImage[i][j] == 0):
                if(prewitGyImage[i][j] > 0):
                    theta = 90
                else:
                    theta = -90
            else:
                theta = math.degrees(math.atan(prewitGyImage[i][j] /  prewitGxImage[i][j]))

            if(theta < 0):
                theta = theta + 360
            #Based on Theta value, sector will be decided. 
            if( 0 <= theta <= 22.5 or  157.5 < theta <= 202.5 or 337.5 < theta <= 360):
                sector = 0
            elif ( 22.5 < theta <= 67.5 or  202.5 < theta <= 247.5):
                sector = 1
            elif ( 67.5 < theta <= 112.5 or  247.5 < theta <= 292.5):
                sector = 2
            elif ( 112.5 < theta <= 157.5 or  292.5 < theta <= 337.5):
                sector =3
            # based on sector, we will compare neighbour pixel and decide whether image pixel will retain value or not.
            if (sector == 0):
                if(prewitImage[i][j] > prewitImage[i][j-1] and prewitImage[i][j] > prewitImage[i][j+1]):
                    imageSupprresed[i][j] = prewitImage[i][j]
            elif (sector == 1):
                if(prewitImage[i][j] > prewitImage[i-1][j+1] and prewitImage[i][j] > prewitImage[i+1][j-1]):
                    imageSupprresed[i][j] = prewitImage[i][j]
            elif (sector == 2):
                if(prewitImage[i][j] > prewitImage[i-1][j] and prewitImage[i][j] > prewitImage[i+1][j]):
                    imageSupprresed[i][j] = prewitImage[i][j]   
            elif (sector == 3):
                if(prewitImage[i][j] > prewitImage[i-1][j-1] and prewitImage[i][j] > prewitImage[i+1][j+1]):
                    imageSupprresed[i][j] = prewitImage[i][j]

    # cv2.imwrite("suppressedImage.bmp",imageSupprresed)

    return imageSupprresed

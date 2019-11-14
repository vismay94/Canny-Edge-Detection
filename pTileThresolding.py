import numpy as np
import cv2
import math

def thresolding(imageSupprresed,thresold,rows,cols):

    totalpixelcount = 0;
    histogramcount = np.zeros((256,), dtype=np.int)
    for i in range(0,rows):
        for j in range(0,cols):
            if(imageSupprresed[i][j] > 0):
                histogramcount[int(imageSupprresed[i][j])] += 1;  #Histogram 
                totalpixelcount +=1 # Counting Total Number of pixels

    thresoldimage = np.zeros((imageSupprresed.shape[0],imageSupprresed.shape[1]))
    #Based on thresold value, we will determine thresold value.
    pixelnumthresold = totalpixelcount * thresold
    print("Total Pixel", totalpixelcount)
    print("Thresold Percent:", thresold*100,"%")
    # print("EdgePixels", pixelnumthresold)
    
    edgepixel=0
    count = 0;
    mainthresold = 0;
    for i in range(255,0,-1):
        if(count < pixelnumthresold):
            count = count + histogramcount[i]
        else:
            mainthresold = i
            break
    print("Thresold Value",mainthresold)
    
    for i in range(0,rows):
        for j in range(0,cols):
            if(imageSupprresed[i][j] > mainthresold):
                thresoldimage[i][j] = 255
                edgepixel += 1
    # cv2.imwrite("ThresoldedImage.bmp",thresoldimage) 
    print("Total Edge pixels",edgepixel)
    print("***********************************")
    return thresoldimage

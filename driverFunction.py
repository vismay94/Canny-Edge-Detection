import numpy as np
import cv2
import math
import gaussian as gauss
import prewitt as prwt
import nonMaximaSuppression as nms
import pTileThresolding as ptile

def main():
    img = cv2.imread('/users/vismay/desktop/Lena.bmp',cv2.IMREAD_GRAYSCALE)
    rows, cols = img.shape

    # Gaussian Function will take original image as a input and after performing
    # convolution, returns blurred image with reduced noise.
    gaussImage,height,width = gauss.gaussian(img)
    cv2.imwrite('Gaussian.bmp',gaussImage)

    # After Gaussian, we will use blurred image and using Prewit Operator we will
    # Detect the edges.
    prewitGxImage,prewitGyImage,prewitImage = prwt.prewitt(gaussImage,height,width,rows,cols)
    cv2.imwrite('PrewitGx.bmp',prewitGxImage)
    cv2.imwrite('PrewitGy.bmp',prewitGyImage)
    cv2.imwrite("PrewitOperation.bmp",prewitImage)

    # To detect accurate edges we will use non maxima suppresion method.
    nmsImage = nms.suppression(gaussImage,prewitGxImage,prewitGyImage,prewitImage,height,width,rows,cols)
    cv2.imwrite("suppressedImage.bmp",nmsImage)

    # Ptile method will take SuppressedImage, Percent Thresold, rows and column
    #  value of the image as a input and returns Thresolded image.
    ptileImage1 = ptile.thresolding(nmsImage,0.1,rows,cols)
    ptileImage2 = ptile.thresolding(nmsImage,0.3,rows,cols)
    ptileImage3 = ptile.thresolding(nmsImage,0.5,rows,cols)
    cv2.imwrite("ThresoldedImage10PercentThresold.bmp",ptileImage1)
    cv2.imwrite("ThresoldedImage30PercentThresold.bmp",ptileImage2)
    cv2.imwrite("ThresoldedImage50PercentThresld.bmp",ptileImage3)


if __name__ == '__main__':
    main()

import numpy as np
import cv2
import conf
 

cam = cv2.VideoCapture(0)
 

while(True):

 

    # Capture the frames

    ret, img = cam.read()

 

    # Crop the image

    img = cv2.resize(img, (340, 220))
    img = img[conf.camCropLT[0]:conf.camCropLT[1], conf.camCropLT[2]:conf.camCropLT[3]]

 

    # Convert to grayscale

    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

 

    # Gaussian blur

    blur = cv2.GaussianBlur(img_gray,(5,5),0)

 

    # Color thresholding

    ret,thresh = cv2.threshold(blur,60,255,cv2.THRESH_BINARY_INV)

 

    # Find the contours of the frame

    _,contours,h = cv2.findContours(thresh.copy(), 1, cv2.CHAIN_APPROX_NONE)

 

    # Find the biggest contour (if detected)

    if len(contours) > 0:

        c = max(contours, key=cv2.contourArea)

        M = cv2.moments(c)

        try:

            cx = int(M['m10']/M['m00'])

            cy = int(M['m01']/M['m00'])

        except ZeroDivisionError:
            continue

        cv2.line(img,(cx,0),(cx,720),(255,0,0),1)

        cv2.line(img,(0,cy),(1280,cy),(255,0,0),1)

        cv2.drawContours(img, contours, -1, (0,255,0), 1)
        cdiff = 70-cx
        linecoord = [cx,cy,cdiff]
        print(linecoord)


    #Display the resulting frame

    cv2.imshow('frame',img)

    if cv2.waitKey(1) & 0xFF == ord('q'):

        break

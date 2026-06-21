#IN OPEN CV THERE IS NO PERTICULAR FUNCTION FOR SLICING SO WELL USE NUMPY SLICING

import cv2 as cv
img=cv.imread("D:\opencv\photos\cat.jpg")

if img is not None:
    print("image loaded successfully")


              #[start row:end row,start col: end col]
    cropped=img[100:500,50:500]

    cv.imshow("Cropped",cropped)
    cv.imshow("original",img)

    cv.waitKey(0)
    cv.destroyAllWindows()
else:
    print("image not loaded")

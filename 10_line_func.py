import cv2 as cv

# cv.line(src,pt1,pt2,color,thickness)  row column (row,column) point formation

img=cv.imread("photos\cat.jpg")

if img is not None:
    print("image loaded successfully")
    #our image(428,630)

    cv.line(img,(100,100),(300,300),(255,0,0),4)
    cv.imshow("draw",img)
    cv.waitKey(0)
    cv.destroyAllWindows()
else:
    print("image not loaded")


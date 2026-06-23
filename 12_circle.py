import cv2 as cv

# cv.circle(src,centre,radius,color,thickness)

img=cv.imread("photos\cat.jpg")

if img is not None:
    print("image loaded successfully")
    #our image(428,630)

    cv.circle(img,(100,100),50,(255,0,0),4)
    cv.imshow("draw",img)
    cv.waitKey(0)
    cv.destroyAllWindows()
else:
    print("image not loaded")
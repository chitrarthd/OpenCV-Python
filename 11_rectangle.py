import cv2 as cv

# cv.rectangle(src,pt1,pt2,color,thickness)  pt1=top left corner pt2 = bottem right corner

img=cv.imread("photos\cat.jpg")

if img is not None:
    print("image loaded successfully")
    #our image(428,630)

    cv.rectangle(img,(100,100),(300,300),(255,0,0),4)
    cv.imshow("draw",img)
    cv.waitKey(0)
    cv.destroyAllWindows()
else:
    print("image not loaded")
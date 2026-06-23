import cv2 as cv

# cv.putText(src,txt,org(bottem left corner of txt),font,font scale,color,thickness)

img=cv.imread("photos\cat.jpg")

if img is not None:
    print("image loaded successfully")
    #our image(428,630)

    cv.putText(img,"hello im a cat",(200,50),cv.FONT_HERSHEY_COMPLEX,1,(255,0,0),4)
    cv.imshow("draw",img)
    cv.waitKey(0)
    cv.destroyAllWindows()
else:
    print("image not loaded")
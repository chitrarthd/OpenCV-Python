import cv2 as cv

#flip function : cv.flip(src,flipcode)   flip code = the axis you want to flim img with 0 = verticle flip 1= horizontal flip -1=both

img = cv.imread("photos\cat.jpg")

if img is not None:
    print("image loaded successfully")
    flippedv= cv.flip(img,0)
    flippedh= cv.flip(img,1)
    flippedboth= cv.flip(img,-1)
    cv.imshow("original",img)
    cv.imshow("verticle",flippedv)
    cv.imshow("horizontal",flippedh)
    cv.imshow("both",flippedboth)
    cv.waitKey(0)
    cv.destroyAllWindows()
else:
    print("image not loaded successfully")
import cv2 as cv

#coverting image to grey scale

img = cv.imread("photos/cats.jpg")

if img is not None:
    grey=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    cv.imshow('grey',grey)
    cv.waitKey(0)
    cv.destroyAllWindows()
else:
    print("error loading image")



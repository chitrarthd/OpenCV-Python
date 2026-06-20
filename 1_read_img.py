import cv2 as cv

#reading a image as matrix
img=cv.imread('D:/opencv/photos/cat.jpg')

cv.imshow('cat',img)   #creates window named cat with img in it

cv.waitKey(0) 

cv.destroyAllWindows() 
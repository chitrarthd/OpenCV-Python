import cv2 as cv

location=input("Enter location of image : ")

img=cv.imread(location)

a=int(input("Enter 1 if you want to see or 2 if you want save the image : "))
if img is not None :
    if a == 1:
        cv.imshow('read',img)
        cv.waitKey(0)
        cv.destroyAllWindows()
    else :
        b=input("enter the name of the savefile : ")
        cv.imwrite(b,img)
else :
    print("error loading image")

  


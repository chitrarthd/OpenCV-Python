import cv2 as cv

img=cv.imread("D:\opencv\photos\cat.jpg")

if img is not None:
    print("Image loaded\n")
     
             #resize(source,(width,height),fx,fy,interpolation)
    resize=cv.resize(img,(300,500)) 
    cv.imshow("original",img)
    cv.imshow("resized",resize)

    cv.imwrite("resized.jpg",resize)

    cv.waitKey(0)
    cv.destroyAllWindows()


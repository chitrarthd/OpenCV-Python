import cv2 as cv

img = cv.imread("photos/cats.jpg")

if img is not None:
    sucess= cv.imwrite('cats_output.jpg',img)
    if sucess:
        print('image saved success fully')
    else:
        print("failed to save") 
else:
    print('erroe')

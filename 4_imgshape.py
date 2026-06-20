import cv2 as cv

#getting dimensions of a image 

img = cv.imread('photos/cats.jpg')

if img is not None:
    h,w,c=img.shape
    print(f"image loaded:\n Heights: {h}\n Width: {w}\n Channels: {c} " )
else:
    print("Error loading image")

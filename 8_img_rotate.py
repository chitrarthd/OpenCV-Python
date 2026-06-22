import cv2 as cv

img = cv.imread("photos/cat.jpg")

if img is not None:
    (h,w)=img.shape[:2]
    center=(w//2,h//2)
    M=cv.getRotationMatrix2D(center,90,1.0)
    rotated_img=cv.warpAffine(img,M,(w,h))

    cv.imshow("original",img)
    cv.imshow("rotated",rotated_img)
    cv.waitKey(0)
    cv.destroyAllWindows()

else:
    print("image not loaded")

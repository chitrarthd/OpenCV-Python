import cv2 as cv


#cv.VideoCApture can capture a video file(path) webcam(0) camera stream(1) 
capture = cv.VideoCapture('D:/opencv/videos/dog.mp4')

while True:  #infinite loop 
    isTrue, frame= capture.read()
    cv.imshow('video',frame)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows() 
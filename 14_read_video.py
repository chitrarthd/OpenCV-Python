import cv2 as cv

cap= cv.VideoCapture(0)

while True:
    ret,Frame=cap.read()

    if not ret:
        print("could no read frames")
        break
    
    cv.imshow("webcam feed",Frame)

    if cv.waitKey(1) & 0xFF == ord("q"):  #in every 1 ms it checks if key 1 is pressed or not and 0xff == ord ("q") return q's ascii walue
        print("Quitting...")
        break

cap.release()
cv.destroyAllWindows()
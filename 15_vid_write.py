import cv2 as cv

#cv2.videowriter(filename,codec,fps,frame size)\
#filename = like "output.mp4"
#odec = how video is compressed mp4 xvid mjpg..etc
#fps frames per sec
#framesize= (width,height)


camera=cv.VideoCapture(0)

frame_Width=int(camera.get(cv.CAP_PROP_FRAME_WIDTH))
frame_height=int(camera.get(cv.CAP_PROP_FRAME_HEIGHT))

codec=cv.VideoWriter_fourcc(*"XVID")
recorder=cv.VideoWriter("my_video.avi",codec,20,(frame_Width,frame_height))

while True:
    success, image=camera.read()

    if not success:
        break

    recorder.write(image)
    cv.imshow("recordin live",image)

    if cv.waitKey(1) & 0xFF == ord("q"):
        break


camera.release()
recorder.release()
cv.destroyAllWindows()

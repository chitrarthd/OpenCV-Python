#Q. WRITE A PROGRAMME IN WHICH YOU TAKE THE PATH OF IMAGE FROM USER THEN GIVE HIM/HER COICE TO SEE IT SAVE IT WITH NAME THEY
# WANT CHECK ITS SHAPE OR CONVERT IT TO GREY SCALE 

import cv2 as cv

location=input("Enter the path of image : ")

img = cv.imread(location)

if img is not None:

    a=int(input("Enter \n1. if you to see the picture \n2. if you want to save the picture \n3. if ypu want shape of picture\n" \
    "4. if you want to convert the picure to grey and see :\n ==>Enter your choice:  "))
    if a==1:
        cv.imshow("cat",img)
        cv.waitKey(0)
        cv.destroyAllWindows()
    if a==2:
        name=input("Enter the name you want to save with : ")
        if not name.lower().endswith(".jpg"):
            name+=".jpg"   
        cv.imwrite(name,img)
    if a==3:
        height,width,channel=img.shape
        print("Height =",height,"\nwidth =",width,"\nchannels =",channel) 
    else:
        grey=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
        cv.imshow("grey cat",grey)
        cv.waitKey(0)
        cv.destroyAllWindows()        


else:
    print("can't load image")

